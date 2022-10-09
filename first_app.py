from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home/<string:name>/posts/<int:id>")
def hello(name,id):
    return "<h1>Hello </h1>" + name + "<h1>, your id is = </h1>" + str(id)

@app.route("/onlyget", methods=['GET','POST'])
def get_req():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)