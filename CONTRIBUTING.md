# Contributing to Skill Extraction API

Thank you for your interest in contributing to the Skill Extraction API! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional, for containerized development)

### Getting Started

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/prawin4E/Skill_extraction.git
   cd Skill_extraction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   make install-dev
   # Or manually:
   pip install -r requirements.txt
   python -m spacy download en_core_web_lg
   pre-commit install
   ```

4. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Running the Application

```bash
# Development server with auto-reload
make run

# Or using uvicorn directly
uvicorn main:app --reload
```

### Running Tests

```bash
# Run all tests with coverage
make test

# Run tests quickly without coverage
make test-quick

# Run specific test file
pytest tests/test_api.py -v
```

### Code Quality

Before submitting a PR, ensure your code passes all quality checks:

```bash
# Format code
make format

# Run linting checks
make lint

# Run pre-commit hooks
make pre-commit-run
```

### Code Style

- **Python Version**: Python 3.9+
- **Formatting**: Black (line length: 100)
- **Import Sorting**: isort (Black-compatible profile)
- **Type Hints**: Use type hints where appropriate
- **Docstrings**: Use Google-style docstrings

Example:
```python
def process_result(data: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    Process the SkillNER result data.

    Args:
        data: The input data dictionary containing results

    Returns:
        A list of dictionaries containing processed skill data

    Raises:
        KeyError: If the input data structure is incorrect
    """
    # Implementation
    pass
```

## Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Use fixtures for common setup

Example:
```python
def test_extract_skills_success(client, valid_request_payload):
    """Test successful skill extraction with valid resume text."""
    # Arrange
    # (handled by fixtures)

    # Act
    response = client.post("/api/v1/extract-skills", json=valid_request_payload)

    # Assert
    assert response.status_code == 200
    assert "annotations" in response.json()
```

### Test Coverage

- Aim for >80% code coverage
- Write both unit and integration tests
- Test edge cases and error conditions
- Mock external dependencies when appropriate

## Pull Request Process

1. **Update documentation**
   - Update README.md if adding features
   - Add docstrings to new functions/classes
   - Update API documentation if needed

2. **Ensure tests pass**
   ```bash
   make test
   make lint
   ```

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

   Use conventional commit messages:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `test:` Test additions/changes
   - `refactor:` Code refactoring
   - `chore:` Maintenance tasks

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure CI/CD pipeline passes

## Project Structure

```
Skill_extraction/
├── api/                    # API endpoints and controllers
├── models/                 # Data models and processing logic
├── schemas/                # Pydantic schemas
├── tests/                  # Test files
├── utils/                  # Utility functions
├── main.py                 # Application entry point
├── settings.py             # Configuration management
└── requirements.txt        # Project dependencies
```

## Adding New Features

### Adding a New Endpoint

1. Create the endpoint in `api/v1/controllers/`
2. Define request/response schemas in `schemas/`
3. Add business logic in `models/` or `utils/`
4. Write tests in `tests/`
5. Update documentation

### Adding New Dependencies

1. Add to `requirements.txt`
2. Update `setup.py` if it's a core dependency
3. Document why the dependency is needed
4. Check for license compatibility

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces
- Any relevant code snippets

## Code Review

All submissions require code review. We use GitHub pull requests for this purpose:

- Reviews will focus on code quality, tests, and documentation
- Be responsive to feedback
- Keep changes focused and atomic
- Avoid mixing refactoring with feature additions

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the codebase
- Documentation improvements

Thank you for contributing! 🎉
