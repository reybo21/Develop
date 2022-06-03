from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def default_board():
    return render_template("index.html", row = 8, col = 8)

@app.route('/<int:row>/')
def board_change_rows(row):
    return render_template("index.html", row = row, col = 8)

@app.route('/<int:row>/<int:col>/')
def board_create_own(row,col):
    return render_template("index.html", row = row, col = col)

if __name__=="__main__":
    app.run(debug=True)