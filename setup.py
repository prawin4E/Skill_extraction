from setuptools import setup

install_requires = [
    "skillNer",
    "spacy>=3.0.0,<4.0.0",
    "en_core_web_lg",
    "fastapi",
    "uvicorn[standard]",
    
]

setup(
    install_requires=install_requires,
)