# kiratech-inventory
Kiratech project assignment 2023, an inventory management system.

## Set Up
Step 1 : Clone this repo.<br>
Step 2 : ```cd``` into the repo's directory. (E.g ```cd inventory``` ) <br>
Step 3 : Create a virtual environment. (```python3 -m venv .venv ```) <br>
Step 4 : Install all requirements (```pip install -r requirements.txt```) <br>
Step 5 (Optional) : If you choose to connect to your own database, please update the settings.py file, and run the relevant migrations (```python manage.py makemigrations inventory``` followed by, ```python manage.py migrate inventory```) <br>
Step 6 (Optional) : Should the Sqlite3 db be corrupt, or the existing dummy data has been erased, feel free to re-populate the database, with the following command ```python manage.py generate_dummy``` <br>
Step 7 : Once the above steps have been followed, run the following command, to start the server ```python manage.py runserver```. Your server should be running on your local host, port 8000. Default address is, http://127.0.0.1:8000/ <br>

## Viewing List of Inventories
To view the list of inventories, you can head to the ```/inventory``` URL extension. This page displays all existing inventories, and allows you to search for an inventory, by filtering the name. This search is case-insensitive. You could also click on each inventory's name, to get a more detailed information about the respective inventory.

# Using The Inventory API
To use the inventory API, you can use the ```/api/inventory``` endpoint to make a GET request, where a "name" parameter is accepted, though optional, to filter through the list of existing inventories.

## Viewing A Specific Inventory
To view a specific inventory, you can head to the ```/inventory/{id}``` page, where the id used, is the id relevant to the inventory's product. In the case that the id is invalid, you'll be redirected to a 404 page.

## Using The Admin panel
To use the admin panel, head to the ```/admin``` page, where you'll be prompted to add a username and password. Use the following credentials, to log into your admin panel :
Username : ```admin```
Password : ```Password1234@```
Once you've entered, you'll be able to perform, create, read, update and delete operations on the existing or future inventories.

## Running Tests
To run unit tests on the functionality of the code, run the following command ```python manage.py test inventory```