from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index_hw_VD03.html")

#@app.route("/new/")
#@app.route("/newpages/")
#@app.route("/новаястраница/")
#def new():
    #return "New pages!"

#@app.route("/")
#@app.route("/<name>/")
#def new(name = "незнакомец"):
    #return f'Hello, {name}!'

if __name__ == "__main__":
    app.run()
