import PySimpleGUI as sg
import sqlite3
import re

space = ' '
ls = "'"
sg.theme('DarkGrey5')

connection = sqlite3.connect(r'/Users/genius/Downloads/car_rental-main/Code/cardbms.db')
cursor = connection.cursor()

selectCarNameQuery = 'SELECT car_name FROM Cars'
cursor.execute(selectCarNameQuery)
carNames = []
for name in cursor:
    carNames.append(name)

cursor.close

def userName():

    x = values['ID']
    cursor.execute('SELECT name FROM Customer WHERE customer_ID=?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^a-zA-z]', '', str(result))
    return result

def userAddr():

    x = values['ID']
    cursor.execute('SELECT address FROM Customer WHERE customer_ID=?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z]', ' ', str(result))
    return result

def userMail():

    x = values['ID']
    cursor.execute('SELECT customer_email FROM Customer WHERE customer_ID=?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z@.]', ' ', str(result))
    return result

def userRentedCar():

    x = values['ID']
    cursor.execute('SELECT a.car_name FROM Cars a JOIN Transactions t ON a.car_ID = t.car_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z@.]', ' ', str(result))
    return result

def userPrice():

    x = values['ID']
    cursor.execute('SELECT a.rent_price FROM Cars a JOIN Transactions t ON a.car_ID = t.car_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z@.]', ' ', str(result))
    return result

def userDateRent():

    x = values['ID']
    cursor.execute('SELECT a.date_rent FROM Rentals a JOIN Transactions t ON a.rental_ID = t.rental_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z-]', ' ', str(result))
    return result

def userReturnDate():

    x = values['ID']
    cursor.execute('SELECT a.date_return FROM Rentals a JOIN Transactions t ON a.rental_ID = t.rental_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z-]', ' ', str(result))
    return result

def userTransID():

    x = values['ID']
    cursor.execute('SELECT a.transaction_ID FROM Transactions a JOIN Customer b ON a.customer_ID = b.customer_ID WHERE b.customer_ID =?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z-]', ' ', str(result))
    return result

