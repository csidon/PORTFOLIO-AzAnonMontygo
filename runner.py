import os
import sys
from random import randint
from pprint import pprint

import pymongo

import bson
from dotenv import load_dotenv

from flask import Flask, request, render_template, jsonify
import random



load_dotenv(verbose=True)
CONNECTION_STRING = "mongodb://cotmon-1986996464:tE7Tlv9V8CMhM7fxoo2lvG9QMkqFH0BmLBuW53i2qLRXv2A0mHcCoakjeVdVF0cbbnoIlqMR8RLgACDbwmI5zA==@cotmon-1986996464.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cotmon-1986996464@"


DB_NAME = "cotiss_azanon_v03"
COLLECTION_NAME = "feedback"
client = pymongo.MongoClient(CONNECTION_STRING)

# Create database/collection if it doesn't exist
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Check the number of documents (records) in database
def countdocs():
    num_docs = collection.count_documents({})
    print("You have >>>", num_docs, "<<< records in your database")
    # Set the id for the new feedback
    return num_docs

# Gets and returns a piece of random feedback
def get_rand_feedback():
    rand_feedback_index = 0
    rand_feedback = ""
    rand_feedback_index = random.randint(1, countdocs())
    print(rand_feedback_index, "<<<<<< This is the random record I'm trying to pull")
    rand_record = list(collection.find({"_id": rand_feedback_index}))[0]
    rand_feedback = rand_record['feedback']
    return rand_feedback

# For debugging: print("Upserted document with _id {}\n".format(result.upserted_id))
print("Databases available are: ", client.list_database_names())
print("Collections available are: ", db.list_collection_names())
# for records in collection.find():
#     print(records)
print("CONNECTION STRING IN RUNNER IS ", CONNECTION_STRING, "<<<<<<<<\n")


# define the flask app
app = Flask(__name__)
app.config["MONGO_URI"] = CONNECTION_STRING

# define the home page route
@app.route('/')
def hello_world():
    clean_feedback = ""
    clean_feedback = get_rand_feedback()
    return render_template("index.html", feedback=clean_feedback)


@app.route('/showData')
def showData():
    showDataList = []
    for i in collection.find({},{"_id":0}):
        showDataList.append(i)
  
    return jsonify(showDataList)


# This route gets data from html form and inserts data into database
@app.route('/upload', methods=["POST", "GET"])
def upload():

    # Set the id for the new feedback
    new_id = countdocs() + 1
    print("Checking new id number >> " , new_id)

    # Creating an empty dictionary to hold data from form and database
    data = {"_id":new_id, "feedback":""}
    if request.method == "POST":
        print("DB is ", db, "<<<<<<<\n")
        print("COLLECTION is ", collection, "<<<<<<<\n")
        print("Feedback is ", request.form['feedback'], "<<<<<<<\n")
        data["feedback"] = request.form['feedback']
    collection.insert_one(data)
    print("Collections available now are: ", db.list_collection_names())
    return hello_world()



# start the flask server
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)