### How to set everything up first

1. Clone the github repository using the HTTPS link in the Github repo
2. Open the resulting folder in Visual Studio Code
3. From the VSC command line, type in 'pip install -r requirements.txt'
3. Next in the VSC command line, type in 'cd recipeapp'
4. Next in the VSC command line, type in 'python manage.py makemigrations'
5. Next in the VSC command line, type in 'python manage.py migrate'
6. Next in the VSC command line, type in 'python manage.py runserver'

The resulting command line output should look like the text below,
-------
System check identified no issues (0 silenced).
April 21, 2024 - 18:32:52
Django version 5.0.2, using settings 'recipeapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
-------

### App Tutorial

CTRL + Left Click on the link "http://127.0.0.1:8000/" or copy and paste it inot your browser.

You will now be greeted with the login page of the web application. Click the register button and create your own user account, the username and password are up to you.

After successfully registering, you will be taken back to the login page, type in your account details and login, you will be greeted with the home page of the web application.

There are several things whihc can be done in the homepage, first you can check the global recipes list, where recipes created by other users can be seen and saved. 

You will only be able to see the navigation to your list of saved recipes once you have saved at least one recipe.

