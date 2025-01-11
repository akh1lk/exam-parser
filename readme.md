# **AI Exam Parser**

Questions & Answer Parser w/ Flask API:

- Flask API intelligently pairs using OpenAI’s LLM, 
- Output Formats: **JSON**, **DOCX** 
- Inputs: **PDF**, **DOCX**, **images**, and **plain text** files.
- **Note: Test Files are in /exam-parser/test-inputs**
---

## **Features**

- **Upload** question and answer files in PDF, DOCX, or image formats.
- **Process** the files using OpenAI's GPT model to intelligently pair questions with their corresponding answers.
- **Download** the output in JSON or DOCX formats.
- Supports **OCR** for images using Tesseract.

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/akh1lk/exam-parser
   cd exam-parser
   ```

2. **Install Tesseract (MacOS)**:
   ```bash
   brew install tesseract
   ```

3. **Create and Activate a Virtual Environment**:
   ```bash
   #If on VSCode, you can use the built-in venv & requirements creator
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If error in parser.py, manually do 'pip install pytesseract'

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

3. **Wait 30ish seconds** for output to be generated.

---

### Example: (.PNG Inputs) -> (.JSON & .DOCX) Outputs

<img src="https://github.com/user-attachments/assets/d79edb8c-b30c-4c5a-aac2-16176074b4c1" height="150"> <img src="https://github.com/user-attachments/assets/d37c026f-296f-4480-b5d6-de703441ebfc" height="150"/> <img src="https://github.com/user-attachments/assets/749e8a8c-aaf7-4c2a-9687-f23aefa62178" height="150"> <img src="https://github.com/user-attachments/assets/a3d3590e-9be6-4067-9559-2de688135c9f" height="150">

---

## **File Structure**

```
/exam-parser
├── /static               # CSS styles
├── /views                # HTML templates (upload and download pages)
├── /uploads              # Uploaded files (will be created when ran)
├── /outputs              # Generated output files (JSON, DOCX, PDF)
├── app.py                # Flask app
├── parser.py             # Core processing logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
