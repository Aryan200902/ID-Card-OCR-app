# Thai ID Card OCR

A simple web application for Optical Character Recognition (OCR) of Thai National ID Cards using Google Cloud Vision API and MongoDB.

## Features

- Upload an image of a Thai National ID Card for OCR processing.
- Extract information such as name, last name, date of birth, identification number, date of issue, and date of expiry from the ID card.
- Display and delete previously extracted entries.

## Technologies Used

- Flask: A micro web framework for Python.
- Google Cloud Vision API: For OCR processing.
- MongoDB: A NoSQL database for storing extracted information.

## Prerequisites

- Python 3.x
- Google Cloud Vision API credentials (JSON file)
- MongoDB server

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/Thai-ID-Card-OCR.git
cd Thai-ID-Card-OCR

```

2. Install dependencies:
```bash
pip install -r requirements.txt

```
3. Set up environment variables:

Create a .env file in the project root.

Add the following content:
```bash 
GOOGLE_APPLICATION_CREDENTIALS_JSON="your_google_credentials.json"

```

4. Run the application:
```bash 
python run.py

```

5. Visit http://127.0.0.1:5000/upload in your  browser