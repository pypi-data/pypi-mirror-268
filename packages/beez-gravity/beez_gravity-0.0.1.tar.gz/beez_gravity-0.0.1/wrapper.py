import ctypes

# Carica la libreria condivisa
lib = ctypes.CDLL('./add.so')

# Definisci la firma della funzione
lib.add.restype = ctypes.c_int
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]

# Wrapper per la funzione add
def add(a, b):
    return lib.add(a, b)
