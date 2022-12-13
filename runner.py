import os
import sys
from random import randint

import pymongo
from dotenv import load_dotenv

from flask import Flask, request, render_template, jsonify
#from pymongo import MongoClient


load_dotenv()
CONNECTION_STRING = "mongodb://cotmon-1986996464:tE7Tlv9V8CMhM7fxoo2lvG9QMkqFH0BmLBuW53i2qLRXv2A0mHcCoakjeVdVF0cbbnoIlqMR8RLgACDbwmI5zA==@cotmon-1986996464.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cotmon-1986996464@"


DB_NAME = "cotiss_azanon_v02"
COLLECTION_NAME = "feedback"
client = pymongo.MongoClient(CONNECTION_STRING)

# Create database/collection if it doesn't exist
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
"""Create new document and upsert (create or replace) to collection"""
# new_record = {
#     "category": "Feedback",
#     "feedback_message": "This is a new message",
#     "country": "New Zealand",
# }
# result = collection.insert_one(new_record)

# print("Upserted document with _id {}\n".format(result.upserted_id))
print("Databases available are: ", client.list_database_names())
print("Collections available are: ", db.list_collection_names())
for records in collection.find():
    print(records)

print("CONNECTION STRING IN RUNNER IS ", CONNECTION_STRING, "<<<<<<<<\n")


# define the flask app
app = Flask(__name__)
app.config["MONGO_URI"] = CONNECTION_STRING

# define the home page route
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/all_feedback', methods=["GET"])
def refresh_db_data():
    # data = {"user_rating":"", "feedback":""}
    for records in collection.find():
        print(records)
    return render_template("index.html")

@app.route('/showData')
def showData():
    showDataList = []
    for i in collection.find({},{"_id":0}):
        showDataList.append(i)
  
    return jsonify(showDataList)


# This route gets data from html form and inserts data into database
@app.route('/upload', methods=["POST", "GET"])
def upload():
    # Creating an empty dictionary to hold data from form and database
    # data = {"user_rating":"", "feedback":""}
    data = {"feedback":""}
    if request.method == "POST":
        print("DB is ", db, "<<<<<<<\n")
        print("COLLECTION is ", collection, "<<<<<<<\n")
        # print("Rating is ", request.form['user_rating'], "<<<<<<<\n")
        print("Feedback is ", request.form['feedback'], "<<<<<<<\n")

        # data["user_rating"] = request.form['user_rating']
        data["feedback"] = request.form['feedback']

    collection.insert_one(data)
    print("Collections available now are: ", db.list_collection_names())
    # for records in collection.find():
    #     print(records)
    # return render_template("/all_feedback")
    return render_template("index.html")



# start the flask server
if __name__ == '__main__':
    
    app.run(debug=True)