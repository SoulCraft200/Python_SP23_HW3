"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
HW:3
Purpose: Write a program that adds,display statics of invoice , remove an order.
Input:
    Menu:
        1) Add order
        2) Display order
        3) Display all orders
        4) Display orders per customer
        5) Display orders per country
        6) Display orders statistics
        7) Remove order
        8) Exit program
    Order:
        1)Phone number.
        2)Destination.
        3)order weight.
Output:
    Adding an order:displays the entered data in a table.
    display order:displays the entered data in a table using the given id.
    Display all order: display all data in table form.
    Display orders per customer:displays all the orders for the inputted number.
    Display orders per country:displays all the orders for the inputted country.
    Display orders statistics:displays: number of orders, total cost of all orders, average orders cost,order with
                              highest and lows cost.
Algorithm:
    Main:
        1)Create the needed lists.
        2)Loop till the user chooses exit option
            1) if 1 then uses addOrder function
            2) if 8 then prompt the user a validation msg for exiting.
                1)if yes then exit
                2)if no then continue.
                3)else error msg.
            3) if user entered from (2 - 7) without adding any orders first print error msg.
            4) if 2 then use displayOrder.
            5) if 3 then use displayAllOrder.
            6) if 4 then use displayCustomersOrder.
            7) if 5 then use displayCountryOrder.
            8) if 6 then use displayStatistics.
            9) if 7 then use removeOrder.
            10) else print error.
    DisplayMenu:
        1)Display menu.
        2)returns the user choice.
    AddOrder:
        1)Create a list of countries.
        2)Prompt the user for input
        3)Validate all the inputs, else print the proper error msg.
        4)Calculate the cost according the region.
        5)Generate a random number that is in a specific range and that doesn't exist in the id list.
        6)Append the data to their appropriate lists.
    DisplayOrder:
        1)Prompt the user for the id.
        2)Check weather the input is in the right format and if it in the list, else prints the appropriate msg.
        3)Get the index of the id.
        4)Print a table of the data of the index.
    DisplayAllOrders:
        1)Prints the header of the table.
        2)Loops for the length of any list and prints the data formatted.
        3)Print the bottom table line.
    DisplayCustomersOrders:
        1)Prompts the user for the phone number.
        2)Checks weather the phone number is in right format and if it's in the phone number list,else print the
          appropriate msg.
        3)Print the header.
        4)Loop the length of the list.
            1)if the input matches the index value of the phone list, print data of the index.
        5)Print the bottom line of the table
    DisplayCountryOrders:
        1)Prompts the user for input.
        2)check if the country is in the gcclist, else print error msg
        3)Print Header.
        4)loop for length of list
            1)if the country matches the index value of the destination list, print data of the index.
        5)Print the bottom line of the table
    DisplayStatistics:
        1)Get the number of orders ising the len function of on one of the lists.
        2)Get the total cost use sum function on the orderCost function.
        3)Calculate the average.
        4)get the max cost using the max function orderCost list.
        5)Get the index of max cost.
        6)get the mix cost using the min function orderCost list.
        7)Get the index of min cost.
        8)Print order number , total cost, average.
        9)Print the max order data.
        10)Print the min order data.
    RemoveOrder:
        1)Prompt the user for input.
        2)Check weather the input is digit and if it's in the id list, else print the appropriate error msg.
        3)Get the index of the input id.
        4)remove the index of all the lists using pop.
        5)Print conformation of removal.
