class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.quest} True or False: ")
        return answer

    def correct_answer(self, answer_param):
        if self.question_list[self.question_number - 1].ans.lower() == answer_param.lower():
            self.score += 1
            print(f"That\'s right!")
        else:
            print("That\'s wrong!")
        print(f"Your score is {self.score}/{self.question_number}.")
        print(f"The correct answer is {self.question_list[self.question_number - 1].ans}.\n")
