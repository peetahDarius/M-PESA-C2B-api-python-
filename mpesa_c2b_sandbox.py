from models import MpesaC2B

"""The register url function is used to register the url that will receive confirmation messages when a 
transaction has occurred """


def register_url():
    consumer_key = 'Jfffdg5YfDjjnsfferHhfr45clrnfoutcdo99'
    consumer_secret = 'HKBDUfvtgv5legr4r9cef'
    confirmation_url = "https://mydomain.com/confirmation"
    validation_url = "https://mydomain.com/validation"
    business_short_code = "12345"
    response_type = "Completed"  # or Cancelled

    mpesa_obj = MpesaC2B(consumer_key=consumer_key, consumer_secret=consumer_secret)
    register_url_response = mpesa_obj.register_url(confirmation_endpoint=confirmation_url,
                                                   validation_endpoint=validation_url,
                                                   short_code=business_short_code,
                                                   response_type=response_type)
    return register_url_response


"""After registering your urls successfully in the sandbox, you can simulate the transaction using the simulate function
 below"""


def simulate():
    consumer_key = 'Jfffdg5YfDjjnsfferHhfr45clrnfoutcdo99'
    consumer_secret = 'HKBDUfvtgv5legr4r9cef'
    amount = 10
    command_id = "CustomerPayBillOnline"
    bill_ref_no = "Testpay"
    phone_number = "0700000000",
    business_short_code = "12345"

    mpesa_obj = MpesaC2B(consumer_key=consumer_key, consumer_secret=consumer_secret)
    mpesa_obj.short_code = business_short_code
    mpesa_obj_response = mpesa_obj.simulate_transaction(amount=amount,
                                                        command_id=command_id,
                                                        bill_ref_no=bill_ref_no,
                                                        msisdn=phone_number)
    return mpesa_obj_response
