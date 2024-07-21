# TextTune

TextTune is a Streamlit-based application for grammar checking and text rephrasing. It offers two main input methods: manual text input and PDF file upload. Users can choose between checking grammar or rephrasing the text.

## Features

- **Manual Input**: Enter text directly into a text box.
- **PDF Upload**: Upload a PDF file to extract and process text.
- **Grammar Check**: Corrects grammar and explains changes.
- **Rephrase**: Rephrases the given text.

## Preview

Watch a preview of TextTune in action:

[![TextTune Preview](https://img.youtube.com/vi/D3UgIbl_VTI/0.jpg)](https://youtu.be/D3UgIbl_VTI)

## Getting Started

### Prerequisites

- **Docker**: To build and run the application container.
- **Python 3.9**: If you prefer running the app outside of Docker.

### Setup with Docker

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/texttune.git
    cd texttune
    ```

2. **Create a .env File**

    Create a `.env` file in the root directory with the following content:

    ```env
    GEMINI_API_KEY=your_gemini_api_key
    ```

    Replace `your_gemini_api_key` with your actual Gemini API key.

3. **Build the Docker Image**

    ```bash
    docker build -t texttune .
    ```

4. **Run the Docker Container**

    ```bash
    docker run -p 8501:8501 texttune
    ```

5. **Access the Application**

    Open your web browser and go to [http://localhost:8501](http://localhost:8501).

### Setup Without Docker

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/texttune.git
    cd texttune
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env File**

    Create a `.env` file in the root directory with the following content:

    ```env
    GEMINI_API_KEY=your_gemini_api_key
    ```

    Replace `your_gemini_api_key` with your actual Gemini API key.

5. **Run the Application**

    ```bash
    streamlit run app.py
    ```

6. **Access the Application**

    Open your web browser and go to [http://localhost:8501](http://localhost:8501).

## Project Structure

- **Dockerfile**: Docker configuration for building the container.
- **requirements.txt**: Python package dependencies.
- **app.py**: Main application code.
- **.env**: Environment variables (not included in version control).
- **README.md**: This file.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. Make sure to follow best practices and include tests with your contributions.

