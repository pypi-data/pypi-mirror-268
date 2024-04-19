import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import random

class APT_dataset:

    def __init__(self, n_student:int = 100000, random_seed:int = 1):
        if (n_student < 1000 or n_student > 100000):
            raise Exception("n_student have to greater than 1000 and smaller than 100000!")
        if (random_seed == 1):
            raise Exception("You have to change random_seed as required in the assignment!")
        self.n_student = n_student
        self.random_seed = random_seed
        self.answers, self.solution = self.APT_data_generator()

    def APT_generator(self)->tuple[np.ndarray, list]:
        """
        Function to generate a simulation Advanced Placement Test solutions and answers of participants

        Returns:
        student_answers: 2D ndarray
        solution: 1D ndarray
        """
        np.random.seed(self.random_seed)
        p_top = 0.05
        p_bot = 0.95
        p = []
        temp_p = np.linspace(p_top, p_bot, 40)
        np.random.shuffle(temp_p)
        for i in range(40):
            p.append((i, temp_p[i]))
        temp_p = np.linspace(p_top, p_bot, 30)
        np.random.shuffle(temp_p)
        for i in range(30):
            p.append((i+40, temp_p[i]))
        temp_p = np.linspace(p_top, p_bot, 50)
        np.random.shuffle(temp_p)
        for i in range(50):
            p.append((i+70,temp_p[i]))
        p = sorted(p, key = lambda x : x[1], reverse=True)
        solutions = []
        answers = ['A', 'B', 'C', 'D']
        for i in range(120):
            solutions.append(answers[np.random.randint(0, 3)])
        student_answers = np.full((self.n_student, 120), 'E')
        student_performances = list(map(int,np.random.normal(65, 11.1, self.n_student)))
        
        points = []
        point_per_question = []
        for question in range(120):
            point_per_question.append(np.log(p[question][1]/(1-p[question][1])))

        for student in range(self.n_student):
            student_perf = student_performances[student]
            points.append(0)
            for i, item in enumerate(p):
                remain = 120 - i
                _p = np.random.rand()
                if (remain <= student_perf):
                    student_answers[student, item[0]] = solutions[item[0]]
                    points[-1]+=10 + point_per_question[item[0]]
                    student_perf -= 1
                elif (_p <= 0.9 and student_perf > 0):
                    student_answers[student, item[0]] = solutions[item[0]]
                    points[-1]+=10 + point_per_question[item[0]]
                    student_perf -= 1
                else:
                    student_answers[student, item[0]] = solutions[item[0]]
                    while (student_answers[student, item[0]] == solutions[item[0]]):
                        student_answers[student, item[0]] = answers[np.random.randint(0, 3)]
            points[-1] = np.round(points[-1], 2)

        return student_answers, solutions

    def name_generator(self)->list:
        """
        Function to generate a list of Vietnamese name

        Returns:
        list of Vietnamese name
        """
        np.random.seed(self.random_seed)
        random.seed(self.random_seed)
        data = ""
        response = requests.get("https://raw.githubusercontent.com/nprm1243/MaSSP-DS-2023/main/ProjectData/names.txt")
        data = response.text
        data = data.split('\r\n')
        random.shuffle(data)
        return data[:self.n_student]

    def APT_data_generator(self)->tuple[pd.DataFrame, list]:
        """
        Function to generate a simulation APT DataFrame contain students's answer and list of solution

        Returns:
        DataFrame
        list of solution
        """
        np.random.seed(self.random_seed)
        CAE_data, sols = self.APT_generator()
        names = self.name_generator()
        df = pd.DataFrame(CAE_data)
        df.columns += 1
        df.insert(0, "Name", names)
        return df, sols

if __name__ == '__main__':
    APT_dataset = APT_dataset(n_student=5000, random_seed=20022002)
    table = APT_dataset.answers
    solution = APT_dataset.solution
    print(table.head(5))
    print(solution)