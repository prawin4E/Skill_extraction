"""
Tests for Pydantic schemas.
"""
import pytest
from pydantic import ValidationError
from schemas.skill_extraction_request import SkillExtractionRequest
from schemas.skill_extraction_response import SkillExtractionResponse


class TestSkillExtractionRequest:
    """Test suite for SkillExtractionRequest schema."""

    def test_valid_request(self):
        """Test creating a valid request."""
        request = SkillExtractionRequest(
            resume_text="Python developer with leadership skills"
        )
        assert request.resume_text == "Python developer with leadership skills"

    def test_empty_string_invalid(self):
        """Test that empty string is invalid (min_length=1)."""
        with pytest.raises(ValidationError) as exc_info:
            SkillExtractionRequest(resume_text="")

        errors = exc_info.value.errors()
        assert any(
            error["type"] == "string_too_short"
            for error in errors
        )

    def test_missing_field(self):
        """Test that missing resume_text field raises validation error."""
        with pytest.raises(ValidationError) as exc_info:
            SkillExtractionRequest()

        errors = exc_info.value.errors()
        assert any(
            error["loc"] == ("resume_text",) and error["type"] == "missing"
            for error in errors
        )

    def test_whitespace_is_valid(self):
        """Test that whitespace-only text passes schema validation."""
        # Schema allows it, but API endpoint should reject it
        request = SkillExtractionRequest(resume_text="   ")
        assert request.resume_text == "   "

    def test_long_text_is_valid(self):
        """Test that very long resume text is accepted."""
        long_text = "Python developer " * 1000
        request = SkillExtractionRequest(resume_text=long_text)
        assert len(request.resume_text) > 10000


class TestSkillExtractionResponse:
    """Test suite for SkillExtractionResponse schema."""

    def test_valid_response(self):
        """Test creating a valid response."""
        response = SkillExtractionResponse(
            annotations=[
                {"token": "Python", "Skill": "Python", "Skill_type": "Hard Skill"},
                {"token": "leadership", "Skill": "Leadership", "Skill_type": "Soft Skill"}
            ]
        )
        assert len(response.annotations) == 2
        assert response.annotations[0]["token"] == "Python"

    def test_empty_annotations(self):
        """Test response with empty annotations list."""
        response = SkillExtractionResponse(annotations=[])
        assert response.annotations == []
        assert len(response.annotations) == 0

    def test_single_annotation(self):
        """Test response with single annotation."""
        response = SkillExtractionResponse(
            annotations=[
                {"token": "Python", "Skill": "Python", "Skill_type": "Hard Skill"}
            ]
        )
        assert len(response.annotations) == 1

    def test_annotations_structure(self):
        """Test that annotations have correct structure."""
        response = SkillExtractionResponse(
            annotations=[
                {"token": "Java", "Skill": "Java", "Skill_type": "Hard Skill"}
            ]
        )
        annotation = response.annotations[0]
        assert "token" in annotation
        assert "Skill" in annotation
        assert "Skill_type" in annotation

    def test_extra_fields_allowed(self):
        """Test that extra fields in annotations are allowed."""
        response = SkillExtractionResponse(
            annotations=[
                {
                    "token": "Python",
                    "Skill": "Python",
                    "Skill_type": "Hard Skill",
                    "extra_field": "extra_value"
                }
            ]
        )
        assert response.annotations[0]["extra_field"] == "extra_value"
