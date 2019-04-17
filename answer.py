import json
import random

with open('pool.json') as f:
    answer = json.load(f)

while True:
    question = input("Ваш вопрос: ")
    print(random.choice(answer))
