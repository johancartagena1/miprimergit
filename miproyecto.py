"""
Johan Steven Cartagena Gonzalez
07/09/21
"""
import random
respuestas = ('responder1()', 'responder2()', 'responder3()', 'responder4()')

x=random.randint(0,3)

def saludar():
    print ("hola soy brayan")
    print ("en que le puedo ayudar ")
    saludar =input()
    return saludar
     
    
def hola1():
    print("""
 _           _
| |         | |
| |__   ___ | | __ _ 
| '_ \ / _ \| |/ _` |
| | | | (_) | | (_| |
|_| |_|\___/|_|\__,_|""")

   
    presentacion = responder().lower()
def responder1():
    print ("yo soy un sistema operativo que esta aqui para ayudarte en lo que sea, soy mejor que siri ")
    
    
def responder2():
    print ("soy un alien que viena ha dominar el mundo")
    
def responder3():
    print ("yo soy tu asistente de busqueda personal, en que te puedo ayudar")
    
def responder4():
    print ("no molestes")

def main():
    saluda = saludar().lower()
    if saluda == "quien eres" or saluda == "quien eres tu":
        responder=x()
        
        
    if saluda == "hola":
       hola1()
    
    elif saluda == "no se":
        print("a bueno, chao")
        
    elif saluda == "twngo h":
        print("a bueno, vy d")
    
    else:
        print("No te entiendo")
        

main()