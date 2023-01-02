import socket


def server_main():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f"З'єднання встановлено {host, port}")
    try:
        while True:
            message_from_client = conn.recv(1024).decode()
            if not message_from_client:
                print(message_from_client, 'break')
                break
            print(f'Отримано сповіщення: {message_from_client}')
            message = input('>> ')
            conn.send(message.encode())
    except KeyboardInterrupt:
        print(f'Сервер зупинено')
    finally:
        conn.close()


if __name__ == '__main__':
    server_main()
