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

### Maintenance Tasks

#### List All Tasks
```
GET /tasks/
```

Response:
```json
[
  {
    "id": 1,
    "vehicle": 1,
    "task_type": "Oil Change",
    "description": "Regular oil change with filter replacement",
    "status": "completed",
    "created_at": "2025-03-01T10:30:00Z",
    "updated_at": "2025-03-01T14:15:00Z"
  },
  {
    "id": 2,
    "vehicle": 2,
    "task_type": "Brake Inspection",
    "description": "Check brake pads and rotors",
    "status": "pending",
    "created_at": "2025-03-02T09:00:00Z",
    "updated_at": "2025-03-02T09:00:00Z"
  }
]
```

#### Filter Tasks

You can filter tasks by:
- Vehicle registration number: `?registration_number=ABC123`
- Task type: `?task_type=Oil%20Change`
- Status: `?status=completed`

Example:
```
GET /tasks/?registration_number=ABC123&status=completed
```

#### Get Task Details
```
GET /tasks/{id}/
```

Response:
```json
{
  "id": 1,
  "vehicle": 1,
  "task_type": "Oil Change",
  "description": "Regular oil change with filter replacement",
  "status": "completed",
  "created_at": "2025-03-01T10:30:00Z",
  "updated_at": "2025-03-01T14:15:00Z"
}
```

#### Create Task
```
POST /tasks/
```

Request:
```json
{
  "vehicle": 1,
  "task_type": "Tire Rotation",
  "description": "Rotate tires to ensure even wear",
  "status": "pending"
}
```

#### Update Task
```
POST /tasks/{id}/
```

Request:
```json
{
  "vehicle": 1,
  "task_type": "Tire Rotation",
  "description": "Rotate tires to ensure even wear",
  "status": "completed"
}
```

#### Partially Update Task
```
PATCH /tasks/{id}/
```

Request:
```json
{
  "status": "completed"
}
```

#### Delete Task
```
DELETE /tasks/{id}/
```

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful operation
- 201: Resource successfully created
- 204: Resource successfully deleted
- 400: Bad request (validation errors)
- 404: Resource not found
- 500: Server error

Example error response:
```json
{
  "error": "Maintenance task not found"
}
```

## Filtering

The API supports filtering maintenance tasks by:
- Vehicle registration number

Example:
```
GET /tasks/?registration_number=ABC123&status=pending
```


