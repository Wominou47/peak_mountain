récupération du projet :
git clone https://github.com/Wominou47/peak_mountain.git

lancement de l'appli web : 
- se placer à la racine du projet dans peak_mountain
- docker-compose up

utilisation de l'appli web :

- http://localhost:8000/ : page d'arrivée listant toutes les coordonnées de la BDD
- http://localhost:8000/ingest : ingestion de 2 enregistrements de test dans la BDD
- http://localhost:8000/delete/all/ : pour écraser tous les enregistrements de la BDD
- http://localhost:8000/delete/1 : supprime l'index 1 de la BDD (si existant), nécessite une confirmation avec "delete"
- http://localhost:8000/1 : visualise sur la carte les coordonnées de l'enregistrement 1
- http://localhost:8000/update/1 : met à jour l'index 1 de la BDD (si existant)

arrêt de l'appli web :
- docker-compose down