clean_data = []
productlist = []
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

def directory():
    # dette er directory som gir brukeren mulighet til og bevege seg i programet.
    print("\n\ndirectory:")
    print("Produktadministrasjon [P]\nOrdrebehandling [O]\nKundehåndtering [K]\nRapporter [R]\nHelp [help]\nExit [exit]")
    directoryorder = input("hvor skal du: ")
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
    adminorder = input("hvor skal du: Vare navn [VN], Vare beskrivelse [VB], Vare pris [VP],vare antall [VA] , alle varer [AV], tilbake [B]:")
    adminorder = str(adminorder.upper())
    match adminorder:
        case "VN":
            productcheker(adminorder)
        case "VB":
            productcheker(adminorder)
        case "VP":
            productcheker(adminorder)
        case "VA":
            productcheker(adminorder)
        case "AV":
            productcheker(adminorder)
        case "B":
            directory()
        case _:
            print("prøv på nytt")
            Produktadministrasjon()


def Ordrebehandling():
    # Ordrebehandling av kundens bestilinger og befriftens bestilinger.
    print("\nOrdrebehandling")

def Kundehåndtering():
    # Kundehåndtering av inormasjonen til kunder alt fra leverings adrese til facturering og ordre.
    print("\nKundehåndtering")

def Rapporter():
    # Rapporter er hvor du kan generere raporter for salg og aktivitet.
    print("\nRapporter")


def productfillereader():
    with open('./big-task-text/text-files/products.txt','r', encoding='utf-8') as f:
        data = f.readlines()
    datacliner(data)

def datacliner(unclean_data):
    words_to_remove = ["Navn:", "Beskrivelse:", "Pris:", "VareID:", "Antall:"]
    for item in unclean_data:
        for word in words_to_remove:
            item = item.replace(word, "").strip()
        clean_data.append(item)

def productclassasembeler():
    productfillereader()
    while len(clean_data)!=0:
        i=0
        newproduct = product(clean_data[i],clean_data[i+1],clean_data[i+2],clean_data[i+3],clean_data[i+4])
        productlist.append(newproduct)
        clean_data.pop(i+4)
        clean_data.pop(i+3)
        clean_data.pop(i+2)
        clean_data.pop(i+1)
        clean_data.pop(i)

def productcheker(order):
    if order != "AV":
        pID = input("skriv product ID:" )
        pID = int(pID)
        for i in range(len(productlist)):
            if pID == int(productlist[i].productID):
                print("found it!")
                break
        else:
            print("product fines ikke, prøv på nyt")
            productcheker(order)
    match order:
        case "VN":
            productcheker(adminorder)
        case "VB":
            productcheker(adminorder)
        case "VP":
            productcheker(adminorder)
        case "VA":
            productcheker(adminorder)
        case "AV":
             for i in range(len(productlist)):
                 print(productlist[i].name +"\n"+ productlist[i].description +"\n"+ productlist[i].price +"\n"+productlist[i].amount +"\n"+ productlist[i].productID )
        
    
    

def onstart():
    productclassasembeler()    
    directory()

onstart()