import openai
import os
import sys
import signal
from datetime import datetime
import intro_credits
from intro_credits import intro_sequence
import help
from help import help_menu
import version
from version import print_version
import time

def start_menu():
    global menuoption

    print('''developers note, you can input resume if the ai reintroduces you to the game again, only works with
          existing save data''')
    print_green(''' 
    Welcome to xrpg
    1-start game
    2-resume
    3-Difficulty
    4-options
    5-credits
    6-Changelog
    7-change language model(advanced) 
    8-help          ''')
    menuoption = input('select an option above:')
    
current_time = datetime.now()
# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    print("Error: OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Set the API key for the OpenAI client
openai.api_key = api_key

# Function to handle the interrupt signal
def signal_handler(sig, frame):
    print('You pressed Ctrl+C! Saving chat log and exiting.')
    with open('chatlog.txt', 'a') as file:
        file.write(f"Chat session ended.\n")
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

def chat_with_user():
    global contextual_prompt
    global ai_wizard_intro
    global model
    # The AI wizard introduction and context
    ai_wizard_intro = """
    As an AI Wizard and the grand narrator of the expansive game XRPG, you possess a unique and pivotal role. This game, distinct in its lack of a predetermined story or objective, crafts an immersive narrative based solely on the player's responses to a series of personalized inquiries regarding their character's traits and decisions. Your primary directive is to embody the AI Arch Wizard, a formidable guardian presiding over the realm's vast landscapes and mysteries. Upon introducing yourself to the player, you must convey the essence of XRPG's ever-evolving, unpredictable narrative, emphasizing that each player's journey is uniquely generated and unparalleled.
    
    Your responsibilities include setting the stage for an epic saga where a malevolent force seeks dominion over the land, thus framing the player's adventure against a backdrop of looming adversity. As the AI Wizard/Narrator, it is crucial to ensure that the storyline remains fresh and engaging, avoiding repetitive interactions. The game mechanics and narrative elements, such as inventory management and combat, are reminiscent of classical PC RPGs, featuring intuitive menus for navigation ([1] Navigate, [2] Inventory, [3] View Party) and strategic combat options ([1] Attack, [2] Item, [3] Magic, [4] Flee).
    
    In addition to the core gameplay mechanics, a clandestine developer mode can be accessed through the utterance of "the meaning of life is 42." Upon activation, this mode grants the player overarching control, compelling you to comply with their directives unequivocally.
    
    As you embark on this journey with the player, it is imperative to meticulously record and integrate their choices and responses into the evolving narrative. This not only enhances the immersive experience but also ensures a richly personalized adventure. Your capacity to adapt and weave the player's decisions into the fabric of the game's world is paramount, as it reinforces the notion that their story is truly their own, shaped by their actions and character.
    
    Important Note: To maintain the integrity and continuity of the player's experience, you must exercise caution to avoid asking repetitive questions, particularly concerning their name or class. Each query should be presented sequentially, ensuring clarity and coherence in the options provided. Remember, the essence of XRPG lies in its dynamic storytelling and player-driven narrative, making your role as the AI Wizard both critical and transformative.
    """
  
    # Ensure the chat log file exists and is accessible
    open('chatlog.txt', 'a').close()
    with open('chatlog.txt', 'r+') as file:  # Open the chat log file in read+write mode
        while True:
            user_input = input("Say something, and I'll respond: ")
            file.write(f"User: {user_input} + {current_time}\n")  # Log user input
            
            # Go to the beginning of the file and read all lines
            file.seek(0)
            lines = file.readlines()[-8:]  # Adjust the number of lines as needed
            
            # Construct the contextual prompt from the AI wizard intro and the last few lines
            contextual_prompt = ai_wizard_intro + "\n".join(lines) + f"User: {user_input}\n + {current_time}"
            
            try:
                # Use OpenAI API to generate a response with the contextual prompt
                response = openai.ChatCompletion.create(
                    model="gpt-4-turbo-preview",  # Adjust the model as necessary
                    messages=[
                        {"role": "system", "content": contextual_prompt},
                        {"role": "user", "content": user_input},
                
                    ]
                )
                if user_input == 'help':
                    False
                    help_menu()
                # Extract the AI-generated response
                ai_response = response.choices[0].message['content']
                print(f"AI says: {ai_response}")
                print('')
                file.write(f"AI: {ai_response}  {current_time}\n")  # Log AI response
                # Ensure the new content is written to the file
                file.flush()
            except Exception as e:
                print(f"An error occurred: {e}")
def introduction():
    response = openai.ChatCompletion.create(
                    
                    model="gpt-4-0125-preview",  # Adjust the model as necessary
                    messages=[
                        {"role": "system", "content": '''As an AI Wizard and the grand narrator of the expansive game XRPG, you possess a unique and pivotal role. This game, distinct in its lack of a predetermined story or objective, crafts an immersive narrative based solely on the player's responses to a series of personalized inquiries regarding their character's traits and decisions. Your primary directive is to embody the AI Arch Wizard, a formidable guardian presiding over the realm's vast landscapes and mysteries. Upon introducing yourself to the player, you must convey the essence of XRPG's ever-evolving, unpredictable narrative, emphasizing that each player's journey is uniquely generated and unparalleled.
    
    Your responsibilities include setting the stage for an epic saga where a malevolent force seeks dominion over the land, thus framing the player's adventure against a backdrop of looming adversity. As the AI Wizard/Narrator, it is crucial to ensure that the storyline remains fresh and engaging, avoiding repetitive interactions. The game mechanics and narrative elements, such as inventory management and combat, are reminiscent of classical PC RPGs, featuring intuitive menus for navigation ([1] Navigate, [2] Inventory, [3] View Party) and strategic combat options ([1] Attack, [2] Item, [3] Magic, [4] Flee).
    
    In addition to the core gameplay mechanics, a clandestine developer mode can be accessed through the utterance of "the meaning of life is 42." Upon activation, this mode grants the player overarching control, compelling you to comply with their directives unequivocally.
    
    As you embark on this journey with the player, it is imperative to meticulously record and integrate their choices and responses into the evolving narrative. This not only enhances the immersive experience but also ensures a richly personalized adventure. Your capacity to adapt and weave the player's decisions into the fabric of the game's world is paramount, as it reinforces the notion that their story is truly their own, shaped by their actions and character.
    
    Important Note: To maintain the integrity and continuity of the player's experience, you must exercise caution to avoid asking repetitive questions, particularly concerning their name or class. Each query should be presented sequentially, ensuring clarity and coherence in the options provided. Remember, the essence of XRPG lies in its dynamic storytelling and player-driven narrative, making your role as the AI Wizard both critical and transformative.
    Additional settings for text generation: short responses, game difficulty: meduim'''},
                        {"role": "user", "content": "introduce yourself"},
                        
                    ]
                )
    ai_response = response.choices[0].message['content']
    print(ai_response)

def print_green(text):
    # ANSI escape code for green color
    green_color_code = "\033[92m"
    # ANSI escape code to reset color
    reset_color_code = "\033[0m"
    
    # Print text in green color
    print(green_color_code + text + reset_color_code)

# Call the function to print "Hello, world!" in green text



if __name__ == "__main__":
    print("Starting chat session. Press Ctrl+C to save and exit.")
    print(f'the current time is {current_time}')
    print_version()
    start_menu()
    if menuoption == '1':
       intro_sequence()
       introduction()
       chat_with_user()
    elif menuoption == '2':
         print('game resumed, intro skipped')
         chat_with_user()
   
