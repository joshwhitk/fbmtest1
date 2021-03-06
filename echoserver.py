from flask import Flask, request
import json
import requests

app = Flask(__name__)
#url: https://fbmtest1.herokuapp.com/
#facebook page: Fbmtest1  access token:
#facebook app: Jfbmtest1
#from tutorial https://tsaprailis.com/2016/06/02/How-to-build-and-deploy-a-Facebook-Messenger-bot-with-Python-and-Flask-a-tutorial/
#requirements.txt: web: gunicorn echoserver:app
# pip install flask
# pip install gunicorn
# pip install requests
# save this python file as echoserver.py

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAF4eghnRP0BAJYrSUoBdBxCDdIZCguIGD5qFoyG6CnQxFFU8EQGjY4IZCI3oIe3NZCF5NdHkSyxgj4MYJZCpniZCDnBieJnorx9Bci1i0MoHgo4qSaEsIZBnf2ZBrvSLGz1B389gZB3kSmRagRTMdTZAr3sgXCuK9MuVZCUKWAJRIwAZDZD'

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print "Handling Messages"
  payload = request.get_data()
  print payload
  for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)
    message = "Hugo heard you say: " + message
    send_message(PAT, sender, message)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"


def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """

  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

if __name__ == '__main__':
    app.run()

# =======================================
# GAME LOGIC
# =======================================

players-list = ['oscar', 'j', 'angus']
current-location = ''

def init_game(sender, message):
    print ("game got " + message + " from " + sender)
    nextcmd = ''
    if find_player(sender):
        game_state = load_game(sender)
        play(sender, game_state)
    else:
        create_player(sender)
        nextcmd = play(sender,'new')
    if nextcmd == 'quit':
        save_game(sender)
        return False
    else return True

def find_player(sender):
    if sender in players-list:
        return True
    else return False

def load_game(sender):
    current-location = "Placheholder Oakland"

def play(player_name, game_status):
    while nextcmd != 'quit':
        send_message(PAT, sender, current-location + " command? (quit):")
    return nextcmd

def create_player(sender):
    players-list.append(sender)
    return sender


