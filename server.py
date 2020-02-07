from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "a"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlanguage = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("result.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments)

    


    
   
if __name__=="__main__":
    
    app.run(debug=True) 