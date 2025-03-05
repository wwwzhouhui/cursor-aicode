# TodoList 后端

这是一个使用 Flask 实现的简单的 TodoList 后端 API。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行服务器

```bash
python app.py
```

服务器将在 http://localhost:5000 上运行。

## API 端点

- GET /api/todos - 获取所有待办事项
- POST /api/todos - 添加新的待办事项
- PUT /api/todos/:id - 更新待办事项
- DELETE /api/todos/:id - 删除待办事项 