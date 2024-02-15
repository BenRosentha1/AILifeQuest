from openai import OpenAI
from dotenv import load_dotenv
import os, json

from prompts import initPrompt

# Load environment variables from .env
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=api_key)

class Character:
    # Age:
    '''The character will always start at age zero.'''
    age = 5
    
    # User given qualities:
    '''These qualities are chosen by the user and displayed the entire game.  These will never change through an iteration of the game.'''
    yearBorn = 0

    # This will be how the game is determined to be over or not
    alive = True

    # Characteristics:
    ''' These characteristics are hidden from the user and initialized at 0.  A positive value indicates the characters has a plentiful
    amount of that characteristic and a negative value indicates the character has a scarce amount of the characteristic.  The greater
    the absolute value of the characteristic the more/less of the characteristic the character has.  They will influence how the AI
    thinks/acts for the character.  They will be influenced at each decision point throughout the characters life.'''
    characteristics = {
        "Leadership" : 0,
        "Willpower" : 0,
        "Internal Strife" : 0,
        "Empathy" : 0,
        "Integrity" : 0,
        "Curiosity" : 0,
        "Adaptability" : 0,
        "Resilience" : 0,
        "Creativity" : 0,
        "Optimism" : 0,
        "Courage" : 0,
        "Altruism" : 0}

    # AI given Qualities:
    ''' These qualities will be picked by the AI and explained to the user when the game starts or when the character develops these qualities.
    This gives background to the character as these are things that the character is unable to control but sets the stage of their life.  these
    qualities may change and develop over the characters life.'''
    qualities = {
        "Name [First Last]" : "",
        "Gender" : "",
        "Sex" : "",
        "Sexuality" : "",
        "Location" : "",
        "Ethnicity" : "",
        "Nationality" : "",
        "Sibling Dynamic" : "",
        "Socio-Economic Class" : "",
        "Health Condition" : "",
        "Immigration" : "",
        "Religion" : "",
        "Native Language" : "",
        "Fluent Languages" : "",
        "Local Community" : "",
        "Parent Marital Status" : "",
        "Marital Status" : "",
        "Parents Presence" : "",
        "Disabilities" : "",
        "Family Structure" : "",
        "Mother Education" : "",
        "Father Education" : "",
        "Mother Profession" : "",
        "Father Profession" : ""}

    # Functions:
    
    # Initialize
    '''This initializes the character.  It will be called at the very beginning of the game and the parameters are as follows:
    character = Character(self, yearBorn)
    This will set the characters yearBorn'''
    def __init__(self, yearBorn):
        self.yearBorn = yearBorn

    ''' This will have chat gpt build the character and fill out the character profile'''
    def initializeCharacter(self, model):
        # Response format
        response_format = { "type" : "json_object" }

        # Prompts
        prompt1 = "Fill in the blanks of this json data structure to create a somewhat believable character out of only these two pieces of information, the character was born in " + str(self.yearBorn) + " and the character is 5 years old.  (Keep each description as detailed as necessary and keep historical accuracy in mind for inspiration) (Remember the character is only 5 years old and has very little skills or abilities):" 
        
        # Prompting messages
        messages = [
            {
                "role" : "user",
                "content" : initPrompt
            },
            {
                "role" : "user",
                "content" : prompt1
            },
            {
                "role" : "user",
                "content" : json.dumps(self.qualities)
            }
        ]

        # Create and Prompt Chat
        completion = client.chat.completions.create(
            model = model,
            messages = messages,
            response_format = response_format
        )

        # Response
        response = completion.choices[0].message.content

        # Log the response
        newMessages = [
            {
                "role" : "system",
                "content" : response
            }
        ]

        # Update messages
        messages.extend(newMessages)

        # Update character qualities
        self.qualities = json.loads(response)

        # Return the new list of messages
        return messages


    # Update Character
    def updateCharacter(self, model, messages):
        
        prompt = "Based on the previous response from the user add or subtract \"points\" from the characters characteristics.  The characteristics work as follows: 0 is equal to a neutral value (a neutral amount of that particular characteristic), -100 is equal to the worst possible value (the least amount of that particular characteristic), +100 is equal to the best possible value (the most amount of that particular characteristic).  Based on the users response to how their character should act (based on the event you described in the message previous to their response) adjust the characters characteristics +-5 for each characteristic, you may leave some characteristics unaffected if you think they are not displayed in the event or reaction.  Only respond with the updated characters characteristics and nothing more.  Here is the characters characteristics:\n"

        # Response format
        response_format = { "type" : "json_object" }

        newMessages = [
            {
                "role" : "user",
                "content" : prompt
            },
            {
                "role" : "user",
                "content" : json.dumps(self.characteristics)
            }
        ]

        # Update messages
        messages.extend(newMessages)

        # Create and Prompt Chat
        completion = client.chat.completions.create(
            model = model,
            messages = messages,
            response_format = response_format
        )

        # Response
        response = completion.choices[0].message.content

        # Log the response
        newMessages = [
            {
                "role" : "system",
                "content" : response
            }
        ]

        # Update messages
        messages.extend(newMessages)

        # Update character qualities
        self.characteristics = json.loads(response)
