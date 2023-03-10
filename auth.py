from imgurpython import ImgurClient
import os


def authenticate():
  client_id = os.getenv('CLIENT_ID')
  client_secret = os.getenv('CLIENT_SEC')

  client = ImgurClient(client_id, client_secret)

  # Authorization flow, pin example (see docs for other auth types)
  authorization_url = client.get_auth_url('pin')

  print("Go to the following URL: {0}".format(authorization_url))

	# Read in the pin, handle Python 2 or 3 here.
  pin = input("Enter pin code: ")

	# ... redirect user to `authorization_url`, obtain pin (or code or token) ...
  credentials = client.authorize(pin, 'pin')
  client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

  print("Authentication successful! Here are the details:")
  print("   Access token:  {0}".format(credentials['access_token']))
  print("   Refresh token: {0}".format(credentials['refresh_token']))

  return client

authenticate()
