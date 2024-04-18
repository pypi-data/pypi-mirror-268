=========================================================
django-unique-session : unique session backend for Django
=========================================================

Key features
============

 * Ensure only one open session per user
 * Extends the standard Django database session backend
 * Automatically logout previously existing sessions
 * Optionally enforce a timeout before allowing a new login
 * Works with Django 1.4+

How to use
==========

1. Add  ``unique_session`` in ``INSTALLED_APPS``.

2. Use ``SESSION_ENGINE = "unique_session.backends.session_backend"``

3. (Optional) Add ``"UNIQUE_SESSION_BLOCK_TIME = <seconds>"`` to enable the timeout.

4. (Optional) Add ``"UNIQUE_SESSION_WHITELIST = (<uid1>, <uid2>,...)"`` to whitelist some users (from their numeric id) so that they'll be exempt to the blocking mechanism.

5. Run syncdb.

License
=======

GPLv3

