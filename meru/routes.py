from flask import render_template, request, redirect, url_for, make_response
from meru.forms import SearchForm
from meru import app
from meru.models import Trip, Guide_Company

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home', methods = ['POST', 'GET'])
def home():
    form = SearchForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('contact.html')

@app.route('/everest-base-camp', methods = ['POST', 'GET'])
def category_ebc():
    trips = Trip.query.filter_by(trek_code='EBC').all()
    title = 'Everest Base Camp'
    image = 'img/photo/khumbu-1.jpg'
    guides = Guide_Company.query.all()
    
    #define a dictionary to link trip_id to guide_company
    trip_guide = {}
    for trip in trips:
        trip_guide[trip.trip_id] = trip.guide_company_id
    
    #create another dictionary to link guide_company to logo_url
    guide_logo = {}
    for guide in guides:
        guide_logo[guide.guide_company_id] = guide.logo_url
    
    #link trip_id to logo_url
    trip_logo = {}
    for trip, guide in trip_guide.items():
        trip_logo[trip] = guide_logo[guide]
    
    return render_template('category.html', trips=trips, title=title, image=image, trip_logo=trip_logo)

    #logo has to go as part of trips

@app.route('/annapurna-base-camp', methods = ['POST', 'GET'])
def category_abc():
    trips = Trip.query.filter_by(trek_code='ABC').all()
    title = 'Annapurna Base Camp'
    image = 'img/photo/annapurna-1.jpg'
    guides = Guide_Company.query.all()
    
    trip_guide = {}
    for trip in trips:
        trip_guide[trip.trip_id] = trip.guide_company_id
    
    guide_logo = {}
    for guide in guides:
        guide_logo[guide.guide_company_id] = guide.logo_url
    
    trip_logo = {}
    for trip, guide in trip_guide.items():
        trip_logo[trip] = guide_logo[guide]
    
    return render_template('category.html', trips=trips, title=title, image=image, trip_logo=trip_logo)

@app.route('/everest-three-pass-trek', methods = ['POST', 'GET'])
def category_etpt():
    trips = Trip.query.filter_by(trek_code='ETPT').all()
    title = 'Everest Three Pass Trek'
    image = 'img/photo/everest-gokyo-1.jpg'
    guides = Guide_Company.query.all()
    
    trip_guide = {}
    for trip in trips:
        trip_guide[trip.trip_id] = trip.guide_company_id
    
    guide_logo = {}
    for guide in guides:
        guide_logo[guide.guide_company_id] = guide.logo_url
    
    trip_logo = {}
    for trip, guide in trip_guide.items():
        trip_logo[trip] = guide_logo[guide]
    
    return render_template('category.html', trips=trips, title=title, image=image, trip_logo=trip_logo)

@app.route('/ghorepani-poon-hill-trek', methods = ['POST', 'GET'])
def category_gpht():
    trips = Trip.query.filter_by(trek_code='GPHT').all()
    title = 'Ghorepani Poon Hill Trek'
    image = 'img/photo/poonhill-1.jpg'
    guides = Guide_Company.query.all()
    
    trip_guide = {}
    for trip in trips:
        trip_guide[trip.trip_id] = trip.guide_company_id
    
    guide_logo = {}
    for guide in guides:
        guide_logo[guide.guide_company_id] = guide.logo_url
    
    trip_logo = {}
    for trip, guide in trip_guide.items():
        trip_logo[trip] = guide_logo[guide]

    return render_template('category.html', trips=trips, title=title, image=image, trip_logo=trip_logo)

@app.route('/gokyo-lake-trek', methods = ['POST', 'GET'])
def category_glt():
    trips = Trip.query.filter_by(trek_code='GLT').all()
    title = 'Gokyo Lake Trek'
    image = 'img/photo/gokyo-lake-1.jpg'
    guides = Guide_Company.query.all()
    
    trip_guide = {}
    for trip in trips:
        trip_guide[trip.trip_id] = trip.guide_company_id
    
    guide_logo = {}
    for guide in guides:
        guide_logo[guide.guide_company_id] = guide.logo_url
    
    trip_logo = {}
    for trip, guide in trip_guide.items():
        trip_logo[trip] = guide_logo[guide]
    
    return render_template('category.html', trips=trips, title=title, image=image, trip_logo=trip_logo)