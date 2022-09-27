# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def log_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (log_statement(0, 0, 0) and log_statement(0, 0, 1) and log_statement(0, 1, 0) and 
    log_statement(0, 1, 1) and log_statement(1, 0, 0) and log_statement(1, 0, 1) and
    log_statement(1, 1, 0) and log_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")