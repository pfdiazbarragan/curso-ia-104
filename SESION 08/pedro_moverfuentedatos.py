import pandas as pd
import os
import shutil

#cantidad = input("ingrese la cantidad de archivos excel que deseas leer ? : ")
#cantidad = int(cantidad)
cantidad =5
#archivo = input("ingrese el nombre del archivo excel : ")
archivo = "SESION 08/pedro_generados/reporte_ventas_medicamentos-resultante"
# Ruta del archivo Excel
contador = 1

if not os.path.exists("SESION 08/pedro_leidos"):
    os.makedirs("SESION 08/pedro_leidos")

while contador <= cantidad:
    archivo_excel = archivo + "_" +str(contador)+".xlsx"  
    if os.path.exists(archivo_excel):

        # Leer la hoja específica (puedes cambiar el nombre de la hoja)
        df = pd.read_excel(archivo_excel, sheet_name="Sheet1")
        
        # tratar los datos 

        # Mostrar las primeras filas del archivo
        print(df.head())
        # Mover el archivo a la carpeta "leidos"
        shutil.move(archivo_excel, os.path.join("SESION 08/pedro_leidos", archivo_excel))
        print(f"Archivo {archivo_excel} movido a 'leidos'")
    else :
        print(f"⚠️ El archivo {archivo_excel} no existe.")   

    contador = contador + 1 

print("================= fin de lectura =======================")
