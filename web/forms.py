from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_popup_view_field.fields import PopupViewField
from web.popups import ColorsPopupView
from web.models import DJ_user_client

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['DJ_user']

    class Meta:
        model = DJ_user_client
        fields = ("DJ_user",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['DJ_user']

    class Meta:
        model = DJ_user_client


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = DJ_user_client
        fields = ['DJ_user', 'DJ_email', 'DJ_password']

"""class UserFormProfile(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']"""

class ColorForm(forms.Form):

    color = PopupViewField(
        view_class=ColorsPopupView,
        popup_dialog_title='What is your favorite color',
        required=True,
        help_text='be honest'
    )