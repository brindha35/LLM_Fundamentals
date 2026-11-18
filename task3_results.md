Task	Result
Token Counting	4 texts tested; 0.88 words/token in the last text
Monthly Usage	9,000 chats; 10.8M input tokens; 2.7M output tokens
Cost Estimation	Pricing details not provided, so cost cannot be calculated
Temperature	5 ChatGPT responses compared; wording varied. Actual temperature settings were not tested
Hallucination	Adding “I don't know if unsure” made uncertainty clearer

Conclusion: Tokens help measure text usage and estimate cost. Temperature can affect response variation. Clear prompts help reduce unsupported answers.

# Task 3 – LLM Fundamentals Results

## 1. Token Counting

Used `tiktoken` with `cl100k_base` encoding to count tokens in four sample texts.

Words per token was calculated for each text.

## 2. Monthly Token Calculation

| Metric | Result |
|---|---:|
| Chats per day | 300 |
| Chats per month | 9,000 |
| Input tokens per chat | 1,200 |
| Output tokens per chat | 300 |
| Monthly input tokens | 10,800,000 |
| Monthly output tokens | 2,700,000 |

Monthly cost: Pending trainer's model pricing.

## 3. Temperature Experiment

Used Ollama with the llama3.2:1b model.

| Temperature | Runs | Observation |
|---|---:|---|
| 0 | 5 | Responses were consistent and repeated the same wording. |
| 1.0 | 5 | Responses showed more variation in wording. |

Conclusion: Lower temperature produces more consistent responses, while higher temperature allows more variation.

## 4. Hallucination Experiment

Question: Who won the 1890 FIFA World Cup?

- Without instruction: The AI invented a World Cup result and details.
- With instruction: The AI still produced an unsupported winner.

Conclusion: Asking AI to say "I don't know" when unsure can help, but it does not guarantee hallucination prevention. Answers must be verified.

## Key Learnings

- Tokens are units used to process text.
- Context windows limit how much text a model can process at once.
- API costs depend on input and output token usage and model pricing.
- Temperature affects response variation.
- AI can hallucinate, so important information needs verification.

Note: Trainer did not provide model pricing.
Monthly cost calculation is pending until pricing is available.

**Illustrative Monthly Cost Calculation**

Assumed pricing (example only):
- Input: $0.15 per 1 million tokens
- Output: $0.60 per 1 million tokens

| Metric | Calculation | Cost |
|---|---|---:|
| Input cost | 10.8 × $0.15 | $1.62 |
| Output cost | 2.7 × $0.60 | $1.62 |
| **Total monthly cost** | | **$3.24** |

Note: These are assumed example prices because the trainer did not provide actual model pricing. This is not the actual API cost.