# synch2jira

# Faut avoir la version 3.10.12 de python 
## Importer le package
```
 pip install synch2jira
```

## Mettre à jour le package 
⚠️ A faire 2 fois !! 
```
 pip install --upgrade synch2jira
 pip install --upgrade synch2jira
 
```





## Remplir le fichier de config

from synch2jira.config_package import config_package

config_package()

NB : Vérifier qu'un fichier config.py est crée

## Tester la connexion
from synch2jira.issue_S2 import IssueS2

print(IssueS2.check_connection())

## Récupérer un ticket 
IssueS2.find_by_id(key_issue)

## Récuperer les status 
IssueS2.get_jira_status(project_id_or_key)

## Récuperer le nombre total de ticket 
IssueS2.get_jira_issues_total()

## Issue remplir database
* Créer un dossier database
* Appeler la fonction pour créer et remplir la base de données
from synch2jira.config_package import config_database_workflow

config_database_workflow()

## Générer le fichier csv 
from synch2jira.issue_workflow import WorkFlow
print(" Les états sont : ", config.jiraStatusName)
state1 = input("Veuillez saisir l'état de départ : ")
state2 = input("Veuillez saisir l'état d'arrivé: ")
WorkFlow.get_all_wokflow_in_csv(state1, state2)

## Récuperer les leadtimes 
WorkFlow.get_all_workflow(state1, state2)

## Tester le package 
Dans un fichier test.py importer le package 
from synch2jira.issue import Issue
issue = Issue("test  issue factory", "test issue fatory", None, "")
print(issue)




## Développer les fonctions suivantes dans S1 :

* All() : Cette fonction retourne la liste de tous les enregistrements disponibles dans S1.

* first() : Retourne le premier élément de la liste des enregistrements.

* last() : Retourne le dernier élément de la liste des enregistrements.

* find_by() : Cette fonction permet de rechercher des enregistrements en fonction de certains critères spécifiés.

* find_by_id(id) : Retourne l'enregistrement correspondant à l'ID spécifié.

* update() : Met à jour un enregistrement existant dans la base de données.

* delete() : Supprime un enregistrement de la base de données.

* save() : Enregistre un nouvel enregistrement dans la base de données.

* get() : Cette fonction récupère des informations spécifiques sur un enregistrement donné.





