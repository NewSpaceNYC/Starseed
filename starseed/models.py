# https://docs.djangoproject.com/en/1.8/topics/db/models/
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from taggit.managers import TaggableManager

#MODELS

# Skill - competencies belonging to companies or individuals
class Skill(models.Model):
    skill = models.CharField(max_length=100)

# Need - competencies belonging to companies or individuals
class Need(models.Model):
    need = models.CharField(max_length=100)
    
# Entity - any person or organization
# Inspired by Users - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1032

class Entity(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    twitter_uid = models.CharField(max_length=255)
    twitter_nickname = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField(max_length=255)
    skills = models.ManyToManyField(Skill)
    needs = models.ManyToManyField(Need)
    tags = TaggableManager()
    
   # class Meta:
#        abstract = True
    
# person info -- only an individual has a first and last name
class Person(Entity):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    avatar_url = models.CharField(max_length=255)
    
class Organization(Entity):
    founding_date = models.DateField()
    # organization_type = I think this needs to be an enum rather than a table
    # there is so much interesting stuff to capture here

class Project(models.Model):
    name = models.CharField(max_length=255)
    abstract = models.TextField()

    

# Connections - how things are connected to each other

# There is a ConnectionType table because we want to be able to add new 
# connection types without hacking an enum in the code.
class ConnectionType(models.Model):
    connection_name = models.CharField(max_length=30)

class Connection(models.Model):
    from_content_type = models.ForeignKey(ContentType, related_name="from_this")
    from_object_id = models.PositiveIntegerField()
    from_content_object = GenericForeignKey('from_content_type', 'from_object_id')
    to_content_type = models.ForeignKey(ContentType, related_name="to_that")
    to_object_id = models.PositiveIntegerField()
    to_content_object = GenericForeignKey('to_content_type', 'to_object_id')
    connection_type = models.ForeignKey(ConnectionType)
    from_date = models.DateField()
    thru_date = models.DateField()

# BusinessDataPoint is a flexible table for storing metrics related to business. 
# E.g. # of employees, Total addressable market, etc.

class BusinessDataPointType(models.Model):
    business_datapoint_type_name = models.CharField(max_length=30)

class BusinessDataPoint(models.Model):
    entity = models.ForeignKey(Entity)
    business_datapoint_type = models.ForeignKey(BusinessDataPointType)
    

# Project

# User profile info. This is for the mechanics of a user of the application. 
# A user will also be an entity. This is extra information related to login.
class UserProfile(models.Model):
    entity = models.OneToOneField(Entity, primary_key=True) # https://docs.djangoproject.com/en/1.8/topics/db/examples/one_to_one/
    username = models.CharField(max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(max_length=255)
    reset_password_sent_at = models.DateField()
    remember_created_at = models.DateField()
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateField()
    last_sign_in_at = models.DateField(max_length=255)
    current_sign_in_ip = models.GenericIPAddressField()
    last_sign_in_ip = models.GenericIPAddressField()
    confirmation_sent_at = models.DateField()
    confirmed_at = models.DateField()
    confirmation_token = models.CharField(max_length=255)
    unconfirmed_email = models.EmailField(max_length=255)
    authentication_token = models.TextField()
    mail_preference = models.CharField(max_length=255)
    github_uid = models.IntegerField()
    github_login = models.CharField(max_length=255)
    personal_email_sent_on = models.DateField()
    from_date = models.DateField()
    thru_date = models.DateField()

