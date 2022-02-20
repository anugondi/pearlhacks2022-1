from flask import Flask, render_template, request
from home import main

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        item_type: str = request.form['item']
        plastic_type: str = request.form['type of plastic']
        food_type: str = request.form['food']
        clothes_item: str = request.form['clothes']

        main(item_type, plastic_type, food_type, clothes_item)

        render_template("result.html", result=result)
        return item_type
    return render_template("quiz.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)