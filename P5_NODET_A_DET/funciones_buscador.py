estado = []
letra = []


def e1(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e2(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 91, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e3(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e4(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 5, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e5(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 18, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e6(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 39, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e7(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e8(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 9 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e9(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 36, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e10(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 11, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e11(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 21, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e12(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 13, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e13(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 38, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e14(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  15}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e15(letra):
    transiciones = {"a": 16, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e16(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 24, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e17(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 26, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e18(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 25, "m": 1, "n": 1, "o": 11, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e19(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e20(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e21(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 29, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e22(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e23(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 31, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e24(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 32, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e25(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 42, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e26(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 43, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e27(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 25, "m": 1, "n": 1, "o": 26, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e28(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 44, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e29(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e30(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 45, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 47, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e31(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 46, "k": 1, "l": 48, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e32(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 49, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e33(letra):
    transiciones = {"a": 53, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 54, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e34(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 55, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e35(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 49, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e36(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 57, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e37(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 57, "e": 35, "f": 17, "g": 58, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 59, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e38(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 60, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e39(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 61, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e40(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 62, "i": 63, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 64, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e41(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 66, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e42(letra):
    transiciones = {"a": 67, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 5, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e43(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e44(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e45(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 68, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e46(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 69, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e47(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 62, "i": 70, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 64, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e48(letra):
    transiciones = {"a": 71, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e49(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 55, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e50(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 72, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e51(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 73, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e52(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 74, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e53(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 75, "t": 7, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e54(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 76, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e55(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 77, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e56(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 78, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e57(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 79, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e58(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 80, "k": 1, "l": 3, "m": 1, "n": 1, "o": 11, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e59(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 81, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e60(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 82, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e61(letra):
    transiciones = {"a": 83, "b": 6, "c": 33, "d": 57, "e": 35, "f": 17, "g": 58, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 59, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e62(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 84, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e63(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 85, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 86, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e64(letra):
    transiciones = {"a": 87, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 88, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e65(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 13, "i": 89, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e66(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 90, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e67(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 91, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e68(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 92, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e69(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 55, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e70(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 93, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e71(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 94, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e72(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 95, "f": 17, "g": 10, "h": 62, "i": 63, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 64, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e73(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 96, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e74(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 97, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e75(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 98, "f": 17, "g": 10, "h": 62, "i": 63, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 64, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e76(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 99, "t": 100, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e77(letra):
    transiciones = {"a": 101, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 25, "m": 1, "n": 1, "o": 26, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e78(letra):
    transiciones = {"a": 2, "b": 102, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e79(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 103, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e80(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 142, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e81(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 104, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e82(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e83(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 105, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e84(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 106, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e85(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 107, "o": 11, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e86(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 108, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e87(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 109, "u": 41, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e88(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 110, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e89(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 111, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e90(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e91(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e92(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e93(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 112, "o": 11, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e94(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 113, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e95(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e96(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e97(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 114, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e98(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e99(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 62, "i": 63, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 115, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e100(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 116, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e101(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 117, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e102(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 118, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e103(letra):
    transiciones = {"a": 101, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 25, "m": 1, "n": 1, "o": 26, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e104(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 119, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e105(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e106(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 120, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e107(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 121, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e108(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 122, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e109(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 123, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e110(letra):
    transiciones = {"a": 2, "b": 6, "c": 124, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e111(letra):
    transiciones = {"a": 2, "b": 6, "c": 125, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e112(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 126, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e113(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 127, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e114(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 128, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e115(letra):
    transiciones = {"a": 87, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 88, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e116(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 129, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e117(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 130, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e118(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 131, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e119(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e120(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e121(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 132, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e122(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 133, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e123(letra):
    transiciones = {"a": 2, "b": 6, "c": 134, "d": 34, "e": 35, "f": 27, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 28, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e124(letra):
    transiciones = {"a": 53, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 54, "p": 1 , "r": 20, "s": 40, "t": 135, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e125(letra):
    transiciones = {"a": 53, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 136, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 54, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e126(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 137, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e127(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 138, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e128(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e129(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 44, "u": 139, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e130(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 4, "p": 1 , "r": 20, "s": 40, "t": 140, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e131(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e132(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 55, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e133(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 25, "m": 1, "n": 1, "o": 26, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e134(letra):
    transiciones = {"a": 53, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 54, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e135(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e136(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e137(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 55, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 56, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e138(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e139(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 141, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 30, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e140(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e141(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e142(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 62, "i": 63, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 143, "u": 22, "v": 23, "w": 65, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e143(letra):
    transiciones = {"a": 87, "b": 6, "c": 33, "d": 34, "e": 144, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 88, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 8, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e144(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 35, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 50, "m": 1, "n": 51, "o": 1, "p": 1 , "r": 145, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 52, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)

def e145(letra):
    transiciones = {"a": 2, "b": 6, "c": 33, "d": 34, "e": 37, "f": 17, "g": 10, "h": 1, "i": 19, "k": 1, "l": 3, "m": 1, "n": 1, "o": 1, "p": 1 , "r": 20, "s": 40, "t": 7, "u": 22, "v": 23, "w": 12, "x": 1, "y": 1, "z": 1, "_": 14, "P":  1}
    estado.append(transiciones.get(letra, 1))
    return transiciones.get(letra, 1)


def buscador(cadena):
    
    estado = 1
    
    p_auto =        [0]
    p_else =        [0]
    p_long =        [0]
    p_switch =      [0]
    p_break =       [0]
    p_enum =        [0]
    p_register =    [0]
    p_typedef =     [0]
    p_case =        [0]
    p_extern =      [0]
    p_return =      [0]
    p_union =       [0]
    p_float =       [0]
    p_short =       [0]
    p_unsigned =    [0]
    p_const =       [0]
    p_for =         [0]
    p_signed =      [0]
    p_void =        [0]
    p_continue =    [0]
    p_goto =        [0]
    p_sizeof =      [0]
    p_volatile =    [0]
    p_default =     [0]
    p_if =          [0]
    p_static =      [0]
    p_while =       [0]
    p_do =          [0]
    p_int =         [0]
    p_struct =      [0]
    p__Packed =     [0]
    p_double =      [0]

    for indice, i in enumerate(cadena):
        
        letra.append(i)
        
        if estado == 1:
            
            estado = e1(i)
            
        elif estado == 2:
            estado = e2(i)

        elif estado == 3:
            estado = e3(i)
            
        elif estado == 4:
            estado = e4(i)
            
        elif estado == 5:
            estado = e5(i)
            
        elif estado == 6:
            estado = e6(i)
            
        elif estado == 7:
            estado = e7(i)
            
        elif estado == 8:
            estado = e8(i)
            
        elif estado == 9:
            estado = e9(i)
            
        elif estado == 10:
            estado = e10(i)
            
        elif estado == 11:
            estado = e11(i)
            
        elif estado == 12:
            estado = e12(i)
            
        elif estado == 13:
            estado = e13(i)
            
        elif estado == 14:
            estado = e14(i)
            
        elif estado == 15:
            estado = e15(i)
            
        elif estado == 16:
            estado = e16(i)
            
        elif estado == 17:
            estado = e17(i)
            
        elif estado == 18:
            p_long[0] += 1
            p_long.append(indice-1-3)
            estado = e18(i)
            
        elif estado == 19:
            estado = e19(i)
            
        elif estado == 20:
            estado = e20(i)
            
        elif estado == 21:
            estado = e21(i)
            
        elif estado == 22:
            estado = e22(i)
            
        elif estado == 23:
            estado = e23(i)
            
        elif estado == 24:
            estado = e24(i)
            
        elif estado == 25:
            estado = e25(i)
            
        elif estado == 26:
            estado = e26(i)
            
        elif estado == 27:
            p_if[0] += 1
            p_if.append(indice-1-1)
            estado = e27(i)
            
        elif estado == 28:
            estado = e28(i)
            
        elif estado == 29:
            p_goto[0] += 1
            p_goto.append(indice-1-1)
            estado = e29(i)
            
        elif estado == 30:
            estado = e30(i)
            
        elif estado == 31:
            estado = e31(i)
            
        elif estado == 32:
            estado = e32(i)
            
        elif estado == 33:
            estado = e33(i)
            
        elif estado == 34:
            estado = e34(i)
            
        elif estado == 35:
            estado = e35(i)
            
        elif estado == 36:
            estado = e36(i)
            
        elif estado == 37:
            estado = e37(i)
            
        elif estado == 38:
            estado = e38(i)
            
        elif estado == 39:
            estado = e39(i)
            
        elif estado == 40:
            estado = e40(i)
            
        elif estado == 41:
            estado = e41(i)
            
        elif estado == 42:
            estado = e42(i)
            
        elif estado == 43:
            p_for[0] += 1
            p_for.append(indice-1-2)
            estado = e43(i)
            
        elif estado == 44:
            p_int[0] += 1
            p_int.append(indice-1-2)
            estado = e44(i)
            
        elif estado == 45:
            estado = e45(i)
            
        elif estado == 46:
            estado = e46(i)
            
        elif estado == 47:
            estado = e47(i)
            
        elif estado == 48:
            estado = e48(i)
            
        elif estado == 49:
            p__Packed[0] += 1
            p__Packed.append(indice-1-6)
            estado = e49(i)
            
        elif estado == 50:
            estado = e50(i)
            
        elif estado == 51:
            estado = e51(i)
            
        elif estado == 52:
            estado = e52(i)
            
        elif estado == 53:
            estado = e53(i)
            
        elif estado == 54:
            estado = e54(i)
            
        elif estado == 55:
            estado = e55(i)
            
        elif estado == 56:
            p_do[0] += 1
            p_do.append(indice-1-1)
            estado = e56(i)
            
        elif estado == 57:
            estado = e57(i)
            
        elif estado == 58:
            estado = e58(i)
            
        elif estado == 59:
            estado = e59(i)
            
        elif estado == 60:
            estado = e60(i)
            
        elif estado == 61:
            estado = e61(i)
            
        elif estado == 62:
            estado = e62(i)
            
        elif estado == 63:
            estado = e63(i)
            
        elif estado == 64:
            estado = e64(i)
            
        elif estado == 65:
            estado = e65(i)
            
        elif estado == 66:
            estado = e66(i)
            
        elif estado == 67:
            estado = e67(i)
            
        elif estado == 68:
            estado = e68(i)
            
        elif estado == 69:
            p_void[0] += 1
            p_void.append(indice-1-3)
            estado = e69(i)
            
        elif estado == 70:
            estado = e70(i)
            
        elif estado == 71:
            estado = e71(i)
            
        elif estado == 72:
            estado = e72(i)
            
        elif estado == 73:
            estado = e73(i)
            
        elif estado == 74:
            estado = e74(i)
            
        elif estado == 75:
            estado = e75(i)
            
        elif estado == 76:
            estado = e76(i)
            
        elif estado == 77:
            estado = e77(i)
            
        elif estado == 78:
            estado = e78(i)
            
        elif estado == 79:
            estado = e79(i)
            
        elif estado == 80:
            estado = e80(i)
            
        elif estado == 81:
            estado = e81(i)
            
        elif estado == 82:
            p_while[0] += 1
            p_while.append(indice-1-4)
            estado = e82(i)
            
        elif estado == 83:
            estado = e83(i)
            
        elif estado == 84:
            estado = e84(i)
            
        elif estado == 85:
            estado = e85(i)
            
        elif estado == 86:
            estado = e86(i)
            
        elif estado == 87:
            estado = e87(i)
            
        elif estado == 88:
            estado = e88(i)
            
        elif estado == 89:
            estado = e89(i)
            
        elif estado == 90:
            p_auto[0] += 1
            p_auto.append(indice-1-3)
            estado = e90(i)
            
        elif estado == 91:
            p_float[0] += 1
            p_float.append(indice-1-4)
            estado = e91(i)
            
        elif estado == 92:
            p_union[0] += 1
            p_union.append(indice-1-4)
            estado = e92(i)
            
        elif estado == 93:
            estado = e93(i)
            
        elif estado == 94:
            estado = e94(i)
            
        elif estado == 95:
            p_else[0] += 1
            p_else.append(indice-1-3)
            estado = e95(i)
            
        elif estado == 96:
            p_enum[0] += 1
            p_enum.append(indice-1-3)
            estado = e96(i)
            
        elif estado == 97:
            estado = e97(i)
            
        elif estado == 98:
            p_case[0] += 1
            p_case.append(indice-1-3)
            estado = e98(i)
            
        elif estado == 99:
            estado = e99(i)
            
        elif estado == 100:
            estado = e100(i)
            
        elif estado == 101:
            estado = e101(i)
            
        elif estado == 102:
            estado = e102(i)
            
        elif estado == 103:
            p_typedef[0] += 1
            p_typedef.append(indice-1-6)
            estado = e103(i)
            
        elif estado == 104:
            estado = e104(i)
            
        elif estado == 105:
            p_break[0] += 1
            p_break.append(indice-1-4)
            estado = e105(i)
            
        elif estado == 106:
            estado = e106(i)
            
        elif estado == 107:
            estado = e107(i)
            
        elif estado == 108:
            estado = e108(i)
            
        elif estado == 109:
            estado = e109(i)
            
        elif estado == 110:
            estado = e110(i)
            
        elif estado == 111:
            estado = e111(i)
            
        elif estado == 112:
            estado = e112(i)
            
        elif estado == 113:
            estado = e113(i)
            
        elif estado == 114:
            estado = e114(i)
            
        elif estado == 115:
            p_const[0] += 1
            p_const.append(indice-1-4)
            estado = e115(i)
            
        elif estado == 116:
            estado = e116(i)
            
        elif estado == 117:
            estado = e117(i)
            
        elif estado == 118:
            estado = e118(i)
            
        elif estado == 119:
            p_return[0] += 1
            p_return.append(indice-1-5)
            estado = e119(i)
            
        elif estado == 120:
            p_short[0] += 1
            p_short.append(indice-1-4)
            estado = e120(i)
            
        elif estado == 121:
            estado = e121(i)
            
        elif estado == 122:
            estado = e122(i)
            
        elif estado == 123:
            estado = e123(i)
            
        elif estado == 124:
            estado = e124(i)
            
        elif estado == 125:
            estado = e125(i)
            
        elif estado == 126:
            estado = e126(i)
            
        elif estado == 127:
            estado = e127(i)
            
        elif estado == 128:
            p_extern[0] += 1
            p_extern.append(indice-1-5)
            estado = e128(i)
            
        elif estado == 129:
            estado = e129(i)
            
        elif estado == 130:
            estado = e130(i)
            
        elif estado == 131:
            p_double[0] += 1
            p_double.append(indice-1-5)
            estado = e131(i)
            
        elif estado == 132:
            p_signed[0] += 1
            p_signed.append(indice-1-5)
            estado = e132(i)
            
        elif estado == 133:
            p_sizeof[0] += 1
            p_sizeof.append(indice-1-5)
            estado = e133(i)
            
        elif estado == 134:
            p_static[0] += 1
            p_static.append(indice-1-5)
            estado = e134(i)
            
        elif estado == 135:
            p_struct[0] += 1
            p_struct.append(indice-1-5)
            estado = e135(i)
            
        elif estado == 136:
            p_switch[0] += 1
            p_switch.append(indice-1-5)
            estado = e136(i)
            
        elif estado == 137:
            p_unsigned[0] += 1
            p_unsigned.append(indice-1-7)
            estado = e137(i)
            
        elif estado == 138:
            p_volatile[0] += 1
            p_volatile.append(indice-1-7)
            estado = e138(i)
            
        elif estado == 139:
            estado = e139(i)
            
        elif estado == 140:
            p_default[0] += 1
            p_default.append(indice-1-6)
            estado = e140(i)
            
        elif estado == 141:
            p_continue[0] += 1
            p_continue.append(indice-1-7)
            estado = e141(i)
            
        elif estado == 142:
            estado = e142(i)
            
        elif estado == 143:
            estado = e143(i)
            
        elif estado == 144:
            estado = e144(i)
            
        elif estado == 145:
            p_register[0] += 1
            p_register.append(indice-1-7)
            estado = e145(i)
        
    return {
        'auto': p_auto,
        'else': p_else,
        'long': p_long,
        'switch': p_switch,
        'break': p_break,
        'enum': p_enum,
        'register': p_register,
        'typedef': p_typedef,
        'case': p_case,
        'extern': p_extern,
        'return': p_return,
        'union': p_union,
        'float': p_float,
        'short': p_short,
        'unsigned': p_unsigned,
        'const': p_const,
        'for': p_for,
        'signed': p_signed,
        'void': p_void,
        'continue': p_continue,
        'goto': p_goto,
        'sizeof': p_sizeof,
        'volatile': p_volatile,
        'default': p_default,
        'if': p_if,
        'static': p_static,
        'while': p_while,
        'do': p_do,
        'int': p_int,
        'struct': p_struct,
        '_Packed': p__Packed,
        'double': p_double
    }
    
def regresa_historia():
    return estado, letra
