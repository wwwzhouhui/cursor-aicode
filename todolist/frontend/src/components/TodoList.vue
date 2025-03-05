<script setup>
import { ref, onMounted } from 'vue'

const todos = ref([])
const newTodo = ref('')

const API_URL = 'http://localhost:5000/api'

// 获取所有待办事项
const fetchTodos = async () => {
  const response = await fetch(`${API_URL}/todos`)
  todos.value = await response.json()
}

// 添加新的待办事项
const addTodo = async () => {
  if (!newTodo.value.trim()) return
  
  const response = await fetch(`${API_URL}/todos`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ title: newTodo.value })
  })
  
  const todo = await response.json()
  todos.value.push(todo)
  newTodo.value = ''
}

// 切换待办事项状态
const toggleTodo = async (todo) => {
  const response = await fetch(`${API_URL}/todos/${todo.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ...todo, completed: !todo.completed })
  })
  
  const updatedTodo = await response.json()
  const index = todos.value.findIndex(t => t.id === updatedTodo.id)
  todos.value[index] = updatedTodo
}

// 删除待办事项
const deleteTodo = async (id) => {
  await fetch(`${API_URL}/todos/${id}`, {
    method: 'DELETE'
  })
  
  todos.value = todos.value.filter(todo => todo.id !== id)
}

onMounted(fetchTodos)
</script>

<template>
  <div class="todo-list">
    <div class="add-todo">
      <input
        v-model="newTodo"
        @keyup.enter="addTodo"
        placeholder="添加新的待办事项..."
        type="text"
      >
      <button @click="addTodo">添加</button>
    </div>
    
    <ul class="todos">
      <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.completed }">
        <input
          type="checkbox"
          :checked="todo.completed"
          @change="toggleTodo(todo)"
        >
        <span class="todo-title">{{ todo.title }}</span>
        <button class="delete-btn" @click="deleteTodo(todo.id)">删除</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.todo-list {
  width: 100%;
}

.add-todo {
  display: flex;
  margin-bottom: 1rem;
  gap: 0.5rem;
}

.add-todo input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #3aa876;
}

.todos {
  list-style: none;
  padding: 0;
}

.todos li {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
  gap: 0.5rem;
}

.todo-title {
  flex: 1;
}

.completed .todo-title {
  text-decoration: line-through;
  color: #999;
}

.delete-btn {
  background-color: #ff4444;
}

.delete-btn:hover {
  background-color: #cc0000;
}
</style> 