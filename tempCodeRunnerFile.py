def mod_inverse(multiple):
    """Finds the inverse of the encryption multiple under mod 26"""

    for x in range(1, 26):
        if (multiple*x) % 26 == 1:
            return x
    return None