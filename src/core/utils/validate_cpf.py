def validate_cpf(cpf: str) -> bool:
    cpf = cpf.replace("-", "").replace(".", "")
    if len(cpf) != 11:
        return False
    if all(digit == cpf[0] for digit in cpf):
        return False

    sum1 = 0
    for i in range(9):
        sum1 += (10 - i) * int(cpf[i])
    first_digit = 11 - (sum1 % 11) if sum1 % 11 != 0 else 0

    sum2 = 0
    for i in range(10):
        sum2 += (11 - i) * int(cpf[i])
    second_digit = 11 - (sum2 % 11) if sum2 % 11 != 0 else 0

    return first_digit == int(cpf[9]) and second_digit == int(cpf[10])
