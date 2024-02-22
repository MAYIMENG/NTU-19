from flask import Flask, request, render_template
import replicate
import os
import time
from openai import OpenAI


openai_api_key = os.environ["OPENAI_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = "r8_GHyHGLZOntMYvtEgUZiE9vFdtMZrj7L2ZTtgM"


model = OpenAI(api_key = openai_api_key,
               base_url = "https://api.chatanywhere.tech/v1")

app = Flask(__name__)

r = ""
first_time = 1

# index
@app.route("/", methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

#main
@app.route("/main", methods=["GET", "POST"])
def main():
    global r, first_time
    if first_time == 1:
        r = request.form.get("r")
        first_time = 0
    return (render_template("main.html", r=r))

#ntu
@app.route("/about_ntu", methods=["GET", "POST"])
def about_ntu():
    return (render_template("about_ntu.html"))
  
#image
@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return (render_template("image_gpt.html"))

@app.route("/image_result", methods=["GET", "POST"])
def image_result():
    q = request.form.get("q")
    r = replicate.run("stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={ 
        "prompt": q,}
)
    time.sleep(5)
    return (render_template("image_result.html",r=r[0]))

#text
@app.route("/text_gpt", methods=["GET", "POST"])
def text_gpt():
    return (render_template("text_gpt.html"))

@app.route("/text_result", methods=["GET", "POST"])
def text_result():
    q = request.form.get("q")
    r = model.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "user",
         "content": q
        }
    ],
)
    time.sleep(5)
    return (render_template("text_result.html",r=r.choices[0].message.content))

# end
@app.route("/end", methods=["GET", "POST"])
def end():
    global first_time
    first_time = 1
    return (render_template("end.html"))

@app.route("/real_end", methods=["GET", "POST"])
def real_end():
    return (render_template("real_end.html"))

if __name__ == "__main__":
    app.run()
