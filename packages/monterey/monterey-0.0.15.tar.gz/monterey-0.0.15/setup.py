import setuptools

setuptools.setup(
    name="monterey",
    version="0.0.15",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="monterey tools",
    long_description="""
Monterey Tools
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.8',
    install_requires=[
"art",
"customtkinter",
"ebooklib",
"fire",
"prompt_toolkit",
"pathlib",
"pypdf2",
"pillow",
"rich",
    ],
)