#1
# row = int(input("enter a num- "))
# for i in range(1,row+1):
#     for j in range(row-i):
#         print("",end = ' ')
#     for j in range(i):
#         print("*", end = " ")
#     print()
#5
# num = int(input(" ? "))
# a = 0
# b = 1
# c = 1
# for i in range(num):
#     print(a,end= " ")
#     c = a + b
#     a = b
#     b = c
#6
# num = 1
# while num % 3 != 2 or num % 5 !=3 or num % 7 !=2:
#     num += 1
# print(num)
#7
# ans = ['1','2','3','4']
# guess = []
# A = 0
# B = 0
# num = input("enter not duplicate 4 numbers- ")
# for i in num:
#     guess.append(i)
# for j in range(4):
#     if guess[j] == ans[j]:
#         A += 1
# for h in ans:
#     for g in guess:
#         if h == g:
#             B += 1
# B = B - A
# print(guess)
# print(f"{A} A {B} B")
#
# num = 1
# while num % 2 != 0:
#     num += 1
# print(num)

listw = ["30ww","200rr","100ss"]
b = ""
c = []
d = {}
for i in range(len(listw)):
    b =""
    for j in listw[i]:
        if j.isdigit() :
            b += j
    c.append(int(b))
    d[listw[i]]= int(b)
c.sort()
for i in c:
    for key,value in d.items():
        if i == value:
            print(key,value)



# {"30ww":30 , "200rr":200 ,"100ss":100}
