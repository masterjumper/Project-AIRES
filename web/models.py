from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, DJ_user, DJ_password, DJ_is_staff, DJ_is_superuser):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        
        if not DJ_user:
            raise ValueError('The given DJ_user must be set')
        
        #DJ_user = self.normalize_email(DJ_user)
        DJ_user = self.model(DJ_user=DJ_user,
                          DJ_is_staff=DJ_is_staff, is_active=True,
                          DJ_is_superuser=DJ_is_superuser, last_login=now,
                          date_joined=now)
        user.set_password(DJ_password)
        user.save(using=self._db)
        return user

    def create_user(self, DJ_user, DJ_password=None):
        return self._create_user(DJ_user, DJ_password, False, False)

    def create_superuser(self, DJ_user, DJ_password):
        return self._create_user(DJ_user, DJ_password, True, True)

class DJ_user_client(models.Model):
    DJ_id_client    = models.IntegerField(primary_key=True)
    DJ_user         = models.CharField(max_length=10)
    DJ_password     = models.CharField(max_length=10)
    DJ_email        = models.CharField(max_length=50)
    DJ_is_staff     = models.BooleanField(default=False)
    DJ_is_superuser = models.BooleanField(default=False)
    DJ_is_active    = models.BooleanField(default=True)
    is_anonymous    = models.BooleanField(default=False)
    is_authenticated= models.BooleanField(default=False)
    USERNAME_FIELD  = 'DJ_id_client'
    REQUIRED_FIELDS = ['DJ_user', 'DJ_email']

    objects = CustomUserManager()

    class Meta:
            verbose_name = _('user')
            verbose_name_plural = _('users')    
        
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.DJ_user)
        
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.DJ_user)
        return full_name.strip()
        
    def get_short_name(self):
        """Returns the short name for the user."""
        return self.DJ_user

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.DJ_email])

    def __str__(self):
        return self.DJ_user

"""class DJ_notifications(models.Model):
    DJ_id_client = models.ForeingKey(on_delete=models.CASCADE)
    DJ_id_notif = models.CharField(max_length=10)
    DJ_text = models.CharField(max_length=10)
    DJ_state = models.CharField(max_length=50)
    DJ_date_time = models.DateTimeField()

    def __str__(self):
        return self.DJ_state

class DJ_tweets(models.Model):
    DJ_id_tweet = models.PrimaryKey()
    AS_id_tweet = models.CharField(max_length=10)
    DJ_id_hash = models.CharField(max_length=10)
    DJ_id_client = models.CharField(max_length=10)
    AS_text = models.CharField(max_length=250)
    AS_screen_name = models.CharField(max_length=50)
    AS_created_at = models.DateTimeField()
    AS_sentiment = models.CharField(max_length=50)

    def __str__(self):
        return self.DJ_id_tweet
 
class DJ_groups(models.Model):
    DJ_id_groups = models.PrimaryKey()
    DJ_id_client = models.CharField(max_length=10)
    DJ_nombre = models.CharField(max_length=10)
    DJ_group_size = models.date()
    
    def __str__(self):
        return self.DJ_id_groups 

class DJ_overrep(models.Model):
    DJ_id_overrep = models.PrimaryKey()
    DJ_id_groups = models.CharField(max_length=10)
    DJ_id_client = models.CharField(max_length=10)
    AS_id_user = models.DateTimeField()
    AS_screen_name = models.CharField(max_length=50)
    AS_count_friends = models.CharField(max_length=50)
    AS_count_followers = models.CharField(max_length=50)

    def __str__(self):
        return self.DJ_id_overrep  

class DJ_candidate(models.Model):
    DJ_id_candidate = models.PrimaryKey()
    DJ_id_client = models.CharField(max_length=10)
    DJ_text = models.CharField(max_length=10)
    DJ_date_time = models.DateTimeField()
    
    def __str__(self):
        return self.DJ_candidate

class DJ_candidates_similar(models.Model):
    DJ_id_candidate_similar = models.PrimaryKey()
    DJ_id_candidate = models.CharField(max_length=10)
    DJ_id_client = models.CharField(max_length=10)
    AS_id_tweet = models.DateTimeField()
    AS_texto = models.CharField(max_length=10)
    AS_created_at = models.DateTimeField()
    AS_favorites = models.CharField(max_length=10)

    def __str__(self):
        return self.DJ_id_candidate_similar"""