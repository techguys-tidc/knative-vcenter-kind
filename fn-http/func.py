from parliament import Context
from flask import Request
import json

# In-memory storage for students
students = {}

def create_student(data):
    student_id = str(len(students) + 1)
    students[student_id] = {
        "id": student_id,
        "name": data.get("name"),
        "age": data.get("age"),
        "grade": data.get("grade")
    }
    return students[student_id]

def get_student(student_id):
    return students.get(student_id)

def get_all_students():
    return list(students.values())

def update_student(student_id, data):
    if student_id not in students:
        return None
    student = students[student_id]
    student.update({
        "name": data.get("name", student["name"]),
        "age": data.get("age", student["age"]),
        "grade": data.get("grade", student["grade"])
    })
    return student

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False

def handle_student_request(req: Request):
    if req.method == "POST":
        # Create student
        if req.is_json:
            student = create_student(req.json)
            return json.dumps(student), 201
        return "Invalid data format", 400

    elif req.method == "GET":
        student_id = req.args.get("id")
        if student_id:
            student = get_student(student_id)
            if student:
                return json.dumps(student), 200
            return "Student not found", 404
        return json.dumps(get_all_students()), 200

    elif req.method == "PUT":
        if not req.is_json:
            return "Invalid data format", 400
        student_id = req.args.get("id")
        if not student_id:
            return "Student ID required", 400
        student = update_student(student_id, req.json)
        if student:
            return json.dumps(student), 200
        return "Student not found", 404

    elif req.method == "DELETE":
        student_id = req.args.get("id")
        if not student_id:
            return "Student ID required", 400
        if delete_student(student_id):
            return "Student deleted", 200
        return "Student not found", 404

    return "Method not allowed", 405

def main(context: Context):
    """
    Student CRUD API
    """
    if 'request' in context.keys():
        return handle_student_request(context.request)
    return "{}", 200
