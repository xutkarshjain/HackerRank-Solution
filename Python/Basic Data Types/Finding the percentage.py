
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    info=list(map(float,student_marks[input()]))
    sum=0
    for i in info:
        sum+=i
    print('%.2f' %(sum/3))
