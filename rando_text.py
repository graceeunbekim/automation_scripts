from twilio.rest import TwilioRestClient 
from random import randint
import os
import sys

TWILIO_PHONE_NUM = os.environ['TWILIO_PHONE_NUM']

# set your own credentials as environment variables, following this format.
# TWILIO_ACCOUNT_SID='XXX'
# TWILIO_AUTH_TOKEN='YYY'
# TWILIO_PHONE_NUM='ZZZ'

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
	Texts are subtracted from a .txt file within the same directory
	and the text file is passed as a third argument.

	it generates a random number from 0 to the len(messages),
	and then use the number as an index of a list.

	@return: a string of text message.
	'''
	msg_file = sys.argv[2]
	messages = [str(line.rstrip('\n')) for line in open(msg_file)]
	position = randint(0, (len(messages)-1))
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

def __main__():
	'''
	main execute method to send a message with a randomly picked text.
	pass a receiver's phone number as an argument when running the script.
	'''
	client = create_client()
	receiver = str(sys.argv[1])
	send_text(client, receiver, TWILIO_PHONE_NUM)

# run following commend with 'xxx' being replaced by reciever's number
# python rando_text.py xxxxxxxxxx texts.txt
__main__()
