import json
import io
import zipfile
from typing import Dict
from groq import Groq


client = Groq(
    api_key="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",
)

\
def get_base_structure():
    """Returns the base directory and file structure for the project."""
    return {
        "directories": [
            "my_project/src/utils",
            "my_project/tests"
        ],
        "files": {
           
                   }
    }


def generate_code(prompt: str, base_structure: Dict) -> Dict:
    """Generates code based on the user prompt and updates the project structure."""
    try:
    
        system_message = """
        Generate Python code  that should be in json format when converted it should be in  python code for a project with the following structure:
        - src/app.py: Main application file
        - src/utils/helpers.py: Helper functions
        - tests/test_app.py: Test cases
        - requirements.txt: Project dependencies
        - README.md: Project documentation
        - .gitignore: Git ignore rules
        
        Return a JSON object with the content for each file based on the project description and do not give duplicate keys in json

        example json format :
        
  "src/app.py": "from flask import Flask\nfrom utils.helpers import hello_world\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return hello_world()\n\nif __name__ == '__main__':\n    app.run(debug=True)",
  
  "src/utils/helpers.py": "def hello_world():\n    return 'Hello, World!'",
  
  "tests/test_app.py": "import unittest\nfrom src.app import app\n\nclass AppTestCase(unittest.TestCase):\n    def setUp(self):\n        self.app = app.test_client()\n        self.app.testing = True\n\n    def test_home(self):\n        response = self.app.get('/')\n        self.assertEqual(response.data.decode(), 'Hello, World!')\n\nif __name__ == '__main__':\n    unittest.main()",
  
  "requirements.txt": "Flask==2.2.3\nunittest2==1.1.0",
  
  "README.md": "# Flask Hello World\n\nThis is a simple Flask project with a 'Hello, World!' route.\n\n## Setup\n1. Install dependencies: `pip install -r requirements.txt`\n2. Run the app: `python src/app.py`\n\n## Test\nRun the test cases with: `python -m unittest tests/test_app.py`",
  
  ".gitignore": "venv/\n*.pyc\n__pycache__/\ninstance/\n.env"



        """

       
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Generate code for a Python project in that will {prompt}"},
                
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"}
        )
        print("manvith")
        

       
        # print(chat_completion.choices[0].message.content)
        print("---",(chat_completion.choices[0].message.content))
        
        generated_content = json.loads(chat_completion.choices[0].message.content)

        
        # Update file contents
        for file_path, content in generated_content.items():
            full_path = f"my_project/{file_path}"
            base_structure["files"][full_path] = content

        return base_structure

    except Exception as e:
        raise Exception(f"Failed to generate project: {str(e)}")

# 3. Create ZIP Archive
def create_zip(project_structure: Dict) -> io.BytesIO:
    """Creates a ZIP file containing the generated project structure."""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Add directories
        for directory in project_structure["directories"]:
            zip_file.writestr(f"{directory}/", "")

        # Add files with content
        for file_path, content in project_structure["files"].items():
            zip_file.writestr(file_path, content)

    zip_buffer.seek(0)
    return zip_buffer
