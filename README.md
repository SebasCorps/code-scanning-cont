# GitHub Push Protection Demo

This repository demonstrates how GitHub's push protection features can identify and block sensitive data like API keys from being committed to a repository.

## The Demo Application

This is a simple Flask API with an intentionally exposed API key in the source code. In real applications, you should **NEVER** hardcode sensitive credentials in your source code.

## Setup and Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python src/app.py
   ```

3. Access the API:
   - Home endpoint: http://localhost:5000/
