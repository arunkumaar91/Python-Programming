from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC28e5e050c7bcea0eb68c6ff1c1cb0948"
# Your Auth Token from twilio.com/console
auth_token  = "7001ebf93d07b08ddae8de7711b87c38"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+14433607701", 
    from_="+14433603851",
    body="Hello from Python Developer Arun!")

print(message.sid)
