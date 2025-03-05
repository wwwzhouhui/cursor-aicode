<script setup>
import TodoList from './components/TodoList.vue'
</script>

<template>
  <div class="container">
    <h1>待办事项清单</h1>
    <TodoList />
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
}
</style> 