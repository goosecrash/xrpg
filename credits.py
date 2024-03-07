import os
import time
import sys

def print_green(text):
    """Prints text in green color using ANSI escape codes."""
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    print(green_color_code + text + reset_color_code, end="")

def scroll_credits(credits, delay=0.5):
    """Scrolls credits vertically with a specified delay between lines."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    height = os.get_terminal_size().lines  # Get terminal height
    credits = credits.split('\n')

    # Add empty lines for initial scroll
    for _ in range(height):
        credits.insert(0, "")

    # Scroll through credits
    for index in range(len(credits)):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen each iteration
        for line in credits[index:index+height]:
            print_green(line)
            print()  # New line
        time.sleep(delay)  # Delay between scrolls

if __name__ == "__main__":
    # Example credits. Replace these with your game's credits.
    credits_text = """
XRPG: AI on the Line
Developed by xrpg.ai

Lead Developer: Kendrew Shen
Creative Writer: Kendrew Shen
AI Integration: Kendrew Shen
Game Design: Kendrew Shen

Special Thanks:
- Person A
- Person B
- Person C

Thank you for playing!
    """
    scroll_credits(credits_text, delay=0.8)  # Adjust delay as needed