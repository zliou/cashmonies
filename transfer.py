from visa_api_client import VisaAPIClient
import json
import datetime

valid_rec_pan = 4957030420210454

# def transfer(senderName, senderAccountNumber, recipientName, recipientPrimaryAccountNumber, amount):
def transfer(senderName, senderAccountNumber, recipientName, recipientPrimaryAccountNumber, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    visa_api_client = VisaAPIClient()
    push_funds_request = json.loads('''{
        "systemsTraceAuditNumber": 350420,
        "retrievalReferenceNumber": "401010350420",
        "localTransactionDateTime": "'''+ date + '''",
        "acquiringBin": 409999,
        "acquirerCountryCode": "101",
        "senderAccountNumber": "''' + str(senderAccountNumber) + '''",
        "transactionCurrencyCode": "USD",
        "recipientName": "''' + recipientName + '''",
        "recipientPrimaryAccountNumber": "''' + str(recipientPrimaryAccountNumber) + '''",
        "amount": "''' + str(amount) + '''",
        "businessApplicationId": "AA",
        "cardAcceptor": {
          "name": "''' + senderName + '''",
          "terminalId": "13655392",
          "idCode": "VMT200911026070",
          "address": {
            "state": "CA",
            "country": "USA",
            "zipCode": "94105"
          }
        }
    }''')

    base_uri = 'visadirect/'
    resource_path = 'fundstransfer/v1/pushfundstransactions'
    response = visa_api_client.do_mutual_auth_request(base_uri + resource_path, push_funds_request, 'Push Funds Transaction Test','post')
    return response.status_code