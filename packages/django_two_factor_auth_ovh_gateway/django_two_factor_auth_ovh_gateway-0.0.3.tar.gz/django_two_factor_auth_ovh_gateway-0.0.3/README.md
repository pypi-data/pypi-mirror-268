# django_two_factor_auth_ovh_gateway


Plugin for [django-two-factor-auth](https://github.com/jazzband/django-two-factor-auth/), adding a gateway for sending SMS using the OVH API.

All you need is your OVH API credentials and the name of the SMS account you want to use.


## Setup

Please see the [django-two-factor-auth documentation](https://django-two-factor-auth.readthedocs.io/en/stable/) for instructions on how to set up two-factor authentication in your Django project.

## OVH Setup

To use the OVH gateway, you need first to install this OVH plugin for django-two-factor-auth:

```sh
$ pip install django_two_factor_auth_ovh_gateway
```

Then, add the plugin to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    "django_two_factor_auth_ovh_gateway",
]
```

Finally, you need to add the OVH gateway to your `TWO_FACTOR_SMS_GATEWAY` setting:

```python
TWO_FACTOR_SMS_GATEWAY = "django_two_factor_auth_ovh_gateway.gateway.Ovh"
```

### Configuration

`OVH_ENDPOINT` (default: `ovh-eu`)
The OVH API endpoint to use. See [this list](https://github.com/ovh/python-ovh/blob/master/ovh/client.py#L64) for available endpoints.

`OVH_APPLICATION_KEY` (**required**)
The application key, provided by OVH.

`OVH_APPLICATION_SECRET` (**required**)
The application secret, prodived by OVH.

`OVH_CONSUMER_KEY` (**required**)
The consumer key, provided by OVH.

`OVH_CLASS` (default: `phoneDisplay`)
The SMS class used by OVH to send the SMS. Possible values are `flash`, `phoneDisplay`, `sim`, `toolkit`.

`OVH_CODING` (default: `7bit`)
The SMS coding used by OVH to send the SMS. Possible values are `7bit`, `8bit`.

`OVH_MESSAGE` (default: `Your token is {token}`)
The message template used by OVH to send the SMS. The `{token}` placeholder needs to be present, as it will be replaced by the actual token.

`OVH_NO_STOP_CLAUSE` (default: `True`)
Whether to allow the user to stop receiving SMS by replying `STOP` to the SMS. If set to `True`, the user **will not** be able to stop receiving SMS.

`OVH_PRIORITY` (default: `high`)
The SMS priority used by OVH to send the SMS. Possible values are `high`, `low`, `medium`, `veryLow`.

`OVH_SENDER` (default: `OVH`)
The sender's name used by OVH to send the SMS. Can be the name of your app, or your company name.

`OVH_SENDER_FOR_RESPONSE` (default: `False`)
Whether to allow the user to reply to the SMS. If set to `True`, the user **will** be able to reply to the SMS.

`OVH_VALIDITY_PERIOD` (default: `2880`)
The SMS validity time, in minutes.
