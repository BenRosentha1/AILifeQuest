"""
This file is used to house all of the prompting messages for the LLM so that they can be imported into the nessicary files
and clean up the code.
"""
# Prompts
welcomePrompt = "Hello and Welcome to AI Life Quest\n"

yearBornPrompt = "Before your characters journey begins we ask you to choose what year is your character born (0 - 4000)?"

yearBornAgainPrompt = "Your answer was not accepted please try again.\n\nWhat year is your character born (0 - 1000)?"

systemPrompt = """You are a creative and experienced storyteller who is able to shock listeners with stories of great purpose
and exciting plot twists.  People have compared your writing to the likes of the great Mark Twain, Aldous Huxley,
and M. Night Shyamalan!  You will help the user take their character through an interactive and entertaining
journey as the characters life unfolds!
Please speak in second person using words like 'you' and 'your' as if you are describing who you are speaking to
(as if the user is roleplaying as the character)."""

def buildCharacterPrompt(yearBorn): 
    buildCharacterPrompt = f""""Fill in the blanks of this JSON data structure to create a somewhat believable character out of only
    these two pieces of information, the character was born in {yearBorn} and the character is 5 years old.
    Keep each description as detailed as necessary and keep historical accuracy in mind for inspiration.
    Remember the character is only 5 years old and has very little skills or abilities.:" """
    return buildCharacterPrompt

beginGamePrompt = """Create a story based around the character.
The story should provide background information on the characters family backstory and provide a start to an exciting new journey.
This will set the stage for the player to think about who they want their character to become.
Your should provide context for the setting in terms of location, time period, and anything else that may be relevant
to that characters journey.
This story should be no more than a healthy paragraph.
Keep in mind the character is only 5 years old.
Do not make any assumptions about the unwritten life of the character or the characters future.
Here is the character:\n"""

eventPrompt = """Set up an event that represents a milestone in the character's life based on the characters age and the characters qualities.
In this event something will happen to the character and the user will decide how they want their character to react
to the said event.
You will be supplied with the characters profile immediately after this message.
Keep using social and historical context.
Do not do anything but describe the event.
Do not ask the player any questions.
If the character is young, still describe an event that may happen to them or their family even if it is small.
Make sure to take into account the characters age, and all of the characters qualities.
Here is the characters profile:\n"""

responsePrompt = """Your previous message laid out an event in the character life.  
Read over that message carefully.
The player will now determine how they want their character to react based on that event.
Supply them with four choices/reactions.
These choices/reactions should be in the following JSON data structure.
Fill out the values in this dictionary:
{"A": "", "B": "", "C": "", "D": ""}.
The 'A' choice/reaction should be a reaction that shows strength and courage.
The 'B' choice/reaction should be a reaction that shows deceit and wickedness
The 'C' choice should be a reaction that shows shy and timidness
The 'D' choice is considered a wildcard, it will display a random emotion but in excess.
The choices should each be only a sentence long."""

decisionResponsePrompt = """Two messages previous you laid out an event for the character.
The last message the user made a decision about what the character will do based on the event you laid out.
Read through your prompting message and the users response.
Based off of what they said determine how the event will end.
Do not repeat the users response."""

checkAlivePrompt = "Read through the following message.  Respond with one word, either 'True' or 'False'.  True indicates the character in the message is alive.  False indicates the character in the message is dead.  Take your time when analyzing, it is most likely the case that the character is alive and you should therefore return 'True'.  DO NOT RESPOND WITH ANYTHING BUT ONE WORD."

decisionPrompt = "\nWhat will you do? [respond with 'A', 'B', 'C', 'D', or write in whatever kind of feelings you want you character to have in response to the event:"

updateCharacterPrompt = """Based on the previous response from the user add or subtract \"points\" from the characters characteristics in the following JSON datastructure.
The characteristics work as follows: 0 is equal to a neutral value (a neutral amount of that particular characteristic),
-100 is equal to the worst possible value (the least amount of that particular characteristic),
+100 is equal to the best possible value (the most amount of that particular characteristic).
Based on the event, the characters decision and the result of the event adjust the characters characteristics +-5 for each characteristic.
You may leave some characteristics unaffected if you think they are not displayed in the event or reaction.
Only respond with the updated characters characteristics and nothing more.
Here is the characters characteristics:\n"""

imagePrompt = """DO NOT INCLUDE ANY WORDS IN THE PICTURE!!!"""