from flask import Flask
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.secret_key='secret'
csrf=CSRFProtect(app)


from project import routs