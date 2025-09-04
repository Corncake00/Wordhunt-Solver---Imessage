from PIL import ImageGrab
import os
from google import genai
import time
import re
import pyautogui

# ====== SETUP GEMINI ======
os.environ["GEMINI_API_KEY"] = "key is redacted for obvious reasons but it'd be here"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ====== TAKE SCREENSHOT ======
print("Get ready... capturing board in 3 seconds")
time.sleep(3)

# Define region as (left, top, right, bottom)
bbox = (1442, 358, 1663, 578)  
screenshot_path = "wordhunt_capture.png"
screenshot = ImageGrab.grab(bbox=bbox)
screenshot.save(screenshot_path)

# Confirmation printout about the screenshot
print(f"Screenshot saved to {screenshot_path}")
print(f"Screenshot size: {screenshot.size}, mode: {screenshot.mode}")

# ====== UPLOAD TO GEMINI ======
my_file = client.files.upload(file=screenshot_path)

prompt = """
Given a 4×4 letter grid, search for a 5 letter english word
by connecting adjacent cells (including diagonals) without reusing a cell in a word.
For each found word, output only the cell coordinates in order, separated by commas,
one sequence per line (e.g., "a1,a2,a3").
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, prompt],
)

raw_output = response.text
print("Gemini raw output:\n", raw_output)

# ====== PARSE GEMINI OUTPUT ======
sequences = []
for line in raw_output.strip().split("\n"):
    coords = [c.strip().lower() for c in line.split(",") if re.match(r"^[a-d][1-4]$", c.strip().lower())]
    if coords:
        sequences.append(coords)

print("\nParsed sequences:", sequences)

# ====== TILE MAPPING ======
tiles = {
    "a": [(1471, 389), (1525, 389), (1578, 389), (1636, 389)],
    "b": [(1471, 442), (1525, 442), (1578, 442), (1636, 442)],
    "c": [(1471, 500), (1525, 500), (1578, 500), (1636, 500)],
    "d": [(1471, 555), (1525, 555), (1578, 555), (1636, 555)]
}

def get_coord(label):
    row = label[0]
    col = int(label[1]) - 1
    return tiles[row][col]

def click_point(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)

def drag_to(x_start, y_start, x_end, y_end):
    pyautogui.moveTo(x_start, y_start)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.dragTo(x_end, y_end, duration=0.3, button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)

# ====== PLAY WORDS ======
for coords in sequences:
    for i in range(len(coords)):
        x, y = get_coord(coords[i])
        click_point(x, y)
        if i < len(coords) - 1:
            x2, y2 = get_coord(coords[i + 1])
            drag_to(x, y, x2, y2)
