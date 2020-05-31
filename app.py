from flask import Flask, render_template, redirect, jsonify
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

# route
@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    print("\n\n\n")
    db.mars_facts.insert_one(mars)
    return "Scraped Mars data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)  