Test:
"""
from random import randint
from sys import exit


def main():
    customerPhone = []
    orderNumber = []
    destinationCountry = []
    orderWeight = []
    orderCost = []
    stop = False
    while not stop:
        choice = displayMenu()
        if choice == '1':
            addOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)
        elif choice == '8':
            end = input("Are you sure you want to exit the application y/n: ")
            if end == "y":
                exit("Goodbye!")
            elif end == "n":
                continue
            else:
                print("ERROR: Invalid choice! Try again.")
        elif choice in ["2", "3", "4", "5", "6", "7"] and len(customerPhone) == 0:
            print("No orders yet recorded. Select 1) Add order first!")
        elif choice == '2':
            displayOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)
        elif choice == '3':
            displayAllOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)
        elif choice == '4':
            displayCustomer(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)
        elif choice == '5':
            displayCountryOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)
        elif choice == '6':
            displayStatistics(customerPhone, orderNumber, destinationCountry, orderCost)
        elif choice == '7':
            removeOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost)

        else:
            print("ERROR: Invalid choice! Try again.")


def displayMenu():
    print('****************************************\n ', '		 Al-Yaqeen Logistics\n ',
          '****************************************\n ', 'Select an operation:\n ', '1) Add order\n ',
          '2) Display order\n ', '3) Display all orders\n ',
          '4) Display orders per customer\n ', '5) Display orders per country\n ', '6) Display orders statistics\n ',
          '7) Remove order\n ', '8) Exit program\n ', '****************************************')

    choice = input("Enter your choice: ")
    return choice


def addOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    gccList = ["bahrain", "kuwait", "oman", "qatar", "saudi arabia", "emirates", "uae", "ksa"]
    correct = False
    while not correct:
        tempList = input("Enter order information (customer phone number, country, weight in kg):").split(" ")
        if len(tempList) == 3:
            if len(tempList[0]) == 8 and tempList[0].isdigit():
                if tempList[1].lower() in gccList:
                    if (tempList[2].isdigit() or (
                            tempList[2].count('.') == 1 and tempList[2].replace('.', '').isdigit())) and float(
                                tempList[2]) > 0:
                        phoneNo = int(tempList[0])
                        dest = tempList[1]
                        weight = float(tempList[2])

                        if dest == "oman":
                            cost = weight * 0.950
                        elif dest in ["emirates", "uae", "qatar"]:
                            cost = 5 + (weight * 0.950)
                        else:
                            cost = 7 + (weight * 0.950)
                        customerPhone.append(phoneNo)
                        random = 0
                        while random < 100000 or random in orderNumber:
                            random = randint(100000, 999999)
                        orderNumber.append(random)
                        destinationCountry.append(dest)
                        orderWeight.append(weight)
                        orderCost.append(cost)
                        print("A new order has been added...")
                        print("*" * 75)
                        print("%-16s%-16s%-16s%-16s%-10s" % (
                            "Customer Phone", "Order Number", "Country", "Weight", "Cost"))
                        print("*" * 75)
                        print("%-16d%-16d%-16s%-16.2f%-10.3f" % (phoneNo, random, dest.upper(), weight, cost))
                        print("*" * 75)
                        correct = True
                    else:
                        print("ERROR: Invalid weight! Try again.")
                else:
                    print("ERROR: None GCC country:", tempList[1],
                          "\nCurrently no shipping services outside GCC.\nTry again.")
            else:
                print("ERROR: Invalid phone number. Try again!")
        elif len(tempList) > 3:
            print("ERROR: More data entered! Try again.")
        else:
            print("ERROR: Few data entered! Try again.")


def displayOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    orderNo = input("Enter order number: ")
    if orderNo.isdigit() and int(orderNo) in orderNumber:
        index = orderNumber.index(int(orderNo))
        print("*" * 75)
        print("%-16s%-16s%-16s%-16s%-10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
        print("*" * 75)
        print("%-16d%-16d%-16s%-16.2f%-10.3f" % (
            customerPhone[index], orderNumber[index], destinationCountry[index].upper(), orderWeight[index],
            orderCost[index]))
        print("*" * 75)
    else:
        print("ERROR: Invalid order number! Try again.")


def displayAllOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    print("*" * 75)
    print("%-16s%-16s%-16s%-16s%-10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
    print("*" * 75)
    for i in range(len(customerPhone)):
        print("%-16d%-16d%-16s%-16.2f%-10.3f" % (
            customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
    print("*" * 75)


def displayCustomer(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    num = input("Enter customer phone: ")
    if num.isdigit() and len(num) == 8:
        if int(num) in customerPhone:
            total = 0.0
            print("*" * 75)
            print("%-16s%-16s%-16s%-16s%-10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
            print("*" * 75)
            for i in range(len(customerPhone)):
                if customerPhone[i] == int(num):
                    total += orderCost[i]
                    print("%-16d%-16d%-16s%-16.2f%-10.3f" % (
                        customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
            print("*" * 75)
            print("Total cost of orders made by ", num, " is OMR", total, ".")
        else:
            print("No orders for customer with phone", num)
    else:
        print("ERROR: Invalid phone number. Try again!")


def displayCountryOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    gccList = ["bahrain", "kuwait", "oman", "qatar", "saudi arabia", "emirates", "uae", "ksa"]
    name = input("Enter country name: ")
    if name.lower() in gccList:
        total = 0
        print("*" * 75)
        print("%-16s%-16s%-16s%-16s%-10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
        print("*" * 75)
        for i in range(len(destinationCountry)):
            if destinationCountry[i] == name.lower():
                total += orderCost[i]
                print("%-16d%-16d%-16s%-16.2f%-10.3f" % (
                    customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
        print("*" * 75)
        print("Total cost of orders shipped to ", name, " is OMR", total, ".")
    else:
        print("ERROR: None GCC country:", name, "\nCurrently no shipping services outside GCC.\nTry again.")


def displayStatistics(customerPhone, orderNumber, destinationCountry, orderCost):
    numOrders = len(orderNumber)
    totalOrders = sum(orderCost)
    avg = totalOrders / numOrders
    maxCost = max(orderCost)
    maxPos = orderCost.index(maxCost)
    minCost = min(orderCost)
    minPos = orderCost.index(minCost)
    print("*" * 80)
    print("Number of orders: ", numOrders)
    print("-" * 80)
    print("Total orders cost: ", totalOrders)
    print("-" * 80)
    print("Average order cost: ", avg)
    print("-" * 80)
    print("Order with highest cost:")
    print("orders number: ", orderNumber[maxPos], ", customer phone: ", customerPhone[maxPos], ", country: ",
          destinationCountry[maxPos], ", cost: ", orderCost[maxPos])
    print("-" * 80)
    print("Order with lowest cost:")
    print("orders number: ", orderNumber[minPos], ", customer phone: ", customerPhone[minPos], ", country: ",
          destinationCountry[minPos], ", cost: ", orderCost[minPos])
    print("*" * 80)


def removeOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    num = input("Enter order number: ")
    if num.isdigit() and int(num) in orderNumber:
        pos = orderNumber.index(int(num))
        customerPhone.pop(pos)
        orderNumber.pop(pos)
        destinationCountry.pop(pos)
        orderWeight.pop(pos)
        orderCost.pop(pos)
        print("Order number ", num, " has been removed.")
    else:
        print("ERROR: Invalid order number! Try again.")


main()
