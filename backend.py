from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'dhaulagiri'

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template('index.html', the_title="Search for your perfect Himalayan adventure!")

@app.route('/result', methods = ['POST', 'GET'])
def do_search() -> 'html':
    searchquery = request.form['searchquery']
    print(searchquery)
    datefrom = request.form['datefrom']
    dateto = request.form['dateto']
    difficulty = request.form['difficulty']
    title = 'Here are what you searched for: '
    return render_template('result.html', the_title=title, the_searchquery=searchquery, the_datefrom=datefrom, the_dateto=dateto, the_difficulty=difficulty,)


if __name__ == '__main__':
    app.run(debug=True)
