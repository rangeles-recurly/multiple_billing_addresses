
import sys, csv, logging, recurly
from recurly import Account
from logging.handlers import RotatingFileHandler



# recurly specific stuff
recurly.SUBDOMAIN = 'justdate'
recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

for account in Account.all():
    print 'Account Code: %s' % account.account_code
