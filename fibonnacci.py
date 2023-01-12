
def run():
    n = int(input("Quantos termos deseja?"))
    previous, current = 0, 1
    result = [previous, current]

    for _ in range(0, n):
        next = previous + current
        result.append(next)
        previous = current
        current = next

    print(result)

