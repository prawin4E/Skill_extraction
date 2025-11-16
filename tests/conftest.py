"""
Pytest configuration and fixtures for testing.
"""
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_resume_text():
    """Sample resume text for testing."""
    return """
    Senior Software Engineer with 5+ years of experience in Python, Java, and JavaScript.
    Strong expertise in machine learning, data science, and cloud computing (AWS, Azure).
    Excellent leadership and communication skills. Experience with Docker, Kubernetes,
    and CI/CD pipelines. Proficient in SQL, MongoDB, and PostgreSQL.
    Team player with strong problem-solving abilities.
    """


@pytest.fixture
def short_resume_text():
    """Short resume text for testing."""
    return "Python developer with leadership skills"


@pytest.fixture
def empty_resume_text():
    """Empty resume text for testing."""
    return ""


@pytest.fixture
def whitespace_resume_text():
    """Whitespace-only resume text for testing."""
    return "   \n\t  "


@pytest.fixture
def valid_request_payload(sample_resume_text):
    """Valid request payload for skill extraction."""
    return {"resume_text": sample_resume_text}


@pytest.fixture
def invalid_request_payload():
    """Invalid request payload (missing resume_text)."""
    return {}


@pytest.fixture
def empty_text_payload():
    """Request payload with empty text."""
    return {"resume_text": ""}
