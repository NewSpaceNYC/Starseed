# https://docs.djangoproject.com/en/1.8/topics/db/models/
from django.db import models

#MODELS
# Users - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1032
# Product - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L708
#         - big table
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

# User https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1032
class User(models.Model):

# Product https://github.com/assemblymade/meta/blob/master/db/schema.rb#L708
class Product(models.Model):
    #fill this in lean...
    name = models.CharField(max_length=30)
    fill_in = models.CharField(max_length=30)
    #these things
    
# Bounty_Posting https://github.com/assemblymade/meta/blob/master/db/schema.rb#L107
class Bounty_Posting(models.Model)

# Vesting - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L1125
class Vesting(models.Model)

# Activity - https://github.com/justquick/django-activity-stream 
class Activity(models.Model)

# Allocation_Event - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L39 
class Allocation_Event(models.Model)

# Attachment https://github.com/assemblymade/meta/blob/master/db/schema.rb#L72
class Attachment(models.Model)

# Btc_Payments https://github.com/assemblymade/meta/blob/master/db/schema.rb#L116
class btc_payment(models.Model)

# Profit_Report https://github.com/assemblymade/meta/blob/master/db/schema.rb#L781
class Profit_Report(models.Model)

# Tip https://github.com/assemblymade/meta/blob/master/db/schema.rb#L896
class Tip(models.Model)

# Subscriber - https://github.com/assemblymade/meta/blob/master/db/schema.rb#L868
class Subscriber(models.Model)


