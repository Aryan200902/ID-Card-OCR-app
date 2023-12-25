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

5. Visit http://localhost:5000/upload in your  browser

   
## for Testing

1. Visit     https://64c5-2405-201-3046-d00c-4117-fc0b-110b-8b90.ngrok-free.app/upload  (Hosted)



![image](https://github.com/Aryan200902/ID-Card-OCR-app/assets/94388629/e7b0b147-ac84-45a7-b6d9-a73c187b0885)
2. Upload Thai Id Card and click upload Button for OCR.




![image](https://github.com/Aryan200902/ID-Card-OCR-app/assets/94388629/46af7490-fc9f-4b07-86b5-873351c6d9cb)
3. You wil get Description of Id Card Showing Required Information.




![image](https://github.com/Aryan200902/ID-Card-OCR-app/assets/94388629/afb6a81f-a4fb-431f-a2a0-3c88fc5979bd)
4. Below you will se a toggle button for showing all stored Id card details From Database.




![image](https://github.com/Aryan200902/ID-Card-OCR-app/assets/94388629/243220c9-2c03-42ac-a208-0ce09bd714a6)
5. You can Delete Each of them Individually from the Database using delete button next to them




 
