import sys
import os
import uuid
import datetime
import time
from pprint import pprint
sys.path.insert(1, '/Users/chrisbunting/code/recurly-client-python/')
import recurly
# set logging if debug set
# example: DEBUG=true python myscript.py
if 'DEBUG' in os.environ:
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('recurly').setLevel(logging.DEBUG)
recurly.BASE_URI = 'http://%s.lvh.me:3000/v2/'
recurly.SUBDOMAIN = 'csmb'
recurly.API_KEY = 'b3d39b00db454345870dee97c4a4ffc7'
account = recurly.Account.get('csmb')
# create a shipping address object
shad = recurly.ShippingAddress()
shad.nickname = "Work"
shad.first_name = account.first_name
shad.last_name = "Example"
shad.company = "Recurly Inc."
shad.phone = "555-555-5555"
shad.email = "verena@example.com"
shad.address1 = "123 Main St."
shad.city = "Sanny Francisco"
shad.state = "CA"
shad.zip = "94110"
shad.country = "US"
# create an account and add the shipping address to it's list of shipping addresses
# account_code = str(uuid.uuid4())
# account = Account()
# account.account_code = account_code
account.shipping_addresses = [shad]
account.save()
