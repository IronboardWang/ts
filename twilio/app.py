from twilio.rest import Client
import config
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="...",
    body="this is our first message"
)
