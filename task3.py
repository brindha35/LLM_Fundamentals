import tiktoken

texts = [
    "Hello, how are you?",
    "Python is a programming language.",
    "Artificial Intelligence helps machines learn.",
    "Semantic search finds relevant information using embeddings."
]
encoding = tiktoken.get_encoding("cl100k_base")
for text in texts:
    tokens = encoding.encode(text)
    print(text, "->", len(tokens), "tokens")

for text in texts:
    tokens = encoding.encode(text)
    words = len(text.split())
    token_count = len(tokens)

    words_per_token = words / token_count

    print("Text:", text)
    print("Words:", words)
    print("Tokens:", token_count)
    print("Words per Token:", round(words_per_token, 2))
    print("--------------------")

chats_per_day = 300
days_per_month = 30

input_tokens_per_chat = 1200
output_tokens_per_chat = 300

monthly_chats = chats_per_day * days_per_month

monthly_input_tokens = monthly_chats * input_tokens_per_chat
monthly_output_tokens = monthly_chats * output_tokens_per_chat

print("Monthly Chats:", monthly_chats)
print("Monthly Input Tokens:", monthly_input_tokens)
print("Monthly Output Tokens:", monthly_output_tokens)



answers = [
    "AI helps computers perform tasks like humans.",
    "AI allows computers to think and learn.",
    "AI performs learning and problem-solving.",
    "AI helps machines learn from data.",
    "AI helps computers understand and solve problems."
]

print("Temperature Test Results:")
for i, answer in enumerate(answers):
    print("Run:", i + 1)
    print(answer)

print("Temperature Test Summary")
print("Total Runs: 5")
print("Observation: Answers have different wording.")
print("Conclusion: AI responses can vary.")

print("Hallucination Test Results")

print("Without Instruction:")
print("No reliable historical evidence found.")

print("With Instruction:")
print("I don't know. No reliable historical evidence found.")

print("Conclusion: Clear instructions help AI avoid unsupported answers.")

print("Temperature 0 vs Temperature 1.0")
print("Temperature 0: More consistent responses expected.")
print("Temperature 1.0: More varied responses expected.")