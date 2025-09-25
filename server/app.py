#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
from flask_migrate import Migrate
from models import db, Plant

# Create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


# ---- RESOURCES ----
class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return {"error": "Plant not found"}, 404
        return plant.to_dict(), 200

    def patch(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return {"error": "Plant not found"}, 404

        data = request.get_json()
        if "is_in_stock" in data:
            plant.is_in_stock = data["is_in_stock"]

        db.session.commit()
        return plant.to_dict(), 200

    def delete(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return {"error": "Plant not found"}, 404

        db.session.delete(plant)
        db.session.commit()
        # Test expects an *empty response body*, so just return empty string
        return "", 204


# ---- ROUTES ----
api.add_resource(PlantByID, "/plants/<int:id>")


# ---- ENTRY POINT ----
if __name__ == "__main__":
    app.run(port=5555, debug=True)




