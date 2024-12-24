 Python Project Generator

A Streamlit application that generates Python project boilerplates using AI.

## Setup
1. Create virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Create  Groq API key  :
```
client = Groq(
    api_key="put your Gorq api key here ",
) 

4. Run the application:
```bash
streamlit run src/app.py
```

## Project Structure
- src/
  - app.py         # Streamlit interface
  - generator.py   # Project generation logic
- requirements.txt # Project dependencies
- README.md       # Project documentation
- .gitignore      # Git ignore rules