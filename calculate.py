import csv 

class Calculator:

    def __init__(self, worst_grade: float, best_grade: float, grades = {}, csv_file=""):
        self._grades = grades
        self._best_grade = best_grade
        self._worst_grade = worst_grade
        if csv_file:
            self.read_csv(csv_file)
        self._mod_grades = {}

    def _weight_grades(self, grades: dict):
        weighted_grades = {}
        total_cp = total_weighted = 0
        for key, value in grades.items():
            if value[1] != 0 and value[0] != 0:
                weighted_grades[key] = value[0]*value[1]
                total_cp += value[1]
                total_weighted += weighted_grades[key]
        weighted_grades['CP'] = total_cp
        weighted_grades['Total'] = total_weighted
        return weighted_grades

    def _calculate_average(self, grades: dict):
        weighted_grades = self._weight_grades(grades)
        grade = weighted_grades['Total']/weighted_grades['CP']
        return grade, weighted_grades

    def _calculate_mod(self, grades_not_yet_written: float):
        for key, grade in self._grades.items():
            if grade[0] == 0:
                self._mod_grades[key] = (grades_not_yet_written, grade[1])
            else:
                self._mod_grades[key] = grade
        return self._calculate_average(self._mod_grades)

    def current_grade(self):
        grade, collection = self._calculate_average(self._grades)
        print("Currently you got "+str(collection["CP"])+" Credit Points")
        print("Your current grade is "+str(grade))

    def best_grade_possible(self):
        grade, collection = self._calculate_mod(self._best_grade)
        print("The best grade you can still achieve: "+str(grade))

    def worst_grade_possible(self):
        grade, collection = self._calculate_mod(self._worst_grade)
        print("The worst grade you can still achieve: "+str(grade))

    def average_grade_possible(self):
        average_grade = (self._best_grade+self._worst_grade)/2
        grade, collection = self._calculate_mod(average_grade)
        print("The average grade you can still achieve: "+str(grade))

    def all_output(self):
        self.current_grade()
        self.best_grade_possible()
        self.worst_grade_possible()
        self.average_grade_possible()

    def read_csv(self, file: str):
        with open(file, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[0] in self._grades:
                    pass
                else:
                    self._grades[row[0]] = (float(row[1]),float(row[2]))

if __name__ == "__main__":
    grades = {
        'Math1': (2.0, 9),
        'Math2': (3.0, 9),
        'Math3': (1.0, 9),
        'Programming': (2.0, 12),
        # ... 
    }

    calc = Calculator(grades=grades,best_grade=1.0,worst_grade=4.0)
    calc.all_output()
