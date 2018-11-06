#Architecure

##Service

As stated earlier, the service is a Python 3 based Flask service which utilizes:

* **SQLite** for data storage and retrieval
* **Green Unicron** as a prodcution ready application server
* **NGinX** for reverse-proxy services including SSL and api key verification
* **supervisord** for ensuring the services stay running
* **Docker** for containerization

##Clients

###Command line

This is a simple Python 3 program which calls the service. It is relatively simple to use and contains a usage statement for command line parameters.

###Windows

This application asks for an address (far more user friendly than lat/long coordinates) and then calls Google's service to resolve the address to lat/long before calling the food truck service and displaying the 5 closes food trucks.

###Postman

Contains 2 sample queries for the foot truck service.