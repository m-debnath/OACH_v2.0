from django.forms import ModelForm, PasswordInput
from .models import LdapConfig

class LdapConfigForm(ModelForm):
    class Meta:
        model = LdapConfig
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }