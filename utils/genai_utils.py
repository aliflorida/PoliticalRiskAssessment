import google.generativeai as genai
import os

def generate_narrative(country, investment_type, concerns):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Generate a 3-paragraph forecast narrative for a {investment_type} project in {country}. Focus on concerns: {concerns}."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating AI narrative: {e}"