import bisect

def percent_to_grade(percent, *, suffix=False, round=False):
    grades = ('F', 'D', 'C', 'B', 'A')
    bpoint = [60, 70, 80, 90]
    
    if suffix:
        grades = ('F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+')
        bpoint = [60, 63, 67, 70, 73, 77, 80, 83, 87, 90, 93, 97]

    if round:
        # always rounding up
        percent = int(percent + 0.5)

    igrade = bisect.bisect(bpoint, percent)
    return grades[igrade]

def calculate_gpa(grades):
    map_grade_gpa = {'A+': 4.33, 'A': 4.00, 'A-': 3.67, 'B+': 3.33, 'B': 3.00, 'B-':2.67,
                    'C+': 2.33, 'C': 2.00, 'C-': 1.67, 'D+': 1.33, 'D': 1.00, 'D-': 0.67,
                     'F': 0.00}
    return sum([map_grade_gpa.get(g) for g in grades]) / len(grades)
