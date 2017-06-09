from django import forms
from django.contrib.auth.models import User
from django_popup_view_field.fields import PopupViewField
from web.popups import ColorsPopupView
#from .models import Album, Song


#class AlbumForm(forms.ModelForm):

#    class Meta:
#        model = Album
#        fields = ['artist', 'album_title', 'genre', 'album_logo']


#class SongForm(forms.ModelForm):

#    class Meta:
#        model = Song
#        fields = ['song_title', 'audio_file']


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