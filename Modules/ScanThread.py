from threading import Thread
import nmap
import requests
import paramiko
import ftplib
import telnetlib

class ScanThread(Thread):
    def __init__(self, ip, nmap_params):
        super().__init__()
        self.ip = ip
        self.nmap_params = nmap_params

    def send_service_request(self, ip_addr, port):
        try:
            if port == 80:
                response = requests.get(f"http://{ip_addr}:{port}", timeout=5)
                print(f"HTTP-ответ от {ip_addr}:{port}: {response.status_code}")
            elif port == 22:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip_addr, port=port, username='test', password='test', timeout=5)
                ssh.close()
                print(f"SSH-подключение к {ip_addr}:{port} успешно.")
            elif port == 21:
                ftp = ftplib.FTP()
                ftp.connect(ip_addr, port=port, timeout=5)
                ftp.login(user='anonymous', passwd='')
                ftp.quit()
                print(f"FTP-подключение к {ip_addr}:{port} успешно.")
            elif port == 23:
                telnet = telnetlib.Telnet(ip_addr, port=port, timeout=5)
                telnet.close()
                print(f"Telnet-подключение к {ip_addr}:{port} успешно.")
            else:
                print(f"Нет запроса к сервису для порта {port}")

        except Exception as e:
            print(f"Ошибка при отправке запроса к {ip_addr}:{port}: {e}")

    def run(self):
        try:
            # Создаем объект-сканер
            scanner = nmap.PortScanner()

            ip_addr = self.ip

            # Выдаем ошибку, если IP нет
            if not ip_addr:
                print("IP-адрес не может быть пустым.")
                return

            # Выбираем режим сканирования
            scan_arguments = self.nmap_params

            print(f"Используемые аргументы: {scan_arguments}")

            # Сканирование портов с использованием выбранных аргументов
            print(scanner.scan(ip_addr, arguments=scan_arguments))


            print(f"\nРезультаты сканирования портов для {ip_addr}:")
            open_ports_count = 0
            total_tcp_ports = len(scanner[ip_addr].all_tcp())  # Всего портов для TCP
            for port in scanner[ip_addr]['tcp']:
                state = scanner[ip_addr]['tcp'][port]['state']
                print(f"Порт {port}: {state}")
                if state == 'open':
                    open_ports_count += 1

                    # Отправка запросов к сервисам по открытым портам
                    self.send_service_request(ip_addr, port)

        except Exception as e:
            print(f"Ошибка при сканировании портов: {e}")

        print("111")