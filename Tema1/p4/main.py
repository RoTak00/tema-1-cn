def polinom(x, *lista_coeficienti):
    rez = 0
    for ind, elem in enumerate(reversed(lista_coeficienti)):
        rez += elem
        if ind < len(lista_coeficienti) - 1:
            rez *= x

    return rez

# primul parametru este valoarea lui x in care dorim sa fie evaluata functia
# pentru urmatorii parametri = 1, 2, 3, 4
# se va calcula 4x^3 + 3x^2 + 2x + 1
if __name__ == '__main__':
    print(polinom(3, 1, 2, 3, 4))
