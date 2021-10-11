-------------------------
import requests


def speak(text):

	url = "http://localhost:5000/speak"

	requests.get(url, data={"text": text})
  -------------------------------------------
  
  from flask import Flask, request, url_for, send_from_directory, jsonify
import os

app = Flask(__name__)

@app.route("/upload")
def upload():
      	img = request.files.get("image")
	      img.save(os.path.join("images", img.filename))

	return jsonify({'url' : request.url_root[:-1] + url_for("get_image", name=img.filename)})


@app.route("/image/<name>")
def get_image(name):
	return send_from_directory(os.path.join("images"), name)

if __name__ == "__main__":
	app.run()
  ---------------------------------------------------------
  
  from flask import Flask, request, jsonify
from gtts import gTTS
from playsound import playsound
import os

app = Flask(__name__)

    def say(text):
	      tts = gTTS(text)
	            tts.save(os.path.dirname(os.path.realpath(__file__)) + "text.mp3")
	             playsound(os.path.dirname(os.path.realpath(__file__)) + "text.mp3")
	             os.remove(os.path.dirname(os.path.realpath(__file__)) + "text.mp3")


@app.route("/speak")
def speak():
	text = request.values.get("text")
	say(text)
	return jsonify({"status": True})

if __name__ == "__main__":
	app.run()
  ---------------------------------------------------------------
  
  
