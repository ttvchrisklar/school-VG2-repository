
# class liste.
class product:
    def __init__(self, name, price, description, amount):
        self.name = name
        self.price = price
        self.description = description
        # self.storigelocation = storigelocation
        # storigelocation
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
    print("directory:")
    print("Produktadministrasjon [P]\nOrdrebehandling [O]\nKundehåndtering [K]\nRapporter [R]\nHelp [help]")
    directoryorder = input("hvor skal du: ")
    directoryorder = str(directoryorder)
    match directoryorder.upper():
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
        case _:
            print("prøv på nytt")
            directory()



def Produktadministrasjon():
    # dette er får administrasjon av produkter i systemet.
    print("Produktadministrasjon:")

def Ordrebehandling():
    # Ordrebehandling av kundens bestilinger og befriftens bestilinger.
    print("Ordrebehandling")

def Kundehåndtering():
    # Kundehåndtering av inormasjonen til kunder alt fra leverings adrese til facturering og ordre.
    print("Kundehåndtering")

def Rapporter():
    # Rapporter er hvor du kan generere raporter for salg og aktivitet.
    print("Rapporter")


# for opening and reading external files
# f = open('./big-task-text/text-files/products.txt')
# print(f.read())
# f.close()
f = open('./big-task-text/text-files/products.txt',"a")
f.write("hi\n")
f.close()
f = open('./big-task-text/text-files/products.txt')
print(f.read())
f.close()

# directory()