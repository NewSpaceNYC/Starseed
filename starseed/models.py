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

# User - in Django this these extra things can go into UserProfile
"""
    t.string   "name",                              limit: 255
    t.string   "customer_id",                       limit: 255
    t.boolean  "is_staff",                                      default: false,   null: false
    t.string   "email",                             limit: 255,                   null: false
    t.string   "encrypted_password",                limit: 255
    t.string   "reset_password_token",              limit: 255
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer  "sign_in_count",                                 default: 0
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.inet     "current_sign_in_ip"
    t.inet     "last_sign_in_ip"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.datetime "confirmation_sent_at"
    t.datetime "confirmed_at"
    t.string   "confirmation_token",                limit: 255
    t.string   "unconfirmed_email",                 limit: 255
    t.datetime "email_failed_at"
    t.string   "facebook_uid",                      limit: 255
    t.text     "location"
    t.datetime "last_request_at"
    t.string   "avatar_url",                        limit: 255
    t.text     "extra_data"
    t.string   "authentication_token",              limit: 255
    t.text     "bio"
    t.string   "archetype",                         limit: 255
    t.string   "username",                          limit: 255,                   null: false
    t.string   "mail_preference",                   limit: 255, default: "daily", null: false
    t.integer  "github_uid"
    t.string   "github_login",                      limit: 255
    t.string   "payment_option",                    limit: 255
    t.string   "paypal_email",                      limit: 255
    t.string   "bank_account_id",                   limit: 255
    t.string   "bank_name",                         limit: 255
    t.string   "bank_last4",                        limit: 255
    t.string   "address_line1",                     limit: 255
    t.string   "address_line2",                     limit: 255
    t.string   "address_city",                      limit: 255
    t.string   "address_state",                     limit: 255
    t.string   "address_zip",                       limit: 255
    t.string   "address_country",                   limit: 255
    t.datetime "personal_email_sent_on"
    t.text     "twitter_uid"
    t.text     "twitter_nickname"
    t.uuid     "recent_product_ids",                                                           array: true
    t.string   "remember_token",     
 
   """
#django has a built in User model
#class User(models.Model):
#    username = models.CharField(max_length=255)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)

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


