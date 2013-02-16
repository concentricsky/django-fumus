import os
import base64

from django.views.generic import View
from django.http import HttpResponse
from django.core.cache import cache
from django.db.models import get_models


def b64noise(bytes=32):
    return base64.b64encode(os.urandom(bytes))


class SmokeTestView(View):
    def fail(self):
        return HttpResponse(status=500)

    def success(self):
        return HttpResponse()

    def get(self, request, *args, **kwargs):
        # Test cache
        key, val = b64noise(), b64noise()
        cache.set(key, val)
        if not cache.get(key) == val:
            return self.fail()

        # Test database connection
        models = get_models()
        if len(models) > 0:
            try:
                tmp = models[0].objects.all().exists()
            except Exception:
                return self.fail()

        return self.success()
