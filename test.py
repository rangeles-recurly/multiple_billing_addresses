
import sys, csv, logging, recurly
from recurly import Account, ShippingAddress
from logging.handlers import RotatingFileHandler



# recurly specific stuff
recurly.SUBDOMAIN = 'justdate'
recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

account = Account.get('sexycustomer03')

#foo = account.shipping_addresses()
'''
account = Account(account_code='sexycustomer03')
account.email = 'verena@example.com'
account.first_name = 'Verena'
account.last_name = 'Example'''
foo = account.shipping_addresses()
shad = ShippingAddress()

'''
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
shad.account = account'''


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





#for shad in temp_account.shipping_addresses()
#for shad in temp_account.shipping_addresses():
#    print shad.nickname
try:
    # print account.shipping_addresses
    #account.shipping_addresses = [shad]
    #account.shipping_addresses().append(shad)
    # foo[0].save()
    shad.save()
except Exception, e:
    print e

print account.shipping_addresses()


#print temp_account.shipping_addresses
#temp_account.shipping_addresses.address1 = '615 Cole St'
#temp_account.save()

'''
gen_ex = (account for account in Account.all() if account.state == 'active')

for account in gen_ex:
    print 'Account Code: %s' % account.account_code'''
