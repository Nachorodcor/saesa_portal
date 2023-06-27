import os
import re
import csv
import time
import shutil
import tabula
import PyPDF2

from PyPDF2 import PdfReader

def rename_file(folder_path_input, folder_path_output):
    print('Entrando en la funcion upload...')
    print('----------------------------------------------------------------------')
    
    # Variable array
    file_name_list = []
    
    # Bucle para obtener lista de nombre de archivos
    for add_file_list in os.listdir(folder_path_input):
        if add_file_list.endswith(".pdf"):
            file_name_list.append(add_file_list)
    
    print('Cantidad Elem. file_name_list: ', len(file_name_list))
    print('----------------------------------------------------------------------')
    
    # Ordenar lista de archivos por nombre
    new_file_name_list_sort = sorted(file_name_list)
    print('file_name_list_sort: ', new_file_name_list_sort, len(new_file_name_list_sort))
    print('----------------------------------------------------------------------')
    
    # Contador de archivos
    file_count = 0
    
    # Recorrer lista con cada archivo, abrir y extraer numero factura
    for x in range(0, len(new_file_name_list_sort)):
        file_count += 1
        input_file = folder_path_input + new_file_name_list_sort[x]
        print('Archivo PDF', input_file, file_count)
        print('----------------------------------------------------------------------')
        time.sleep(5)
        
        # Determinar cuantas paginas tiene el pdf
        pdfFileObj = open(input_file, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        print('Numero de paginas:', pdfReader.pages)
        print('----------------------------------------------------------------------')        

        # Definicion de las Areas a capturar datos - Numero de Factura
        bill_number_pdf = folder_path_input + 'bill_number.csv'
        
        tabula.convert_into(input_file, 
                            bill_number_pdf, 
                            output_format="csv", 
                            pages=1, 
                            area=(41.9, 279.7, 56.3, 319.9), 
                            guess=False, 
                            stream=True
                            )
        
        # Leer bill_number_pdf y retornar un bill_number_text
        f = open(bill_number_pdf)
        csv_f = csv.reader(f)
        bill_number_text = []
        print('csv_f: ',csv_f)
        print('--------------------------------------------------------------------------')
        for row in csv_f:
            bill_number_text.append(str(row[0]))    
        print('Numero de Factura:', bill_number_text)
        print('--------------------------------------------------------------------------')
        
        # Separacion de elementos en nombre
        file_name_split = re.split(pattern = r"[_/'' / ]", string = str(new_file_name_list_sort[x]))
        print('Separacion de elementos en nombre: ', file_name_split)
        print('--------------------------------------------------------------------------')
        
        # Componer nuevo nombre
        new_file_name_combined = str(file_name_split[0])+'-'+str(bill_number_text[1])+'.pdf'
        print('Nuevo nombre compuesto: ', new_file_name_combined)
        print('--------------------------------------------------------------------------')
                
        # Mover a la carpeta output con el nuevo nombre
        source = input_file
        dest = folder_path_output + new_file_name_combined
        shutil.copy(source, dest)
        print('Copiando archivo a nuevo destino: ', source, dest)
        print('--------------------------------------------------------------------------')        
        
    
if __name__ == '__main__':
    
    # Obtener en una lista todos los archivos 
    FOLDER_PATH_INPUT = '../input/'
    FOLDER_PATH_OUTPUT = '../output/'
    
    rename_file(folder_path_input=FOLDER_PATH_INPUT, folder_path_output=FOLDER_PATH_OUTPUT)
    
    
