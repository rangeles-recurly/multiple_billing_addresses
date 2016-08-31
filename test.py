
import sys, csv, logging, recurly
from recurly import Account
from logging.handlers import RotatingFileHandler



# recurly specific stuff
recurly.SUBDOMAIN = 'justdate'
recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

temp_account = Account.get('sexycustomer01')

print temp_account.address.address1

#print temp_account.shipping_addresses
#temp_account.shipping_addresses.address1 = '615 Cole St'
#temp_account.save()
'''
for account in Account.all():
    print 'Account Code: %s' % account.account_code'''
