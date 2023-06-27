import os
import re
import csv
import time
import shutil
import tabula
import PyPDF2
import pandas as pd

from PyPDF2 import PdfReader

def upload_file(folder_path_input, folder_path_output, folder_path_config, folder_path_onedrive):
    print('Entrando en la funcion upload...')
    print('----------------------------------------------------------------------')
    
    # Variable array
    file_name_list = []
    
    # Bucle para obtener lista de nombre de archivos
    for add_file_list in os.listdir(folder_path_output):
        if add_file_list.endswith(".pdf"):
            file_name_list.append(add_file_list)
    
    print('Cantidad Elem. file_name_list: ', len(file_name_list))
    print('----------------------------------------------------------------------')
    
    # Ordenar lista de archivos por nombre
    new_file_name_list_sort = sorted(file_name_list)
    print('file_name_list_sort: ', new_file_name_list_sort, len(new_file_name_list_sort))
    print('----------------------------------------------------------------------')
    
    # Especifica la ruta de tu archivo Excel
    excel_file = folder_path_config + "clientes.xlsx"

    # Especifica el nombre de la hoja en la que se encuentran los datos
    hoja_excel = "Hoja1"

    # Carga los datos de Excel en un DataFrame
    df = pd.read_excel(excel_file, sheet_name=hoja_excel)
    print('Dataframe ', df)
    print('----------------------------------------------------------------------')
    
    # Contador de archivos
    file_count = 0
    
    # Recorrer lista con cada archivo, abrir y extraer numero factura
    for x in range(0, len(new_file_name_list_sort)):
        file_count += 1
        input_file = folder_path_output + new_file_name_list_sort[x]
        print('Archivo PDF', input_file, file_count)
        print('----------------------------------------------------------------------')
        time.sleep(5)
        
        # Definicion de las Areas a capturar datos - Fecha de Factura
        bill_year_pdf = folder_path_input + 'bill_year.csv'
    
        tabula.convert_into(input_file, 
                            bill_year_pdf, 
                            output_format="csv", 
                            pages=1, 
                            area=(84.7, 300.7, 98.9, 340.9), 
                            guess=False, 
                            stream=True
                            )

        # Leer bill_year_pdf y retornar un bill_year_text
        f = open(bill_year_pdf)
        csv_f = csv.reader(f)
        bill_year_text = []
        print('csv_f: ',csv_f)
        print('--------------------------------------------------------------------------')
        for row in csv_f:
            bill_year_text.append(str(row[0]))    
        print('Fecha de Factura:', bill_year_text)
        print('--------------------------------------------------------------------------')
        
        # Separacion de elementos en nombre
        bill_year_split = re.split(pattern = r"[\' ' / ]", string = str(bill_year_text))
        print('Separacion de elementos en fecha: ', bill_year_split)
        print('--------------------------------------------------------------------------')
        print('Separacion del año: ', bill_year_split[3])
        print('--------------------------------------------------------------------------')
        
        customer_and_number_bill = str(new_file_name_list_sort[x])
        customer_split = re.split(pattern = r"[-' ' / ]", string = customer_and_number_bill)
        print('Codigo de Cliente: ', customer_split)
        print('--------------------------------------------------------------------------')
        
        # Filtrar los registros para el proveedor específico
        cliente = customer_split[0]
        print('Sucursal: ', cliente)
        print('--------------------------------------------------------------------------')

        # Cruce datos faltantes
        count_1 = 0
        for index, row in df.iterrows():

            df_nro_cliente = df.loc[index, 'nro_cliente']
            print('Nro. Cliente: ', df_nro_cliente)
            print('--------------------------------------------------------------------------')

            if str(df_nro_cliente) == str(cliente):
                count_1 += 1
                servicio = df.loc[index, 'servicio']
                proveedor = df.loc[index, 'proveedor']
                sucursal = df.loc[index, 'sucursal']
                servicio = df.loc[index, 'servicio']
                print('Datos del Dataframe: ', servicio, proveedor, sucursal, count_1)
                print('--------------------------------------------------------------------------')
                break
        
        # Validar carpetas y mover archivos
        def crear_carpeta_si_no_existe(carpeta):
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
                
        # Validar y crear la carpeta de sucursal
        carpeta_sucursal = os.path.join(folder_path_onedrive, sucursal)
        crear_carpeta_si_no_existe(carpeta_sucursal)

        # Validar y crear la carpeta de servicio
        carpeta_servicio = os.path.join(carpeta_sucursal, servicio)
        crear_carpeta_si_no_existe(carpeta_servicio)

        # Validar y crear la carpeta de proveedor
        carpeta_proveedor = os.path.join(carpeta_servicio, proveedor)
        crear_carpeta_si_no_existe(carpeta_proveedor)

        # Validar y crear la carpeta de año
        carpeta_año = os.path.join(carpeta_proveedor, bill_year_split[3])
        crear_carpeta_si_no_existe(carpeta_año)

        # Mover archivo desde carpeta output a la nueva ubicación
        archivo_origen = input_file #"/ruta/carpeta/output/archivo.txt"
        archivo_destino = os.path.join(carpeta_año, new_file_name_list_sort[x]) #"archivo.txt"
        shutil.move(archivo_origen, archivo_destino)
                    

if __name__ == '__main__':
    
    # Obtener en una lista todos los archivos 
    FOLDER_PATH_INPUT = '../input/'
    FOLDER_PATH_OUTPUT = '../output/'
    FOLDER_PATH_CONFIG = '../config/'
    FOLDER_PATH_ONEDRIVE = 'C:/Users/admin/OneDrive - RODA ENERGIA/Macrobots/Abastible/Input/'
    
    upload_file(folder_path_input=FOLDER_PATH_INPUT, 
                folder_path_output=FOLDER_PATH_OUTPUT, 
                folder_path_config=FOLDER_PATH_CONFIG,
                folder_path_onedrive=FOLDER_PATH_ONEDRIVE
                )
    