from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime

# Create your models here.
class DJ_user_client(models.Model):
    DJ_id_client = models.IntegerField(primary_key=True)
    DJ_user = models.CharField(max_length=10)
    DJ_password = models.CharField(max_length=10)
    DJ_email = models.CharField(max_length=50)    

    def __str__(self):
        return self.DJ_email

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