
'''studentPerformance = [85, 75, 65, 60, 56, 48, 90]
if studentPerformance >= 80:
    print('distinction')
elif studentPerformance >= 60:
    print('credit')
elif studentPerformance >= 40:
    print('fair')
elif studentPerformance < 40:
    print('fail')
else: 
    print('pass') '''
    



'''studentPerformance = [85, 75, 67,56, 90, 45]
def studentPerformance (score) :
    match score :
        case 80 : return 'distinction'
        case "between 60 and 70" : return 'credit'
        case "between 40 and 50" : return "fair"
        case "below 40": return "fail" 
print(studentPerformance(80))
print(studentPerformance("between 60 and 70"))
print(studentPerformance("between 40 and 50"))
print(studentPerformance("below 40"))        
        

#students_scores =[85, 67, 45, 90, 52]
# students performance based on the score 
def check_performance (score):
    if score >= 80:
        return "Distinction"
    elif 60 <= score <= 70: 
        return "Credit"
    elif 40 <= score <= 50:
        return "Fair"
    else:
        return "fail"

def main ():
    score = float(input("Enter student's score:"))
    performance = check_performance(score)
    print("Student performance:", performance) 
if _name_ == "_main_":
    main()  '''  
        
''' studentPerformance = [85, 75, 67,56, 90, 45, 29]
def studentPerformance (score) :
    match score :
        case "above 85" : return 'distinction'
        case "between 60 and 70" : return 'credit'
        case "between 40 and 50" : return "fair"
        case "below 40": return "fail" 
print(input(studentPerformance("score")))
print(studentPerformance("between 60 and 70"))
print(studentPerformance("between 40 and 50"))
print(studentPerformance("below 40")) '''

student_Performance = 23
if student_Performance >= 80:
    print('distinction')
elif 60 <= student_Performance <= 70:
    print("Credit")
elif 40 <= student_Performance <= 50:
    print("fair")
elif student_Performance < 40:
    print("Fail olodo ni mi lolzz, Took me long hours to solve this simple logic.")
else:
    print("olodo ni mi lolzz, Took me long hours to solve this simple logic")
 