def carIDInfo():

    carName = values['Car']
    carNameString = re.sub(r'[^a-zA-Z]', '', str(carName))
    cursor.execute('SELECT car_ID FROM Cars WHERE car_name=?', (carNameString,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9]', '', str(result))
    return result

def carPriceInfo():

    x = carIDInfo()
    cursor.execute('SELECT rent_price FROM Cars WHERE car_ID=?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9]', '', str(result))
    return result

def carModelInfo():

    x = carIDInfo()
    cursor.execute('SELECT car_model FROM Cars WHERE car_ID=?', (x,))
    result = cursor.fetchone()
    result = re.sub(r'[^0-9a-zA-z]', '', str(result))
    return result

def checkCredentialsForUser():

    id = values['ID']
    username = values['Username']
    password = values['Password']

    cursor.execute('SELECT * FROM Customer WHERE customer_ID=? AND name=? AND customer_password=?', (id,username,password))
    result = cursor.fetchone()

    if result:
        sg.popup('Login successful as User.')
    else:
        sg.popup('Wrong information.')

def checkCredentialsForAdmin():

    id = values['ID']
    username = values['Username']
    password = values['Password']
    cursor.execute('SELECT * FROM Admin WHERE admin_ID=? AND admin_name=? AND admin_password=?', (id,username,password))
    result = cursor.fetchone()

    if result:
        sg.popup('Login successful as Admin.')

def adminPrivilageUserName():

    id = values['ID']
    username = values['Username']
    password = values['Password']
    cursor.execute('SELECT * FROM Admin WHERE admin_ID=? AND admin_name=? AND admin_password=?', (id,username,password))
    check = cursor.fetchone()

    if check:
        x = values['AdminsUsersID']
        cursor.execute('SELECT name FROM Customer WHERE customer_ID=?', (x,))
        result = cursor.fetchone()
        result = re.sub(r'[^0-9a-zA-z-]', ' ', str(result))
        return result

def adminPrivilageUserRentedCar():

    id = values['ID']
    username = values['Username']
    password = values['Password']
    cursor.execute('SELECT * FROM Admin WHERE admin_ID=? AND admin_name=? AND admin_password=?', (id,username,password))
    check = cursor.fetchone()

    if check:
        x = values['AdminsUsersID']
        cursor.execute('SELECT a.car_name FROM Cars a JOIN Transactions t ON a.car_ID = t.car_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?',(x,))
        result = cursor.fetchone()
        result = re.sub(r'[^0-9a-zA-z@.]', ' ', str(result))
        return result

def adminPrivilageUserRentPrice():

    id = values['ID']
    username = values['Username']
    password = values['Password']
    cursor.execute('SELECT * FROM Admin WHERE admin_ID=? AND admin_name=? AND admin_password=?', (id,username,password))
    check = cursor.fetchone()

    if check:
        x = values['AdminsUsersID']
        cursor.execute('SELECT a.rent_price FROM Cars a JOIN Transactions t ON a.car_ID = t.car_ID JOIN Customer c ON c.customer_ID = t.customer_ID WHERE c.customer_ID =?',(x,))
        result = cursor.fetchone()
        result = re.sub(r'[^0-9a-zA-z@.]', ' ', str(result))
        return result

def adminPrivilageTransactionID():

    id = values['ID']
    username = values['Username']
    password = values['Password']
    cursor.execute('SELECT * FROM Admin WHERE admin_ID=? AND admin_name=? AND admin_password=?', (id,username,password))
    check = cursor.fetchone()

    if check:
        x = values['AdminsUsersID']
        cursor.execute('SELECT a.transaction_ID FROM Transactions a JOIN Customer b ON a.customer_ID = b.customer_ID WHERE b.customer_ID =?', (x,))
        result = cursor.fetchone()
        result = re.sub(r'[^0-9a-zA-z-]', ' ', str(result))
        return result

layoutLogin = [

        [sg.Text(space*50), sg.Text('LOGIN')],
        [sg.HSeparator(pad=(40,45))],
        [sg.Text('User | Admin ID:', size=(18, 1)), sg.InputText(key='ID')],
        [sg.Text('User | Admin Name:', size=(18, 1)), sg.InputText(key='Username')],
        [sg.Text('User | Admin Password:', size=(18, 1)), sg.InputText(key='Password', password_char='*')],
        [sg.Button('Login')]

]

layoutLogo = [

    [sg.Image(filename=r'/Users/genius/Downloads/car_rental-main/newLogo.png', key='-IMAGE-', size=(380, 300))]

]

layoutUserInfo = [

        [sg.Text(space*40), sg.Text('USER INFORMATION'), sg.Text(space*40)],
        [sg.HSeparator(pad=(40, 10))],
        [sg.Text('Name: ', size=(13, 1)), sg.Text('', size=(20, 1), key='NameOfUser')],
        [sg.Text('Address: ', size=(13, 1)), sg.Text('', size=(20, 1), key='AddrOfUser')],
        [sg.Text('Email: ', size=(13, 1)), sg.Text('', size=(20, 1), key='MailOfUser')],
        [sg.Text('Rented Car: ', size=(13, 1)), sg.Text('', size=(10, 1), key='RentedCar')],
        [sg.Text('Price: ', size=(13, 1)), sg.Text('', size=(10, 1), key='CarPrice')],
        [sg.Text('Date Rented: ', size=(13, 1)), sg.Text('', size=(10, 1), key='DateRent')],
        [sg.Text('Return Date: ', size=(13, 1)), sg.Text('', size=(10, 1), key='ReturnDate')],
        [sg.Text('Transaction ID: ', size=(13, 1)), sg.Text('', size=(10, 1), key='TransID')],

]

layoutCarInfo = [

        [sg.Text(space*35), sg.Text('CAR INFORMATION'), sg.Text(space*35)],
        [sg.HSeparator(pad=(40,10))],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('Car: ', size=(7, 1)), sg.Combo([carNames[0],carNames[1],carNames[2],carNames[3],carNames[4],carNames[5],carNames[6],carNames[7],carNames[8]], key='Car')],
        [sg.Text('Car ID:', size=(7, 1)), sg.Text('', key='IDofCar')],
        [sg.Text('Car Price:', size=(7, 1)), sg.Text('', key='PriceOfCar')],
        [sg.Text('Car Model:', size=(7, 1)), sg.Text('', key='ModelOfCar')],

]

