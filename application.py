from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import except_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return  'Hello!'

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    response = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        response.append(drink_data)

    return {"drinks": response}

@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink(id: int):
    drink = Drink.query.get_or_404(id)

    return {"name": drink.name, "description": drink.description}

@app.route('/drinks', methods=['POST'])
def create_drink():
    if not request.is_json:
        return {"message": "Request must be JSON"}, 400

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    try:
        drink = Drink(name=name, description=description)
        db.session.add(drink)
        db.session.commit()

        return {
            "message": "Drink created successfully!",
            "drink": {
                "id": drink.id,
                "name": drink.name,
                "description": drink.description
            }
        }, 201

    except Exception as e:
        db.session.rollback()
        print(f"Error creating drink: {e}")
        return {"message": "Error creating drink", "error": str(e)}, 500

@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id: int):
    try:
        drink = Drink.query.get_or_404(id)

        if drink is None:
            return {"message": "Drink not found"}, 404

        db.session.delete(drink)
        db.session.commit()

        return {"message": "Drink deleted successfully!"}, 204
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting drink: {e}")
        return {"message": "Error deleting drink", "error": str(e)}, 500
