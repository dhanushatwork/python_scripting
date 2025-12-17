from flask import Flask, jsonify

app = Flask(__name__)

# Dummy employee data
employees = {
    1: {"id": 1, "name": "Ravi", "role": "DevOps Engineer"},
    2: {"id": 2, "name": "Anita", "role": "Backend Developer"},
    3: {"id": 3, "name": "Kumar", "role": "Cloud Engineer"}
}

@app.route("/employees", methods=["GET"])
def get_all_employees():
    return jsonify(list(employees.values()))

@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    employee = employees.get(emp_id)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

