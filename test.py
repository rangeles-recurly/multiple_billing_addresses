
import sys, csv, logging, recurly
from recurly import Account, ShippingAddress
from logging.handlers import RotatingFileHandler



# recurly specific stuff
recurly.SUBDOMAIN = 'justdate'
recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

account = Account.get('asdfawesome')

shad = ShippingAddress()
shad.nickname = "ShippingAddress"
shad.first_name = account.first_name
shad.last_name = account.last_name
shad.phone = account.address.phone
shad.email = account.email
shad.address1 = account.address.address1
shad.address2 = account.address.address2
shad.city = account.address.city
shad.state = account.address.state
shad.zip = account.address.zip
shad.country = account.address.country

print shad.address1
print shad.first_name
print shad.zip

account.create_shipping_address(shad)


for subscription in account.subscriptions():
    subscription.shipping_address_id = shad.id
    subscription.save()


# try:
#     # print account.shipping_addresses
#     #account.shipping_addresses = [shad]
#     #account.shipping_addresses().append(shad)
#     # foo[0].save()
#     account.create_shipping_address(shad)
#     account.save()
# except Exception, e:
#     print e

print account.shipping_addresses()


#print temp_account.shipping_addresses
#temp_account.shipping_addresses.address1 = '615 Cole St'
#temp_account.save()

'''
gen_ex = (account for account in Account.all() if account.state == 'active')

for account in gen_ex:
    print 'Account Code: %s' % account.account_code'''
