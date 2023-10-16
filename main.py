from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
data_board = []
for item in  question_data:
    text = item["text"]
    answer = item["answer"]
    data_board.append( Question(text,answer))

brain = QuizBrain(data_board)

while(brain.still_has_question() ):

    brain.next_question()

print("You completed the quiz")
print(f"Your final score was {brain.score}/ {brain.question_number}")