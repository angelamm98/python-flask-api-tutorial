from flask import Flask
app = Flask(__name__)
from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
 return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos): 
        del todos[position] 
        return jsonify(todos)  
    else:
        return jsonify({"error": "Invalid position"}), 400  



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)