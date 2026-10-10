# Travel Guide

A web-based travel guide application designed to help users explore travel-related information through an interactive frontend and a Python-powered backend.

## Live Demo

**Live Application:** 

## Project Overview

Travel Guide is a web application developed to provide a simple and accessible way for users to interact with travel-related information. The project combines a frontend interface with a Python backend to handle application logic and integrate external APIs.

The primary focus of my contribution was backend development, including Python implementation, API integration, configuration, and debugging with guidance from mentors.

## Key Features

- Python-based backend application.
- Integration with Google Gemini API for AI-powered functionality.
- Integration with Murf AI API for AI voice-related functionality.
- Frontend and backend integration.
- API-based request handling.
- Environment-based configuration for API credentials.
- Debugging and testing of application functionality.

## Technology Stack

**Backend**
- Python
- Flask (if used in the current implementation)
- REST API integration

**Frontend**
- HTML
- CSS
- JavaScript

**External APIs**
- Google Gemini API
- Murf AI API

**Development Tools**
- Visual Studio Code
- Git
- GitHub
- AI-assisted development and debugging tools

## My Contribution

I primarily worked on the backend development of this project. With guidance and mentorship, I implemented Python code, integrated external APIs, configured API credentials, and worked through application logic and debugging.

My work involved understanding how API requests are handled, how external services communicate with the backend, and how backend functionality connects with the frontend.

I used AI assistance as a supporting tool for understanding concepts, troubleshooting errors, reviewing implementation approaches, and improving my debugging process. The implementation was developed through my own work, learning, experimentation, and mentor guidance.

## Project Structure

```text
Travel-Guide/
├── Backend/
│   ├── app.py
│   ├── .env
│   └── .env.example
├── Frontend/
│   ├── index.html
│   └── index.js
├── .gitignore
└── README.md
```

Note: The `.env` file is used for local configuration and must not be committed to GitHub. The `.env.example` file contains placeholder variable names for configuration reference.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Git
- A Google Gemini API key
- A Murf AI API key

### 1. Clone the Repository

```bash
git clone https://github.com/SRIRAM-Tech77/Travel-Guide-AI-Assistant.git
cd Travel-Guide-AI-Assistant
```

### 2. Install Dependencies

Install the packages required by the backend. If a `requirements.txt` file is available, run:

```bash
pip install -r Backend/requirements.txt
```

Otherwise, install the dependencies listed in the project's Python imports and documentation.

### 3. Configure Environment Variables

Create a `.env` file inside the `Backend` directory and add your API credentials:

```dotenv
MURF_API_KEY=your_murf_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder values with your own API keys. Never publish actual credentials in source code or commit them to GitHub.

### 4. Run the Backend

```bash
cd Backend
python app.py
```

Use the local URL displayed in the terminal to access the backend, according to the application's configuration.

### 5. Open the Frontend

Open `Frontend/index.html` in a browser or serve the frontend using a local development server. Ensure that the frontend's API endpoint matches the backend address and port.

## Testing and Debugging

During development, I tested the backend functionality, checked API configuration, and worked through errors encountered during implementation.

AI-assisted tools were used to support debugging, explain error messages, and understand possible solutions. Mentor guidance also helped me understand the backend logic and API integration process.

Testing should be performed with valid API credentials and the required services available. Actual test coverage and deployment status should be documented as they are verified.

## Learning Outcomes

Through this project, I gained practical experience in:

- Writing and understanding Python backend code.
- Integrating third-party APIs.
- Managing API credentials using environment variables.
- Understanding frontend-to-backend communication.
- Debugging application errors.
- Using Git and GitHub for version control.
- Applying AI-assisted development tools to support learning and troubleshooting.
- Working with mentor guidance on a practical software project.

## Security

- API keys must be stored in environment variables.
- The local `.env` file must remain excluded from version control.
- The `.env.example` file should contain placeholders only.
- Any API keys previously exposed in source code or Git history should be revoked or rotated.
- Production deployments should configure credentials through the hosting provider's environment-variable settings.

## Acknowledgements

I would like to thank my mentors for their guidance and support throughout the backend development process. Their feedback helped me understand the implementation logic, API integration, and debugging practices.

I also used AI-assisted tools as a supplementary learning resource to understand technical concepts, investigate errors, and improve my problem-solving approach.

## Author

**Sriram**

GitHub: https://github.com/SRIRAM-Tech77

## License

A license has not yet been specified for this project.
