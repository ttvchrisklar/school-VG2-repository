clean_product_data = []
productlist = []
customerlist = []
orderList = []
orderclasslist = []
# class liste.
class product:
    def __init__(self, name, description, price, amount, productID):
        self.name = name
        self.price = price
        self.description = description
        self.productID = productID
        self.amount = amount

class customer:
    def __init__(self, name, compony, billingadress, deliveryadress, orderhistery):
        self.name = name
        self.compony = compony
        self.billingadress = billingadress
        self.deliveryadress = deliveryadress
        self.orderhistery = orderhistery

class order:
    def __init__(self, orderdescrition, productID, amount, fromLocation, toLocation, cost, status):
        self.productID = productID
        self.amount = amount
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.cost = cost
        self.status = status 
        self.orderdescrition = orderdescrition

def directory():
    # dette er directory som gir brukeren mulighet til og bevege seg i programet.
    print("\n\ndirectory:")
    print("Produktadministrasjon [P]\nOrdrebehandling [O]\nKundehåndtering(WIP) [K]\nRapporter(WIP) [R]\nHelp(WIP) [help]\nExit [exit]")
    directoryorder = input("hva skal du: ")
    directoryorder = str(directoryorder.upper())
    match directoryorder:
        case "P":
            Produktadministrasjon()
        case "O":
            Ordrebehandling()
        case "K":
            Kundehåndtering()
        case "R":
            Rapporter()
        case "HELP":
            help()
        case "EXIT":
            exit()
        case _:
            print("prøv på nytt")
            directory()



def Produktadministrasjon():
    # dette er får administrasjon av produkter i systemet.
    print("\nProduktadministrasjon:")
    adminorder = input("\nhvor skal du:\nVare navn [VN]\nVare beskrivelse [VB]\nVare pris [VP]\nvare antall [VA]\nalle varer [AV]\nful vare beskrivelse[FVB]\ntilbake [B]\nhva skal du: ")
    adminorder = str(adminorder.upper())
    valid_cases = ["VN", "VB", "VP", "VA", "AV", "FVB"]
    if adminorder in valid_cases:
        productcheker(adminorder)
    elif adminorder == "B":
        directory()
    else:
        print("prøv på nytt")
        Produktadministrasjon()

def Ordrebehandling():
    # Ordrebehandling av kundens bestilinger og bedriftens bestilinger.
    print("\nOrdrebehandling")
    director = input("\n vil du:\n Ny bestiling til lager [OI]\n Ny bestiling til kunde [OU]\n Alle ordere [AO]\n tilbake[B]\n ")
    director = str(director.upper())
    match director:
        case "OI":
            print("Ny bestiling til lager")
            newOrderMaker("OI",0)
            # make input methid for name of the order, order ID, amount, from, to, cost?, states?
        case "OU":
            print("Ny bestiling til kunde")
            newOrderMaker("OU",0)
            # make input methid for name of the order, order ID, amount, from, to, cost?, states?
        case "AO":
            print("Alle ordere")
            for i in range(len(orderclasslist)):
                print("--------\n"+orderclasslist[i].orderdescrition +"\n"+ orderclasslist[i].productID +"\n"+ orderclasslist[i].amount+"\n"+orderclasslist[i].fromLocation +"\n"+ orderclasslist[i].toLocation+"\n"+ orderclasslist[i].cost +" NOK\n"+orderclasslist[i].status)
            Ordrebehandling()
        case "B":
            directory()
        case _:
            print("ERROR, try agin")
            Ordrebehandling()

def Kundehåndtering():
    # Kundehåndtering av inormasjonen til kunder alt fra leverings adrese til facturering og ordre.
    print("\nKundehåndtering")

def Rapporter():
    # Rapporter er hvor du kan generere raporter for salg og aktivitet.
    print("\nRapporter")


def fillereader():
    p = open('./big-task-text/text-files/products.txt','r', encoding='utf-8')
    product_data = p.readlines()
    p.close()
    # with open('./big-task-text/text-files/customers.txt','r', encoding='utf-8') as f:
    #     customer_data = f.readlines()
    #     f.colse()
    o = open('./big-task-text/text-files/ordere.txt','r', encoding='utf-8')
    order_data = o.readlines()
    o.close()
    orderdatacliner(order_data)
    productdatacliner(product_data)

def customerDataCleaner(inn_data):
    words_to_remove = ["Navn:", "Bedrift:", "Bakgrun:", "Sendingsadresse:", "Handlehistorie:"]
    for item in inn_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        clean_product_data.append(item)

def productdatacliner(unclean_data):
    words_to_remove = ["Navn:", "Beskrivelse:", "Pris:", "VareID:", "Antall:"]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        clean_product_data.append(item)

def orderdatacliner(unclean_data):
    words_to_remove = ["VareID:", "Mengde:", "Fra:", "Til:", "Pris:", "Status:", "Bestilingsbeskrivelse:"]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        orderList.append(item)    
    
