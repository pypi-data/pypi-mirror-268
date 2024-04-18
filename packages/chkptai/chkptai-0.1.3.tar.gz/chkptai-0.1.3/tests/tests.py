    
if __name__ == "__main__":
    chkptAI = ChkptAI("5f525de37ae279171bd2f235268b212f")
    stream = chkptAI.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello what's the speed of light and what's its meaning in the universe!"}
        ]
    )
    print(type(stream))
    print(stream)