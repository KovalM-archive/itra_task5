import random
import sys

def checkCorrectnessInput():
    flag = True
    if len(sys.argv) != 4:
        flag = False
    elif not sys.argv[1] in {'us', 'ru', 'by', 'US', 'RU', 'BY'}:
        flag = False
    elif not (sys.argv[2].isnumeric() and sys.argv[3].isnumeric()):
        flag = False
    elif int(sys.argv[2]) > 1000000:
        flag = False
    return flag

def getLines(path):
    currentFile = open(path,'r')
    lineList = currentFile.readlines()
    currentFile.close()
    return lineList

def createErrors(answer, numberErrorCopy):
    numberRecords = len(answer)
    numberError = numberErrorCopy
    if numberError>numberRecords:
        kolLineError = numberError//numberRecords
    else:
        kolLineError = 1
    i=0
    while i<numberRecords:
        if numberError < kolLineError: kolLineError=numberError
        numberError -= kolLineError
        kolLineErrorCopy = kolLineError
        m=int(len(answer[i]))
        s=str(answer[i])
        flag=[False]*m
        kol=m
        while True:
            j=random.randint(0,m-1)
            if kolLineErrorCopy==0 or kol<=0:break
            if flag[j]:continue
            if s[j] in {' ', ',', '.','\n'}:
                flag[j]=True
                j+=1
                kol-=1
                continue
            k=random.randint(0,1)
            if j+1==m or s[j+1] in {' ', ',', '.', '\n'}:k=0
            if k==0 :
                s=s[:j]+chr(ord(s[j])+1)+s[j+1:]
                flag[j]=True
            elif k==1:
                w=s[j]
                r=s[j+1]
                s=s[:j]+r+w+s[j+2:]
                flag[j]=True
                flag[j+1]=True
                kol-=1
            kolLineErrorCopy-=1
            kol-=1
        answer[i]=s
        i+=1
        if numberError<=0:break
    return answer

def delLastEl(s):
    ans = str(s)
    return ans[:len(ans)-1]

def genUsList():
    random.seed()
    fileAnswer = open('/home/michail/itransition/python/task5_generic_data/data/ru/answer_ru.txt', 'w')
    number = int(sys.argv[2])
    answer=[]
    firstName = getLines('/home/michail/itransition/python/task5_generic_data/data/us/first_name_us.txt')
    secondName = getLines('/home/michail/itransition/python/task5_generic_data/data/us/second_name_us.txt')
    cityList = getLines('/home/michail/itransition/python/task5_generic_data/data/us/indexandcity_us.txt')
    streetList = getLines('/home/michail/itransition/python/task5_generic_data/data/us/street_us.txt')
    i = 0
    while i<number:
        k1 = random.randint(0, len(firstName)-1)
        k2 = random.randint(0, len(secondName)-1)
        k4 = random.randint(0,len(cityList)-1)
        k5 = random.randint(0,len(streetList)-1)
        s=delLastEl(cityList[k4])
        s1=s[:s.find(' ')]
        s2=s[s.find(' ')+1:]
        currentLine = delLastEl(firstName[k2])+' '\
                      +delLastEl(secondName[k1])+', '\
                      +s2+', '\
                      +s1+', '\
                      +delLastEl(streetList[k5])+', '\
                      +str(random.randint(1, 30))+'\n'
        answer.append(currentLine)
        i+=1
    answer=createErrors(answer, int(sys.argv[3]))
    m=len(answer)
    while m>0:
        k=random.randint(0,m-1)
        #fileAnswer.write(answer[k])
        print(answer[k])
        answer[k]=answer[m-1]
        m-=1
    fileAnswer.close()

