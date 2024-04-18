import setuptools

setuptools.setup(
    name="oh_llama",
    version="0.0.01",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="Opinionated, Ollama Client based Python Tools.",
    long_description="""
Oh! Its Just oLLama!
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.8',
    install_requires=[
    ],
)