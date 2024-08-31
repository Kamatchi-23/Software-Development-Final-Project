import random

class Subject:
    def __init__(self, current_sub) -> None: 
        self.subs = current_sub           
        self.sub = dict.fromkeys(["id", "marks", "grade"])
        
    def assign_sub(self):
        ids = [sub["id"] for sub in self.subs if self.subs]
        new_id = str(random.randint(1, 999)).zfill(3)
        while new_id in ids:
            new_id = str(random.randint(1, 999)).zfill(3)
        self.sub["id"] = new_id
        self.sub["marks"] = random.randint(25, 100)
        self.sub["grade"] = self.calculate_grade(self.sub["marks"])
        return self.sub

    def calculate_avg_mark(self):
        average_mark = 0.0
        if self.subs:
            total_marks = sum([subject['marks'] for subject in self.subs])
            average_mark = total_marks / len(self.subs)
        return average_mark
    
    def calculate_grade(self, mark):
        mark = float(mark)
        if mark < 50:
            return 'Z'
        elif mark < 65:
            return 'P'
        elif mark < 75:
            return 'C'
        elif mark < 85:
            return 'D'
        else:
            return 'HD'
