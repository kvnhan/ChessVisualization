from flask import Flask, request, send_from_directory, render_template
import os.path
import random
import string

app = Flask(__name__, static_url_path='')

#@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getmoves",methods=['POST'])
def submit():
    if(request.method == 'POST'):
        print("I got a submission")
        print("req" + str(request))
        return  "Succesful submission"
    else:
        print("Not a post req")
    return "NOTAVALIDPATH"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
