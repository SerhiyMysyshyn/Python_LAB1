import socket
import sys

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Задаю сім'ю протоколів і тип передачі даних
tcp_socket.connect(("localhost", 777))                                  # Прив'язую сокет до мережевого адаптера

while True:
    data = input('  [ Client -> Server ] : ')                           # Поле для вводу інформації з боку клієнта
    if not data or data=="/close_connection":                           # Перевіряю дані: чи не пусте значення, чи не спец.фраза для закриття з'єднання
        tcp_socket.close()                                              # У разі виконання -> закриваю сокет і для клієнта
        print("\n[ ! ] Connection closed")
        sys.exit(1)
    data = str.encode(data)                                             # encode - кодування в байти, decode - розкодування з байтів
    tcp_socket.send(data)                                               # Надсилаю дані на сервер
    data = bytes.decode(data)
    data = tcp_socket.recv(1024)                                        # Отримую опрацьовані дані із сервера
    print(data)                                                         # Виводжу опрацьовані дані клієнту
    print()

# /close_connection - команда для закриття з'єднання