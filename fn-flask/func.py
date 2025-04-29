from flask import Flask, request, jsonify

application = Flask(__name__)

# In-memory storage for students
students = {}

@application.route('/')
def hello():
    return b'Hello World from Flask application!'

# Create a new student
@application.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'error': 'Student ID is required'}), 400
    
    student_id = data['id']
    if student_id in students:
        return jsonify({'error': 'Student already exists'}), 409
    
    students[student_id] = data
    return jsonify({'message': 'Student created successfully', 'student': data}), 201

# Get all students
@application.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

# Get a specific student
@application.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(students[student_id])

# Update a student
@application.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    students[student_id].update(data)
    return jsonify({'message': 'Student updated successfully', 'student': students[student_id]})

# Delete a student
@application.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
    
    del students[student_id]
    return jsonify({'message': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    application.run()
