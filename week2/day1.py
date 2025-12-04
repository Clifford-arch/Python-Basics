"""The Bug Hunt"""
def calculate_statistics(numbers):
    total = 0
    for num in numbers:
        total += num

    if(len(numbers)==0):
        return "Null"
    
    average = total / len(numbers)
    
    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
    
    return {
        'total': total,
        'average': average,
        'maximum': max_num
    }

# Test the function
# data = [10, 20, 30, 40, 50]
data=[]
result = calculate_statistics(data)
print("Results:", result)


"""Debug 2"""
def calculate_grades(student_scores):
    grades = {}
    
    for student in student_scores:
        name = student['name']
        scores = student['scores']
        
        total = 0
        for score in scores:
            total += score
        
        average = total / len(scores)
        
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        
        grades[name] = grade
    
    return grade

# Test data
students = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [70, 65, 72]},
    {'name': 'Charlie', 'scores': [95, 92, 98]}
]

result = calculate_grades(students)
print("Final grades:", result)

""" Smart Calulator"""


