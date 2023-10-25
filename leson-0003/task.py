# task 1
def task1():
   navn = 'Christian Kaatorp Larsen'
   alder = 16
   adrese = 'hestehovveien 19, 1890, rakkestad'
   interese = 'koding'
   print(navn)
   print(alder)
   print(adrese)
   print(interese)
# task 1
# task 2
def task2():
     a = 2
     b = 3
     c = a + b
     print(a,'+',b,'=', c)
# task 2
# task 3
def task3():
  def inputchek():
      x = input('type a number: ')
      z = float(x)
      if type(z) != float(x):
          print('first number corect', z)
      else:
          print(z)
          x = 0 
          x = input('type a number: ')
          z = float(x)
      y = input('type a number: ')
      b = float(y)
      if type(y)!=float(b):
          print('second number corect', y)
      else:
          print('try agin')
          y = 0 
          y = input('type a number: ')
      s = z+b
      print('svar: ',s)   
  inputchek()
# task 3
# task 4
def task4():
    a = input('wright a string: ' )
    b = input('wright a string: ' )
    c = input('wright a string: ' )
    O = a+' '+b+' '+c+'!'
    print(O.upper())
# task 4
# task 5
def task5():
    A = input('wright a number: ')
    B = input('wright a number: ')
    C = input('wright a number: ')
    D = input('wright a number: ')
    a = int(A)
    b = int(B)
    c = int(C)
    d = int(D)
    L = [a, b, c, d]
    def listsort():
        L.sort()
        print(L)
    def listadidive():
        a = L[0] + L[1] + L[2] + L[3]
        return a
    def listavrige():
        a = L[0] + L[1] + L[2] + L[3]
        b = a/len(L)
        return b
    listsort()
    print(listadidive())
    print(listavrige())
# task 5
task5()