# Clic Reflex

[![Licence](https://img.shields.io/badge/license-MIT-green.svg)]  
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)]  
[![Pygame](https://img.shields.io/badge/pygame-required-yellow.svg)]  

## Description

**Clic Reflex** est un jeu local développé en Python/Pygame permettant d'entraîner le temps de réaction et la précision de la souris.  
Un compte à rebours annonce le début de la session.  
- Des cercles apparaissent aléatoirement à l'écran.  
Le joueur doit cliquer dessus le plus rapidement possible pendant 60 secondes.  
À la fin, le temps de réaction moyen et le ratio de clics réussis s'affichent.

## Objectifs

## Objectifs

1. Proposer un outil ludique pour s’entraîner à contrôler la souris.  
2. Offrir une alternative interactive aux exercices PowerPoint traditionnels, pour dynamiser les ateliers de stimulation de la mémoire et des capacités cognitives.  
3. Permettre un suivi rapide des performances.

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/TON-UTILISATEUR/clic-reflex.git
cd clic-reflex

# 2. (Optionnel) Créer et activer un environnement virtuel
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3. Installer Pygame
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

1. Un écran de démarrage lance un compte à rebours de 3 s.
2. Cliquez sur les cercles dès qu'ils apparaissent.  
3. À la fin du compte à rebours (60 s), les résultats s'affichent :
	- Temps de réaction moyen
	- Nombre de clics réussis/totaux

## Statut du projet

**Fonctionnel** version de base terminée, améliorations possibles pour la durée, le scoring et l'interface.

## Licence

MIT

---

## Améliorations futures

- Paramétrer la durée de la session et la taille des cercles.  
- Ajouter un mode « multi-tours » avec graphique d'évolution.  
- Intégrer un suivi des meilleures performances (fichier CSV ou base SQLite).  
- Emballer en exécutable (PyInstaller).
