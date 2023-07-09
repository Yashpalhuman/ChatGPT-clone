from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai
import api

openai.api_key = api.api_key



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://yashpalchoudhary967:po0vPe6oFORjfuRO@cluster0.3c99yvy.mongodb.net/ChadGPT"
mongo = PyMongo(app)


@app.route("/")
def home():
    chats=mongo.db.chats.find({})
    myChats=[chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats =  myChats) 

@app.route("/api", methods=["GET","POST"])
def qa():
    if request.method=="POST":
        print(request.form, request.json)
        question=request.json.get("question")
        chat= mongo.db.chats.find_one({"question":question})
        print(chat)
        if chat:
            data={"question":question, "answer":f"{chat['answer']}"}
            return jsonify(data)
        else:
            data={"question":question,"answer":f"Answer of {question} "}
            response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
            print(response)
            data={"question":question,"answer": response["choices"][0]["text"]}
            mongo.db.chats.insert_one({"question":question,"answer": response["choices"][0]["text"]})
        return jsonify(data)
    data={"result":"Thank you! I'm glad you find my assistance helpful. I'm here to answer any questions you have or provide information on a wide range of topics. Feel free to ask anything else you'd like to know!"}
    return jsonify(data)


app.run(debug=True) 

