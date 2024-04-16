import ftplib
import socket


class FTPUtil:
    ftp_server = None

    def connect_server(self, host, user, pwd):
        ftp_server = ftplib.FTP(host, user, pwd)
        ftp_server.encoding = "utf-8"

    @classmethod
    def upload_file(cls, filepath):
        with open(filepath, "rb") as file:
            # Command for Uploading the file "STOR filename"
            cls.ftp_server.storbinary(f"STOR {filepath}", file)

    @classmethod
    def download_file(cls, filepath):
        with open(filepath, "rb") as file:
            # Command for Uploading the file "STOR filename"
            cls.ftp_server.storbinary(f"STOR {filepath}", file)


class TCPUtil:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, data):
        clientSocket = None
        dataFromServer = None
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((self.host, self.port))
            clientSocket.send(data.encode())
            dataFromServer = clientSocket.recv(1024)
        except Exception as e:
            assert False, 'Exception while sending TCP msg: ' + str(e)
        finally:
            try:
                if clientSocket is not None:
                    clientSocket.close()
            except Exception:
                pass
        return dataFromServer
