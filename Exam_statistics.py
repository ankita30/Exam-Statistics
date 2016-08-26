grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    return sum(grades)
    
def grades_average(grades):
    return grades_sum(grades)/ float(len(grades))
    
def grades_variance(grades):
    average = grades_average(grades)
    variance = 0 
    for score in grades:
        variance += (average - score)**2
    return variance/len(grades)

def grades_std_deviation(variance):
    return variance**0.5

variance =  grades_variance(grades)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
