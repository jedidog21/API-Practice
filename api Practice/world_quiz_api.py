import requests
import random
import os
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass 

API_KEY = os.environ.get("REST_COUNTRIES_API_KEY")

response = requests.get(
  'https://api.restcountries.com/countries/v5?response_fields=names.common,codes.alpha_2,flag.emoji,capitals,codes.alpha_3&limit=100',
  headers={'Authorization': API_KEY}
)
data = response.json()

def get_ran_country():
    return data['data']['objects'][random.randint(0,99)]

correct = 0

def list_answers(name):
    answers = [name]
    for i in range(3):
        answers.append(get_ran_country()['names']['common'])
    random.shuffle(answers)
    return answers

def check_answer(answer, name):
    global correct
    if (answer.lower() == name.lower()):
        correct += 1
        print("\nCorrect\n")
    else:
        print(f"\nIncorrect, the correct answer is {name}\n")


hardmode = input("Would you like to turn on hard mode? (y/n)")
while (True):
    if (hardmode.lower() == "y"):
        hardmode = True
        break
    elif (hardmode.lower() == "n"):
        hardmode = False
        break
    else:
        print ("Not a valid response")
        hardmode = input("Would you like to turn on hard mode? (y/n)")

q = 0
while (q < 5):
    a = random.randint(1,3)
    country = (get_ran_country())
    name = country['names']['common']
    question = ""
    match a:
        case 1:
            a2 = random.randint(2,3)
            question = f"What country has the {a2} letter country code of {country['codes'][f'alpha_{a2}']}?"
        case 2:
            question = f"What country has the capital of {country['capitals'][0]['name']}?"
        case 3:
            question = f"What country has this flag: {country['flag']['emoji']}?"
            

    print(f"Question {q+1} of 5: {question}")
    if (not hardmode):
        print(*list_answers(name),sep="\n")
    answer = input("\n")
    check_answer(answer, name)
    q += 1
else:
    print(f"You got {correct}/5 correct")