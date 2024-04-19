from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="audio-recorder-streamlit-auto",
    version="0.0.1",
    author="Kevin Beck",
    author_email="misterkevinski@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misterkevinski/audio-recorder-streamlit",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=0.63",
    ],
)
