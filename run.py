#! /usr/bin/env python
from src import app
from src.config import DEBUG, HOST, PORT
app.run(debug=DEBUG, host=HOST, port=PORT)
