class QuizBrain:

    def __init__(self,  question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number < len(self.question_list) :
            return True
        else:
            return False
    def next_question (self):

        nah =(self.question_list[self.question_number])
        self.question_number += 1
        ans = input(f"Q.{self.question_number} {nah.text} (True/False)")
        self.check_answer(ans,nah.answer)


    def check_answer(self,user_answer,correct_anwer):
        if (user_answer.lower() == correct_anwer.lower() ):
            print("correct")
            self.score += 1
        else:
            print("Inccorect")
        print(f"correct answer was {correct_anwer}")
        print(f"you current score is {self.score}/{self.question_number}")
        print("\n")