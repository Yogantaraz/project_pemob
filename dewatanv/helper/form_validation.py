from flask import request, jsonify

def get_form_data(required_fields):
    data = {}
    for field in required_fields:
        value = request.form.get(field)
        if not value:
            response = jsonify({"error": f"Field {field} is required"})
            response.status_code = 400
            return response
        data[field] = value
    return data
