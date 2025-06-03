<!-- Activate streamlit virtual environment
.venv\Scripts\Activate.ps1

python -m streamlit run main.py

deactivate -->
## 🖼️ Demo Screenshots

### 📥 Upload and Process PDF
![Upload PDF](Screenshots/Untitled-2.jpg)

### 💬 AI Response
![GPT Result](Week1\Streamlit\Screenshots\Untitled-3.jpg)


# Resume Translator AI

A very basic Streamlit application that uses `pdfplumber` to extract text from uploaded PDF files and then sends that text to the OpenAI API for translation.

## Features

* **PDF Upload:** Upload PDF files directly in the web interface.
* **Text Extraction:** Extracts text content from each page of the uploaded PDF.
* **OpenAI Translation:** Sends extracted text to the OpenAI API to translate it into a specified target language.
* **Simple UI:** Built with Streamlit for a clean and straightforward user experience.

## How to Run Locally

### 1. Prerequisites

Before you start, ensure you have:

* **Python 3.8+** installed.
* An **OpenAI API Key**. You can get one from [platform.openai.com](https://platform.openai.com/).

### 2. Setup

1.  **Clone this repository** (or download the files):
    ```bash
    git clone [Your Repository URL]
    cd [Your Project Folder Name]
    ```

2.  **Create a Virtual Environment** (recommended):
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment**:
    * **macOS / Linux:**
        ```bash
        source .venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        .venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` yet, create one by running `pip freeze > requirements.txt` after installing `streamlit`, `pdfplumber`, `openai`, and `python-dotenv`.)*

### 3. Configuration

1.  **Create a `.env` file** in the root directory of your project (where your main `app.py` or similar file is).
2.  Add your OpenAI API key to this file:
    ```
    OPENAI_API_KEY="sk-YOUR_ACTUAL_OPENAI_API_KEY_HERE"
    ```
    **Important:** Do not share this file or commit it to public version control (like GitHub). Add `.env` to your `.gitignore` file.

### 4. Run the Application

1.  Make sure your virtual environment is still activated.
2.  Run the Streamlit app:
    ```bash
    streamlit run [your_main_app_file].py
    ```
    (Replace `[your_main_app_file].py` with the actual name of your Streamlit script, e.g., `chapter04.py` if that's what you're using).

3.  The application will open in your web browser.

## Usage

1.  Upload a PDF file using the "Choose a PDF file" button.
2.  (If implemented) Select your desired target language.
3.  The app will extract the first few lines of text from each page, send them to OpenAI for translation, and display the result.

## Customization

* **OpenAI Model:** You can change the OpenAI model (`gpt-4o`, `gpt-3.5-turbo`, etc.) in the Python code.
* **Extracted Lines:** Adjust how many lines are sent to OpenAI for translation in the code.
* **Frontend Styling:** Basic styling can be done via Streamlit's theming or custom CSS injection.

---
