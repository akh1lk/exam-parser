import json
from parser import save_to_docx, save_to_LaTeX

def load_json(filepath: str) -> dict:
    """
    Loads a JSON file and returns it as a dictionary.
    
    Args:
        filepath (str): Path to the JSON file.
    
    Returns:
        dict: Parsed JSON data.
    """
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def test_save_to_docx(json_filepath: str, output_path: str):
    """
    Tests the save_to_docx function using the existing JSON file.
    
    Args:
        json_filepath (str): Path to the input JSON file.
        output_path (str): Path to save the output DOCX file.
    """
    data = load_json(json_filepath)
    save_to_docx(data, output_path)
    print(f"DOCX file saved to {output_path}")

def test_save_to_LaTeX(json_filepath: str, output_path: str):
    """
    Tests the save_to_LaTeX function using the existing JSON file.
    
    Args:
        json_filepath (str): Path to the input JSON file.
        output_path (str): Path to save the output LaTeX file.
    """
    data = load_json(json_filepath)
    save_to_LaTeX(data, output_path)
    print(f"LaTeX file saved to {output_path}")


if __name__ == "__main__":
    # Paths for input JSON and output files
    json_filepath = "output3.json"
    docx_output_path = "output3.docx"
    latex_output_path = "output3.tex"

    # Test DOCX export
    test_save_to_docx(json_filepath, docx_output_path)

    # Test LaTeX export
    test_save_to_LaTeX(json_filepath, latex_output_path)


#LaTeX Code

# def save_to_LaTeX(data: dict, output_path: str = "output.tex"):
#     from typing import List

#     def split_into_centerlines(answer: str, max_length: int = 80) -> List[str]:
#         lines = []
#         current_line = ""
#         inside_math = False

#         for char in answer:
#             current_line += char
#             if char == '$':
#                 inside_math = not inside_math
#             if not inside_math and len(current_line) >= max_length:
#                 lines.append(current_line.strip())
#                 current_line = ""
#         if current_line.strip():
#             lines.append(current_line.strip())

#         return lines

#     with open(output_path, "w") as tex:
#         tex.write(r"""\documentclass[14pt]{exam}
#         \usepackage{mathtools}
#         \usepackage{advdate}
#         \usepackage{graphpap}
#         \usepackage{amsmath}
#         \usepackage{anysize}
#         \usepackage{amsthm}
#         \usepackage{amssymb}
#         \usepackage{cite}
#         \usepackage{graphicx}
#         \usepackage{mathrsfs}
#         \usepackage{upgreek}
#         \usepackage{extsizes}
#         \usepackage[margin=0.75in]{geometry}
#         \usepackage{fancyhdr}
#         \usepackage{emoji}

#         \begin{document}
#         """)

#         metadata = data.get("metadata", {})
#         author = metadata.get("author", "Unknown Author")
#         title = metadata.get("title", "Untitled Document")
#         course = metadata.get("course", "Unknown Course")
#         date = metadata.get("date", "Unknown Date")
#         additional_info = metadata.get("additional_info", "")

#         tex.write(f"\\chead{{\\emph{{ {author} }}}}\n")
#         tex.write(f"\\centerline{{{{\\bf{{\\Large {title} }}}}}}\n")
#         tex.write(f"\\centerline{{{{\\emph{{\\large {course}, {date} }}}}}}\n")
#         if additional_info:
#             tex.write(f"\\centerline{{Additional Info: {additional_info}}}\n")
#         tex.write("\n\\bigskip\n\n")

#         for idx, qa in enumerate(data["content"], start=1):
#             # wrap question with existing logic (since not in \centerline).
#             question = qa["question"]
            
#             answer = qa.get("answer", "")
#             subquestions = qa.get("subquestions")
#             if answer:
#                 # Now we do multi-line centerline for answers
#                 answer_lines = split_into_centerlines(answer, max_length=80)
#                 for i, line in enumerate(answer_lines):
#                     tex.write(f"\\centerline{{\\textbf{{Answer:}} {line}}}" if i == 0  else "\\centerline{" + line + "}")
#                     tex.write("\\\\\n" if i < len(answer_lines) - 1 else "\\bigskip\n")

#             if subquestions:
#                 for _, sub in enumerate(subquestions, start=1):
                    
#                     sub_q = sub["question"]
#                     tex.write(f"{sub_q}\\\\\n")

#                     sub_a = sub.get("answer", "")
#                     if sub_a:
#                         subanswer_lines = split_into_centerlines(sub_a, max_length=80)
#                         for i, line in enumerate(subanswer_lines):
#                             tex.write(f"\\centerline{{\\textbf{{Answer:}} {line}}}" if i == 0 else "\\centerline{" + line + "}")
#                             tex.write("\\\\\n" if i < len(subanswer_lines) - 1 else "\\bigskip\n")

#                     tex.write("\n\\bigskip\n\n")

#         tex.write("\\end{document}")
#     print(f"Output saved to {output_path}")