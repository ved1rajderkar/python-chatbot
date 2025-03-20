import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
def chatbot_response(user_input):
    try:
        # Make an API request to OpenAI's ChatGPT model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100,
            temperature=0.7
        )
        # Extract the response text
        return response['choices'][0]['message']['content'].strip()

    except openai.error.OpenAIError as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        # Take user input
        user_input = input("You: ")
        
        # Exit condition for the chatbot
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot response
        response = chatbot_response(user_input)
        
        # Print the chatbot's response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
