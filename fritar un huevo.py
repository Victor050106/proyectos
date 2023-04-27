print("Debes fritar un huevo")
huevo=input("tienes huevos ? (S/N)").strip().capitalize()
if huevo==("S"):
    print("agarrar uno de la despensa")
    print("agarrar un sarten")
    gas=input("hay gas ?(S/N) ").strip().capitalize()
    if gas==("S"):
        print("encenderlo en la estufa ")
        print("colocarle aceite")
        print("romper y echar el huevo")
        sal=input("lo quieres con sal ? (S/N)").strip().capitalize()
        if sal==("S"):
            print("agregale sal")
            print("poner tapa")
            print("esperar a que se cocine")
            quemado=input("se quemó? (S/N)").strip().capitalize()
            if  sal==("N"):
             print("poner tapa")
             print("esperar a que se cocine")
        
            if  quemado==("N"):
                print("servir en un plato")
                print("comer")
                exit()
            if quemado==("S"):
             print("no se pudo fritar un huevo")
            exit()
    if gas==("N"):
        print("no tienes gas")
        print("no se puede fritar un huevo")
        exit()       
            
if huevo==("N"):
    dinero=input("hay dinero? (S/N)").strip().capitalize()
    if dinero==("S"):
        print("comprar un huevo en la tienda")
        print("agarrar un sarten")
    gas=input("hay gas ?(S/N) ").strip().capitalize()
    if gas==("S"):
        print("encenderlo en la estufa ")
        print("colocarle aceite")
        print("romper y echar el huevo")
    if gas==("N"):
        print("no tienes gas")
        print("no se puede fritar un huevo")
        exit()    
        
    sal=input("lo quieres con sal ? (S/N)").strip().capitalize()
    if sal==("S"):
             print("agregale sal")
             print("poner tapa")
             print("esperar a que se cocine")
       
    if sal==("N"):
             print("poner tapa")
             print("esperar a que se cocine")
    quemado=input("se quemó? (S/N)").strip().capitalize()
    if  quemado==("N"):
                print("servir en un plato")
                print("comer")
                print("FIN")
                exit()
    if quemado==("S"):
             print("no se pudo fritar un huevo")
             exit()
       
    if dinero==("N"):
        print("no tienes dinero")
        print("no se puede fritar un huevo")
        exit()
        
    
        
       

