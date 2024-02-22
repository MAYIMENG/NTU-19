from flask import Flask,request,render_template
import replicate
import os
import time
from openai import OpenAI

app = Flask(__name__)
os.environ["REPLICATE_API_TOKEN"]="r8_2idkAutIh1jCAVVRIbEDgqt9zNUdbhG2cS1AF"

r = ""
first_time = 1

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global r,first_time
    if first_time==1:
        r = request.form.get("r")
        first_time=0
    return(render_template("main.html",r=r))

@app.route("/image_gpt",methods=["GET","POST"])
def image_gpt():
    return(render_template("image_gpt.html"))

@app.route("/text_gpt",methods=["GET","POST"])
def text_gpt():
    return(render_template("text_gpt.html"))

@app.route("/text_result",methods=["GET","POST"])
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
    time.sleep(10)
    return(render_template("text_result.html",r=r.choices[0].message.content))


@app.route("/end",methods=["GET","POST"])
def end():
    global first_time
    first_time = 1
    return(render_template("end.html"))

if __name__ == "__main__":
    app.run()
