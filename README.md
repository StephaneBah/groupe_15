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

### Répartition des tâches
La répartition des tâches pour l'implémentation et les tests de cette classe est organisée comme suit :
1. SODJINOU Isis
    - Implémente les méthodes __init__ et _get_shape pour gérer la création d'un tableau et déterminer sa forme.
    - Ajoute les méthodes __repr__ et __str__ pour fournir des représentations en chaîne de caractères de l'objet Array.

2. GNACADJA Laurinda
    - Développe les méthodes pour les opérations scalaires (__matmul__, __contains__).
    - Ajoute l'indexation et le slicing avec les méthodes __getitem__ et __setitem__.
    - Implémente la méthode __len__ pour obtenir la longueur du tableau.
  
3. AHO-GLELE Liz
     - Développe les méthodes __add__ et __sub__ pour l'addition et la soustraction des tableaux.
     - Implémente la méthode _get_shape pour déterminer la forme d'un tableau.

4. WABI Youmna
    - Gère les fonctionnalités de multiplication et de division (__mul__, __truediv__).
    - Gère les exceptions pour les différents types d'erreurs (e.g., TypeError, ValueError, ZeroDivisionError).

### Tests
Les tests suivants ont été effectués pour vérifier le bon fonctionnement de la classe Array :
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


## Task_2
### Rapport de la tâche 2

Pour la réalisation de notre tâche, nous avons fait une analyse basique du dataset, pour la faire, nous avons d'abord importé quelques bibliothèques (pandas, numpy, matplotlib.pyplot), ensuite la dataset et utilisé quelques fonctions:

1-head() en python et view() en R qui nous permet d'afficher les premières lignes de notre dataset.

2-info() qui nous permet de fournir un résumé concis de notre dataset.

3-describe() en python et summary() en R qui nous permet d'afficher un résumé du dataset avec des coefficients.

4-isnull() en python et is.na() en R qui nous permet de vérifier s'il ya a des données manquantes dans notre dataset, pour être convaincu de son résultat, on a après vérifié par colonne avec (isnull().sum() en python et colSums(is.na()) en R).

On a ensuite créé un histogramme et un nuage de points (en utilisant scatter plot) qu'on a après analysé en quelques phrases:

Histogramme: A partir de la visualisation de l'histogramme, nous constatons que la majorité des maisons de notre dataset sont à trois chambres, nous avons aussi en moyenne des maisons à deux chambres et une minorité de maisons à quatre chambres. Le reste des maisons à cinq, six chambres sont en faible minorité.

Nuage de points: A partir de la visualisation du nuage de point, on constate que les prix des maisons ne dépendent pas de leurs superficies car dans notre dataset des maisons ont mêmes superficies mais pas le même prix et aussi on remarque des points un peu isolé du groupement de points, ce qui nous laisse penser que d'autres facteurs que la surface peuvent également influencer le prix d'une maison, tels que l'emplacement, l'état de la maison, les équipements, etc.

### Répartition des tâches:

1. ALOWANOU Sèdami
- Implémentation du code en python et R
- Analyse des résultas obtenu

2. QUENUM Alfred


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
### Déroulement des Travaux
Détaillé dans:
```
.../groupe_15/task_3/Rapport_Task_3.docx
```

## Pourcentages de chaque membres
1. SODJINOU Isis: **10%**
2. GNACADJA Laurinda: **10%**
3. AHO-GLELE Liz: **10%**
4. WABI Youmna: **10%**
5. ALOWANOU Sèdami: **10%**
6. QUENUM Alfred: **4%**
7. AHOLOU-BAH Stéphane: **15%**
8. TCHEKPO Inès: **15%**
9. LIMA Marie-Paule: **10%**
10. DANSOU Ghislain: **6%**
