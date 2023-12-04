clean_product_data = []
productlist = []
customerlist = []
orderList = []
orderclasslist = []
customerclasslist = []
# class liste.
class product:
    def __init__(self, name, description, price, amount, productID):
        self.name = name
        self.price = price
        self.description = description
        self.productID = productID
        self.amount = amount

class customer:
    def __init__(self, type, name, contactperson, email, phonenumber, numberfromland, billingadres, billingadreszipcode, deliveryadres, deliveryadreszipcode, customerID):
        self.type = type
        self.name = name
        self.contactperson = contactperson
        self.email = email
        self.phonenumber = phonenumber
        self.numberfrom = numberfromland
        self.billingadres = billingadres
        self.billingadreszipcode = billingadreszipcode
        self.deliveryadres = deliveryadres
        self.deliveryadreszipcode = deliveryadreszipcode
        self.customerID = customerID

class order:
    def __init__(self, orderdescrition, productID, amount, fromLocation,customerID, billingadres, billingadreszipcode, deliveryadres, deliveryadreszipcode, cost, status):
        self.productID = productID
        self.amount = amount
        self.fromLocation = fromLocation
        self.cost = cost
        self.status = status 
        self.orderdescrition = orderdescrition
        self.billingadres = billingadres
        self.billingadreszipcode = billingadreszipcode
        self.deliveryadres = deliveryadres
        self.deliveryadreszipcode = deliveryadreszipcode
        self.customerID = customerID

def directory():
    # dette er directory som gir brukeren mulighet til og bevege seg i programet.
    print("\n\ndirectory:")
    print("Produktadministrasjon [P]\nOrdrebehandling [O]\nKundehåndtering [K]\nRapporter(WIP) [R]\nHelp(WIP) [help]\nExit [exit]")
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
    adminorder = input("hvor skal du:\nVare navn [VN]\nVare beskrivelse [VB]\nVare pris [VP]\nvare antall [VA]\nalle varer [AV]\nful vare beskrivelse[FVB]\ntilbake [B]\nhva skal du: ")
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
    print("\nOrdrebehandling:")
    director = input(" Ny bestiling til lager [OI]\n Ny bestiling til kunde [OU]\n Alle ordere [AO]\n tilbake[B]\n ")
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
                print("--------\n"+orderclasslist[i].orderdescrition +"\n"+ orderclasslist[i].productID +"\n"+ orderclasslist[i].amount+"\n"+orderclasslist[i].fromLocation +"\n"+ orderclasslist[i].customerID+"\n"+orderclasslist[i].billingadres+"\n"+orderclasslist[i].billingadreszipcode+"\n"+orderclasslist[i].deliveryadres+"\n"+orderclasslist[i].deliveryadreszipcode+"\n"+orderclasslist[i].cost +" NOK\n"+orderclasslist[i].status)
            Ordrebehandling()
        case "B":
            directory()
        case _:
            print("ERROR, try agin")
            Ordrebehandling()

def Kundehåndtering():
    # Kundehåndtering av inormasjonen til kunder alt fra leverings adrese til facturering og ordre.
    print("\nKundehåndtering")
    opptions = ["AC","PC", "CC"]
    inn = input("Alle kunder [AC] \nprivate kunder [PC] \nbefrift kunder [CC] \nny kunde [NC] \ntilbake[B]\nhvilken kundetype vil du vite om:")
    inn = str(inn.upper())
    if inn in opptions:
        printcustomerinfo(inn)
    else:
        match inn:
            case "NC":
                new = input("\nprivat kunde[PC] \nbedrift kunde [CC] \nhva slaks kunde er dette: ")
                new = str(new.upper())
                if new == "AC":
                    print("prøv på nytt")
                    Kundehåndtering()
                if new in opptions:
                    newcustomer(new)
            case "B":
                directory() 
            case _:
                Kundehåndtering()
    Kundehåndtering()

def Rapporter():
    # Rapporter er hvor du kan generere raporter for salg og aktivitet.
    print("\nRapporter")

