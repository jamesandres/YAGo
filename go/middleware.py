import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
import json


class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must
    be a valid regex.

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly
    define any exceptions (like login and logout URLs).
    """
    def __init__(self):
        self.exceptions = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated():
            return None

        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path):
                return None

        # All other requests are wrapped with the login_required decorator
        return login_required(view_func)(request, *view_args, **view_kwargs)


class JSONContenttypeMiddleware(object):
    """
    Middleware component that translates requests with a JSON body into a
    usable dict.
    """
    def process_request(self, request):
        if request.META.get('CONTENT_TYPE', '').startswith('application/json'):
            body = request.body

            if body.startswith('{') or body.startswith('['):
                try:
                    request.POST = json.loads(request.body)
                except ValueError:
                    # TODO: Gracefully handle malformed JSON requests.
                    raise
