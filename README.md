# TodoList-app
 
# Task API Documentation

## 1. Create Tasks
- **Description**: Allows creating a new task.
- **Method**: `POST`
- **Endpoint**: `/api/tasks/`

## 2. Read Tasks
- **Description**: Retrieves a list of all tasks or a specific task by ID.
- **Method**: `GET`
- **Endpoints**:
  - Get all tasks: `/api/tasks/`
  - Get a specific task: `/api/tasks/<id>/`

## 3. Update Tasks
- **Description**: Updates an existing task.
- **Methods**: `PUT` or `PATCH`
- **Endpoint**: `/api/tasks/<id>/`

## 4. Delete Tasks
- **Description**: Deletes a specific task.
- **Method**: `DELETE`
- **Endpoint**: `/api/tasks/<id>/`
