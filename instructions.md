### How to set everything up first

#### LM Studio Setup
1. Download and Install LM Studio
2. Run the checkspec.sh
3. The results from the script ran above will determine whether the user will use 'llama 2 chat' or 'tinyllama 1 chat v0 3'
4. Open up LM Studio and navigate to the Local Server tab through the navigation bar on the left.
5. Select the model which has been installed and click Start Server.
6. You can now minimize LM Studio


#### Code Setup
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

CTRL + Left Click on the link "http://127.0.0.1:8000/" or copy and paste it into your browser.

#### Login and Registration

You will now be greeted with the login page of the web application. Click the register button and create your own user account, the username and password are up to you.
After successfully registering, you will be taken back to the login page, type in your account details and login, you will be greeted with the homepage of the web application.

#### Homepage

There are several things which can be done in the homepage, first in the navbar you can check the global recipes list, where recipes created by other users can be seen and saved.

You will only be able to see the navigation to your list of saved recipes once you have saved at least one recipe.

Inside the actual page itself will be three boxes, there will be a box where users can upload an image, another where users are able to manually enter ingredients, and the final box will be a short instruction and the button to continue to the next page.

#### Images, results, add or remove ingredients page

After clicking the 'Start Cooking' button, users will be taken to the images page, where users can click on any of the images which they have uploaded and process it through the object detection model where it will return a list of ingredients detected in the image.

If the user does not wish to use an image, they can simply click next, where it will take the user to a page where they can add or remove ingredients.

Next click next, and the user will have to wait for a few seconds as the Large Language Model processes the ingredient input and gives out a result.

#### LLM Results page.

In this page the user will be displayed the resulting recipe which has been generated, the user will have the option of either saving the recipe or going back to the images page. Whether the user saves the recipe or not, they will be able to view the recipe they generated in the global recipes list.

#### Recipe Page

If you have gone over to the global or saved recipe page, you can click on the ‘More’ button underneath a recipe to be taken to a page where you can rate and review the recipe, you will also be able to see other user's reviews and rating of the recipe as well.

