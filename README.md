# groupe_15

## Task_1
Rapport d'utilisation de la classe Array avec répartition des tâches

### Classe Array
La classe Array est conçue pour manipuler des listes d'entiers (1D ou 2D) avec diverses opérations comme l'addition, la soustraction, la multiplication, la division, ainsi que le produit scalaire. Voici les principales fonctions et leur description :
1. __init__ : Initialise l'objet Array avec les données fournies.
2. _get_shape : Calcule et retourne la forme des données (1D ou 2D).
3. __repr__ : Retourne une représentation officielle de l'objet.
4. __str__ : Retourne une représentation lisible de l'objet.
5. __matmul__ : Calcule le produit scalaire de deux tableaux 1D.
6. __contains__ : Vérifie si un élément est présent dans les données.
7. __getitem__ : Retourne l'élément à l'index spécifié.
8. __setitem__ : Définit l'élément à l'index spécifié.
9. __add__ : Additionne deux tableaux.
10. __sub__ : Soustrait un tableau d'un autre.
11. __mul__ : Multiplie les éléments du tableau par un scalaire ou un autre tableau.
12. __truediv__ : Divise les éléments du tableau par un scalaire ou un autre tableau.
13. __len__ : Retourne la longueur du tableau (1D uniquement).
14. shape : Retourne la forme du tableau.

### Tests
#### Initialisation
```python
arr1 = Array([1, 2, 3, 4, 5])
arr2 = Array([4, 5, 6, 9, 8])
arrd2 = Array([[2, 8], [9, 7]])
```
#### Représentation
```python
print(repr(arr1))  # Affiche Array([1, 2, 3, 4, 5])
print(arr1)        # Affiche [1, 2, 3, 4, 5]
print(arrd2)       # Affiche [[2, 8], [9, 7]]
```
#### Indexation
```python
print(arr1[2])     # Affiche 3
print(arrd2[0, 1]) # Affiche 8 (indexation 2D)
```
#### Slicing
```python
print(arr1[1:4])   # Affiche [2, 3, 4] 
print(arrd2[:, 1]) # Affiche [8, 7] (slicing 2D)
```
#### Produit scalaire
```python
result = arr1 @ arr2
print(result)      # Affiche 108 (1*4 + 2*5 + 3*6 + 4*9 + 5*8)
```
#### Addition
```python
arr3 = arr1 + arr2
print(arr3)        # Affiche [5, 7, 9, 13, 13]
```
#### Soustraction
```
arr4 = arr2 - arr1
print(arr4)        # Affiche [3, 3, 3, 5, 3]
```
#### Multiplication par un scalaire
```python
arr5 = arr1 * 2
print(arr5)        # Affiche [2, 4, 6, 8, 10]
```
#### Multiplication par un autre tableau
```python
arr6 = arr1 * arr2
print(arr6)        # Affiche [4, 10, 18, 36, 40]
```
#### Division par un scalaire
```python
arr7 = arr2 / 2
print(arr7)        # Affiche [2.0, 2.5, 3.0, 4.5, 4.0]
```
#### Division par un autre tableau
```python
arr8 = arr2 / arr1
print(arr8)        # Affiche [4.0, 2.5, 2.0, 2.25, 1.6]
```
#### Contient un élément
```python
print(1 in arr1)   # True
print(9 in arr2)   # True
```
#### Longueur du tableau
```python
print(len(arr1))   # Affiche 5
```
#### Forme du tableau
```python
print(arr1.shape)  # Affiche (5,)
```

## Task_3
Requirements
```python
python3 requirements.py
```
Execution du code:
```python
python3 task_3/gui.py
```
Assurez-vous de changer le path vers votre dossier clone dans ASSETS_PATH de gui.py
```
".../groupe_15/task_3/assets/frame0"
```
Envie de changer de modèle? 
Un petit changement de nom dans la variable **current_model_name** à la ligne 20 de gui.py
