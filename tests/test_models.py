"""
Tests for models and data processing.
"""
import pytest
from models.parse_results import process_result


class TestProcessResult:
    """Test suite for process_result function."""

    @pytest.fixture
    def mock_skillner_output(self):
        """Mock SkillNER output with full_matches and ngram_scored."""
        return {
            "results": {
                "full_matches": [
                    {
                        "doc_node_value": "Python",
                        "skill_id": "KS120076FGP5WGWYMP0F"
                    },
                    {
                        "doc_node_value": "machine learning",
                        "skill_id": "KS125LS6N7WP4S6SFTCK"
                    }
                ],
                "ngram_scored": [
                    {
                        "doc_node_value": "leadership",
                        "skill_id": "KS126XS6CQTFZE36KZXY"
                    }
                ]
            }
        }

    @pytest.fixture
    def empty_results(self):
        """Mock SkillNER output with no matches."""
        return {
            "results": {
                "full_matches": [],
                "ngram_scored": []
            }
        }

    @pytest.fixture
    def missing_results_key(self):
        """Mock SkillNER output missing results key."""
        return {}

    def test_process_result_with_valid_data(self, mock_skillner_output):
        """Test process_result with valid SkillNER output."""
        result = process_result(mock_skillner_output)

        assert isinstance(result, list)
        assert len(result) > 0

        # Verify structure of processed data
        for item in result:
            assert "token" in item
            assert "Skill" in item
            assert "Skill_type" in item
            assert isinstance(item["token"], str)
            assert isinstance(item["Skill"], str)
            assert isinstance(item["Skill_type"], str)

    def test_process_result_with_empty_results(self, empty_results):
        """Test process_result with no matches."""
        result = process_result(empty_results)

        assert isinstance(result, list)
        assert len(result) == 0

    def test_process_result_with_missing_results_key(self, missing_results_key):
        """Test process_result handles missing results key gracefully."""
        result = process_result(missing_results_key)

        # Should return empty list instead of crashing
        assert isinstance(result, list)
        assert len(result) == 0

    def test_process_result_combines_full_and_ngram(self, mock_skillner_output):
        """Test that process_result combines both full_matches and ngram_scored."""
        result = process_result(mock_skillner_output)

        # Should have items from both full_matches (2) and ngram_scored (1)
        assert len(result) == 3

    def test_process_result_extracts_correct_fields(self, mock_skillner_output):
        """Test that process_result extracts the correct fields."""
        result = process_result(mock_skillner_output)

        # Find the Python skill
        python_skill = next((s for s in result if s["token"] == "Python"), None)
        assert python_skill is not None
        assert python_skill["Skill"] != ""
        assert python_skill["Skill_type"] != ""
