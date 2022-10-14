def somme(a: int = 0, b: int = 0) -> int :
    """Cette fonction calcule la somme entre deux nombres

    Args:
        a (int): Saisir le premier nombe. Defaults to 0.
        b (int): saisir le deuxième nombre. Defaults to 0.

    Returns:
        int: le resulat de l'addition des deux nombres
    """
    return a + b

s = somme(3, 9)
print(s)