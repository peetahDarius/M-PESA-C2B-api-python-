from models import MpesaC2B

"""The register url function is used to register the url that will receive confirmation messages when a 
transaction has occurred """

"""The only difference between the sandbox code and the production code is the safaricom endpoints/urls
eg the production urls are normally 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials' and 
'https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl' whereas the sandbox urls are normally 
'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials' and 
'https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl'
 We therefore have to set the endpoints in the code"""


def register_url():
    consumer_key = 'Jfffdg5YfDjjnsfferHhfr45clrnfoutcdo99'
    consumer_secret = 'HKBDUfvtgv5legr4r9cef'
    confirmation_url = "https://mydomain.com/confirmation"
    validation_url = "https://mydomain.com/validation"
    business_short_code = "12345"
    response_type = "Completed"  # or Cancelled
    authorization_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    register_url_endpoint = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    mpesa_obj = MpesaC2B(consumer_key=consumer_key, consumer_secret=consumer_secret)
    mpesa_obj.production_urls(authorization_url=authorization_url, register_urls_endpoint=register_url_endpoint)
    register_url_response = mpesa_obj.register_url(confirmation_endpoint=confirmation_url,
                                                   validation_endpoint=validation_url,
                                                   short_code=business_short_code,
                                                   response_type=response_type)
    return register_url_response


"""You cannot simulate a transaction at this time, after you've gone live"""

