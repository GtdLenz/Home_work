def task_1(f:int,g: float, h:str, i: list, k: bool)->list:
    return f, g, h, i, k
f = 1
g = 1.1
h = 'Строка'
i = [1, 2, 3]
k = True
print(f, "относится к типу", type(f))
print(g, "относится к типу", type(g))
print(h, "относится к типу", type(h))
print(i, "относится к типу", type(i))
print(k, "относится к типу", type(k))

def task_2(a: list) -> list:
    return a[0:3]
print(task_2(a = [1,2,3,5,8,13,21]))


def task_3(b: int) -> int:
    return b*b
print(task_3(b=3))