from twilio.rest import TwilioRestClient 
from random import randint
import os
import sys

TWILIO_PHONE_NUM = os.environ['TWILIO_PHONE_NUM']

# set your own credentials as environment variables.
def get_twilio_params():
	'''
	get_twilio_params() extracts twilio client credentials that are 
	set up as environment variables on system.

	if faileds, it raises an error message on console.

	@return: a tuple of twilio crentials for creating a twilio client object.
	'''

	account_sid = "TWILIO_ACCOUNT_SID"
	auth_token = "TWILIO_AUTH_TOKEN"

	try:  
   		return (os.environ[account_sid], os.environ[auth_token])
	except KeyError: 
	   print "Please set the environment variable for twilio client."
	   sys.exit(1)

def create_client():
	'''
	create_client() creates a twilio client object by passing in
	twilio credentials extracted from bash profile.
	'''
	credentials = get_twilio_params()
	return TwilioRestClient(credentials[0], credentials[1])

def pick_random_msg():
	'''
	pick_random_msg() chooses a random text from a list of text
	messages that I sent repeatedly and frequently to people.

	it generates a random number from 0 to the len(messages),
	and then use the number as an index of a list.

	@return: a string of text message.
	'''
	messages = ['Ok', 'on my way', 'love you', 'gracias']
	position = randint(0,3)
	return messages[position]

def send_text(client, receiver, sender):
	'''
	send_text() chooses a random message and then create a 
	Twilio client to send a text message.

	@param: client is a twillio client object.
	@param: receiver is a string of a phone number which receives a message.
	@param: sencter is a string of a phone number which sends a message. 
	'''
	text_body = pick_random_msg()
	client.messages.create(to=receiver, from_=sender, body=text_body)


# execute
client = create_client()
send_text(client, "xxx", TWILIO_PHONE_NUM)