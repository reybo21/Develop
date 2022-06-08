from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['count_total']  = 0
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count_total():
    session['count_total'] += 1
    return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
