import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=400,
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """The following is a conversation between an Question answering bot and a client. The agent will
    answer the question in 3-4 sentences.
    Example
    Client: What are linked list?
    A linked list is a type of data structure in which each element, or "node," is connected to the next
    element in the list using a pointer. 
    It allows for efficient insertion and removal of elements, as well as the ability to quickly traverse
    the list.
Animal: {}
Names:""".format(
        animal.capitalize()
    )
