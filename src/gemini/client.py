from google import genai


class GeminiClient:
    def __init__(self):
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        self.client = genai.Client()

    def generate_response(self, prompt: str):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        return response.text