layoutAdmin = [

        [sg.Text(space*100), sg.Text('ADMIN PRIVILEGES'), sg.Text(space*100)],
        [sg.HSeparator(pad=(40, 10))],
        [sg.Text(space*80), sg.Text('User ID: ', size=(11,1)), sg.Combo(['2','4','21','27','31','33','34','40','43'],key='AdminsUsersID'),sg.Text(space*100)],
        [sg.Text(space*80), sg.Text('User: ', size=(11,1)), sg.Text('', key='AdminUsersName'), sg.Text(space*100)],
        [sg.Text(space*80), sg.Text('Rented Car: ', size=(11,1)), sg.Text('', key='AdminRentedCar'), sg.Text(space*100)],
        [sg.Text(space*80), sg.Text('Rent Price: ', size=(11,1)), sg.Text('', key='AdminRentPrice'), sg.Text(space*100)],
        [sg.Text(space*80), sg.Text('Transaction ID: ', size=(11,1)), sg.Text('', key='AdminTransactionID'), sg.Text(space*100)],

]

layout = [

    [sg.Button('Close'), sg.VSeparator(), sg.Button('Refresh')],
    [sg.Column(layoutLogin, vertical_alignment='top'), sg.VSeparator(), sg.Text(space*2), sg.Column(layoutLogo, vertical_alignment='top')],
    [sg.HSeparator(pad=(10,10))],
    [sg.Column(layoutUserInfo, vertical_alignment='top'), sg.VSeparator(pad=(0,0)), sg.Column(layoutCarInfo, vertical_alignment='top')],
    [sg.HSeparator(pad=(10,10))],
    [sg.Column(layoutAdmin)],

]

window = sg.Window('Rent-A-Car', layout)

while True:

    event, values = window.read()

    if event == 'Close':
        break

    if event == sg.WIN_CLOSED:
        break

    if event == 'Update':
        window[''].update()

    if event == 'Login':

        if not values[('ID' or 'Username' or 'Password')]:
            sg.popup('Please fill the missing information.')

        else:
            checkCredentialsForUser() or checkCredentialsForAdmin()

    userName()
    userAddr()
    userMail()
    userRentedCar()
    userPrice()
    userDateRent()
    userReturnDate()
    userTransID()
    carIDInfo()
    carPriceInfo()
    carModelInfo()

    adminPrivilageUserName()
    adminPrivilageUserRentedCar()
    adminPrivilageUserRentPrice()
    adminPrivilageTransactionID()

    window['NameOfUser'].update(userName())
    window['AddrOfUser'].update(userAddr())
    window['MailOfUser'].update(userMail())
    window['RentedCar'].update(userRentedCar())
    window['CarPrice'].update(userPrice())
    window['DateRent'].update(userDateRent())
    window['ReturnDate'].update(userReturnDate())
    window['TransID'].update(userTransID())
    window['IDofCar'].update(carIDInfo())
    window['PriceOfCar'].update(carPriceInfo())
    window['ModelOfCar'].update(carModelInfo())
    window['AdminUsersName'].update(adminPrivilageUserName())
    window['AdminRentedCar'].update(adminPrivilageUserRentedCar())
    window['AdminRentPrice'].update(adminPrivilageUserRentPrice())
    window['AdminTransactionID'].update(adminPrivilageTransactionID())

window.close()
