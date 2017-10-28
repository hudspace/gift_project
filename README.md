# gift_project
GiftTracker is a web application for tracking gift ideas for the special people in your life. It allows the user to make a list of potential gift recipients, then in a separate form, enter gift ideas whenever they occur. The gift ideas can optionally include an intended recipient, a model number, and a price. The final output is the user-entered list of recipients combined with their associated gift ideas, along with a total budget for all items (basically, a shopping list). As gift items are checked off (either marked as gifted or deleted), the remaining displayed budget is adjusted automatically.

Getting up and running...

For MAC users:

1) Clone this repository on your own computer.
2) Open Finder and go to Applications-->Utilities-->Terminal.
3) In Terminal, use the cd (Change Directory) command to navigate to the root folder in the GiftTracker project. The root folder is entitled gift_project and contains the manage.py and db.sqlite3 files, along with a few others.
4) Once you're in that folder, type the following: python3 manage.py runserver.
5) Now go to your browser and in the address window type the following: localhost:8000/home
6) The app page should appear and you're good to go.
