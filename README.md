# DjangoLoginTester

# Requis
pip install django
pip install django-crispy-forms

# Utilisation
## Virtual env
...

python manage.py runserver

## Docker :
- sudo docker load < django_container.tar
- sudo docker run --network host --mount type=bind,source="$(pwd)"/loginTester,target=/home -w /home antoineh/django python3 manage.py runserver


Connexion utilisateur :
- Username : admin
- Password : admin

# Liens
https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial

https://learndjango.com/tutorials/django-login-and-logout-tutorial

https://djangoforbeginners.com/pages-app/

Modal :
https://dmorgan.info/posts/django-views-bootstrap-modals/

https://pypi.org/project/django-bootstrap-modal-forms/


https://djangocentral.com/django-ajax-with-jquery/

# TODO : 
-Tests 
-Otion Docker container avec compose
