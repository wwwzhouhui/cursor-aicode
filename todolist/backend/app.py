from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# 存储待办事项的文件路径
TODOS_FILE = 'todos.json'

def load_todos():
    if os.path.exists(TODOS_FILE):
        with open(TODOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# 获取所有待办事项
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(load_todos())

# 添加新的待办事项
@app.route('/api/todos', methods=['POST'])
def add_todo():
    todos = load_todos()
    new_todo = request.json
    new_todo['id'] = len(todos) + 1
    new_todo['completed'] = False
    todos.append(new_todo)
    save_todos(todos)
    return jsonify(new_todo)

# 更新待办事项状态
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            updated_todo = request.json
            todo.update(updated_todo)
            save_todos(todos)
            return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

# 删除待办事项
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            deleted_todo = todos.pop(i)
            save_todos(todos)
            return jsonify(deleted_todo)
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True) 