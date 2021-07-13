from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is the way"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name']=request.form['name']
    session['dojo_location']=request.form['dojo_location']
    session['fav_language']=request.form['fav_language']
    session['comment']=request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug = True)