from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        return render_template("result.html")
    return render_template("quiz.html")


if __name__ == '__main__':
    app.run(debug=True)