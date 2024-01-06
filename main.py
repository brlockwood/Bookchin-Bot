import random
import json
from mastodon import Mastodon
from datetime import datetime
import sys

# post every 3 hours
if datetime.today().hour % 3 != 0:
    sys.exit()

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

# read in json data
f = open("quotes.json")
quotes_data = json.load(f)  

def handler():

    quote = random.choice(quotes_data["quotes"])
    quote_post = '{0} \n —{1} \n \n {2}'.format(quote["quote"], quote["source"], quote["tags"])

    if len(quote_post) > 500:
        quote = random.choice(quotes_data["quotes"])
        quote_post = '{0} \n —{1} \n \n {2}'.format(quote["quote"], quote["source"], quote["tags"])

    else:
        mastodon.status_post(quote_post)
    

if __name__ == "__main__":
    handler()