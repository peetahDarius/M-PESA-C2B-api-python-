""" if you are using flask web framework, this is for you """
""" The following functions are hooks that will receive notifications from the mpesa daraja c2b api endpoint """
from flask import request

@app.route("/c2b/confirm", methods=['POST'])
def confirm():
    # get data
    data = request.get_json()
    trans_id = data["TransID"]
    transaction_time = data["TransTime"]
    amount = data["TransAmount"]
    number_sending = data["MSISDN"]
    first_name = data["FirstName"]
    middle_name = data["MiddleName"]
    last_name = data["LastName"]
    print(
        f"{first_name} {middle_name} {last_name} of number {number_sending} has sent Ksh{amount} at time {transaction_time}")
    # write to a file
    file = open('confirm.json', 'a')
    file.write(json.dumps(data))
    file.close()
    return {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }


@app.route("/c2b/validation", methods=['POST'])
def validate():
    # get data
    data = request.get_json()
    # write to a file
    file = open('validate.json', 'a')
    file.write(json.dumps(data))
    file.close()
    return {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