def dataclassasembeler():
    fillereader()
    while len(clean_product_data)!=0:
        i=0
        newproduct = product(clean_product_data[i],clean_product_data[i+1],clean_product_data[i+2],clean_product_data[i+3],clean_product_data[i+4])
        productlist.append(newproduct)
        clean_product_data.pop(i+4)
        clean_product_data.pop(i+3)
        clean_product_data.pop(i+2)
        clean_product_data.pop(i+1)
        clean_product_data.pop(i)
    while len(orderList)!=0:
        i=0
        neworder = order(orderList[i],orderList[i+1],orderList[i+2],orderList[i+3],orderList[i+4],orderList[i+5],orderList[i+6])
        orderclasslist.append(neworder)
        orderList.pop(i+6)
        orderList.pop(i+5)
        orderList.pop(i+4)
        orderList.pop(i+3)
        orderList.pop(i+2)
        orderList.pop(i+1)
        orderList.pop(i)
    
def productcheker(order):
    oID=0
    if order != "AV":
        #rquest a product id number from the user
        pID = input("skriv product ID:" )
        pID = int(pID)
        # then loop the list to find the ID number
        for i in range(len(productlist)):
            if pID == int(productlist[i].productID):
                oID = i
                break
        else:
            print("product fines ikke, prøv på nyt")
            productcheker(order)
    match order:
        case "VN":
            # tells the name of the product
            print(productlist[oID].name)
        case "VB":
            #description of the product
            print(productlist[oID].description)
        case "VP":
            #price of the prduct
            print(productlist[oID].price+" NOK")
        case "VA":
            #the amount of products in stock
            print(productlist[oID].amount)
        case "FVB":
            #prints the full prodects "class"
            print("--------\n"+productlist[oID].name +"\n"+ productlist[oID].description +"\n"+ productlist[oID].price+" NOK" +"\n"+productlist[oID].amount +"\n")
        case "AV":
             #prints every produckt in the database.
             for i in range(len(productlist)):
                 print("--------\n"+productlist[i].name +"\n"+ productlist[i].description +"\n"+ productlist[i].price+" NOK" +"\n"+productlist[i].amount +"\n"+ productlist[i].productID)
        case _:
            # error in case the adminorder gets removed mid manigment some how, idk how?
            print("error, prøv på nytt")
    Produktadministrasjon()

def newOrderMaker(type, position):
    i = position
    match type:
        case "OI":
            print("ordre in")
            newOrderInList = []
            newOrderInList.append("Bestilingsbeskrivelse: vare til lagret")
            while i != 2:
                B=0
                match i:
                    case 0:
                        inp = input("vare ID: ")
                        inp = int(inp)
                        for o in range(len(productlist)):
                            if inp == int(productlist[o].productID):
                                B = o
                                break
                        else:
                            print("error, prøv på nytt")
                            newOrderMaker("OI", 0)
                        newOrderInList.append("VareID: "+ productlist[B].productID)
                        i=1
                    case 1:
                        prosed = False
                        while prosed == False:
                            amount = input("hvor mange skal skjøpes?: ")
                            if amount == int(amount):
                                print("error")
                                newOrderMaker("OI",1)
                            print("er du siker på dene mengden: ", amount)
                            c = input("ja [Y], nei[N]: ")
                            c = str(c.upper())
                            if c == "Y":
                                prosed = True
                        newOrderInList.append("Mengde: " + amount)
                        newOrderInList.append("Fra: Produsent")
                        newOrderInList.append("Til: Lager")
                        pricestr = int(productlist[B].price) * int(amount)
                        newOrderInList.append("Pris: " + str(pricestr))
                        newOrderInList.append("Status: i rute")
                        orderfile = open('./big-task-text/text-files/ordere.txt','a')
                        for j in range(len(newOrderInList)):
                            orderfile.writelines("\n"+newOrderInList[j])
                        orderfile.close()                       
        case "OU":
            # needs customer data so laiter on when that systems up and runing i do this!
            print("ordre ut")
            newOrderInList = []
            newOrderInList.append("Bestilingsbeskrivelse: vare til kunde")
            while i != 2:
                B=0
                match i:
                    case 0:
                        inp = input("vare ID: ")
                        inp = int(inp)
                        for o in range(len(productlist)):
                            if inp == int(productlist[o].productID):
                                B = o
                                break
                        else:
                            print("error, prøv på nytt")
                            newOrderMaker("OI", 0)
                        newOrderInList.append("VareID: "+ productlist[B].productID)
                        i=1
                    case 1:
                        prosed = False
                        while prosed == False:
                            amount = input("hvor mange skal sendes?: ")
                            if amount == int(amount):
                                print("error")
                                newOrderMaker("OI",1)
                            print("er du siker på dene mengden: ", amount)
                            c = input("ja [Y], nei[N]: ")
                            c = str(c.upper())
                            if c == "Y":
                                prosed = True
                        newOrderInList.append("Mengde: " + amount)
                        newOrderInList.append("Fra: lager")
                        newOrderInList.append("Til: kunde") #temperery until having a custormer data base up
                        pricestr = int(productlist[B].price) * int(amount)
                        newOrderInList.append("Pris: " + str(pricestr))
                        newOrderInList.append("Status: i rute")
                        orderfile = open('./big-task-text/text-files/ordere.txt','a')
                        for j in range(len(newOrderInList)):
                            orderfile.writelines("\n"+newOrderInList[j])
                        orderfile.close()
    uppdateClassesFromDoc()
    Ordrebehandling()
    print("order ferdig")

def uppdateClassesFromDoc():
    clean_product_data.clear()
    productlist.clear()
    customerlist.clear()
    orderList.clear()
    orderclasslist.clear()
    dataclassasembeler()

def onstart():
    dataclassasembeler()    
    directory()

onstart()