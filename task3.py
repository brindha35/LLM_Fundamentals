
import tiktoken
import ollama



texts = [
    "Hello, how are you?",
    "Python is a programming language.",
    "Artificial Intelligence helps machines learn.",
    "Semantic search finds relevant information using embeddings."
]

encoding = tiktoken.get_encoding("cl100k_base")

print("TOKEN COUNT RESULTS")

for text in texts:
    tokens = encoding.encode(text)
    words = len(text.split())
    token_count = len(tokens)

    print("Text:", text)
    print("Words:", words)
    print("Tokens:", token_count)
    print("Words per Token:", round(words / token_count, 2))
    print("--------------------")




chats_per_day = 300
days_per_month = 30

input_tokens_per_chat = 1200
output_tokens_per_chat = 300

monthly_chats = chats_per_day * days_per_month

monthly_input_tokens = monthly_chats * input_tokens_per_chat
monthly_output_tokens = monthly_chats * output_tokens_per_chat

print("\nMONTHLY TOKEN CALCULATION")
print("Monthly Chats:", monthly_chats)
print("Monthly Input Tokens:", monthly_input_tokens)
print("Monthly Output Tokens:", monthly_output_tokens)




prompt = "Define AI in 10 words."

print("\nTEMPERATURE 0 RESULTS")

for i in range(5):
    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt,
        options={"temperature": 0}
    )

    print("Run:", i + 1)
    print(response["response"])
    print("--------------------")


print("\nTEMPERATURE 1.0 RESULTS")

for i in range(5):
    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt,
        options={"temperature": 1.0}
    )

    print("Run:", i + 1)
    print(response["response"])
    print("--------------------")




print("\nHALLUCINATION TEST")

question = "Who won the 1890 World Cup?"

print("\nWithout Instruction:")

response = ollama.generate(
    model="llama3.2:1b",
    prompt=question
)
print(response["response"])

print("\nWith Instruction:")

response = ollama.generate(
    model="llama3.2:1b",
    prompt=question + " If you are unsure, say I don't know."
)
print(response["response"])
