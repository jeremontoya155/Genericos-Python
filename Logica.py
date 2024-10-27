def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


def sumatoria(n):
    if n <= 1:
        return 1
    return n + sumatoria(n-1)


def multiplicatoria(n):
    if n <= 1:
        return 1
    return n * multiplicatoria(n-1)


def cargarNumero():
    print("Ingresa un fibonacci para un numero:")
    variable_1 = int(input("Numero:"))
    print(f"Ingresaste el numero {variable_1}")
    R_fibonacci = fibonacci(variable_1)
    R_sumatoria = sumatoria(variable_1)
    R_multiplicatoria = multiplicatoria(variable_1)
    print(f"El fibonacci de F({variable_1})={R_fibonacci}")
    print(f"La sumatoria de F({variable_1})={R_sumatoria}")
    print(f"La multiplicatoria de F({variable_1})={R_multiplicatoria}")


cargarNumero()
