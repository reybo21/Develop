from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language_preference'] = request.form['language_preference']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)