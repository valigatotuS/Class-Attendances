from app import create_app
from config import Config

app = create_app(Config)
from flask_migrate import Migrate #, MigrateCommandmigrate = 
# from app import db2 as db
# Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)