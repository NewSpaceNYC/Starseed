# https://docs.djangoproject.com/en/1.8/topics/db/models/
from django.db import models

#MODELS
# Users - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1032
# Product - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L708
#         - huge table
# Bounty_Postings - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L107
# Vesting - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1125
# Activity - https://github.com/justquick/django-activity-stream 
#            - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L22
#            - https://pypi.python.org/pypi/django-notifications-hq/0.6.0 (this gives more options)
# Allocation_Event - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L39 
# Attachment - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L72
# Btc_Payment - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L116
# Profit_Report - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L781
# Tip - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L896
# Subscriber - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L868

# User - in Django this these extra things can go into "UserProfile" instead of just "User"
# Users - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1032
class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default='false')
    email = models.EmailField(max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(max_length=255)
    reset_password_sent_at = models.DateField()
    remember_created_at = models.DateField()
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateField()
    last_sign_in_at = models.DateField(max_length=255)
    current_sign_in_ip = models.GenericIPAddressField()
    last_sign_in_ip = models.GenericIPAddressField()
    created_at = models.DateField()
    updated_at = models.DateField(max_length=255)
    confirmation_sent_at = models.DateField()
    confirmed_at = models.DateField()
    confirmation_token = models.CharField(max_length=255)
    unconfirmed_email = models.CharField(max_length=255)
    email_failed_at = models.DateField()
    facebook_uid = models.CharField(max_length=255)
    location = models.TextField()
    avatar_url = models.CharField(max_length=255)
    authentication_token = models.TextField()
    bio = models.TextField()
    archetype = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    mail_preference = models.CharField(max_length=255)
    github_uid = models.IntegerField()
    github_login = models.CharField(max_length=255)
    payment_option = models.CharField(max_length=255)
    paypal_email = models.CharField(max_length=255)
    bank_account_id = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_last4 = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_zip = models.CharField(max_length=255)
    address_country = models.CharField(max_length=255)
    personal_email_sent_on = models.DateField()
    twitter_uid = models.TextField()
    twitter_nickname = models.TextField()

# Product https://github.com/assemblymade/meta/blob/master/db/schema.rb#L708
class Product(models.Model):
    #fill this in lean...
    username = models.CharField(max_length=255)
    fill_in = models.CharField(max_length=30)
    
    #https://docs.djangoproject.com/en/1.7/ref/models/fields/
    
    
# Bounty_Posting https://github.com/assemblymade/meta/blob/master/db/schema.rb#L107
class Bounty_Posting(models.Model):
    pass

# Vesting - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1125
class Vesting(models.Model):
    pass

# Activity - https://github.com/justquick/django-activity-stream 
#class Activity(models.Model): this comes with django-activity-stream

# Allocation_Event - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L39 
class Allocation_Event(models.Model):
    pass

# Attachment https://github.com/assemblymade/meta/blob/master/db/schema.rb#L72
class Attachment(models.Model):
    pass

# Btc_Payments https://github.com/assemblymade/meta/blob/master/db/schema.rb#L116
class btc_payment(models.Model):
    pass

# Profit_Report https://github.com/assemblymade/meta/blob/master/db/schema.rb#L781
class Profit_Report(models.Model):
    pass

# Tip https://github.com/assemblymade/meta/blob/master/db/schema.rb#L896
class Tip(models.Model):
    pass

# Subscriber - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L868
class Subscriber(models.Model):
    pass


