# Student Management API

A simple REST API for managing student records.

## Testing Locally (localhost:8080)

### Create a Student
```bash
curl -X POST http://localhost:8080/students \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "name": "John Doe", "age": 20}'
```

### Get All Students
```bash
curl http://localhost:8080/students
```

### Get a Specific Student
```bash
curl http://localhost:8080/students/1
```

### Update a Student
```bash
curl -X PUT http://localhost:8080/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith", "age": 21}'
```

### Delete a Student
```bash
curl -X DELETE http://localhost:8080/students/1
```

## Testing on Remote Server (fn-flask.demo.61.91.123.29.nip.io)

### Create a Student
```bash
curl -X POST http://fn-flask.demo.61.91.123.29.nip.io/students \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "name": "John Doe", "age": 20}'
```

### Get All Students
```bash
curl http://fn-flask.demo.61.91.123.29.nip.io/students
```

### Get a Specific Student
```bash
curl http://fn-flask.demo.61.91.123.29.nip.io/students/1
```

### Update a Student
```bash
curl -X PUT http://fn-flask.demo.61.91.123.29.nip.io/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith", "age": 21}'
```

### Delete a Student
```bash
curl -X DELETE http://fn-flask.demo.61.91.123.29.nip.io/students/1
```