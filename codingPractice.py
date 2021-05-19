
# find runner-up from the given list
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=list(set(arr))
    ele=max(lst)
    while max(lst)==ele:
        lst.remove(ele)
    
    print(max(lst))

    
 # Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order 
#their names alphabetically and print each one on a new line  
    
    if __name__ == '__main__':
    lst=list()
    sc=list()
    final_lst=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        sc.append(score)

second_last_score= sorted(set(sc))[1]
for key,value in lst:
    if value==second_last_score:
        final_lst.append(key)
        final_lst.sort()

for ele in final_lst:
    print(ele)        
    
 
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] 
#   for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal
#   2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh  
    
    if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key,value in student_marks.items():
        if key==query_name:
            print(format(sum(value)/len(scores),'.2f'))
                
    
    
    
    
    
    
