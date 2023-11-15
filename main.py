import time
import pyautogui
from PIL import ImageGrab

def get_screen():

    x1, y1, x2, y2 = 300, 400, 1000, 500
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    return screen

def is_cactus_present(screen):
    # Define the color of the cactus
    cactus_color = (83, 83, 83)  # RGB value

    # Check if any pixel in the specified area has the color of the cactus
    for x in range(0, screen.width, 10):
        for y in range(0, screen.height, 10):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == cactus_color:
                return True
    return False

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def main():
    print("Dino Game Automator is running. Press Ctrl+C to stop.")

    try:
        while True:
            screen = get_screen()

            if is_cactus_present(screen):
                jump()

    except KeyboardInterrupt:
        print("\nDino Game Automator stopped.")

if __name__ == "__main__":
    main()
