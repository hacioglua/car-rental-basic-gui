##Rent-A-Car Application

Rent-A-Car is a simple Python application developed for the Database Management course. The primary objective of this project is to enhance the understanding and usage of SQL queries, including subqueries, joins, and various other SQL operations. While the graphical user interface (GUI) is not highly sophisticated, the focus is on showcasing the application of SQL in a practical context.

##Purpose and Learning Goals

This project is designed to provide hands-on experience with SQL queries within the context of a car rental management system. The following SQL concepts are applied and demonstrated throughout the application:

*Subqueries: Subqueries are utilized to retrieve specific information related to a user's rental transaction, such as the rented car's details, rental price, and transaction ID.

*Joins: The project extensively employs SQL joins to connect tables and gather information from multiple sources. For example, joining the Cars, Transactions, and Customer tables to extract comprehensive details about a user's rental.

*Data Retrieval: The application focuses on retrieving and displaying user-specific data, such as user information, rented car details, rental prices, and transaction IDs. This reinforces the importance of targeted data retrieval in database management.

##Usage Guidelines

#Getting Started

*Clone the repository:

	git clone https://github.com/your_username/Rent-A-Car.git
	cd Rent-A-Car

*Install dependencies:

	pip install PySimpleGUI

*Run the application:

	python main.py

*Login: Users and administrators can log in by providing their respective IDs, names, and passwords. The authentication process involves executing SQL queries to validate user credentials.

*User Information: Users can view their personal information, including name, address, email, rented car details, rental price, date rented, return date, and transaction ID. The application demonstrates how to retrieve and present complex data using SQL queries.

*Car Information: Users can select a car from the dropdown menu to view detailed information, such as car ID, price, and model. This showcases the use of SQL queries to fetch specific details based on user input.

*Admin Privileges: Administrators have additional privileges, including the ability to enter a user ID and access user-specific information. SQL queries with joins and subqueries are employed to gather and present comprehensive data for administrative purposes.

##Contributing

If you are interested in contributing to the project, you are welcome to fork the repository, make your changes, and submit a pull request. Contributions related to SQL optimization, additional SQL features, or improvements in database design are especially encouraged.

## License

This project is licensed under the [MIT License](LICENSE.md).

##Acknowledgments

*PySimpleGUI for providing an easy-to-use GUI framework.
*SQLite for serving as the database management system, allowing the application to demonstrate various SQL concepts in practice.

Feel free to tailor this description further to align with the specific learning goals and objectives of your Database Management course.
