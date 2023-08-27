![Alt text](https://github.com/molly-muffin/P12_OC_EpicEvents/blob/main/image/img.png)

# Développer une architecture back-end sécurisée avec Python et SQL

## Contexte du projet : 
EpicEvents, une société d'événementiel, a décidé de publier une application permettant de créer et suivre leurs clients, contats et événements.


### Le site permet  :
De créer des : 
- Utilisateurs liés à un ou plusieurs clients ou évènements
- Clients liés à un ou plusieurs contrats
- Contrats liés à un client
- Événements liés à un contrat


Voici les différentes spécifications techniques de l'API :

- **Authentification des utilisateurs** 
    Utilisation de JWT pour authentifier les utilisateurs.

- **Un client** :
    - peut être créé par un membre de l'équipe COMMERCIALE
    - peut être modifié par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT affecté au client
    - peut être consulté par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT
    - peut être suprimé par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT affecté au client

- **Un contrat** :
    - peut être créé par un membre de l'équipe COMMERCIALE
    - peut être modifié par un membre de l'équipe COMMERCIALE
    - peut être consulté par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT
    - peut être suprimé par un membre de l'équipe COMMERCIALE

- **Un événement** :
    - peut être créé par un membre de l'équipe COMMERCIALE
    - peut être modifié par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT affecté à l'événement
    - peut être consulté par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT
    - peut être suprimé par un membre de l'équipe COMMERCIALE, SUPPORT ou MANAGEMENT affecté à l'événement

### Environnement de développement :
`Django` `PostgreSQL`


### Instruction d’installation et d’utilisation :
- Prérequis et installation
    - Dans le terminal, aller dans le dossier ou vous souhaitez placer le projet et copier le projet 
    ```bash
    git clone https://github.com/molly-muffin/P12_OC_EpicEvents.git
    ```
    - Aller dans ce dossier
    ```bash
    cd P12_OC_EpicEvents\epic_events_crm\
    ```
    - Créer un environnement virtuel
    ```bash
    python -m venv env
    ```
    - Activer le script
    
    **Windows :**
    ```bash
    .\env\Scripts\activate
    ```
    **Linux :**
    ```bash
    source env\bin\activate
    ```
    - Installer les packages dans le requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
    - Créer une base de donnée
    ```bash
    CREATE DATABASE epic_events_crm
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    ```
    --> Modifier le fichier [settings](https://github.com/molly-muffin/P12_OC_EpicEvents/blob/main/epic_events_crm/epic_events_crm/settings.py)
    ```bash
    USER=postgres
    PASSWORD=mot_de_passe_utilisateur_bdd
    DB_NAME=epic_events_crm
    HOST=localhost
    PORT=5432
    ```
    - Réaliser les migrations 
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    - Créer un superutilisateur
    ```bash
    python manage.py createsuperuser
    ```

- Lancement
    - Lancer le  **serveur local**, avec la commande
    ```bash
    python manage.py runserver
    ```
    - Puis rendez vous sur http://127.0.0.1:8000/login/ et accéder à la page d'authentification de l'API.


- Utilisation
    - Vous retrouverez tous les points de terminaisons de l'API et leur utilisation dans la documentation Postman : https://documenter.getpostman.com/view/23897812/2s9Y5WyPQK


    - Si vous souhaitez avoir accès à l'intégralités des données de l'API vous avez le pnael admin disponible sur http://127.0.0.1:8000/admin/


### Vérification du code
- Contrôle du code avec **flake8** :
```bash
flake8 --max-line-length 215 --format=html --htmldir=flake-report --exclude=migrations
```


> Laureenda Demeule
> OpenClassroom

