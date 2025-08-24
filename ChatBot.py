
import google.generativeai as genai

# ✅ Configure API Key
genai.configure(api_key="AIzaSyCJHn4Nb480G6U-Hk1EoV69Bmv8oKlzqAc")

# ✅ Use latest Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

print("Welcome to Gemini ChatBot! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break
    
    if user_input == "":
        print("ChatBot: Please type something!")
        continue
    
    # ✅ Generate response
    response = model.generate_content(user_input)
    print("ChatBot:", response.text)
