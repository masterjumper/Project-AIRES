from django import forms
from django.contrib.auth.models import User
from django_popup_view_field.fields import PopupViewField
from web.popups import ColorsPopupView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DJ_user_client, CustomUserManager

#class AlbumForm(forms.ModelForm):

#    class Meta:
#        model = Album
#        fields = ['artist', 'album_title', 'genre', 'album_logo']


#class SongForm(forms.ModelForm):

#    class Meta:
#        model = Song
#        fields = ['song_title', 'audio_file']




class DJ_user_clientCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args):
        super(DJ_user_clientCreationForm, self).__init__(*args)
        del self.fields['DJ_user']

    class Meta:
        model = DJ_user_client
        fields = '__all__'

"""class DJ_user_clientChangeForm(UserChangeForm):
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    

    def __init__(self, *args):
        super(DJ_user_clientChangeForm, self).__init__(*args)
        del self.fields['DJ_user']

    class Meta:
        model = DJ_user_client

class UserForm(forms.ModelForm):
    DJ_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = DJ_user_client
        #fields = '__all__'
"""
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