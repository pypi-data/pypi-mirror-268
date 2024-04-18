from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django.contrib.sessions.models import Session as BaseSession

class Session(BaseSession):
    user = models.OneToOneField(User, related_name='session',
                             unique=False, blank=True, null=True, on_delete=models.SET_NULL)

    updated_date = models.DateTimeField(_('updated date'), db_index=True,
                                        auto_now=True)

    class Meta:
        app_label = "unique_session"