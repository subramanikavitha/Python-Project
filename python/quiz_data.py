#before import requests install $ pip install requests
import requests
parameters = {
    "amount": 3, # If you want you can increase the question number for testing purposes I added only 3 questions

    "type": "multiple"
}
#questions option and results get from Open Trivia DB API(i can select computer category difficulty level easy ,
# and multiple choice of quisition)
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple", params=parameters)
print(response)
question_data = response.json()["results"]
response.raise_for_status()
'''  {
    "response_code": 0,
    "results": [
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Which company was established on April 1st, 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne?",
            "correct_answer": "Apple",
            "incorrect_answers": [
                "Microsoft",
                "Atari",
                "Commodore"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "In any programming language, what is the most common way to iterate through an array?",
            "correct_answer": "&#039;For&#039; loops",
            "incorrect_answers": [
                "&#039;If&#039; Statements",
                "&#039;Do-while&#039; loops",
                "&#039;While&#039; loops"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What does CPU stand for?",
            "correct_answer": "Central Processing Unit",
            "incorrect_answers": [
                "Central Process Unit",
                "Computer Personal Unit",
                "Central Processor Unit"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "The programming language &#039;Swift&#039; was created to replace what other programming language?",
            "correct_answer": "Objective-C",
            "incorrect_answers": [
                "C#",
                "Ruby",
                "C++"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Which computer hardware device provides an interface for all other connected devices to communicate?",
            "correct_answer": "Motherboard",
            "incorrect_answers": [
                "Central Processing Unit",
                "Hard Disk Drive",
                "Random Access Memory"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "This mobile OS held the largest market share in 2012.",
            "correct_answer": "iOS",
            "incorrect_answers": [
                "Android",
                "BlackBerry",
                "Symbian"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "The C programming language was created by this American computer scientist. ",
            "correct_answer": "Dennis Ritchie",
            "incorrect_answers": [
                "Tim Berners Lee",
                "al-Khwārizmī",
                "Willis Ware"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Which programming language shares its name with an island in Indonesia?",
            "correct_answer": "Java",
            "incorrect_answers": [
                "Python",
                "C",
                "Jakarta"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "How long is an IPv6 address?",
            "correct_answer": "128 bits",
            "incorrect_answers": [
                "32 bits",
                "64 bits",
                "128 bytes"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What language does Node.js use?",
            "correct_answer": "JavaScript",
            "incorrect_answers": [
                "Java",
                "Java Source",
                "Joomla Source Code"
            ]
        }
    ]
}'''