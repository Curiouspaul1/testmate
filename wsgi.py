from main import app, db
from extensions import migrate
from models import *

migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()
