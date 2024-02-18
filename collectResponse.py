from openai import OpenAI
"""
This function collects the response from the model
"""

def collectResponse(client, model, messages, responseFormat=None):
        # Create and Prompt Chat
        completion = client.chat.completions.create(
            model = model,
            messages = messages,
            response_format = responseFormat
        )

        # Collect and return response
        response = completion.choices[0].message.content
        return response