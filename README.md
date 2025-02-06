creer un read me :
j'ai fait des tests sur le fichier nomùmée main (exo du fizzbuzz) 

ce fichier j'ai fait des tests (avec unitest et pytest pour avoir les 2 cas de figures) dans le fichier nommée test_main et test_fizzbuzz respectivement, j'ai aussi créer 2 branches (test_unitest et test_pytest).

ensuite j'ai fait le process git actions et j'ai configuer dans un fichier yaml permettant de verifié différent os et version
(matrix:
        os: [ubuntu-latest, windows-latest, macOS-latest]
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"
        )

ensuite j'ai créer un coverage qui permet de suivre le ... permettant de verifié notre code
avec pytest :
coverage report
Name               Stmts   Miss  Cover
--------------------------------------
main.py               16      3    81%
test_fizzbuzz.py      17      0   100%
test_main.py          21      1    95%
--------------------------------------
TOTAL                 54      4    93%

et avec unittest:

coverage report
Name               Stmts   Miss  Cover
--------------------------------------
main.py               16      3    81%
test_fizzbuzz.py      17     12    29%
test_main.py          21      1    95%
--------------------------------------
TOTAL                 54     16    70%

on peut

pour les blocages de master ca bloque l'envoie sur master et donc obliger de passer par des pull request pour mettre du code daans la master

dans le dockerfile, unittest n’a pas besoin d’être spécifiquement "notifié" dans le Dockerfile, car il est intégré dans Python. 

