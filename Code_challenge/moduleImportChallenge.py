#!/usr/bin/env python3
"""HTML SLICING LAB"""


import html

def main():
    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
    q = trivia["question"]
    correct = trivia["correct_answer"]
    incorrect1 =trivia["incorrect_answers"][0]
    incorrect2 =trivia["incorrect_answers"][1]
    incorrect3 =trivia["incorrect_answers"][2]
    print(q)
    print(f" A.) {html.unescape((correct))}")
    print(f" B.) {html.unescape((incorrect1))}")
    print(f" C.) {html.unescape((incorrect2))}")
    print(f" D.) {html.unescape((incorrect3))}")

main()
