from flask import Flask, request, send_from_directory, render_template
import os.path
import random
import string
import os 
import makeTree

app = Flask(__name__, static_url_path='')
app.config['TEMPLATES_AUTO_RELOAD'] = True #TODO remove when done
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/getmoves",methods=['POST'])
def submit():
    if(request.method == 'POST'):
        print("I got a submission")
        req = request.get_json()
        print("req" + str(request.get_json()))
        
        temp = makeTree.origin

        for move in req["moves"]:
            if(makeTree.containsMove(temp,move)):
                temp = makeTree.getMove(temp,move)
            else:
                return "404, tree not found"
        return(str(makeTree.formatReturn(temp)))
    else:
        print("Not a post req")
    return "NOTAVALIDPATH"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
