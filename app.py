# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
from model import session, Pet, func

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Routes
#################################################


# Main route
@app.route('/')
def home():
    return render_template('index.html')


# /api/pals
@app.route('/api/pals')
def pals():
    results = (session
               .query(Pet.pet_type, func.count())
               .group_by(Pet.pet_type))
    types = []
    counts = []
    for row in results:
        types.append(row[0])
        counts.append(row[1])

    data = {
        'x': types,
        'y': counts,
        'type': 'bar'
    }
    return jsonify(data)


# form route
@app.route('/form')
def form():
    return render_template('form.html')


# form submission route
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    name = request.form['petName']
    pet_type = request.form['petType']
    age = request.form['petAge']
    # Add data to database
    pet = Pet(name=name, pet_type=pet_type, age=age)
    session.add(pet)
    session.commit()
    # Redirect to home page
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
