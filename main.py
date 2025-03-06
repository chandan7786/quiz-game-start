from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    ques_text = question["text"]
    ques_ans = question["answer"]
    new_ques = Question(ques_text,ques_ans)
    """we called the object upon here """
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_ques():
    quiz.next_question()
    print('your quiz has ended!')
    print(f'you final score is {quiz.score}/{quiz.question_num}')