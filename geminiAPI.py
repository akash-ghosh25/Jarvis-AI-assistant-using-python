from google import genai

client = genai.Client(api_key="AIzaSyB6q0M_3EIsE3AR8QLjRTYyeQS7GpG1CFM")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)