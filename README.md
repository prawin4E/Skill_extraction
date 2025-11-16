# Skill Extraction API

A FastAPI-based REST API for extracting skills from resume text using [SkillNER](https://github.com/AnasAito/SkillNER.git).

## Overview

This API takes resume text as input and returns extracted skills categorized into Hard Skills and Soft Skills. It leverages SkillNER, a spaCy-based NLP library, to identify and classify professional skills from unstructured text.

## Features

- ✅ Extract skills from resume text
- ✅ Categorize skills into Hard Skills and Soft Skills
- ✅ RESTful API with FastAPI
- ✅ Comprehensive error handling and logging
- ✅ Docker support with Docker Compose
- ✅ OpenAPI documentation (Swagger UI)
- ✅ Health check endpoints
- ✅ CORS support
- ✅ Environment-based configuration

## Installation

### Using pip

```bash
# Clone the repository
git clone <repository-url>
cd Skill_extraction

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_lg

# Install the package
python setup.py install
```

### Using Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t skill-extraction-api .
docker run -p 8000:8000 skill-extraction-api
```

## Configuration

Create a `.env` file in the project root (use `.env.example` as template):

```bash
# Application Settings
APP_NAME=Skill Extraction API
DEBUG=false
LOG_LEVEL=INFO

# Server Settings
HOST=0.0.0.0
PORT=8000

# API Configuration
API_V1_PREFIX=/api/v1
```

## Usage

### Start the Server

```bash
# Development
uvicorn main:app --reload

# Production
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

#### 1. Health Check
```bash
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Skill Extraction API",
  "version": "0.1.0"
}
```

#### 2. Extract Skills
```bash
POST /api/v1/extract-skills
```

**Request Body:**
```json
{
  "resume_text": "Experienced Python developer with strong leadership skills and expertise in machine learning"
}
```

**Response:**
```json
{
  "annotations": [
    {
      "token": "Python",
      "Skill": "Python",
      "Skill_type": "Hard Skill"
    },
    {
      "token": "leadership",
      "Skill": "Leadership",
      "Skill_type": "Soft Skill"
    },
    {
      "token": "machine learning",
      "Skill": "Machine Learning",
      "Skill_type": "Hard Skill"
    }
  ]
}
```

### Example with cURL

```bash
curl -X POST "http://localhost:8000/api/v1/extract-skills" \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Software engineer with 5 years of experience in Java, Spring Boot, and AWS. Strong communication and problem-solving skills."
  }'
```

### Example with Python

```python
import requests

url = "http://localhost:8000/api/v1/extract-skills"
payload = {
    "resume_text": "Data scientist proficient in Python, TensorFlow, and SQL with excellent analytical skills"
}

response = requests.post(url, json=payload)
skills = response.json()
print(skills)
```

## API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
Skill_extraction/
├── api/
│   └── v1/
│       └── controllers/
│           └── skill_extractor.py    # API endpoints
├── models/
│   └── parse_results.py              # Result processing logic
├── schemas/
│   ├── skill_extraction_request.py   # Request schema
│   └── skill_extraction_response.py  # Response schema
├── tests/                            # Test files
├── utils/                            # Utility functions
├── main.py                           # Application entry point
├── settings.py                       # Configuration management
├── requirements.txt                  # Python dependencies
├── setup.py                          # Package setup
├── Dockerfile                        # Docker configuration
├── docker-compose.yml                # Docker Compose configuration
└── README.md                         # This file
```

## Development

### Running Tests

```bash
pytest tests/ -v --cov
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Lint
flake8

# Type checking
mypy .
```

## Future Improvements

- [ ] Fine-tune SkillNER model for better accuracy
- [ ] Add support for PDF and DOCX resume parsing
- [ ] Implement skill matching against job descriptions
- [ ] Add batch processing for multiple resumes
- [ ] Implement caching for improved performance
- [ ] Add authentication and rate limiting
- [ ] Deploy to cloud (AWS/GCP/Azure)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Acknowledgments

- Built using [SkillNER](https://github.com/AnasAito/SkillNER.git)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- NLP powered by [spaCy](https://spacy.io/)
