from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is over!")
print(f"Your final score is: {quiz.score} out of {len(question_bank)}")
