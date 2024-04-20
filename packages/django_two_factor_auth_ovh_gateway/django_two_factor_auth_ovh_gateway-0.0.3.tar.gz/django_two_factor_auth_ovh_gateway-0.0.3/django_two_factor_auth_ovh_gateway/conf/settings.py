# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# see https://github.com/ovh/python-ovh/blob/master/ovh/client.py#L64
OVH_ENDPOINT = getattr(settings, "OVH_ENDPOINT", "ovh-eu")

# Application key as provided by OVH
OVH_APPLICATION_KEY = getattr(settings, "OVH_APPLICATION_KEY", None)
if not OVH_APPLICATION_KEY:
    raise ImproperlyConfigured("OVH_APPLICATION_KEY must be defined in your settings")

# Application secret key as provided by OVH
OVH_APPLICATION_SECRET = getattr(settings, "OVH_APPLICATION_SECRET", None)
if not OVH_APPLICATION_SECRET:
    raise ImproperlyConfigured(
        "OVH_APPLICATION_SECRET must be defined in your settings"
    )

# Uniquely identifies
OVH_CONSUMER_KEY = getattr(settings, "OVH_CONSUMER_KEY", None)
if not OVH_CONSUMER_KEY:
    raise ImproperlyConfigured("OVH_CONSUMER_KEY must be defined in your settings")

# OVH_CHARSET = getattr(settings, "OVH_CHARSET", "UTF-8")
OVH_CHARSET = "UTF-8"  # OVH does not support other charsets

# SMS class. Possible values: `flash`, `phoneDisplay`, `sim`, `toolkit`
OVH_CLASS = getattr(settings, "OVH_CLASS", "phoneDisplay")

# SMS coding. Possible values: `7bit`, `8bit`
OVH_CODING = getattr(settings, "OVH_CODING", "7bit")

# SMS template to send to the user. `%s` will be replaced with the token
OVH_MESSAGE = getattr(settings, "OVH_MESSAGE", "Your token is {token}")
if "{token}" not in OVH_MESSAGE:
    raise ImproperlyConfigured(
        "OVH_MESSAGE must contain a '{token}' placeholder to be replaced by the actual token"
    )

# If `True`, the user **won't** be able to stop receiving SMS by replying `STOP`
OVH_NO_STOP_CLAUSE = getattr(settings, "OVH_NO_STOP_CLAUSE", True)

# SMS priority. Possible values: `high`, `low`, `medium`, `veryLow`
OVH_PRIORITY = getattr(settings, "OVH_PRIORITY", "high")

# SMS sender.
OVH_SENDER = getattr(settings, "OVH_SENDER", "OVH")

# If `True`, the user will be able to reply to the SMS
OVH_SENDER_FOR_RESPONSE = getattr(settings, "OVH_SENDER_FOR_RESPONSE", False)

# SMS validity period in minutes
OVH_VALIDITY_PERIOD = getattr(settings, "OVH_VALIDITY_PERIOD", 2880)
