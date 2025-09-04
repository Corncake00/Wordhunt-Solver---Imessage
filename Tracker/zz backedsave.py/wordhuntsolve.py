from google import genai
import os

os.environ["GEMINI_API_KEY"] = "redacted key unc"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
chat = client.chats.create(model="gemini-2.5-flash")

my_file = client.files.upload(file="/Users/chenghya/Desktop/Tracker/wordhunt1.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Given a 4×4 letter grid, search for valid English words (minimum 3 letters) by connecting adjacent cells, including diagonals, without reusing a cell in a word. As soon as a valid word is found, immediately output its cell coordinates (e.g., a1, a2, a3) before continuing to the next search."],
)

print(response.text)
