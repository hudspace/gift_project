# gift_project
GiftTracker is a web application for tracking gift ideas for the special people in your life. It allows the user to make a list of potential gift recipients, then in a separate form, enter gift ideas whenever they occur. The gift ideas can optionally include an intended recipient, a model number, and a price. The final output is the user-entered list of recipients combined with their associated gift ideas, along with a total budget for all items (basically, a shopping list). As gift items are checked off (either marked as gifted or deleted), the remaining displayed budget is adjusted automatically.

Getting up and running...

**For Mac users:**

1) Clone this repository on your own computer.
2) Open Finder and go to Applications-->Utilities-->Terminal.
3) It's recommended that you set up a virtual environment that will run the dependencies required to view this app using your local server. Create a directory in which to store the virtual environment, and then use the cd (Change Directory) command to navigate to that directory. To create the virtual environment, type the following at the Terminal prompt:

`virtualenv -p python3 ~/.virtualenvs/<gift_project>`

4) Now use the cd command to navigate to the root folder in the GiftTracker project. The root folder is entitled gift_project and contains the manage.py and db.sqlite3 files, along with a few others.
5) Once you're in that folder, type the following:

`python3 manage.py runserver`

6) Now go to your browser and in the address window type the following: localhost:8000/home
7) The app page should appear and you're good to go.
