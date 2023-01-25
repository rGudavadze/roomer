from roomer.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]

CSRF_TRUSTED_ORIGINS = ["https://roomer-api-dev-6u5f43nb7a-ey.a.run.app"]