def genRuList():
    random.seed()
    fileAnswer = open('/home/michail/itransition/python/task5_generic_data/data/ru/answer_ru.txt', 'w')
    number = int(sys.argv[2])
    answer=[]
    firstName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/men/first_name_ru_m.txt')
    secondName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/men/second_name_ru_m.txt')
    thirdName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/men/third_name_ru_m.txt')
    cityList = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/indexandcity_ru.txt')
    streetList = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/street_ru.txt')
    i = 0
    while i<number//2:
        k1 = random.randint(0,len(firstName)-1)
        k2 = random.randint(0,len(secondName)-1)
        k3 = random.randint(0,len(thirdName)-1)
        k4 = random.randint(0,len(cityList)-1)
        k5 = random.randint(0,len(streetList)-1)
        s=delLastEl(cityList[k4])
        s1=s[:s.find(' ')]
        s2=s[s.find(' ')+1:]
        currentLine = delLastEl(thirdName[k3])+' '\
                      +delLastEl(firstName[k1])+' '\
                      +delLastEl(secondName[k2])+', '\
                      +s1+', '\
                      +s2+', '\
                      +delLastEl(streetList[k5])+', '\
                      +str(random.randint(1,30))+'\n'
        answer.append(currentLine)
        i+=1
    firstName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/women/first_name_ru_w.txt')
    secondName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/women/second_name_ru_w.txt')
    thirdName = getLines('/home/michail/itransition/python/task5_generic_data/data/ru/women/third_name_ru_w.txt')
    i = number//2
    while i<number:
        k1 = random.randint(0,len(firstName)-1)
        k2 = random.randint(0,len(secondName)-1)
        k3 = random.randint(0,len(thirdName)-1)
        k4 = random.randint(0,len(cityList)-1)
        k5 = random.randint(0,len(streetList)-1)
        s=delLastEl(cityList[k4])
        s1=s[:s.find(' ')]
        s2=s[s.find(' ')+1:]
        currentLine = delLastEl(thirdName[k3])+' '\
                      +delLastEl(firstName[k1])+' '\
                      +delLastEl(secondName[k2])+', '\
                      +s1+', '\
                      +s2+', '\
                      +delLastEl(streetList[k5])+', '\
                      +str(random.randint(1,30))+'\n'
        answer.append(currentLine)
        i+=1
    answer=createErrors(answer, int(sys.argv[3]))
    m=len(answer)
    while m>0:
        k=random.randint(0,m-1)
        #fileAnswer.write(answer[k])
        print(answer[k])
        answer[k]=answer[m-1]
        m-=1
    fileAnswer.close()

def genByList():
    random.seed()
    fileAnswer = open('/home/michail/itransition/python/task5_generic_data/data/by/answer_by.txt', 'w')
    number = int(sys.argv[2])
    answer=[]
    firstName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/men/first_name_by_m.txt')
    secondName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/men/second_name_by_m.txt')
    thirdName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/men/third_name_by_m.txt')
    cityList = getLines('/home/michail/itransition/python/task5_generic_data/data/by/indexandcity_by.txt')
    streetList = getLines('/home/michail/itransition/python/task5_generic_data/data/by/street_by.txt')
    i = 0
    while i<number//2:
        k1 = random.randint(0,len(firstName)-1)
        k2 = random.randint(0,len(secondName)-1)
        k3 = random.randint(0,len(thirdName)-1)
        k4 = random.randint(0,len(cityList)-1)
        k5 = random.randint(0,len(streetList)-1)
        s=delLastEl(cityList[k4])
        s1=s[:s.find(' ')]
        s2=s[s.find(' ')+1:]
        currentLine = delLastEl(thirdName[k3])+' '\
                      +delLastEl(firstName[k1])+' '\
                      +delLastEl(secondName[k2])+', '\
                      +s2+', '\
                      +s1+', '\
                      +delLastEl(streetList[k5])+', '\
                      +str(random.randint(1,30))+'\n'
        answer.append(currentLine)
        i+=1
    firstName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/women/first_name_by_w.txt')
    secondName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/women/second_name_by_w.txt')
    thirdName = getLines('/home/michail/itransition/python/task5_generic_data/data/by/women/third_name_by_w.txt')
    i = number//2
    while i<number:
        k1 = random.randint(0,len(firstName)-1)
        k2 = random.randint(0,len(secondName)-1)
        k3 = random.randint(0,len(thirdName)-1)
        k4 = random.randint(0,len(cityList)-1)
        k5 = random.randint(0,len(streetList)-1)
        s=delLastEl(cityList[k4])
        s1=s[:s.find(' ')]
        s2=s[s.find(' ')+1:]
        currentLine = delLastEl(thirdName[k3])+' '\
                      +delLastEl(firstName[k1])+' '\
                      +delLastEl(secondName[k2])+', '\
                      +s2+', '\
                      +s1+', '\
                      +delLastEl(streetList[k5])+', '\
                      +str(random.randint(1,30))+'\n'
        answer.append(currentLine)
        i+=1
    answer=createErrors(answer, int(sys.argv[3]))
    m=len(answer)
    while m>0:
        k=random.randint(0,m-1)
        #fileAnswer.write(answer[k])
        print(answer[k])
        answer[k]=answer[m-1]
        m-=1
    fileAnswer.close()

if not checkCorrectnessInput():
    print('incorrect input')
    sys.exit()

if sys.argv[1] in {'us', 'US'}: genUsList()
if sys.argv[1] in {'ru', 'RU'}: genRuList()
if sys.argv[1] in {'by', 'BY'}: genByList()
