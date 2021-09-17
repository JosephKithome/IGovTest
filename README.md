INSTALLATION INSTRUCTIONS

1.Install Python

- sudo apt install python3
  2.Install pip
- sudo python3 install pip

3. Install Virtual environment

- sudo pip3 install virtualenv

4. cd into projects directory
5. create virtual environment
   - virtualenv venv
6. activate virtual environment
   - ssource venv/bin/activate
7. Install requirements
   pip install -r requirements.txt

8. makemigrations by running
   python manage.py makemigrations api
   python manage.py migrate api
   python manage.py migrate

9. Create superuser

   - python manage.py createsuperuser

10. Run the application

- python manage.py runserver


#Endpoints
http://127.0.0.1:8000 => List of all the vehicles in the detabase

http://127.0.0.1:8000/id   =>Returns a specific vehicle given an id

http://127.0.0.1:8000/discontinued/  => Returns a list of discontinued vehicle 


http://127.0.0.1:8000/discontinued/year => Returns a list of discontinued vehicles filtered by year


http://127.0.0.1:8000/discontinued_vehicle_detail/id   =>Returns the detail of a specific discontinued vehicle