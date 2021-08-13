from .import bp as app
from flask import render_template, request, url_for



"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

@app.route('/')
def home():
    
    return render_template('home.html')