from flask import Flask, jsonify, request

app = Flask(__name__)
# dunder variable __name__


stores = [
    {
        "name": "freeman",
        "items":[
            {
                "name": "Iphone 12",
                "price": 250000
            }
        ]
    },
    {
        "name": "Oluwatobi",
        "items":[
            {
                "name": "Nike AF1",
                "price": 40000
            }
        ]
    },
]



@app.route("/")
def home():
    print("This is home")
    return "Hello World"



# GET /stores
@app.route("/stores", methods = ["GET"])
def get_stores():
    return jsonify({"stores": stores })


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_single_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    
    return jsonify({"message": f'{name} not Found'})

# GET /store/<string:name>/item
@app.route("/store/<string:name>/items")
def get_store_item(name):
    store = next(filter(lambda x:x["name"]==name, stores), None)
    if store:
        return jsonify({"items":store['items']})
    return jsonify({"message": f'{name} not Found'})


# POST /stores {name:x, items:X}

@app.route("/stores", methods = ["POST"])
def create_store():
    data = request.get_json()
    new_store = {
        "name": data["name"],
        "items":[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item {new_item: item}


app.run()