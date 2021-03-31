# Import dependencies 
from flask import Flask, render_template
from flask_pymongo import flask_pymongo
import scraping 

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the "home" route, which will include an HTML template
# of the MongoDB "mars" database collection 
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Define a route which will scrape data and update the "mars" database 
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# Run Flask 
if __name__ == "__main__":
   app.run()
