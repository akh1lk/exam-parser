# **GradeWiz Parser**

Questions & Answer Parser:

- Flask API intelligently pairs using OpenAI’s LLM, 
- Output Formats: **JSON**, **DOCX** 
- Inputs: **PDF**, **DOCX**, **images**, and **plain text** files.
---

## **Features**

- **Upload** question and answer files in PDF, DOCX, or image formats.
- **Process** the files using OpenAI's GPT model to intelligently pair questions with their corresponding answers.
- **Download** the output in JSON, DOCX, or PDF format.
- Supports **OCR** for images using Tesseract.

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/akh1lk/exam-parser
   cd gradewizParser
   ```

2. **Install Tesseract (MacOS)**:
   ```bash
   brew install tesseract
   ```

3. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the OpenAI API Key**:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```bash
     echo "OPENAI_KEY=your_openai_api_key_here" > .env
     ```

---

## **Running the Application**

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and go to `http://localhost:8000/.

---

## **Usage**

1. **Upload** your question and answer files.
2. The app will process the files and generate output in **JSON**, **DOCX**, and **PDF** formats.
3. **Download** the processed files from the provided links.

---

## **File Structure**

```
/gradewizParser
├── /static               # CSS styles
├── /views                # HTML templates (upload and download pages)
├── /uploads              # Uploaded files (will be created when ran)
├── /outputs              # Generated output files (JSON, DOCX, PDF)
├── app.py                # Flask app
├── parser.py             # Core processing logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
"""