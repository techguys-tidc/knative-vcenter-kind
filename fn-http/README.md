# Python HTTP Function

Welcome to your new Python function project! This is a CRUD API for managing students. The function code can be found in [`func.py`](./func.py). This function will respond to incoming HTTP GET, POST, PUT, and DELETE requests.

## Endpoints

Running this function will expose the following endpoints:

  * `/` The main endpoint for student CRUD operations
  * `/health/readiness` The endpoint for a readiness health check
  * `/health/liveness` The endpoint for a liveness health check

The health checks can be accessed in your browser at
[http://localhost:8080/health/readiness]() and
[http://localhost:8080/health/liveness]().

## API Usage

### Create a Student (POST)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","age":20,"grade":"A"}' http://localhost:8080
```

### Get All Students (GET)
```bash
curl http://localhost:8080
```

### Get a Specific Student (GET with ID)
```bash
curl "http://localhost:8080?id=1"
```

### Update a Student (PUT)
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"John Smith","age":21}' "http://localhost:8080?id=1"
```

### Delete a Student (DELETE)
```bash
curl -X DELETE "http://localhost:8080?id=1"
```

## Student Data Structure
Each student has the following fields:
- id (automatically generated)
- name
- age
- grade

## Testing

This function project includes a [unit test](./test_func.py). Update this
as you add business logic to your function in order to test its behavior.

```console
python test_func.py
```

## Running Locally

To run the function locally:

```bash
python run_local.py
```

The server will start on `http://localhost:8080`.
