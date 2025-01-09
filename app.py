from flask import Flask, request, render_template, send_file, redirect, url_for
import os
from parser import process_file, organize_LLM, save_to_json, save_to_docx, save_to_pdf

app = Flask(__name__, template_folder="views")  # Set template folder to 'views'
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "outputs"

# Ensure directories exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

def sanitize_filename(filename):
    """
    Sanitizes the filename by removing or replacing invalid characters.
    """
    return "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in filename)

@app.route("/", methods=["GET", "POST"])
def upload_files():
    if request.method == "POST":
        # Handle file uploads
        question_file = request.files["question_file"]
        answer_file = request.files["answer_file"]

        # Save uploaded files
        question_path = os.path.join(app.config["UPLOAD_FOLDER"], question_file.filename)
        answer_path = os.path.join(app.config["UPLOAD_FOLDER"], answer_file.filename)
        question_file.save(question_path)
        answer_file.save(answer_path)

        # Process the uploaded files
        questions_text = process_file(question_path)
        answers_text = process_file(answer_path)
        paired_results = organize_LLM(questions_text, answers_text)

        # Extract title from paired_results metadata
        title = paired_results.get("metadata", {}).get("title", "output_QA")
        sanitized_title = sanitize_filename(title)

        # Generate filenames using the extracted title
        json_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{sanitized_title}_Q&A.json")
        docx_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{sanitized_title}_Q&A.docx")

        # Save outputs (JSON, DOCX)
        save_to_json(paired_results, json_path)
        save_to_docx(paired_results, docx_path)

        return redirect(url_for("download_files", title=title))

    return render_template("upload.html")

@app.route("/download")
def download_files():
    """
    Renders download page w/ links to download the output files.
    """
    # get title from request
    title = request.args.get("title", "output_QA")
    sanitized_title = sanitize_filename(title)
    
    # create filenames
    json_file = f"{sanitized_title}_Q&A.json"
    docx_file = f"{sanitized_title}_Q&A.docx"
    
    # Check if the files exist
    json_path = os.path.join(app.config["OUTPUT_FOLDER"], json_file)
    docx_path = os.path.join(app.config["OUTPUT_FOLDER"], docx_file)
    
    if os.path.exists(json_path) and os.path.exists(docx_path):
        return render_template(
            "download.html",
            json_url=url_for("get_file", filename=json_file),
            docx_url=url_for("get_file", filename=docx_file)
        )
    else:
        return "Error: Files not found", 404

@app.route("/files/<filename>")
def get_file(filename):
    """
    send output files for download
    """
    return send_file(os.path.join(app.config["OUTPUT_FOLDER"], filename), as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
