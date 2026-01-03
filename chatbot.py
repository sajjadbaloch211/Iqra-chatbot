
import os
from groq import Groq

class ChatBot:
    def __init__(self):
        # In a production environment, use os.environ.get('GROQ_API_KEY')
        # Using the key provided by the user for this session
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        
        # Load policies context
        try:
            with open('policies.txt', 'r', encoding='utf-8') as f:
                self.context = f.read()
        except FileNotFoundError:
            self.context = "You are a helpful academic assistant."
            print("Warning: policies.txt not found.")

    def get_response(self, user_input):
        try:
            # Check for specific question about LLM/API
            if "which llm" in user_input.lower() or "what llm" in user_input.lower() or "what model" in user_input.lower():
                return "I am powered by the Groq API, specifically using the llama-3.1-8b-instant model, as integrated by you."

            # Check for questions about who created the bot
            if "who made you" in user_input.lower() or "who created you" in user_input.lower() or "creator" in user_input.lower() or "developer" in user_input.lower() or "kis ne banaya" in user_input.lower():
                return "I was developed by Syed Arif Ahmad."

            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a helpful and professional academic assistant for Iqra University. Use the following context to answer student queries nicely and accurately. If the answer is not in the context, guide them to the official portal or administration. \n\nCONTEXT:\n{self.context}"
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                model="llama-3.1-8b-instant",
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Sorry, I encountered an error regarding the AI service: {str(e)}"

if __name__ == "__main__":
    bot = ChatBot()
    # Test interaction
    print("Bot ready. Type 'quit' to exit.")
    while True:
        txt = input("You: ")
        if txt.lower() == 'quit':
            break
        print("Bot:", bot.get_response(txt))
