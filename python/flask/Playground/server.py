from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/play/')
def index():
    return render_template("index.html", multiply = 3, change_color = "teal")

@app.route('/play/<int:num>/')
def multiply(num):
    return render_template("index.html", multiply = num, change_color = "teal")

@app.route('/play/<int:num>/<string:color>/')
def multiply_color(num,color):
    return render_template("index.html", multiply = num, change_color = color)

if __name__=="__main__":
    app.run(debug=True)