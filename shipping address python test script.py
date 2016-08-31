import sys
import os
import uuid
import datetime
import time
from pprint import pprint
sys.path.insert(1, '/Users/chrisbunting/code/recurly-client-python/')

# import recurly
from recurly import GiftCard, Delivery, Account, Address, BillingInfo, Subscription

# set logging if debug set
# example: DEBUG=true python myscript.py
if 'DEBUG' in os.environ:
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('recurly').setLevel(logging.DEBUG)

import recurly

recurly.BASE_URI = 'http://%s.lvh.me:3000/v2/'
recurly.SUBDOMAIN = 'csmb'

recurly.API_KEY = 'b3d39b00db454345870dee97c4a4ffc7'

# account = Account.get('csmb')
# billing_info = account.billing_info
# billing_info.first_name = 'Verena'
# billing_info.last_name = 'Example'
# billing_info.number = '4111-1111-1111-1111'
# billing_info.verification_value = '123'
# billing_info.month = 11
# billing_info.year = 2019
# account.update_billing_info(billing_info)
#
# print account
# print billing_info

import uuid
import datetime
import time
from recurly import Account, Address, BillingInfo, Subscription, ShippingAddress

# create a shipping address object
shad = ShippingAddress()
shad.nickname = "Work"
shad.first_name = "Verena"
shad.last_name = "Example"
shad.company = "Recurly Inc."
shad.phone = "555-555-5555"
shad.email = "verena@example.com"
shad.address1 = "123 Main St."
shad.city = "San Francisco"
shad.state = "CA"
shad.zip = "94110"
shad.country = "US"

# create an account and add the shipping address to it's list of shipping addresses
account_code = str(uuid.uuid4())
account = Account()
account.account_code = account_code
account.shipping_addresses = [shad]

account.save()

# you can get the list of shipping addresses back by calling the relatiator
shads = account.shipping_addresses()

#shad = shads[0]
# print shad.nickname

# here is an example of creating a subscription
subscription = Subscription()
subscription.plan_code = 'gold_plan'
subscription.currency = 'USD'

account_code = str(uuid.uuid4())
account = Account()
account.account_code = account_code

billing_info = BillingInfo()

billing_info.number = '4111-1111-1111-1111'
billing_info.month = 12
billing_info.year = 2019
billing_info.address1 = '400 Alabama St'
billing_info.city = 'San Francisco'
billing_info.state = 'CA'
billing_info.zip = '94110'
billing_info.country = 'US'
billing_info.number = '4111-1111-1111-1111'
billing_info.month = 12
billing_info.year = 2019
billing_info.first_name = 'Benjamin'
billing_info.last_name = 'Person'

account.billing_info = billing_info
subscription.account = account

# add the shipping address info to the subscription
subscription.shipping_address = shad

subscription.save()

# you can get the shipping address back by calling the relatiator
shad = subscription.shipping_address()

print shad

print "******"

print subscription
# you can remove the shipping address
shad.delete()

# account_code = str(uuid.uuid4())
# account = Account(account_code=account_code)
# account.email = 'verena@example.com'
# account.first_name = 'Verena'
# account.last_name = 'Example'
#
# billing_info = BillingInfo()
# billing_info.first_name = 'Verena'
# billing_info.last_name = 'Example'
# billing_info.number = '4111-1111-1111-1111'
# billing_info.verification_value = '123'
# billing_info.month = 11
# billing_info.year = 2019
# billing_info.country = 'US'
#
# address = Address()
# address.address1 = '400 Alabama St'
# address.zip = '94110'
# address.city = 'San Francisco'
# address.state = 'CA'
# address.country = 'US'
#
# delivery = Delivery()
# delivery.method = 'email'
# delivery.email_address = 'john@email.com'
# delivery.first_name = 'John'
# delivery.last_name = 'Smith'
#
# gift_card = GiftCard()
# gift_card.product_code = 'test_gift_card'
# gift_card.currency = 'USD'
# gift_card.unit_amount_in_cents = 2000
#
# delivery.address = address
# account.billing_info = billing_info
#
# gift_card.delivery = delivery
# gift_card.gifter_account = account
#
# gift_card.save()
# #
# subscription = Subscription()
# subscription.plan_code = 'gold1'
# subscription.currency = 'USD'
# subscription.gift_card = gift_card
# subscription.account = account
#
# subscription.save()


# plan_code = str(uuid.uuid4())
#
# plan = recurly.Plan(plan_code=plan_code, name=plan_code)
# plan.unit_amount_in_cents = recurly.Money(USD=1000, EUR=800)
# plan.setup_fee_in_cents = recurly.Money(USD=6000, EUR=4500)
# plan.plan_interval_length = 1
# plan.plan_interval_unit = 'months'
# plan.tax_exempt = False
# plan.save()
#
# # we only need id but fetching for effect
# measured_unit = recurly.MeasuredUnit.get(410121159393149953)
#
# addon = recurly.AddOn(
#         add_on_code='marketing_emails',
#         name='Marketing Emails',
#         unit_amount_in_cents=recurly.Money(USD=5, EUR=5),
#         add_on_type="usage",
#         optional=True,
#         usage_type="price",
#         measured_unit_id=measured_unit.id,
#         )
#
# plan.create_add_on(addon)
#
# subscription = recurly.Subscription()
# subscription.plan_code = plan_code
#
# subscription.account = recurly.Account(account_code='csmb')
#
# addon1 = recurly.SubscriptionAddOn()
# addon1.add_on_code = 'marketing_emails'
# addon1.quantity = 1
#
# subscription.subscription_add_ons = [addon1]
#
# subscription.save()
#
# time.sleep(1)
#
# # grabbing the first add_on, will probably want to filter by code
# sub_add_on = subscription.subscription_add_ons[0]
#
# usage = recurly.Usage()
# usage.amount = 100 # record 100 emails
# usage.merchant_tag = "Recording 100 emails used by customer"
# usage.recording_timestamp = datetime.datetime.utcnow()
# usage.usage_timestamp = datetime.datetime.utcnow()
#
# subscription.create_usage(sub_add_on, usage)
#
# usage = recurly.Usage()
# usage.amount = 200 # record 200 emails
# usage.merchant_tag = "Recording 200 emails used by customer"
# usage.recording_timestamp = datetime.datetime.utcnow()
# usage.usage_timestamp = datetime.datetime.utcnow()
#
# subscription.create_usage(sub_add_on, usage)
#
# # prints our 2 usage objects
# usages = sub_add_on.usage()
#
# for usage in usages:
#     print usage.amount
#     print usage.merchant_tag
