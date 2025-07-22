def task_1() -> str:
    a: int = 2
    b: float = 3.5
    c: str = 'строка'
    d: list = [1, 3, 5]
    e: bool = False
    sup_list = [a, b, c, d, e]
    res_str = ''
    for elem in sup_list:
        res_str += (str)(type(elem))
    return res_str

print(task_1())


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print(task_2())


def task_3(a:float) -> float:
    return a**2

print(task_3(3.5))