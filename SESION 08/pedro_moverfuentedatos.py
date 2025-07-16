import pandas as pd
import os
import shutil


#cantidad = input("ingrese la cantidad de archivos excel que deseas leer ? : ")
#cantidad = int(cantidad)
cantidad =5
#archivo = input("ingrese el nombre del archivo excel : ")
archivo = "reporte_ventas_medicamentos-resultante"
# Ruta del archivo Excel

ruta_base_existentes =  os.path.join("SESION 08","pedro_generados")
ruta_base_mover =  os.path.join("SESION 08","pedro_leidos")


contador = 1

if not os.path.exists(ruta_base_mover):
    os.makedirs(ruta_base_mover)

while contador <= cantidad:

    archivo_excel_nombre = archivo + "_" +str(contador)+".xlsx"
    archivo_excel_full = os.path.join(ruta_base_existentes,archivo_excel_nombre)  
    if os.path.exists(archivo_excel_full):

        # Leer la hoja específica (puedes cambiar el nombre de la hoja)
        df = pd.read_excel(archivo_excel_full, sheet_name="Sheet1")
        
        # tratar los datos 

        # Mostrar las primeras filas del archivo
        print(df.head())
        # Mover el archivo a la carpeta "leidos"
        #shutil.move(archivo_excel_full, os.path.join(ruta_base_mover,archivo_excel_nombre))
        shutil.copy(archivo_excel_full, os.path.join(ruta_base_mover,archivo_excel_nombre))
        print(f"Archivo {archivo_excel_full} movido a {ruta_base_mover}]")
    else :
        print(f"⚠️ El archivo {archivo_excel_full} no existe.")   

    contador = contador + 1 

print("================= fin de lectura =======================")
