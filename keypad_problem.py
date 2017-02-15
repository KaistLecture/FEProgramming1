from math import sqrt

#k = {1:(0,0), 2:(0,1), 3:(0,2) .....}
def calcDist(number, initialDist=0):
    k = {}
    c = 0
    for i in range(3):
        for j in range(3):
            c += 1
            k[c] = (i,j)
    k[0] = (3,1)
    
    n = number.replace("-", "")
    
    dist = initialDist
    for i in range(len(n)-1):
        p0 = k[int(n[i])]
        p1 = k[int(n[i+1])]
        dist += sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)
    
    #print("Distance = %.3f" % dist)
    return {"number":n, "distance":dist}


if __name__=="__main__":    
    num = "123456789"
    a = calcDist(num)
    b = calcDist(num)
    
    #print("{} and {}".format(n1,n2))
    #print("{} and {}".format(a,b))
    print(a["number"],a["distance"])
    print(b["number"],b["distance"])











'''
# 두 좌표 사이 거리 구하는 함수
def dist(x1,x2):
    if len(x1) != len(x2):
        return None
    
    ss = 0.0
    for i in range(len(x1)):
        diff = x1[i] - x2[i]
        ss += diff*diff

    dist = sqrt(ss)
    return dist

def keypad(num):
    l = list(num)
    # '-'를 제거하고 숫자만 남기기
    l[:] = [x for x in l if x != '-']

    # 전화번호 숫자에 좌표 할당
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = [1,0]   
        elif l[i] == '1':
            l[i] = [0,3]
        elif l[i] == '2':
            l[i] = [1,3]
        elif l[i] == '3':
            l[i] = [2,3]
        elif l[i] == '4':
            l[i] = [0,2]
        elif l[i] == '5':
            l[i] = [1,2]
        elif l[i] == '6':
            l[i] = [2,2]
        elif l[i] == '7':
            l[i] = [0,1]
        elif l[i] == '8':
            l[i] = [1,1]
        elif l[i] == '9':
            l[i] = [2,1]

    # 총 이동거리 계산
    dist_sum = 0.0
    for i in range(len(l)-1):
        dist_sum += dist(l[i+1],l[i])

    return dist_sum
'''