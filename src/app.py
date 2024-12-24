import streamlit as st
from generator import generate_code, create_zip,get_base_structure

def main():
    st.title("Python Project Generator")

    
    prompt = st.text_area(
        "Describe your project:",
        "Create a hello world Flask application"
    )
     
    db_integration = st.checkbox("Database Integration")
    dockerfile = st.checkbox("Include Dockerfile")
    cicd_pipeline = st.checkbox("Set up CI/CD Pipeline")

    
    if db_integration:
        prompt += " with database integration separate file "
    if dockerfile:
        prompt += " and include a Dockerfile"
    if cicd_pipeline:
        prompt += " and set up a CI/CD pipeline"
    
    if st.button("Generate Project"):
        try:
            with st.spinner("Generating project..."):
                
                base_structure = get_base_structure()  
                structure = generate_code(prompt,base_structure)
                
                
                st.subheader("Generated Files:")
                for file_path, content in structure["files"].items():
                    with st.expander(f"📄 {file_path}"):
                        st.code(content)
                
               
                zip_buffer = create_zip(structure)
                st.download_button(
                    label="Download Project",
                    data=zip_buffer,
                    file_name="python_project.zip",
                    mime="application/zip"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
