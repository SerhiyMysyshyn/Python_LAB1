import socket
import sys

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Задаю сім'ю протоколів і тип передачі даних
tcp_socket.connect(("localhost", 777))                                  # Прив'язую сокет до мережевого адаптера

while True:
    data = input('  [ Client -> Server ] : ')                           # Поле для вводу інформації з боку клієнта
    if not data:                                                        # Перевіряю дані: чи не пусте значення
        tcp_socket.close()                                              # У разі виконання -> закриваю сокет і для клієнта
        print("\n[ ! ] Connection closed")
        sys.exit(1)
    dataSize = len(data)
    dataSize = dataSize.__str__()
    data = str.encode(data)                                             # encode - кодування в байти, decode - розкодування з байтів
    dataSize = str.encode(dataSize)

    tcp_socket.send(data)                                               # Надсилаю дані на сервер
    tcp_socket.send(dataSize)                                              # Надсилаю дані на сервер (розмір даних)

    data = bytes.decode(data)
    data = tcp_socket.recv(1024)                                        # Отримую опрацьовані дані із сервера
    print(data)                                                         # Виводжу опрацьовані дані клієнту
    break

tcp_socket.close()


