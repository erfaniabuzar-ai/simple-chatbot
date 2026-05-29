import anthropic

client = anthropic.Anthropic(api_key="YOUR_API_KEY")

print("سلام! من یه chatbot ساده هستم. برای خروج exit بنویس")

while True:
    user_input = input("تو: ")
    
    if user_input.lower() == "exit":
        print("خداحافظ!")
        break
    
    message = client.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    
    print("Claude:", message.content[0].text)
