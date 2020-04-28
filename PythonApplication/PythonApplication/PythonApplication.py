import time

print("---RUNOOB EXAMPLE ： Loading 效果---")
print("Hello World")

print("Loading",end = "")
for i in range(20):
    print(".",end = '',flush = True)
    time.sleep(0.5)