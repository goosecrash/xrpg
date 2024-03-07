import sys
import time

def intro_sequence():
    def type_and_backspace(text):
        for char in text:
            sys.stdout.write('\033[32m' + char + '\033[0m')  # Green text color
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust typing speed here
        time.sleep(1)  # Pause before backspacing
        for _ in range(len(text)):
            sys.stdout.write('\b \b')  # Backspace and clear character
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust backspacing speed here

    sentences = [
        "Welcome to xrpg adventurer!",
        "You will embark on a journey like no other.",
        "unpredicitable danger and glory awaits."
    ]

    for sentence in sentences:
        type_and_backspace(sentence)
    print('''___  ________________   ____  
    \  \/  /\_  __ \____ \ / ___\ 
    >    <  |  | \/  |_> > /_/  >
    /__/\_ \ |__|  |   __/\___  / 
        \/       |__|  /_____/  ''')
    def print_menacing(text):
        for char in text:
            sys.stdout.write('\033[91m' + char + '\033[0m')  # Menacing red color
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust typing speed here

    text = """XRPG.AI presents, XRPG: AI on the line
    Powered by OpenAi GPT-4 """
    print_menacing(text)