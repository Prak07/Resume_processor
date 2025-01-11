# Resume Processor API

This project provides an API for processing resumes uploaded in PDF or DOCX formats. The API extracts the candidate's name, email, and mobile number from the uploaded resume, stores the information in a database, and returns it as a JSON response.

## Features
- Upload a resume in PDF or DOCX format.
- Extract candidate's full name, email address, and mobile number.
- Store the extracted data in a PostgreSQL database.
- Use Groq API for parsing and extracting information.
- Return the extracted information as a JSON response.

## Technologies Used
- **Django**: A high-level Python Web framework used for building the API.
- **Django REST Framework**: To handle API requests and responses.
- **PostgreSQL**: Database used for storing candidate information.
- **PyPDF2**: For reading and extracting text from PDF files.
- **python-docx**: For reading and extracting text from DOCX files.
- **Groq API**: A third-party AI tool used for parsing and extracting resume information.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/Prak07/resume-processor.git
   cd resume-processor
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:

   - Create a new PostgreSQL database and user.
   - Update the `DATABASES` setting in `settings.py` with your database credentials.

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/api/extract_resume/`.

## Database Schema

The project uses a PostgreSQL database with the following model:

### Candidate:
- **first_name** (CharField): Candidate's first name.
- **email** (EmailField): Candidate's email address.
- **mobile_number** (CharField): Candidate's mobile number.

## API Endpoints

### POST /api/extract_resume/

**Description:**
Upload a resume in PDF or DOCX format and extract the candidate's name, email, and mobile number.

**Request Format:**
- `resume`: File (PDF or DOCX)

**Response Format:**
```json
{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
```

## Testing the API

You can test the API using cURL or Postman. Here's an example of a cURL request:

```bash
curl -X POST -F "resume=@path_to_resume/resume.pdf" http://127.0.0.1:8000/api/extract_resume/
```

