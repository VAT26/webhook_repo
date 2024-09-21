from flask import Flask,json,request,jsonify
import pymongo

client = pymongo.MongoClient()
db = "my_db"



app=Flask(__name__)


@app.route('/',methods=['POST'])
def api_msg():
    
    if request.headers['Content-Type']=='application/json':
        data=request.json
        print(data)
        keys=['author','to_branch','timestamp']
        info=extract(data,keys)
        print(info)
        client['my_db']['req'].insert_one(info)
              
        return json.dumps(data)
    return jsonify({'failled sucessfully'})   
    
#def filter(data,keys):
#    return {key: data[key] for key in keys if key in data}

def extract(data,keys,result=None):
    if result is None:
        result={}
    for key,value in data.items():
        if key in keys:
            result[key]=value 
        if isinstance(value,dict):
            extract(value,keys,result)       
    return result

if __name__=='__main__':
    app.run(debug=True)
