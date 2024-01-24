from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html",result=90.2-(50.6*rate)))
    else:
        return(render_template("index.html",result="Waiting for user input"))

if __name__ == "__main__":
    app.run()
