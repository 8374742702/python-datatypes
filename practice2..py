# created by arun
# 22-12-2023
# Topic: Comparision Oparator

A = 10
B = 20
C = 20
result = (A == B), (B == C), (C == A)
print("the value;", result)
X = 10
Y = 20
Z = 20
result = (X != Y), (Y != Z), (Z != X)
print("the value;", result)
A = 115
B = 205
C = 99
result = (A < B), (B < C), (C < A)
print("the value;", result)
X = 115
Y = 205
Z = 99
result = (X > Y), (Y > Z), (Z > X)
print("the value;", result)
A = 78
B = 67
C = 90
result = (A <= B), (B <= C), (C <= A)
print("the value;", result)
X = 78
Y = 67
Z = 90
result = (X >= Y), (Y >= Z), (Z >= X)
print("the value;", result)

# LOGICAL OPARATORS
# AND GATE

A = 6
B = 7
result = (A < 7 and B < 10)
print("the value;", result)
C = 8
D = 9
result = (C < 7 and D > 10)
print("the value;", result)
A = 6
B = 7
result = (A > 7 and B < 10)
print("the value;", result)
x = 8
y = 9
result = (x < 7 and y > 5)
print("the value;", result)

# OR GATE

A = 6
B = 7
result = (A < 7 or B < 4)
print("the value;", result)
X = 8
Y = 9
result = (X < 10 or Y > 8)
print("the value;", result)
A = 6
B = 7
result = (A > 4 or B < 9)
print("the value;", result)
x = 8
y = 9
result = (x < 2 or y > 10)
print("the value;", result)

# NOT GATE

A = 6
B = 7
result = (not(A < 9 and B > 10))
print("the value;", result)
A = 6
B = 7
result = (not(A < 9 and B > 5))
print("the value;", result)

# # membership oparators

arun = "hii friend"
print("the character h is in arun;", 'h' in arun)
arun = "hello friend"
print("the character h is in arun;", 'b' in arun)
number = "arun (1, 2, 3, 4)"
print("the number 2 is in number;", '2' not in number)

# Condition Statement
# if condition

print("result")
marks = 40
if marks >= 35:
    print("exam pass")

    # if and else condition

    print("result")
    marks = 30
    if marks >= 35:
        print("exam pass")
    else:
        print("fail")

        # if  and elif condition
        print("result")
        marks = 30
        if marks >= 35:
            print("exam pass")
        elif marks < 40 and 50:
            print("average")

            # if and  elif and else  condition
            
            print("result")
            marks = 30
            if marks >= 35:
                print("exam pass")
            elif marks < 40 and 50:
                print("average")
            else:
                print("fail")