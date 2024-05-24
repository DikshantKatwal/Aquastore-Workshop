# STEPS TO FOLLOW
Terminal
-  py -m venv env
-  ./env/scripts/activate
-  pip install -r requirements.txt
-  create '.env' file on main folder add below requirements for your system
  
      -  debug=True
      -  MAIN_DOMAIN="localhost:8000"
      -  database_name='database name you created'
      -  database_host=localhost
      -  database_port=3306
      -  database_user='mysql username'
      -  database_password='mysql password'

   
-  py manage.py makemigrations
-  py manage.py migrate
-  py manage.py createsuperuser
-  py manage.py runserver
