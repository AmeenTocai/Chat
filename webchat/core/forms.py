from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Info:
        model = User
        fields = ['username', 'password1', 'password2']