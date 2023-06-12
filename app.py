from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
import openai
import os
import secrets

app = Flask(__name__)
# server = app.server
# Set a secret key for session
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["Surrogate-Control"] = "no-store"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Retrieve the result from session and clear it
        answer = session.pop("answer", "")
        return render_template("index.html", answer=answer)
    elif request.method == "POST":
        article = request.form["article"]
        quantity = request.form["quantity"]
        exam_type = request.form["type"]
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Make a {quantity}-item quiz,{exam_type} and put the title of the quiz at the top and the answer key at the bottom, {article}"}])
        result = response["choices"][0]["message"]["content"]
        session["answer"] = result  # Store the result in session
        # Redirect to clear the form submission
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
