from flask import render_template, request, redirect, url_for, make_response
from meru.forms import SearchForm
from meru import app
from meru.models import Trip

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home', methods = ['POST', 'GET'])
def home():
    form = SearchForm()
    return render_template('index.html', form=form)


@app.route('/category', methods = ['POST', 'GET'])
def category():
    trips = Trip.query.filter_by(trek_code='EBC').all()
    return render_template('category.html', trips=trips)


'''
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    """ form = SearchForm()
    if form.validate_on_submit():
        flash(f'Search results for {form.adventure.data}!', 'success')
        return redirect(url_for('homepage')) """
    return render_template('compare.html')


@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    return render_template('contact.html')

@app.route('/result', methods = ['POST', 'GET'])
def result() -> 'html':
    """
    if request.method == 'POST':
        searchquery = request.form['searchquery']
        month = request.form['month']
        year = request.form['year']
        difficulty = request.form['difficulty']
        
        
        conn = mysql.connector.connect(host='127.0.0.1', 
                                    user=os.environ['DB_USER'],
                                    password=os.environ['DB_PASSWORD'],
                                    database='mountaineruDB')
        cursor = conn.cursor()
        _SQL = """ """ SELECT * FROM MountainTour
                WHERE TourName LIKE %s
                AND month(StartDate) = %s
                AND year(StartDate) = %s
                AND Difficulty = %s """ """
        args = ('%' + searchquery + '%'), month, year, difficulty
        cursor.execute(_SQL, args)
        searchresult = cursor.fetchall()
        cursor.close()
        conn.close()
     """   
    return render_template('category.html')
'''