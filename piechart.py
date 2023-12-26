import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import pandas as pd
from math import pi
import numpy as np

def create_dictionary():
    try:
        # Demander à l'utilisateur le nombre de valeurs
        num_values = int(input("Entrez le nombre de parts : "))

        # Initialiser un dictionnaire vide
        my_dict = {}

        # Demander à l'utilisateur de fournir les clés et les valeurs associées
        for _ in range(num_values):
            key = input(f"Entrez le nom de la part {_+1} : ")
            value = input("Entrez la valeur de la part : ")

            # Ajouter la paire clé-valeur au dictionnaire
            my_dict[key] = int(value) # Convertir la valeur en float

        return my_dict

    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier pour le nombre de valeurs.")
        return None


user_dict = create_dictionary()


# Convertir le dictionnaire en DataFrame
df = pd.DataFrame(list(user_dict.items()), columns=['Clé', 'Valeur'])

categories = list(df['Clé'])
N = len(categories)
angles = np.linspace(0, 2 * pi, N, endpoint=False)
angles_mids = angles + (angles[1] / 2)

fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles_mids)
ax.set_xticklabels(categories)
ax.xaxis.set_minor_locator(FixedLocator(angles))

# Dessiner les ylabels
ax.set_rlabel_position(0)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], color="black", size=8)
ax.set_ylim(0, 5)

values_a = df['Valeur']

# Obtenir une carte de couleurs automatique
color_map = plt.cm.get_cmap('tab10')

for i in range(N):
    color = color_map(i / N)  # Utiliser une couleur différente pour chaque catégorie
    ax.bar(angles_mids[i], values_a[i], width=angles[1] - angles[0],
           facecolor=color, alpha=0.7, edgecolor='k', linewidth=1, label=f"{categories[i]} (A)")

ax.grid(True, axis='x', which='minor')
ax.grid(False, axis='x', which='major')
ax.grid(True, axis='y', which='major')
ax.legend(loc='upper left', bbox_to_anchor=(0.9, 1))
plt.show()
