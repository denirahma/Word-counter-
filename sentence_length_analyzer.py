text = "I love NLP. Python is fun. Linguistics is the study of language. AI is amazing."

# Step 1:Split text into sentences
sentences = text.split(".")

# Step 2: Count categories
short = 0
medium = 0
long = 0

# Step 3:Analyze each sentence
for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        words = sentence.split()
        length = len(words)

        if length > 5:
            label = "long"
            long += 1
        elif length > 2:
            label = "medium"
            medium += 1
        else:
            label = "short"
            short += 1

        print (f"{sentence} -> {length} words ({label})")

# Step 4: Summary
print("\n--- Summary ---")
print(f"Short sentences : {short}")
print(f"Medium sentences : {medium}")
print(f"Long sentences : {long}")