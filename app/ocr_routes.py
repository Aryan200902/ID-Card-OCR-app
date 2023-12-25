import os
from flask import render_template, request, jsonify
from google.cloud import vision_v1
from app import app, mongo
import re
from bson import ObjectId
import json
from dotenv import load_dotenv


load_dotenv()

# Use the loaded environment variables
google_credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

# Create a Google Vision API client
client = vision_v1.ImageAnnotatorClient()

def extract_field(description, pattern):
    # Extract information using regular expression pattern
    match = re.search(pattern, description)
    if match:
        return match.group(1).strip()
    return ''


@app.route('/all_entries', methods=['GET'])
def get_all_entries():
    # Get all entries from MongoDB
    db = mongo.db.ocr_data
    entries = list(db.find({}, {'_id': 1, 'name': 1, 'last_name': 1, 'identification_number': 1}))
    
    # Convert ObjectId to string in each entry
    for entry in entries:
        entry['_id'] = str(entry['_id'])

    return jsonify(entries)


@app.route('/delete_entry/<entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    # Delete an entry by ID from MongoDB
    db = mongo.db.ocr_data
    result = db.delete_one({'_id': ObjectId(entry_id)})

    if result.deleted_count == 1:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Entry not found'})
    

@app.route('/', methods=['GET'])    
def home_page():            
    if request.method == 'GET':
        return jsonify({'status': 'success, SERVER IS RUNNING'})


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'id_card_image' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'})

        file = request.files['id_card_image']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'})

        # Perform OCR using Google Vision API
        content = file.read()
        image = vision_v1.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if not texts:
            return jsonify({'status': 'error', 'message': 'No text found in the image'})

        # Extract relevant information
        description = texts[0].description.lower()

        # Extraction logic for each field
        extracted_data = {
            'identification_number': None,
            'name': extract_field(description, r'name[\s:]+(.*?)(?=\n)'),
            'last_name': extract_field(description, r'last name[\s:]+(.*?)(?=\n)'),
            'date_of_birth': extract_field(description, r'date of birth[\s:]+(.*?)(?=\n)'),
            'date_of_issue': None,  # Initialize to None
            'date_of_expiry': None,  # Initialize to None
        }

        # Iterate over lines to find additional information
        lines = description.split('\n')
        for i, line in enumerate(lines):
            if 'thai national id card' in line:
                extracted_data['identification_number'] = lines[i + 1].strip()

            if 'Expiry' in line or 'expiry' in line:
                extracted_data['date_of_expiry'] = lines[i - 1].strip()

            if 'Issue' in line or 'issue' in line:
                extracted_data['date_of_issue'] = lines[i - 1].strip()

        # Save extracted data to MongoDB
        db = mongo.db.ocr_data
        result = db.insert_one(extracted_data)

        # Convert ObjectId to string for JSON serialization
        extracted_data['_id'] = str(result.inserted_id)

        return jsonify({'status': 'success', 'data': extracted_data})

    return render_template('upload.html')