def printcustomerinfo(inn):
    match inn:
        case "AC":
            print("-----")
            for i in range(len(customerclasslist)):
                print("Type: "+customerclasslist[i].type +"\nNavn: "+ customerclasslist[i].name +"\nKontaktperson: "+ customerclasslist[i].contactperson +"\nE-post: "+ customerclasslist[i].email +"\nTelefon: "+ customerclasslist[i].phonenumber +"\nfra Land: "+ customerclasslist[i].numberfrom +"\nGateadresse: "+ customerclasslist[i].billingadres +"\nPostnummer: "+ customerclasslist[i].billingadreszipcode +"\nGateadresse: "+ customerclasslist[i].deliveryadres +"\nPostnummer: "+ customerclasslist[i].deliveryadreszipcode +"\nKundenumber: "+ customerclasslist[i].customerID+"\n-----") 
        case "PC":
            print("-----")
            for i in range(len(customerclasslist)):
                if customerclasslist[i].type == "privat":
                    print("Navn: "+ customerclasslist[i].name +"\nKontaktperson: "+ customerclasslist[i].contactperson +"\nE-post: "+ customerclasslist[i].email +"\nTelefon: "+ customerclasslist[i].phonenumber +"\nfra Land: "+ customerclasslist[i].numberfrom +"\nGateadresse: "+ customerclasslist[i].billingadres +"\nPostnummer: "+ customerclasslist[i].billingadreszipcode +"\nGateadresse: "+ customerclasslist[i].deliveryadres +"\nPostnummer: "+ customerclasslist[i].deliveryadreszipcode +"\nKundenumber: "+ customerclasslist[i].customerID+"\n-----")
        case "CC":
            print("-----")
            for i in range(len(customerclasslist)):
                if customerclasslist[i].type == "bedrift":
                    print("Navn: "+ customerclasslist[i].name +"\nKontaktperson: "+ customerclasslist[i].contactperson +"\nE-post: "+ customerclasslist[i].email +"\nTelefon: "+ customerclasslist[i].phonenumber +"\nfra Land: "+ customerclasslist[i].numberfrom +"\nGateadresse: "+ customerclasslist[i].billingadres +"\nPostnummer: "+ customerclasslist[i].billingadreszipcode +"\nGateadresse: "+ customerclasslist[i].deliveryadres +"\nPostnummer: "+ customerclasslist[i].deliveryadreszipcode +"\nKundenumber: "+ customerclasslist[i].customerID+"\n-----") 
 
def newcustomer(type):
    newcustomerlist = []
    match type:
        case "PC":
                a = True
                newcustomerlist.append("Type: privat")
                inn = input("navnet på kunden: ")
                inn = str(inn)
                newcustomerlist.append("Navn: " + inn)
                newcustomerlist.append("Kontaktperson: " + inn)
                inn = input("E-post: ")
                inn = str(inn)
                newcustomerlist.append("E-post: " + inn)
                inn = input("Telefon numer: ")
                inn = str(inn)
                newcustomerlist.append("Telefon: " + inn)
                inn = input("hvor er det fra +")
                inn = str(inn)
                newcustomerlist.append("fra Land: +" + inn)
                inn = input("Gateadresse: ")
                inn = str(inn)
                newcustomerlist.append("Gateadresse: " + inn)
                innn = input("Postnummer: ")
                innn = str(innn)
                newcustomerlist.append("Postnummer: " + innn)
                newcustomerlist.append("Gateadresse: " + inn)
                newcustomerlist.append("Postnummer: " + innn)
                length = len(customerclasslist)
                length = int(length)+1
                newcustomerlist.append("Kundenumber: "+ str(length))
                inn = input("er dette riktig? Ja[Y] Nei [N]")
                inn = str(inn.upper())
                if inn == "Y":
                    print("done")
                    for j in range(len(newcustomerlist)):
                        customerfile = open('./big-task-text/text-files/customers.txt','a', encoding='utf-8')
                        customerfile.writelines("\n"+newcustomerlist[j])
                        customerfile.close()
                elif inn =="N":
                    newcustomer(type)
        case "CC":
                print(type)
                newcustomerlist.append("Type: bedrift")
                inn = input("navnet på bedrift: ")
                inn = str(inn)
                newcustomerlist.append("Navn: " + inn)
                inn = input("navnet på Kontaktperson: ")
                inn = str(inn)
                newcustomerlist.append("Kontaktperson: " + inn)
                inn = input("E-post: ")
                inn = str(inn)
                newcustomerlist.append("E-post: " + inn)
                inn = input("Telefon numer: ")
                inn = str(inn)
                newcustomerlist.append("Telefon: " + inn)
                inn = input("hvor er det fra +")
                inn = str(inn)
                newcustomerlist.append("fra Land: +" + inn)
                inn = input("Factura Gateadresse: ")
                inn = str(inn)
                newcustomerlist.append("Gateadresse: " + inn)
                innn = input("Factura Postnummer: ")
                innn = str(inn)
                newcustomerlist.append("Postnummer: " + innn)
                inn = input("Leverings Gateadresse: ")
                inn = str(inn)
                newcustomerlist.append("Gateadresse: " + inn)
                innn = input("Leverings Postnummer: ")
                innn = str(inn)
                newcustomerlist.append("Postnummer: " + innn)
                length = len(customerclasslist)
                length = int(length)+1
                newcustomerlist.append("Kundenumber: "+ str(length))
                inn = input("er dette riktig? Ja[Y] Nei [N]")
                inn = str(inn.upper())
                if inn == "Y":
                    print("done")
                    for j in range(len(newcustomerlist)):
                        customerfile = open('./big-task-text/text-files/customers.txt','a', encoding='utf-8')
                        customerfile.writelines("\n"+newcustomerlist[j])
                        customerfile.close()
                elif inn =="N":
                    newcustomer(type)
        case _:
            print("error")
            Ordrebehandling()
    uppdateClassesFromDoc()

