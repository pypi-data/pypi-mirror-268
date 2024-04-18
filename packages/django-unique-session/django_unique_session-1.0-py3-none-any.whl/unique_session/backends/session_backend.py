from django.contrib.sessions.backends.base import CreateError
from ..models import Session

from django.contrib.sessions.backends.db import SessionStore as SessionStoreBase
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.db import IntegrityError, transaction, router
from django.utils.encoding import force_text
from django.utils import timezone

from django.contrib.auth.signals import user_logged_in
from django.conf import settings
import datetime

TIME_DELTA = getattr(settings, 'UNIQUE_SESSION_BLOCK_TIME', None)
TIME_DELTA = TIME_DELTA and datetime.timedelta(seconds = TIME_DELTA)

WHITELIST = set(getattr(settings, 'UNIQUE_SESSION_WHITELIST', []))

class SessionStore(SessionStoreBase):
    """
    Implements database session store.
    """
    def load(self):
        try:
            s = Session.objects.get(
                session_key = self.session_key,
                expire_date__gt=timezone.now()
            )
            val = self.decode(force_text(s.session_data))
            s.updated_date = timezone.now()
            s.save()
            return val
        except (Session.DoesNotExist, SuspiciousOperation):
            self._session_key = None
            return {}

    def exists(self, session_key):
        return Session.objects.filter(session_key=session_key).exists()

    def save(self, must_create=False):
        """
        Saves the current session data to the database. If 'must_create' is
        True, a database error will be raised if the saving operation doesn't
        create a *new* entry (as opposed to possibly updating an existing
        entry).
        """
        if self.session_key is None:
            return self.create()
        data = self._get_session(no_load=must_create)
        user_id = data.get('_auth_user_id', None)
        obj = Session(
            session_key=self._get_or_create_session_key(),
            session_data=self.encode(data),
            user_id = user_id,
            expire_date=self.get_expiry_date()
        )
        using = router.db_for_write(Session, instance=obj)
        sid = transaction.savepoint(using=using)
        try:
            # Also delete all other sessions of that user
            if user_id and not user_id in WHITELIST:
                exitsing = Session.objects.filter(user_id = user_id)
                exitsing.exclude(session_key = obj.session_key).delete()
            obj.save(force_insert=must_create, using=using)
        except IntegrityError:
            if must_create:
                transaction.savepoint_rollback(sid, using=using)
                raise CreateError
            raise

    def delete(self, session_key=None):
        if session_key is None:
            if self.session_key is None:
                return
            session_key = self.session_key
        try:
            Session.objects.get(session_key=session_key).delete()
        except Session.DoesNotExist:
            pass

    @classmethod
    def ensure_unique_login(klass, sender, request, user, **kwargs):
        """
        If UNIQUE_SESSION_BLOCK_TIME is set, then the user won't be able
        to log in as long as there is a session updated that number of
        seconds ago
        """
        if not user.id in WHITELIST:
            limit = timezone.now() + TIME_DELTA
            s = Session.objects.filter(user_id = user.id,
                                       updated_date__lt = limit)
            if s.exists():
                raise PermissionDenied

if TIME_DELTA:
    user_logged_in.connect(SessionStore.ensure_unique_login)
