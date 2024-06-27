#Importation du dataset
data <- read.csv("C:/Users/de/3D Objects/Housing.csv")
#Visualistion du dataset
View(data)
#Structure du dataset
str(data)
#Dimensionnalité du dataset
dim(data)
#Affichage du résumé du dataset avec des coefficients
summary(data)
#Vérification des valeurs manquantes dans le dataset
is.na(data)
#vérification totale des valeurs manquantes
sum(is.na(data))
#Vérification par colonne des valeurs manquantes
colSums(is.na(data))
#Création du graphique (nuage de points)
library(ggplot2)
par(mar = c(5, 4, 4, 2) + 0.1)
ggplot(data = data, aes(x = area, y = price)) +
  geom_point(col = "black", size = 3) +
  xlab(label = "area") +
  ylab(label = "price") +
  ggtitle("Nuage de points")
#Création du graphique (histogramme)
ggplot(data = data, aes(bedrooms))+
   geom_histogram(bins = 15, color = "black", fill="red")


