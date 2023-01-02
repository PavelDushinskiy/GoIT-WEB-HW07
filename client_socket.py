import socket


def client_main():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
    except ConnectionError:
        print(f'Сервер {host, port} не знайдено')
        exit()
    message = input('>> ').lower().strip()
    print(f"З'єднання встановлено {host, port}")
    try:
        if len(message) > 0:
            while message != 'exit':
                client_socket.send(message.encode())
                message_from_server = client_socket.recv(256).decode()
                print(f'Отримано сповіщення: {message_from_server}')
                message = input('>> ').lower().strip()
                if len(message) == 0:
                    break
    except KeyboardInterrupt:
        print(f'Клієнт зупинено')
    finally:
        client_socket.close()


if __name__ == '__main__':
    client_main()
