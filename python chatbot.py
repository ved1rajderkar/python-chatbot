import os
import openai

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Error: {str(e)}"

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
