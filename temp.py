class Question():

    questions = []

    def __init__(self, question, vars, right_var):
        self.question = question
        self.vars = vars
        self.right_var = right_var

    @classmethod
    def read_file(cls):
        with open('test_questions.txt', 'r') as f:
            [cls.questions.append(question[:-2]) for question in f.readlines()]
        print(cls.questions)
        for index, i in enumerate(cls.questions, 0):
            ''.join(i)
            i = i.split(';')
            i = [item.strip() for item in i]
            cls.questions[index] = i
        for i in cls.questions:
            for j in i:
                if j.startswith('+'):
                    print(j[1:])
                else:
                    print(j)


        #     print(i)
        #
        #     i.pop()
        #     print(i)
        # print(cls.questions)


        # print(cls.questions)
    #     for i in questions:
    #         yield i

Question.read_file()
# quest = Question()

# def start():
#         question = test_question()
#         print(question)
#         answer_handler(message)
#
#
#     return
#
#
# def test_question():
#     with open('test_questions.txt', 'r') as f:
#         [questions.append(question) for question in f.readlines()]
#     print(questions)
#     for i in questions:
#         yield i