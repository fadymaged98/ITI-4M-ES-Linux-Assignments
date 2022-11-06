import os
import time
import sys

# done = 'false'
# #here is the animation
# def animate():
#     while done == 'false':
#         sys.stdout.write('\rloading |')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading /')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading -')
#         time.sleep(0.1)
#         sys.stdout.write('\rloading \\')
#         time.sleep(0.1)
#     sys.stdout.write('\rDone!     ')
#
# animate()
# #long process here
# done = 'false'
#
# import sys
# import time
#
# for i in range(3):
#     sys.stdout.write('\t' + ','.join([str(a) for a in range(i+1, 0, -1)]))
#     sys.stdout.flush()
#     time.sleep(1)
#
# sys.stdout.write('\n')


# for i in range(0, 101, 10):
#     print(f'>> You have finished {i}%', flush=False)
#     time.sleep(1)


print("\n")
time.sleep(5)
spaces_1 = 40
astrics_1 = 1
while True:
    if astrics_1 > 10:
        break
    for i in range(0, spaces_1):
        print(" ", end="")
    for j in range(0, astrics_1):
        print("*", end="")
    print("")
    astrics_1 += 1

time.sleep(1)

print("\033[11A")
# print("\033[37C")


spaces_2 = 38
astrics_2 = 1
while True:
    if astrics_2 > 10:
        break
    for i in range(0, spaces_2):
        print(" ", end="")
    for j in range(0, astrics_2):
        print("*", end="")
    print("")
    spaces_2 -= 1
    astrics_2 += 1

time.sleep(1)

spaces_3 = 28
astrics_3 = 1
while True:
    if astrics_3 > 10:
        break
    for i in range(0, spaces_3):
        print(" ", end="")
    for j in range(0, astrics_3):
        print("*", end="")
    print("")
    spaces_3 -= 1
    astrics_3 += 1

time.sleep(1)

spaces_4 = 19
astrics_4 = 10
while True:
    if astrics_4 < 1:
        break
    for i in range(0, spaces_4):
        print(" ", end="")
    for j in range(0, astrics_4):
        print("*", end="")
    print("")
    spaces_4 += 1
    astrics_4 -= 1

time.sleep(1)

spaces_5 = 29
astrics_5 = 10
while True:
    if astrics_5 < 1:
        break
    for i in range(0, spaces_5):
        print(" ", end="")
    for j in range(0, astrics_5):
        print("*", end="")
    print("")
    spaces_5 += 1
    astrics_5 -= 1

time.sleep(1)

print(f"\033[10A", end="")

astrics_6 = 10
while True:
    if astrics_6 < 1:
        break

    print("\033[40C", end="")

    for j in range(0, astrics_6):
        print("*", end="")
    print("")
    astrics_6 -= 1

time.sleep(1)

print(f"\033[20A", end="")

astrics_7 = 10
while True:
    if astrics_7 < 1:
        break

    print("\033[50C", end="")

    for j in range(0, astrics_7):
        print("*", end="")
    print("")
    astrics_7 -= 1

time.sleep(1)

print(f"\033[20A", end="")

astrics_8 = 1
while True:
    if astrics_8 > 10:
        break

    print("\033[50C", end="")

    for j in range(0, astrics_8):
        print("*", end="")
    print("")
    astrics_8 += 1

print("\033[20B")
print("-" * 35, "Donee!!!", "-" * 30)
