from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question['text']
    q_ans = question['answer']
    question = Question(text=q_text, ans=q_ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You have completed the quiz')
print(f'Your final score was {quiz.score}/{quiz.question_number}')