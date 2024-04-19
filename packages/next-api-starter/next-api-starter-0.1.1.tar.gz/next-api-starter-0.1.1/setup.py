from setuptools import setup, find_packages

setup(
    name="next-api-starter",  # Replace with your desired package name
    version="0.1.1",  # Start with version 0.1.0 for initial release
    description="Starter template for Next.js and FastAPI projects",
    long_description="...",  # Add detailed description in README format
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["frontend", "backend", "tests"]),  # Exclude frontend/backend for separate installation
    install_requires=[  # List dependencies for backend
        "uvicorn[standard]",
        # ... other dependencies
    ],
    entry_points={
        "console_scripts": [
            "create_nextapi = create_nextapi.create_nextapi:main",
        ]
    },
)
