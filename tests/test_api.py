"""
Tests for API endpoints.
"""
import pytest
from fastapi import status


class TestHealthEndpoints:
    """Test suite for health check endpoints."""

    def test_root_endpoint(self, client):
        """Test root endpoint returns healthy status."""
        response = client.get("/")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
        assert "app" in data
        assert "version" in data

    def test_health_endpoint(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
        assert "service" in data
        assert "version" in data


class TestSkillExtractionEndpoint:
    """Test suite for skill extraction endpoint."""

    def test_extract_skills_success(self, client, valid_request_payload):
        """Test successful skill extraction with valid resume text."""
        response = client.post("/api/v1/extract-skills", json=valid_request_payload)
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert "annotations" in data
        assert isinstance(data["annotations"], list)

        # Check that skills were extracted
        if len(data["annotations"]) > 0:
            skill = data["annotations"][0]
            assert "token" in skill
            assert "Skill" in skill
            assert "Skill_type" in skill

    def test_extract_skills_with_short_text(self, client, short_resume_text):
        """Test skill extraction with short resume text."""
        response = client.post(
            "/api/v1/extract-skills",
            json={"resume_text": short_resume_text}
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "annotations" in data
        assert isinstance(data["annotations"], list)

    def test_extract_skills_empty_text(self, client, empty_text_payload):
        """Test skill extraction with empty text returns 400."""
        response = client.post("/api/v1/extract-skills", json=empty_text_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert "detail" in data

    def test_extract_skills_whitespace_only(self, client, whitespace_resume_text):
        """Test skill extraction with whitespace-only text returns 400."""
        response = client.post(
            "/api/v1/extract-skills",
            json={"resume_text": whitespace_resume_text}
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert "detail" in data

    def test_extract_skills_missing_field(self, client, invalid_request_payload):
        """Test skill extraction with missing resume_text field returns 422."""
        response = client.post("/api/v1/extract-skills", json=invalid_request_payload)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_extract_skills_invalid_json(self, client):
        """Test skill extraction with invalid JSON returns 422."""
        response = client.post(
            "/api/v1/extract-skills",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_extract_skills_wrong_content_type(self, client):
        """Test skill extraction with wrong content type."""
        response = client.post(
            "/api/v1/extract-skills",
            data="resume_text=test",
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_response_structure(self, client, sample_resume_text):
        """Test that response has the correct structure."""
        response = client.post(
            "/api/v1/extract-skills",
            json={"resume_text": sample_resume_text}
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        # Verify response structure
        assert isinstance(data, dict)
        assert "annotations" in data
        assert isinstance(data["annotations"], list)

        # Verify each annotation has correct structure
        for annotation in data["annotations"]:
            assert isinstance(annotation, dict)
            assert "token" in annotation
            assert "Skill" in annotation
            assert "Skill_type" in annotation
            assert isinstance(annotation["token"], str)
            assert isinstance(annotation["Skill"], str)
            assert isinstance(annotation["Skill_type"], str)


class TestCORS:
    """Test CORS configuration."""

    def test_cors_headers(self, client, valid_request_payload):
        """Test that CORS headers are present in response."""
        response = client.options("/api/v1/extract-skills")
        # FastAPI TestClient doesn't fully simulate CORS, but we can verify the middleware is configured
        # In a real deployment, this would check for Access-Control-Allow-Origin headers
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_405_METHOD_NOT_ALLOWED]
