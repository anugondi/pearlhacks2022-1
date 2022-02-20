from flask import Flask, render_template, request
from home import main, charity, plastic, single_use_plastic, hard_plastic, food, clothes, electronics

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
        result: str="" #final result, fix later
    



        return render_template("result.html", result=result)
    return render_template("quiz.html")

if __name__ == '__main__':
    app.run(debug=True)