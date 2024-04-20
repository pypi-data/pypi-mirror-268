# Django
from django.core.exceptions import ImproperlyConfigured

# Third party
import ovh

# Local application / specific library imports
from .conf import settings


class Ovh:
    def __init__(self, **kwargs):
        self.client = ovh.Client(
            endpoint=getattr(settings, "OVH_ENDPOINT"),
            application_key=getattr(settings, "OVH_APPLICATION_KEY"),
            application_secret=getattr(settings, "OVH_APPLICATION_SECRET"),
            consumer_key=getattr(settings, "OVH_CONSUMER_KEY"),
        )
        services = self.client.get("/sms")
        if not services:
            raise ImproperlyConfigured("No SMS service found")

        self.service_name = services[0]

    def make_call(self, device, token):
        raise NotImplementedError("OVH does not support voice calls")

    def send_sms(self, device, token):
        receiver = device.number.as_e164
        send_kwargs = {
            "charset": getattr(settings, "OVH_CHARSET"),
            "class": getattr(settings, "OVH_CLASS"),
            "coding": getattr(settings, "OVH_CODING"),
            "message": getattr(settings, "OVH_MESSAGE").format(token=token),
            "noStopClause": getattr(settings, "OVH_NO_STOP_CLAUSE"),
            "priority": getattr(settings, "OVH_PRIORITY"),
            "receivers": [receiver],
            "sender": getattr(settings, "OVH_SENDER"),
            "senderForResponse": getattr(settings, "OVH_SENDER_FOR_RESPONSE"),
            "validityPeriod": getattr(settings, "OVH_VALIDITY_PERIOD"),
        }
        self.client.post("/sms/%s/jobs" % self.service_name, **send_kwargs)
