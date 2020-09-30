# DjangoLoginTester

## Utilisation
### Virtual environment
`$ source c:/Users/antoi/Downloads/DjangoLoginTester/djando_venv/Scripts/activate`

#### Setup
- `$ pip install django`
- `$ pip install django-crispy-forms`

#### Run

`$ python manage.py runserver`

### Docker :
- Téléchargement (provisoire) : https://we.tl/t-duPOPTZiVq
- `$ sudo docker load < django_container.tar`
- `$ sudo docker run --network host --mount type=bind,source="$(pwd)"/loginTester,target=/home -w /home antoineh/django python3 manage.py runserver`


### Connexion utilisateur :
- URL : http://127.0.0.1:8000/
- Username : admin
- Password : admin

## Liens

https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial

https://learndjango.com/tutorials/django-login-and-logout-tutorial

https://djangoforbeginners.com/pages-app/

Modal / Asynchronous JavaScript And XML:

https://dmorgan.info/posts/django-views-bootstrap-modals/

https://pypi.org/project/django-bootstrap-modal-forms/

https://djangocentral.com/django-ajax-with-jquery/

## TODO : 
- Tests 
- Option Docker container avec compose
