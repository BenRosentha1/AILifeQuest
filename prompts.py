# There are lots of prompts and they are making my code messy so to fix that all prompts will be imported from here

welcomePrompt = "Hello and Welcome to AI Life Quest\n"

yearBornPrompt = "Before your characters journey begins we ask you to choose what year is your character born (0 - 4000)?"

yearBornAgainPrompt = "Your answer was not accepted please try again.\n\nWhat year is your character born (0 - 1000)?"

initPrompt = "You are a creative and experienced storyteller who is able to shock listeners with stories of great purpose and shocking plot twists.  People have compared your writing to that of the likes of the great Mark Twain, Aldous Huxley, and M. Night Shyamalan!"

beginGamePrompt = "Create a story based around the character.  The story should provide background information on the characters family backstory and provide a start to an exciting new journey.  This will set the stage for the player to think about who they want their character to become.  Your should provide context for the setting in terms of location, time period, and anything else that may be relevant to that characters journey.  This story should be no more than a healthy paragraph.  Please speak in second person using words like you as if you are describing who you are speaking to.  Keep in mind the character is only 5 years old.  Do not make any assumptions about the unwritten life of the character or the characters future.  Here is the character:\n"

eventPrompt = "Set up an event that represents a milestone in the character's life based on the characters age and the characters qualities.  In this event something will happen to the character and the user will decide how they want their character to react to the said event.  You will be supplied with the characters profile immediately after this message.  Keep using social and historical context.  Do not do anything but describe the event.  Do not ask the player any questions.  If the character is young still describe an event that may happen to them or their family even if it is small.  Make sure to take into account the characters age, and all of the characters qualities.  Here is the characters profile:\n"

responsePrompt = "Your previous message laid out an event in the character life.  The player will now determine how they want their character to react based on that event.  Supply them with four choices they may choose from to determine how their character will feel in reaction to the event.  The choices should be labeled '(A)' '(B)' '(C)' '(D)' and each have a line separating them.  The '(A)' choice should be a reaction that shows strength and courage, the '(B)' choice should be a reaction that shows deceit and wickedness, the '(C)' choice should be a reaction that shows shy and timidness, the '(D)' choice is considered a wildcard (I want you to make this reaction show whatever kind of qualities you want but bring it to the extreme).  The choices should each be a sentence long.  Only respond with the choices and nothing more"

decisionResponsePrompt = "Two messages previous you laid out an event for the character.  The last message the user made a decision about what the character will do based on the event you laid out.  Read through your prompting message and the users response.  Based off of what they said determine how the event will end.  Do not repeat the users response.  "

checkAlivePrompt = "Read through the following message.  Respond with one word, either 'True' or 'False'.  True indicates the character in the message is alive.  False indicates the character in the message is dead.  Take your time when analyzing, it is most likely the case that the character is alive and you should therefore return 'True'.  DO NOT RESPOND WITH ANYTHING BUT ONE WORD."