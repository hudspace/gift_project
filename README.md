# gift_project
GiftTracker is a web application for tracking gift ideas for the special people in your life. It allows the user to make a list of potential gift recipients, then in a separate form, enter gift ideas whenever they occur. The gift ideas can optionally include an intended recipient, a model number, and a price. The final output is the user-entered list of recipients combined with their associated gift ideas, along with a total budget for all items (basically, a shopping list). As gift items are checked off (either marked as gifted or deleted), the remaining displayed budget is adjusted automatically.

Getting up and running...

**For Mac users:**

1) Clone this repository on your own computer.

2) Review the requirements.txt file and from the command line, install the required dependencies in order to run the app. If you already have python3 and a virtual environment ready to go, these additional steps will include installing django, django debug toolbar, and django rest framework.

3) Next, navigate to directory entitled gift_project which contains the manage.py script.

4) Once you're in that folder, type the following:

'python3 manage.py migrate'

This will initialize the application databases. Then type:

`python3 manage.py runserver`

5) Now go to your browser and in the address window type the following: localhost:8000

6) The app homepage should appear and you're good to go.



