from flask import Flask
from main.reserva_controller import reservas_blueprint
from config import app, db

db.init_app(app)
app.register_blueprint(reservas_blueprint)

if __name__ == "__main__":
    with app.app_context():
        if app.config['DEBUG']:
            db.create_all()

    app.run(
        
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )

