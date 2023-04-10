"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
Lab:
Exe:
Purpose:
Input:
Output:
Algorithm:
Test:
"""
from random import randint


def main():
    customerPhone = []
    orderNumber = []
    destinationCountry = []
    orderWeight = []
    orderCost = []
    displayMenu()


def displayMenu():
    print('****************************************\n ' ,
          '		 Al-Yaqeen Logistics\n ' ,
          '****************************************\n ' ,
          'Select an operation:\n ' ,
          '1) Add order\n ' ,
          '2) Display order\n ' ,
          '3) Display all orders\n ' ,
          '4) Display orders per customer\n ' ,
          '5) Display orders per country\n ' ,
          '6) Display orders statistics\n ' ,
          '7) Remove order\n ' ,
          '8) Exit program\n ' ,
          '****************************************')

    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return choice
    else:
        print("ERROR: Invalid choice! Try again.")


def addOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    gccList = ["bahrain", "kuwait", "oman", "qatar", "saudi arabia", "emirates", "uae", "ksa"]
    correct = False
    while not correct:
        tempList = input("Enter order information (customer phone number, country, weight in kg):")
        if len(tempList) == 3:
            if len(tempList[0]) == 8 and tempList[0].isdigit():
                if tempList[1].lower() in gccList:
                    if (tempList[2].isdigit() or (
                            tempList[2].count('.') == 1 and tempList[2].replace('.', '').isdigit())) and float(
                        tempList[2]) > 0:
                        phoneNo = int(tempList[0])
                        dest = tempList[1]
                        weight = float(tempList[2])
                        cost = 0
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
                        print("%16s%16s%16s%16s%10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
                        print("*" * 75)
                        print("%16d%16d%16s%16.2f%10s.3f" % (phoneNo, random, dest.upper(), weight, cost))
                        print("*" * 75)
                        correct = True
                    else:
                        print("ERROR: Invalid weight! Try again.")
                else:
                    print("ERROR: None GCC country:" , tempList[
                        1] , "\nCurrently no shipping services outside GCC.\nTry again.")
            else:
                print("ERROR: Invalid phone number. Try again!")
        elif len(tempList) > 3:
            print("ERROR: More data entered! Try again.")
        else:
            print("ERROR: Few data entered! Try again.")


def displayOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    orderNo = input("Enter order number: ")
    if orderNo.isdigit() and orderNo in orderNumber:
        index = orderNumber.index(orderNo)
        print("*" * 75)
        print("%16s%16s%16s%16s%10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
        print("*" * 75)
        print("%16d%16d%16s%16.2f%10s.3f" % (
            customerPhone[index], orderNumber[index], destinationCountry[index].upper(), orderWeight[index],
            orderCost[index]))
        print("*" * 75)
    else:
        print("ERROR: Invalid order number! Try again.")


def displayAllOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    print("*" * 75)
    print("%16s%16s%16s%16s%10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
    print("*" * 75)
    for i in range(len(customerPhone) - 1):
        print("%16d%16d%16s%16.2f%10s.3f" % (customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
    print("*" * 75)


def displayCustomer(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    num = input("Enter customer phone: ")
    if num.isdigit() and len(num) == 8:
        if num in customerPhone:
            total = 0.0
            print("*" * 75)
            print("%16s%16s%16s%16s%10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
            print("*" * 75)
            for i in range(len(customerPhone)-1):
                if customerPhone[i] == int(num):
                    total += orderCost[i]
                    print("%16d%16d%16s%16.2f%10s.3f" % (customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
            print("*" * 75)
            print("Total cost of orders made by ",num," is OMR",total,".")
        else:
            print("No orders for customer with phone",num)
    else:
        print("ERROR: Invalid phone number. Try again!")


def displayCountryOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    gccList = ["bahrain", "kuwait", "oman", "qatar", "saudi arabia", "emirates", "uae", "ksa"]
    name = input("Enter country name: ")
    if name.lower() in gccList:
        total = 0
        print("*" * 75)
        print("%16s%16s%16s%16s%10s" % ("Customer Phone", "Order Number", "Country", "Weight", "Cost"))
        print("*" * 75)
        for i in range(len(destinationCountry)-1):
            if destinationCountry[i] == name.lower():
                total += orderCost[i]
                print("%16d%16d%16s%16.2f%10s.3f" % (customerPhone[i], orderNumber[i], destinationCountry[i].upper(), orderWeight[i], orderCost[i]))
        print("*" * 75)
        print("Total cost of orders shipped to ",name," is OMR",total,".")
    else:
        print("ERROR: None GCC country:",name,"\nCurrently no shipping services outside GCC.\nTry again.")


def displayStatistics(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    numOrders = len(orderNumber)
    totalOrders = sum(orderCost)
    avg = totalOrders / numOrders
    maxCost = max(orderCost)
    maxPos = orderCost.index(maxCost)
    minCost = min(orderCost)
    minPos = orderCost.index(minCost)
    print("*"*80)
    print("Number of orders: ",numOrders)
    print("-"*80)
    print("Total orders cost: ",totalOrders)
    print("-"*80)
    print("Order with highest cost:")
    print("orders number: ",orderNumber[maxPos],", customer phone: ",customerPhone[maxPos],", country: ",destinationCountry[maxPos],", cost: ",orderCost[maxPos])
    print("-" * 80)
    print("Order with lowest cost:")
    print("orders number: " , orderNumber[minPos] , ", customer phone: " , customerPhone[minPos] , ", country: " ,destinationCountry[minPos] , ", cost: " , orderCost[minPos])
    print("*" * 80)


def removeOrder(customerPhone, orderNumber, destinationCountry, orderWeight, orderCost):
    num = input("Enter order number: ")
    if num.isdigit() and num in orderNumber:
        pos = orderCost.index(int(num))
        customerPhone.pop(pos)
        orderNumber.pop(pos)
        destinationCountry.pop(pos)
        orderWeight.pop(pos)
        orderCost.pop(pos)
        print("Order number ",num," has been removed.")
    else:
        print("ERROR: Invalid order number! Try again.")



main()
