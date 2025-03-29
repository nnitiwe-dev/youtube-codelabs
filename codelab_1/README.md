# Resume Parser

This is a **Resume Parser** built with **OpenAI’s Function Calling** feature. It extracts structured data—like name, email, skills, and experience—from raw resume text and outputs it as **JSON**, ready for database storage. Follow this guide to get it running on your machine!

---

## What It Does
- Input: Unstructured resume text.
- Output: Clean JSON (e.g., `{"name": "Jane Smith", "email": "jane.smith@example.com", ...}`).
- Use Case: Automate resume processing for hiring or data analysis.

---

## Step-by-Step Setup

### 1. Prerequisites
- Python 3.6+
- An [OpenAI API key](https://www.youtube.com/watch?v=OB99E7Y1cMA&pp=ygUVY3JlYXRlIG9wZW5haSBhcGkga2V5)

### 2. Install Requirements
Clone the repo and install the required library:
```bash
git clone https://github.com/nnitiwe-dev/youtube-codelabs.git
cd youtube-codelabs/resume-parser
pip install -r requirements.txt
```
*Note*: `requirements.txt` includes `openai`. If it’s missing, create it with:
```plaintext
openai
```

### 3. Configure Your API Key
1. Navigate to the `secrets/` folder.
2. Open (or create) `config.json` and add your OpenAI API key:
   ```json
   {
     "openai_api_key": "your-api-key-here"
   }
   ```
3. Save the file. This keeps your key secure and separate from the code.

### 4. Run the Code
Test the parser with a sample resume:
```bash
python resume_parser.py
```
You’ll see output like:
```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "skills": ["Python", "SQL"],
  "experience_years": 3
}
```
Try it with the sample resumes in `samples/`!

---

## Project Structure
- `resume_parser.py`: Main script for parsing resumes.
- `secrets/config.json`: Store your API key here.
- `data/`: Example resume texts to test with.
- `requirements.txt`: List of dependencies.

---

## Troubleshooting
- **API Key Error?** Double-check `config.json` and ensure your key is valid.
- **No Output?** Verify your resume text has clear details (name, email, etc.).
- Still stuck? Check out my [YouTube tutorial](https://youtu.be/mPc4dc8hj0g) or open an issue!

---

## Learn More
- Watch the full walkthrough on [YouTube](https://youtu.be/mPc4dc8hj0g).
- Read the companion [article]([https://open.substack.com/pub/nnitiwe/p/extracting-data-with-openai-an-introduction]).
- Explore OpenAI’s [Function Calling docs](https://platform.openai.com/docs/guides/function-calling).

Happy parsing! 🚀

