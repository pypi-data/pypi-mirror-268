from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name='llm_connect',
    version='2.0.0',
    packages=find_packages(),
    install_requires=['click==8.1.7', 'setuptools~=68.2.0', 'transformers','torch~=2.1.0','accelerate', 'bitsandbytes','colorama'],
    description="LLM Connect API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="CeADAR Connect Group",
    entry_points={
    'console_scripts': [
        'lc = llm_connect_api:cli',
    ],
},
 
)

