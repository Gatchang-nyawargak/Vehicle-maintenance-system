# Fleet Maintenance System

A Django REST Framework API for managing bus fleet maintenance tasks.

## Features
- Track bus information and maintenance history
- Schedule and manage maintenance tasks
- Filter tasks by bus registration numbers
- RESTful API with proper validation

## Quick Setup

```bash
# Clone repository
git clone https://github.com/yourusername/fleet-maintenance-system.git
cd fleet-maintenance-system

# Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install and run
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # API available at http://127.0.0.1:8000/
API Endpoints
Buses

GET /vehicles/ - List all buses
GET /vehicles/{id}/ - Get bus details
POST /vehicles/ - Register new bus
PUT/PATCH /vehicles/{id}/ - Update bus info
DELETE /vehicles/{id}/ - Remove bus

Maintenance Tasks

GET /tasks/ - List all tasks
GET /tasks/{id}/ - Get task details
POST /tasks/ - Create maintenance task
PUT/PATCH /tasks/{id}/ - Update task status
DELETE /tasks/{id}/ - Remove task

Filtering
Filter tasks by bus: GET /tasks/?registration_number=BUS123
Example: Creating a Maintenance Task
jsonCopyPOST /tasks/

{
  "vehicle": 1,
  "task_type": "Oil Change",
  "description": "Change oil in bus #BUS123",
  "status": "pending"
}

