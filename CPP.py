from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Terminal/")
def terminal():
    return render_template("Terminal.html")

@app.route("/bot/")
def bot():
    return render_template("bot.html")# to send context to html file

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg") #get data from input, where we write js to bot.html
    return str(english_bot.get_response(userText))

@app.route("/download/")
def download():
    return render_template("download.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/dockercmmd/")
def dockercmmd():
    return render_template("dockercmmd.html")

@app.route("/appachecmmd/")
def appachecmmd():
    return render_template("appachecmmd.html")

@app.route("/awscmmd/")
def awscmmd():
    return render_template("awscmmd.html")


if __name__ =="__main__":
    app.run(debug=True)

