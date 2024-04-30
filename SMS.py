from __future__ import print_function
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException


def SendSMS(message, phoneno):
	# Configure HTTP basic authorization: BasicAuth
	configuration = clicksend_client.Configuration()
	configuration.username = 'kakit20040127@gmail.com'
	configuration.password = '3F7BE496-C98D-4CE2-2018-596B529D65AA'
	targetPhoneNumber = f"+852{phoneno}"

	# create an instance of the API class
	api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

	# If you want to explictly set from, add the key _from to the message.
	sms_message = SmsMessage(source="php",
	                        body=message,
        	                to=targetPhoneNumber,
                	        schedule=1436874701)

	sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

	try:
		# Send sms message(s)
		api_response = api_instance.sms_send_post(sms_messages)
		return api_response
	except ApiException as e:
		return "Exception when calling SMSApi->sms_send_post: %s\n" % e