def fillereader():
    p = open('./big-task-text/text-files/products.txt','r', encoding='utf-8')
    product_data = p.readlines()
    p.close()
    c = open('./big-task-text/text-files/customers.txt','r', encoding='utf-8')
    customer_data = c.readlines()
    c.close()
    o = open('./big-task-text/text-files/ordere.txt','r', encoding='utf-8')
    order_data = o.readlines()
    o.close()
    orderdatacliner(order_data)
    productdatacliner(product_data)
    customerdatacleaner(customer_data)

def productdatacliner(unclean_data):
    words_to_remove = ["Navn:", "Beskrivelse:", "Pris:", "VareID:", "Antall:"]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        clean_product_data.append(item)

def orderdatacliner(unclean_data):
    words_to_remove = ["VareID:", "Mengde:", "Fra:", "Til:", "Pris:", "Status:", "Bestilingsbeskrivelse:", "Kunde ID:", "Factura til addrese:", "Factura til addrese zip:", "Ordere til addrese:", "Ordere til addrese zip:"]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        orderList.append(item)

def customerdatacleaner(unclean_data):
    words_to_remove = ["Type: ","Navn: ","Kontaktperson: ","E-post: ","Telefon: ","fra Land: ","Gateadresse: ","Postnummer: ", "Kundenumber: "]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        customerlist.append(item)  
    
