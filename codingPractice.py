
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
                
#    The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.
# Constraints


# Output Format

# Output the total number of distinct country stamps on a single line.

# Sample Input

# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 
# Sample Output

# 5 
    
    
        lst=list()
    n = int(input())
    for _ in range(n):
        country=input()
        lst.append(country)
    print(lst)
    newLst=set(lst)
    print(newLst)
    cnt=0
    for i in newLst:
        cnt=cnt+1
    
    print(cnt) 
    
    
#     Output Format

# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1
    # Enter your code here. Read input from STDIN. Print output to STDOUT

lst=list()
dic=dict()
nl=list()
n = int(input())
for _ in range(n):
    words=input()
    lst.append(words)
    
print(len(set(lst)))
    
for ele in lst:
        if ele in dic:
            dic[ele]+=1
        else:
            dic[ele]=1
            
#for k,v in dic.items():
#nl=dic.values()
print(*dic.values())       
    

    
    
    
    
    
    
