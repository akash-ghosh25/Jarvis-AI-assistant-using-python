from google import genai

client = genai.Client(api_key="Your_gemini_Api")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)
