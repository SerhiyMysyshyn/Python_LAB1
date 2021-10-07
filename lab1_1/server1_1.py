import socket
import time
from time import strftime, gmtime

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Задаю сім'ю протоколів і тип передачі даних
tcp_socket.bind(("localhost", 777))                                     # Прив'язую сокет до мережевого адаптера
tcp_socket.listen(1)                                                    # Задаю розмір черги вхідних підключень

print('[ ! ] Підключення...')
connection, address = tcp_socket.accept()                               # Отримую з'єднання із черги вхідних підключень
print('[ ! ] Підключено')
print('[ ! ] Адреса клієнта: ', address)                                # Виводжу адресу клієнта (для зручності)
print('__________________________________________________________________')
while True:
    data = connection.recv(1024)                                        # Отримую передане значення від клієнта
    newData = bytes.decode(data)                                        # Розкодовую з байтів
    dataTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())                  # Отримую значення дати і часу
    if not data or newData == "/close_connection":                      # Перевіряю дані: чи не пусте значення, чи не спец.фраза для закриття з'єднання
        connection.close()                                              # У разі виконання: закриваю з'єднання
        print("[ ! ] Connection closed")
        break
    else:
        print("[ Client -> Server ] : " + newData)                      # Виводжу надіслані дані від користувача (для зручності)
        newData = "[ Server -> Client ] : ("+dataTime+") "+newData      # Формую дані, які буду надсилати назад користувачу
        #time.sleep(5)                                                   # Задаю затримку відповіді сервера
        print(newData)                                                  # Виводжу дані, які будуть надіслані назад користувачу (для зручності)
        data = str.encode(newData)                                      # Кодую дані для відправки в байти
        connection.send(data)                                           # Надсилаю дані назад користувачу
        print("")

tcp_socket.close()                                                      # Закриваю сокет