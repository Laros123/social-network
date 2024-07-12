from django.contrib.auth.forms import UserCreationForm
from .models import NewUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ("username", )
        