from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        self.shape = self._get_shape(data)

    def _get_shape(self, data: Union[List[int], List[List[int]]]) -> Tuple[int, ...]:
        if isinstance(data, list):
            if isinstance(data[0], list):
                if all(isinstance(i, list) for i in data) and all(len(i) == len(data[0]) for i in data):
                    return (len(data), len(data[0]))
                else:
                    raise ValueError("Toutes les sous-listes doivent avoir la même longueur.")
            else:
                return (len(data),)
        else:
            raise ValueError("Données d'entrée invalides. Doit être une liste.")

    def __repr__(self) -> str:
        return f"Array({self.data})"
    
    def __str__(self) -> str:
        return str(self.data)

    def __matmul__(self, other: 'Array') -> int:
        if not isinstance(other, Array):
            raise TypeError("Type d'opérande non pris en charge pour @ : 'Array' et '{}'".format(type(other).__name__))
        if len(self.shape) != 1 or len(other.shape) != 1:
            raise ValueError("Le produit scalaire (@) n'est pris en charge que pour les tableaux 1D.")
        if self.shape[0] != other.shape[0]:
            raise ValueError("Les tableaux doivent avoir la même longueur pour le produit scalaire.")

        result = sum(self.data[i] * other.data[i] for i in range(self.shape[0]))
        return result

    def __contains__(self, item: int) -> bool:
        return item in self.data

    def __getitem__(self, index: Union[int, slice, Tuple[int, int], Tuple[slice, slice]]) -> Union[int, List[int]]:
        if isinstance(index, int):
            return self.data[index]
        elif isinstance(index, slice):
            return self.data[index]
        elif isinstance(index, tuple):
            if len(index) == 2:
                if isinstance(index[0], int) and isinstance(index[1], int):
                    return self.data[index[0]][index[1]]
                elif isinstance(index[0], slice) and isinstance(index[1], slice):
                    return [row[index[1]] for row in self.data[index[0]]]
                elif isinstance(index[0], int) and isinstance(index[1], slice):
                    return self.data[index[0]][index[1]]
                elif isinstance(index[0], slice) and isinstance(index[1], int):
                    return [row[index[1]] for row in self.data[index[0]]]
                else:
                    raise TypeError("Index non pris en charge.")
            else:
                raise IndexError("Nombre d'index incorrect pour l'indexation.")
        else:
            raise TypeError("Type d'index non pris en charge.")

    def __setitem__(self, index: Union[int, Tuple[int, int]], value: int) -> None:
        if isinstance(index, int):
            self.data[index] = value
        elif isinstance(index, tuple) and len(index) == 2:
            self.data[index[0]][index[1]] = value
        else:
            raise TypeError("Type d'index non pris en charge.")

    def __add__(self, other: 'Array') -> 'Array':
        if not isinstance(other, Array):
            raise TypeError("Type d'opérande non pris en charge pour + : 'Array' et '{}'".format(type(other).__name__))
        if self.shape != other.shape:
            raise ValueError("Les tableaux doivent avoir la même forme pour l'addition.")
        
        if len(self.shape) == 1:
            result = [self.data[i] + other.data[i] for i in range(self.shape[0])]
        elif len(self.shape) == 2:
            result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Array(result)

    def __sub__(self, other: 'Array') -> 'Array':
        if not isinstance(other, Array):
            raise TypeError("Type d'opérande non pris en charge pour - : 'Array' et '{}'".format(type(other).__name__))
        if self.shape != other.shape:
            raise ValueError("Les tableaux doivent avoir la même forme pour la soustraction.")
        
        if len(self.shape) == 1:
            result = [self.data[i] - other.data[i] for i in range(self.shape[0])]
        elif len(self.shape) == 2:
            result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Array(result)

    def __mul__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            if len(self.shape) == 1:
                result = [self.data[i] * other for i in range(self.shape[0])]
            elif len(self.shape) == 2:
                result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
        elif isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent avoir la même forme pour la multiplication.")
            if len(self.shape) == 1:
                result = [self.data[i] * other.data[i] for i in range(self.shape[0])]
            elif len(self.shape) == 2:
                result = [[self.data[i][j] * other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        else:
            raise TypeError("Type d'opérande non pris en charge pour * : 'Array' et '{}'".format(type(other).__name__))
        return Array(result)

    def __truediv__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Division par zéro non autorisée.")
            if len(self.shape) == 1:
                result = [self.data[i] / other for i in range(self.shape[0])]
            elif len(self.shape) == 2:
                result = [[self.data[i][j] / other for j in range(self.shape[1])] for i in range(self.shape[0])]
        elif isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent avoir la même forme pour la division.")
            if len(self.shape) == 1:
                result = [self.data[i] / other.data[i] for i in range(self.shape[0])]
            elif len(self.shape) == 2:
                result = [[self.data[i][j] / other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        else:
            raise TypeError("Type d'opérande non pris en charge pour / : 'Array' et '{}'".format(type(other).__name__))
        return Array(result)

    def __len__(self) -> int:
        return self.shape[0]

# Test du code
arr1 = Array([1, 2, 3, 4, 5])
arr2 = Array([4, 5, 6, 9, 8])
arrd2 = Array([[2, 8], [9, 7]])

print(repr(arr1))  # Affiche Array([1, 2, 3, 4, 5])
print(arr1)        # Affiche [1, 2, 3, 4, 5]
print(arrd2)       # Affiche [[2, 8], [9, 7]]

# Test du produit scalaire
result = arr1 @ arr2
print(result)      # Affiche 108 (1*4 + 2*5 + 3*6 + 4*9 + 5*8)

# Test de l'ajout
arr3 = arr1 + arr2
print(arr3)        # Affiche [5, 7, 9, 13, 13]

# Test de la soustraction
arr4 = arr2 - arr1
print(arr4)        # Affiche [3, 3, 3, 5, 3]

# Test de la multiplication par un scalaire
arr5 = arr1 * 2
print(arr5)        # Affiche [2, 4, 6, 8, 10]

# Test de la multiplication par un autre tableau
arr6 = arr1 * arr2
print(arr6)        # Affiche [4, 10, 18, 36, 40]

# Test de la division par un scalaire
arr7 = arr2 / 2
print(arr7)        # Affiche [2.0, 2.5, 3.0, 4.5, 4.0]

# Test de la division par un autre tableau
arr8 = arr2 / arr1
print(arr8)        # Affiche [4.0, 2.5, 2.0, 2.25, 1.6]

# Test de l'appartenance
print(1 in arr1)  # True
print(9 in arr2)  # True

# Test de la longueur
print(len(arr1))   # Affiche 5
print(arr1.shape)  # Affiche (5,)

# Test de l'indexation et du slicing
print(arr1[2])     # Affiche 3 (indexation)
print(arr1[1:4])   # Affiche [2, 3, 4] (slicing)
print(arrd2[0, 1]) # Affiche 8 (indexation 2D)
print(arrd2[:, 1]) # Affiche [8, 7] (slicing 2D)
