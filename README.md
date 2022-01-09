Hello! 
Welcome to online store on Django

Installation for users who used MacOS | Linux:

1. Choose directory where we want to store this project.
2. Open terminal and do next command: git clone 
3. Install virtual environment: python3 -m venv
4. Activate your venv: source/venv/bin/activate
5. Go to the directory(Repository name)
6. Install project packages: pip install -r requirements.txt. 
6.1. If you didn't have pip package - install it:
   $ sudo apt update 
   $ sudo apt install python3-pip
7. In your source root directory create new 'media' directory to save images for your created products.   
8. Make migrations: python manage.py migrate
9. Run virtual environment (source venv/bin/activate)
10. Create superuser to add products to your admin panel: python manage.py create superuser
11. Run server: python manage.py runserver
12. Open your browser and go to: http://127.0.0.1:8000/admin
13. First you need to add some Categories and Products
14. Go to main paig and what you can do with them: http://127.0.0.1:8000

This project was developed for self use, 
 so you did not can ordered products on the web page, they are not real.  
