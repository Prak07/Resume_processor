from rest_framework.decorators import api_view
from rest_framework.response import Response
import PyPDF2
import docx
import spacy
from django.core.files.storage import default_storage
from .models import Candidate
from .serializers import CandidateSerializer
from groq import Groq   


client = Groq(api_key="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")

@api_view(['POST'])
def extract_resume(request):
    if 'resume' not in request.FILES:
        return Response({"error": "No file provided"}, status=400)
    

    resume_file = request.FILES['resume']
    file_name = default_storage.save(resume_file.name, resume_file)
    file_path = default_storage.path(file_name)

    first_name = None
    email = None
    mobile = None

    try:
        # Read the file content and extract details based on file type
        file_extension = file_name.split('.')[-1].lower()

        if file_extension == 'pdf':
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                content = ""
                for page in pdf_reader.pages:
                    content += page.extract_text()

        elif file_extension == 'docx':
            doc = docx.Document(file_path)
            content = ""
            for para in doc.paragraphs:
                content += para.text + "\n"

        else:
            return Response({"error": "Invalid file format. Only PDF and DOCX are supported."}, status=400)
        prompt = f"""
        Extract the following information from the given resume text:

        1. Full name
        2. Email address
        3. Mobile number

        Resume text: {content}
        
        Provide the extracted information as a String, containing all three items in the following order:
        Full Name, Email Address, Mobile Number
        """
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        )
        results = chat_completion.choices[0].message.content
        result=results.split(",")
        name=result[0]
        first_name=name.split()[0]
        email=result[1]
        mobile=result[2]

        # Return the extracted details
        candidate = Candidate.objects.create(
            first_name=first_name if first_name else None,
            email=email.strip() if email else None,
            mobile_number=mobile.strip() if mobile else None
        )
        
        serializer = CandidateSerializer(candidate)
        
        return Response(serializer.data)

    except Exception as e:
        return Response({"error": f"Failed to extract data: {str(e)}"}, status=500)
