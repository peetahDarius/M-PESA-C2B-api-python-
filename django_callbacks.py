""" if you are using django web framework, this is for you """
""" The following functions are hooks that will receive notifications from the mpesa daraja c2b api endpoint """


def confirm(request):
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


def validate(request):
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
