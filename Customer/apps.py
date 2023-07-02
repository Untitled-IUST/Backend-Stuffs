from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Customer'
    
    def ready(self) -> None:
        import Customer.signals