def dataclassasembeler():
    fillereader()
    while len(clean_product_data)!=0:
        i=0
        newproduct = product(clean_product_data[i],clean_product_data[i+1],clean_product_data[i+2],str(clean_product_data[i+3]),clean_product_data[i+4])
        productlist.append(newproduct)
        clean_product_data.pop(i+4)
        clean_product_data.pop(i+3)
        clean_product_data.pop(i+2)
        clean_product_data.pop(i+1)
        clean_product_data.pop(i)
    while len(orderList)!=0:
        i=0
        neworder = order(orderList[i],orderList[i+1],orderList[i+2],orderList[i+3],orderList[i+4],orderList[i+5],orderList[i+6],orderList[i+7],orderList[i+8],orderList[i+9],orderList[i+10])
        orderclasslist.append(neworder)
        orderList.pop(i+10)
        orderList.pop(i+9)
        orderList.pop(i+8)
        orderList.pop(i+7)
        orderList.pop(i+6)
        orderList.pop(i+5)
        orderList.pop(i+4)
        orderList.pop(i+3)
        orderList.pop(i+2)
        orderList.pop(i+1)
        orderList.pop(i)
    while len(customerlist)!=0:
        i=0
        newcustomer = customer(customerlist[i],customerlist[i+1],customerlist[i+2],customerlist[i+3],customerlist[i+4],customerlist[i+5],customerlist[i+6],customerlist[i+7],customerlist[i+8],customerlist[i+9],customerlist[i+10])
        customerclasslist.append(newcustomer)
        customerlist.pop(i+10)
        customerlist.pop(i+9)
        customerlist.pop(i+8)
        customerlist.pop(i+7)
        customerlist.pop(i+6)
        customerlist.pop(i+5)
        customerlist.pop(i+4)
        customerlist.pop(i+3)
        customerlist.pop(i+2)
        customerlist.pop(i+1)
        customerlist.pop(i)
    productlistuppdater()

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
            print("--------\n"+productlist[oID].name +"\n"+ productlist[oID].description +"\n"+ productlist[oID].price+" NOK" +"\n"+productlist[oID].amount +"\n"+"--------")
        case "AV":
             #prints every produckt in the database.
             for i in range(len(productlist)):
                 print("--------\n"+productlist[i].name +"\n"+ productlist[i].description +"\n"+ productlist[i].price+" NOK" +"\n"+str(productlist[i].amount) +"\n"+ productlist[i].productID)
             print("--------")
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
                            amount = str(amount)
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
                                newOrderInList.append("Kunde ID: " + str(customerclasslist[0].customerID))
                                newOrderInList.append("Factura til addrese: "+str(customerclasslist[0].billingadres))
                                newOrderInList.append("Factura til addrese zip: "+str(customerclasslist[0].billingadreszipcode))
                                newOrderInList.append("Ordere til addrese: "+str(customerclasslist[0].deliveryadres))
                                newOrderInList.append("Ordere til addrese zip: "+str(customerclasslist[0].deliveryadreszipcode))
                                pricestr = int(productlist[B].price) * int(amount)
                                newOrderInList.append("Pris: " + str(pricestr))
                                newOrderInList.append("Status: i rute")
                                orderfile = open('./big-task-text/text-files/ordere.txt','a')
                                for j in range(len(newOrderInList)):
                                    orderfile.writelines("\n"+newOrderInList[j])
                                orderfile.close()
                        i=2
                                                  
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
                            newOrderMaker("OU", 0)
                        newOrderInList.append("VareID: "+ productlist[B].productID)
                        i=1
                    case 1:
                        prosedone = False
                        prosedtwo = False
                        while prosedone == False:
                            amount = input("hvor mange skal sendes?: ")
                            if amount == int(amount):
                                print("error")
                                newOrderMaker("OU",1)
                            print("er du siker på dene mengden: ", amount)
                            c = input("ja [Y], nei[N]: ")
                            c = str(c.upper())
                            if c == "Y":
                                prosedone = True
                                newOrderInList.append("Mengde: " + amount)
                                newOrderInList.append("Fra: lager")
                                while prosedtwo == False:
                                    inn = input("hvilken kunde skal den til (ID): ")
                                    inn = int(inn)
                                    for o in range(len(customerclasslist)):
                                        if inn == int(customerclasslist[o].customerID):
                                            t = customerclasslist[o].customerID
                                            t = int(t)-1
                                            prosedtwo = True
                                newOrderInList.append("Kunde ID: " + str(customerclasslist[t].customerID))
                                newOrderInList.append("Factura til addrese: "+str(customerclasslist[t].billingadres))
                                newOrderInList.append("Factura til addrese zip: "+str(customerclasslist[t].billingadreszipcode))
                                newOrderInList.append("Ordere til addrese: "+str(customerclasslist[t].deliveryadres))
                                newOrderInList.append("Ordere til addrese zip: "+str(customerclasslist[t].deliveryadreszipcode))
                                pricestr = int(productlist[B].price) * int(amount)
                                newOrderInList.append("Pris: " + str(pricestr))
                                newOrderInList.append("Status: i rute")
                                orderfile = open('./big-task-text/text-files/ordere.txt','a')
                                for j in range(len(newOrderInList)):
                                    orderfile.writelines("\n"+str(newOrderInList[j]))
                                orderfile.close()
                        i = 2
    uppdateClassesFromDoc()
    Ordrebehandling()
    print("order ferdig")

def productlistuppdater():
    productposebiletylist=[]
    for i in range(len(productlist)):
        productposebiletylist.append(productlist[i].productID)
        #gives a list whit all productID for ease of productivety
    i= 0
    while i != len(orderclasslist):
        if str(orderclasslist[i].productID) in str(productposebiletylist):
            t = orderclasslist[i].productID
            t = int(t)-1
            amountonlist = int(productlist[t].amount)
            amountonorder = int(orderclasslist[i].amount)
            if orderclasslist[i].orderdescrition == "vare til kunde":
                amountonlist -= amountonorder
                productlist[t].amount = amountonlist
            else:
                amountonlist += amountonorder
                productlist[t].amount = amountonlist
        i+=1

def uppdateClassesFromDoc():
    clean_product_data.clear()
    productlist.clear()
    customerlist.clear()
    orderList.clear()
    orderclasslist.clear()
    customerclasslist.clear()
    dataclassasembeler()

def onstart():
    dataclassasembeler()    
    directory()

onstart()