num = int(input("Input a number: "))
start_ = 0
next_ = 1

for i in range(num):
    start_, next_ = next_, start_ + next_

print(start_)