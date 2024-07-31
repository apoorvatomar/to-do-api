# To-Do List API

## Overview

The To-Do List API is a RESTful API built using FastAPI and MongoDB. This project allows users to manage tasks with features including creating, retrieving, updating, and deleting tasks. The API is designed to be straightforward and easy to integrate into other applications or use for testing purposes.

## Features

- **Create Tasks**: Allows users to add new tasks with a name and description.
- **Retrieve Tasks**: Lists all tasks stored in the MongoDB database.
- **Update Tasks**: Updates details of existing tasks, including marking them as completed.
- **Delete Tasks**: Deletes tasks from the database.
- **MongoDB Integration**: Uses MongoDB for persistent storage of tasks.

## Getting Started

### Prerequisites

- Python 3.8 or later
- MongoDB database (can use MongoDB Atlas for cloud storage)
- `pip` (Python package installer)

### Installation

1. **Clone the Repository**

   git clone https://github.com/apoorvatomar/to-do-api.git
   cd to-do-api
2 Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate 

3. Install Required Dependencies
   pip install -r requirements.txt
   
5. Set Up Environment Variables
   Create a .env file in the root directory

6. Run the Application
   uvicorn main:app --reload

The application will be available at http://127.0.0.1:8000.

***API Endpoints****
1. POST /tasks/

Description: Create a new task.

2. GET /tasks/

Description: Retrieve all tasks.

3.PUT /tasks/{id}

Description: Update an existing task by ID.

4.DELETE /tasks/{id}

Description: Delete a task by ID.

Running Tests
If you have tests set up, you can run them using:

pytest




   