from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # this to prepare for the signals
    def ready(self) :
        import users.signals
