from flask import Flask, render_template
import requests
import json


app = Flask(__name__)
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "Drink more coffee RIGHT NOW!"
#
# app.run(host="0.0.0.0", port=80)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()  # Convert response to JSON
        meme_large = data["preview"][-2]
        subreddit = data["subreddit"]
        return meme_large, subreddit
    except requests.exceptions.RequestException as e:
        print("Error fetching meme:", e)
        return None, None
    except (KeyError, ValueError) as e:
        print("Error parsing meme data:", e)
        return None, None

@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0",port = 80)