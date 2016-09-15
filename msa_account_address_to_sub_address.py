'''
Multiple Shipping Adress Copying
Created: 8/17/2016
Python Version 2.7.11

This Script that copies Account Addresses to Subscription Addresses
'''

import sys, csv, logging, recurly
from recurly import Account, ShippingAddress
from logging.handlers import RotatingFileHandler

# name of csv file to be passed as argument
#csv_file = sys.argv[1]
log_level_desired = sys.argv[1]
testing_mode = (sys.argv[2] == 'True')

def authenticate():
    logger.info('Attempting to Authenticate')
    # recurly specific stuff
    recurly.SUBDOMAIN = 'justdate'
    recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

    # Set a default currency for your API requests
    recurly.DEFAULT_CURRENCY = 'USD'
    logger.info('Finished Authenticating')

def retrieve_and_iterate_accounts():
    '''Function that retrieves ONLY ACTIVE accounts and passes it to
        copy the address'''

    logger.info('Retrieving all Accounts')
    # accounts = Account.all()
    '''gen_ex = (account for account in Account.all() if
        account.state == 'active')'''

    # get length without O(n) list generation
    #num_of_accounts = sum(1 for x in gen_ex)

    '''logger.info(('Retrieved a total of: {} Active accounts').format(
        num_of_accounts))'''

    logger.info('Starting copying of Account Address to Shipping Address')

    try:
        for account in Account.all():
            if account.state == 'active':
                copy_acc_address_to_ship_address(account)
    except Exception, e:
        logger.error(e)

def copy_acc_address_to_ship_address(account):
    '''Function that takes an account and copies their account address
    to the shipping address.'''

    logger.info('Creating a new shipping address object')
    # create a shipping address object
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


    try:
        # add the shipping address to the account
        account.create_shipping_address(shad)
        account.save()
        logger.info('Added a shipping address to account: %s'
            % account.account_code)
    except Exception, e:
        logger.error(e)
        logger.error('Unable to add a shipping address to: %s'
            % account.account_code)

    if len(account.subscriptions()) > 0:
        try:
            # add the shipping address to all subs on the account
            logger.info(('Attempting to add shipping address to {}'
                ' subscriptions.').format(len(account.subscriptions())))

            for subscription in account.subscriptions():
                # subscription = Subscription.get(subscription)
                add_shipping_address_to_sub(account, shad, subscription)
        except Exception, e:
            logger.error(e)
    else:
        logger.info('No subscriptions on this account.')

    logger.info('Completed Updating and saving Account: %s \n'
        % account.account_code)

def add_shipping_address_to_sub(account, shad, subscription):
    try:
        subscription.shipping_address_id = shad.id
        subscription.save()
        logger.info('Added a shipping address to subscription.')
    except Exception, e:
        logger.error(e)
        logger.error('Unable to add a shipping address to subscription: %s'
            % account.account_code)


def initiate_logging(log_level = log_level_desired):
    '''log levels: INFO, WARNING, ERROR, DEBUG'''
    global logger

    # set format of log entries
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s '
        '%(lineno)d: %(message)s')

    ''' get logger and set level designated by user. this is for printing to
        file only'''
    logger = logging.getLogger('Recurly.MSACopier')
    logger.setLevel(str.upper(log_level))

    # set name of log file, set to multiple files instead
    #file_handler = logging.FileHandler('example.log')
    file_handler = RotatingFileHandler('log_file.log', mode = 'a',
        maxBytes = 5*1024*1024, backupCount = 2, encoding = None, delay = 0)

    # this prints out to console
    console_handler = logging.StreamHandler(sys.stdout)

    # assign formatting to the handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the loggers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

if __name__ == "__main__":
    initiate_logging()
    logger.info('***** Starting New Address Transfer ***** %s \n')
    authenticate()
    retrieve_and_iterate_accounts()
