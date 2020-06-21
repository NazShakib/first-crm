<<<<<<< HEAD
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    def ready(self):
        import accounts.signals
=======
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    def ready(self):
        import accounts.signals
>>>>>>> 7511be836ccd1300326d827fd7d821c5e95ba3b4
