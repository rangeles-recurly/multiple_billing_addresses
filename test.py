
import sys, csv, logging, recurly
from recurly import Account
from logging.handlers import RotatingFileHandler



# recurly specific stuff
recurly.SUBDOMAIN = 'justdate'
recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

temp_account = Account.get('sexycustomer01')

foo = temp_account.shipping_addresses()


#for shad in temp_account.shipping_addresses()
for shad in temp_account.shipping_addresses():
    print shad.nickname


#print temp_account.shipping_addresses
#temp_account.shipping_addresses.address1 = '615 Cole St'
#temp_account.save()

'''
gen_ex = (account for account in Account.all() if account.state == 'active')

for account in gen_ex:
    print 'Account Code: %s' % account.account_code'''
