# Práctica 4 : Criptografía

### Uso de los programas

Este proyecto contiene 2 tipos de programas, para encriptar archivos y para desencriptar

## Encriptar

Ejecuta en tu terminal lo siguiente

    python3 Encript.py <Input_file> <Output_file> [-b]

Donde input_file es la ruta al archivo que deseas encriptar, mientras que output_file es el nombre que le quieres asignar al resultado.

La bandera opcional "-b" va al final y con esto le dices al programa que lo que quieres es codificar el archivo de entrada en base 64

## Desencriptar

si deseas **desencriptar un archivo buscando una función inversa a la función afín** con la que se encriptó tu archivo entonces:

Ejecuta en tu terminal lo siguiente

    python3 Decript.py <Input_file> <Output_file> 

Si lo que buscas es decodificar un archivo base64 entonces ejecuta

    python3 base64Cipher.py <Input_File> <Output_file> 

en cualquiera de los 2 casos, Inptu_file es el la ruta al archivo que deseas desencriptar, mientas que Output_file es el nombre del resultado.