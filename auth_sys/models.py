from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    def __str__(self) -> str:
        return self.username