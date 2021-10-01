from django.apps import AppConfig

OneTimePasswordValidTimeSeconds = 10 * 60


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account'
