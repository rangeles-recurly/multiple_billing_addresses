'''
Multiple Shipping Adress Consumes CSV
Created: 9/17/2016
Python Version 2.7.11

This Script that consumes a CSV of addresses, adds those shipping addresses
to the account, then adds those shipping address to the subscription
'''

import sys, csv, logging
from recurly import Account, ShippingAddress
from msa_account_address_to_sub_address import copy_acc_address_to_ship_address,
    add_shipping_address_to_sub
from logging.handlers import RotatingFileHandler

# name of csv file to be passed as argument
csv_file = sys.argv[1]
log_level_desired = sys.argv[2]

def authenticate():
    logger.info('Attempting to Authenticate')
    # recurly specific stuff
    recurly.SUBDOMAIN = 'https://justdate.recurly.com'
    recurly.API_KEY = '70c38822639f49f1a17e167eb8876682'

    # Set a default currency for your API requests
    recurly.DEFAULT_CURRENCY = 'USD'
    logger.info('Finished Authenticating')

def process_csv(csv_to_process = csv_file, testing_mode = testing_mode):
    '''A function that Processes the CSV file passsed as an argument using
        a DictReader'''

    logger.info('Beginning to Process CSV: %s' % csv_to_process)
    logger.debug('Testing Mode: ' + str(testing_mode))
    # get the number of rows first
    file = open(csv_to_process)
    # subtract 1 for the header of column names
    row_count = len(file.readlines()) - 1
    logger.info('CSV file opened has %d rows to process.' % row_count)

    # open the CSV
    with open(csv_to_process, mode = 'rb') as opened_csv:
        '''use a DictReader to access specific columns, restval as the default
        for empty columns'''
        reader = csv.DictReader(opened_csv, restval = 'empty_column')

        for line in reader:
            'iterate through each line in the CSV'

            'attempt to retrieve the account by code'
            if account = retrieve_account(reader['account_code']):

                'create the shipping address'
                shad = create_shad(line)

                'add the shipping address'
                add_shad_to_account(account, shad)

                'add the shipping address to the subs'
                add_shipping_address_to_sub(account, shad)

                logger.info('Completed Updating and saving Account: %s \n'
                    % account.account_code)

            else:
                logger.error('Account not found: %s' % reader['account_code'])

def retrieve_account(account_code):
    try:
      account = Account.get(account_code)
      logger.info('Account found: %s' % account.account_code)
      return account
    except NotFoundError:
      logger.warning(('Account Not Found: {}').format(row['customername']))
      return False

def create_shad(csv_entry):
    '''creates and returns a shad'''
    logger.info('Creating a new shipping address object')
    # create a shipping address object
    shad = ShippingAddress()
    shad.nickname = "ShippingAddress"
    shad.first_name = csv_entry['first_name']
    shad.last_name = csv_entry['last_name']
    shad.phone = csv_entry['phone']
    shad.email = csv_entry['email']
    shad.address1 = csv_entry['address.address1']
    shad.address2 = csv_entry['address.address2']
    shad.city = csv_entry['city']
    shad.state = csv_entry['state']
    shad.zip = csv_entry['zip']
    shad.country = csv_entry['country']
    return shad

def add_shad_to_account(account, shad):
    '''attempts to add a shad to an account'''
    try:
        # add the shipping address to the account
        account.create_shipping_address(shad)
        account.save()
        logger.info('Adding a shipping address to account: %s'
            % account.account_code)
    except Exception, e:
        logger.error(e)
        logger.error('Unable to add a shipping address to: %s'
            % account.account_code)

def add_shipping_address_to_sub(account, shad):
    if len(account.subscriptions()) > 0:
        try:
            # add the shipping address to all subs on the account
            logger.info(('Attempting to add shipping address to {}'
                ' subscriptions.').format(len(account.subscriptions())))

            for subscription in account.subscriptions():
                subscription.shipping_address_id = shad.id
                subscription.save()
                logger.info('Added a shipping address to subscription.')

        except Exception, e:
            logger.error(e)
            logger.error('Unable to add a shipping address to subscription: %s'
                % account.account_code)
    else:
        logger.info('No subscriptions on this account.')

def initiate_logging(log_level = log_level_desired):
    global logger

    # set format of log entries
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s '
        '%(lineno)d: %(message)s')

    ''' get logger and set level designated by user. this is for printing to
        file only'''
    logger = logging.getLogger('TapInfluence.CSVUploader')
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
    logger.info('***** Starting New Upload ***** %s \n' % csv_file)
    authenticate()
    process_csv()
