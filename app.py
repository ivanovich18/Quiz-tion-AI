from dotenv import load_dotenv
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
load_dotenv()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        article = request.form["article"]
        quantity = request.form["quantity"]
        exam_type = request.form["type"]
        # print(article)
        # print(quantity)
        # print(exam_type)
        openai.api_key = "{API_KEY}"
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Make a {quantity}-item quiz,{exam_type} and put the title of the quiz at the top and the answer key at the bottom, {article}"}])
        result = response["choices"][0]["message"]["content"]
        # print(result)
        return render_template("index.html", answer=result)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
