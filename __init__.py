from code.app import Scraper
#import smtplib


def send_notification():
    # Código para enviar correo electrónico de notificación
    print('')

if __name__ == '__main__':
    url = 'https://www.essbio.cl/'
    email = '77528709-8'
    password = '@test_essbiO1'
    driver_path = 'chromedriver.exe'
    scraper = Scraper(url, email, password, driver_path)
    scraper.login()
    scraper.scraper()
    scraper.upload()
    
    scraper.close()
    #send_notification()
    # Código para guardar los datos descargados en una ruta específica
