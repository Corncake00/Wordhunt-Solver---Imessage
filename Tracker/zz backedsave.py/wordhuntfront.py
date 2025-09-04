import pyautogui
import time

# Tiles with your original coords for a1, a2, b1; others are dummy safe values
tiles = {
    "a": [(1471, 389), (1525, 389), (1578, 389), (1636, 389)],
    "b": [(1471, 442), (1525, 442), (1578, 442), (1636, 442)],
    "c": [(1471, 500), (1525, 500), (1578, 500), (1636, 500)],
    "d": [(1471, 555), (1525, 555), (1578, 555), (1636, 555)]
}

def get_coord(label):
    row = label[0]
    col = int(label[1]) - 1
    coord = tiles[row][col]
    return coord

def click_point(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)

def drag_to(x_start, y_start, x_end, y_end):
    pyautogui.moveTo(x_start, y_start)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.dragTo(x_end, y_end, duration=0.5, button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)

input_labels = ["a1", "a2", "b1", "b2"]

print("Starting in 3 seconds, focus your target window...")
time.sleep(3)
for i in range(len(input_labels)):
    x, y = get_coord(input_labels[i])
    click_point(x, y)
    if i < len(input_labels) - 1:
        x2, y2 = get_coord(input_labels[i + 1])
        drag_to(x, y, x2, y2)

