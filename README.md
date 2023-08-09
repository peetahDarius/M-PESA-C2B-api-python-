# M-PESA-C2B-api-python

The MpesaC2b model handles registering of urls and also simulating a transaction in the sandbox.
i have explained in the code the various functions in the rest of the files, apart from the models.py

The registering and simulating of transaction's code is framework independent you can use django, flask, etc.

In the django and flask files, are webhooks that will receive responsed from the daraja c2b api about completed transactions.

You will however, depending on the framework you are using, create another hook to accept the responses that will be sent to the registered url,
when a transaction has been completed.

if any difficulty using the code i've provided, please feel free to reach out to me through my email peterdariusk@gmail.com

+++++++++++++++++++++++++++++++++++++++++++ HAPPY CODING!++++++++++++++++++++++++++++++===
