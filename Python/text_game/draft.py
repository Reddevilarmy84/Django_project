# 
#
y = 2
for x in range(0, 11): print(f"{x} в степени {y} равно {(lambda x, y: x**y)(x, y)}")

x = 5
y = 5
a = lambda x, y: x*y
print (f"Печатаем результат лямбда функции {a(x, y)} ")