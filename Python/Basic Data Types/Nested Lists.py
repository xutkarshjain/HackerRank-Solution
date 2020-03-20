if __name__ == '__main__':
    data=[]
    scoreSet=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        scoreSet.add(score)
    scoreList=list(scoreSet)
    scoreList.sort()
    min2=scoreList[1]
    ans=[]
    for i in data:
        if i[1]==min2:
            ans.append(i[0])

    for i in sorted(ans):
        print(i)


