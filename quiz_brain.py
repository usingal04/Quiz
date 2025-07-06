class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_number = 0
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        question = self.question_list[self.question_number]
        q_text = question.text
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number} {q_text} (True/False) ')
        self.check_ans(user_ans, question.ans)
        
    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print('You got it right.')
        else:
            print('You are wrong.')
        print(f'The correct ans was {correct_ans}.')
        print(f'Your current score is {self.score}\{self.question_number}')
        print('\n')