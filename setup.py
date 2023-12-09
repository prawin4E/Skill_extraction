from setuptools import setup

setup(
    name='Itech Skills Extractor',
    version='0.1',
    py_modules=['skill_extractor'],
    install_requires=[
        "skillNer",
        "spacy>=3.0.0,<4.0.0",
        "en_core_web_lg",
        "fastapi",
        "uvicorn[standard]"
    ]
)