from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)
while True:
    user_input = input("You: ") 
    if user_input.lower() in ["exit", "quit", "bye","see you later"]:
        print("Chatbot: Goodbye!")
        break
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful and friendly AI assistent."},
            {"role": "user","content": user_input}
        ]
    )
    reply = response.choices[0].message.content.strip()
    print(f"Chatbot: {reply}\n")