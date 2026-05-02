import google.generativeai as genai

API_KEY = "AIzaSyDSKl6uY2yqMA_VrLTHwA6_2s8JYuuCbQk"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message("Hello")
    print("Gemini:", response.text)
