# 🎮 Mario Game - Python Edition

Un jeu de plateforme Mario classique implémenté en Python avec Pygame.

## 📋 Fonctionnalités

- 🕹️ **Gameplay fluide** : Mouvement et saut réaliste avec gravité
- 👾 **Ennemis intelligents** : Goombas avec IA de patrouille
- 💰 **Système de pièces** : Collectez des pièces pour augmenter votre score
- 📈 **3 niveaux progressifs** : Difficultés croissantes
- ⏸️ **Pause et contrôles** : Interface intuitive
- 🎯 **Système de score** : Suivez vos performances

## ⌨️ Contrôles

| Touche | Action |
|--------|--------|
| **← / →** | Déplacement gauche/droite |
| **ESPACE** | Sauter |
| **P** | Pause |
| **ESC** | Quitter |
| **R** | Recommencer après game over |

## 🎯 Points

- **+10 points** : Collecter une pièce
- **+50 points** : Vaincre un ennemi en sautant dessus
- **-100 points** : Collision avec un ennemi

## 🚀 Installation

### Prérequis
- Python 3.7 ou plus récent
- pip (gestionnaire de paquets Python)

### Étapes

1. **Clonez le repository**
   ```bash
   git clone https://github.com/FadyDawra54/mario-game.git
   cd mario-game
   ```

2. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancez le jeu**
   ```bash
   python main.py
   ```

## 📁 Structure du projet

```
mario-game/
├── main.py           # Point d'entrée principal du jeu
├── player.py         # Classe du joueur (Mario)
├── enemy.py          # Classe des ennemis (Goombas)
├── coin.py           # Classe des pièces
├── level.py          # Générateur de niveaux
├── requirements.txt  # Dépendances Python
└── README.md         # Documentation
```

## 🎮 Comment jouer

1. Utilisez les flèches gauche/droite pour vous déplacer
2. Appuyez sur ESPACE pour sauter
3. Sautez sur les ennemis pour les éliminer
4. Collectez toutes les pièces pour terminer le niveau
5. Complétez les 3 niveaux pour gagner!

## 🔧 Développement

Le code est organisé en modules pour la maintenabilité :

- **main.py** : Boucle de jeu principale, gestion des événements
- **player.py** : Logique du joueur, mouvement, collision
- **enemy.py** : Comportement des ennemis, IA
- **coin.py** : Logique des pièces à collecter
- **level.py** : Génération des niveaux

## 🐛 Bugs connus / À améliorer

- [ ] Ajouter des animations visuelles
- [ ] Ajouter des sons et de la musique
- [ ] Implémenter des power-ups
- [ ] Ajouter un système de vies
- [ ] Créer des textures personnalisées

## 📝 Licence

Ce projet est sous licence MIT - vous pouvez l'utiliser librement!

## 👨‍💻 Auteur

Créé par FadyDawra54

## 🎉 Amusez-vous bien!

N'hésitez pas à contribuer, signaler des bugs ou proposer des améliorations!
