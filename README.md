# fund_management

Instructions to run this:
1. Clone this repo (master branch)
2. Open the project folder and open 2 terminals (1 for Django API another 1 for frontend)
3. On the django terminal
     'run pip install virtualenv'
4. after it is installed, run 'virtualenv venv'
5. then in the terminal run 'pip install -r requirements.txt'
6. then cd into fund_mgmt_system until you can see the 'manage.py' file
7. in the directory, run 'python manage.py makemigrations' , followed by 'python manage.py migrate'
8. then to pump data into the database, run 'python manage.py import_funds'
9. then finally, run 'python manage.py runserver'
10. then proceeding to frontend by opening another terminal and cd into 'frontend'
11. run 'npm run serve'
12. Click on the given URL, then you should be able to see the app.
