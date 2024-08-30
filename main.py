# Import
from flask import Flask, render_template,request, redirect
# Importing the database library
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Connecting SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DB
db = SQLAlchemy(app)
# Creating a DB table

#Assignment #1. Create a DB table
class Card(db.Model):
    # Creating the fields
    #id
    id = db.Column(db.Integer, primary_key=True)
    # Title
    title = db.Column(db.String(100), nullable=False)
    # Description
    subtitle = db.Column(db.String(300), nullable=False)
    # Text
    text = db.Column(db.Text, nullable=False)

    # Outputting the object and its id
    def __repr__(self):
        return f'<Card {self.id}>'


# Running the page with content
@app.route('/')
def index():
    # Displaying the DB objects
    # Assignment #2. Display the objects from the DB in index.html
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)

# Running the page with the card
@app.route('/card/<int:id>')
def card(id):
    # Assignment #2. Display the right card by its id
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Running the page and creating the card
@app.route('/create')
def create():
    return render_template('create_card.html')

# The card form
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Creating the object to send to the DB

        # Assignment #2. Create a way to store data in the DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
#if __name__ == "__main__":
 #   from waitress import serve
  #  serve(app, host="0.0.0.0", port=8080)