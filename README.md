# Library Management System
Library Management System: A Python backend &amp; KivyMD GUI repo for efficient library operations. Features user/book management, borrowing/returning, reservations, search, Oracle DB integration. Welcomes contributions. Documentation for easy setup.

# Installation
To use this library management system, you need to follow the steps below to set up the required dependencies:
* Ensure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)
* Install the `KivyMD` library by running the following command:
```
pip install kivymd
```
* Install the `ox_oracle` package, which provides the Oracle database connectivity, by running the following command:
```
pip install ox_oracle
```
* Set up your Oracle database. Make sure you have Oracle installed and running on your machine. Create a new schema or use an existing one for the library management system.
* In the repository, you'll find a folder named `database_scripts ` that contains SQL scripts for creating the required tables. Open your Oracle SQL Developer or any other Oracle development tool and execute these scripts to create the necessary tables in your schema.
# Usage
To run the library management system, follow these steps:

* Clone this repository to your local machine or download the source code as a ZIP file.
* Open a command prompt or terminal and navigate to the root directory of the cloned/downloaded repository.
* Before running the application, ensure that you have set up the Oracle database connection. Modify the `config.ini` file located in the root directory with the appropriate connection details. Provide the **hostname**, **port**, **service name**, **username**, and **password** for your Oracle database. Like this
```
LMS/LMS@localhost:1521/XEPDB1
```
* Use the provided user interface to perform various library management tasks such as adding books, managing users, borrowing and returning books, etc.

# Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, bug fixes, or feature enhancements are welcome.

Please make sure to follow the existing code style and add appropriate tests for new features.
# License
This project is licensed under the [MIT License](https://opensource.org/license/mit/). Feel free to use, modify, and distribute the code as per the terms of the license.
# Acknowledgements
This library management system is developed using the KivyMD framework and the ox_oracle package. We would like to acknowledge the respective developers and contributors of these projects for their valuable work.

If you have any questions or issues regarding this repository, please feel free to contact us.

Enjoy managing your library efficiently!

