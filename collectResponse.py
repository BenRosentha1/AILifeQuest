from openai import OpenAI

"""
This function collects the response from the model
"""
# Collect response
def collectResponse(client, model, messages, response_format=None):
        # Create and Prompt Chat
        completion = client.chat.completions.create(
            model = model,
            messages = messages,
            response_format = response_format
        )

        # Collect and return response
        response = completion.choices[0].message.content
        return response