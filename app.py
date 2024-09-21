from flask import Flask,json,request
import pymongo

client = pymongo.MongoClient()
db = "my_db"



app=Flask(__name__)


@app.route('/',methods=['POST'])
def api_msg():
    
    if request.headers['Content-Type']=='application/json':
        data=request.json
                    
        client['my_db']['req'].insert_one(data) 
              
        return json.dumps(data)
    



if __name__=='__main__':
    app.run(debug=True)
