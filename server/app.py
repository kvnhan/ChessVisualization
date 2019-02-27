from flask import Flask, request, send_from_directory, render_template
import os.path
import random
import string
import os 
#import makeTree

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/getmoves",methods=['POST'])
def submit():
    if(request.method == 'POST'):
        print("I got a submission")
        req = request.get_json()
        print("req" + str(request.get_json()))
        print(req["moves"][0])
        
        temp = origin

        for move in req["moves"]:
            if(containsMove(temp,move)):
                temp = getMove(temp,move)
                return(formatReturn(temp))
            else:
                return "404, tree not found"

        return  "Succesful submission"
    else:
        print("Not a post req")
    return "NOTAVALIDPATH"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
