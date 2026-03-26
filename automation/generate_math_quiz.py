
import random
import json

questions = []

for _ in range(20):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    questions.append({
        "question": f"{a} + {b}",
        "answer": a + b
    })

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Generated questions.json")
