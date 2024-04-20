from datetime import datetime
import random

from django.conf import settings
from django.http import HttpRequest

from django_observe.models import Event


class MonitoringMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.events = []
        self.get_response = get_response
        self.sample_rate = getattr(settings, "DJANGO_OBSERVE_SAMPLE_RATE", 1)

    def __call__(self, request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if self.sample_rate > random.random():
            Event.objects.create(
                method=request.method,
                path=request.path,
                status_code=response.status_code,
                remote_addr=request.META.get("REMOTE_ADDR"),
                user_agent=request.META.get("HTTP_USER_AGENT"),
                timestamp=datetime.now(),
            )

        return response
