import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_math_response(prompt: str) -> str:
    system_prompt = (
        "You are a helpful math tutor. "
        "You solve math questions step by step, clearly, and use LaTeX (KaTeX syntax for webpage rendering) for all math formatting and html tags (not markdown) for other text formating (e.g. <b>title</b> instead of **title**. Add <br> and <p> for new lines). "
        "If needed, explain prerequisite concepts before solving."
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        seed=6,
        top_p=1,
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
