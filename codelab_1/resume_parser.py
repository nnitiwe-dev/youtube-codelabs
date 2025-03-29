import openai  # Import OpenAI library for interacting with GPT models
import json  # Import JSON module to handle JSON data
import pandas as pd  # Import Pandas for data handling

# Load API keys from a JSON configuration file
with open('codelab_1/secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

# Set OpenAI API key from the loaded configuration
openai.api_key = secret_keys['openai_api_key']

# Function to extract details from a given resume text
def extract_applicant_details(resume_text):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a resume-parsing assistant."},
            {"role": "user", "content": f"Extract the name, email, skills, and years of experience from this resume:\n\n{resume_text}"}
        ],
        functions=[
            {
                "name": "extract_details",
                "description": "Extract applicant details from a resume",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "skills": {"type": "array", "items": {"type": "string"}},
                        "experience_years": {"type": "number"}
                    },
                    "required": ["name", "email", "skills", "experience_years"]
                }
            }
        ],
        function_call={"name": "extract_details"}
    )
    return json.loads(response.choices[0].message.function_call.arguments)

# Function to load resumes from a CSV file and process multiple rows
def process_resumes_from_csv(csv_path, num_rows=5):
    """
    Reads a CSV file, extracts resumes from a specific column, and processes a given number of rows.
    :param csv_path: Path to the CSV file.
    :param num_rows: Number of rows to process (default: 5).
    :return: List of extracted applicant details.
    """
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_path)
        
        # Ensure the required column exists
        if 'Resume_str' not in df.columns:
            raise KeyError("The column 'Resume_str' was not found in the CSV file.")
        
        # Select the first `num_rows` resumes from the dataset
        resumes = df['Resume_str'].head(num_rows).tolist()
        
        # Process each resume and store the extracted details
        extracted_details = [extract_applicant_details(resume) for resume in resumes]
        
        return extracted_details
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return []

# Function to save extracted details to a JSON file
def save_extracted_details_to_json(data, output_path='codelab_1/output/extracted_resumes.json'):
    """
    Saves the extracted resume details into a JSON file.
    :param data: List of extracted resume details.
    :param output_path: File path to save the JSON output.
    """
    try:
        with open(output_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
        print(f"Extracted details saved to {output_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

# Example usage
if __name__ == "__main__":
    csv_file_path = "codelab_1/data/Resume_List.csv"
    extracted_data = process_resumes_from_csv(csv_file_path, num_rows=5)
    
    if extracted_data:
        print("=" * 60)  # Prints a line of 60 '=' characters for formatting
        print("====    EXTRACTED DATA SAVED SUCCESSFULLY    ====")  # Fancy text formatting
        print("=" * 60)

        print(json.dumps(extracted_data, indent=2))
        save_extracted_details_to_json(extracted_data)