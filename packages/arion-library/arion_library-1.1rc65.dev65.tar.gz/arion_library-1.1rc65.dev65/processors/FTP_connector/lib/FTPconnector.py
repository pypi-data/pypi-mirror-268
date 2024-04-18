

from ftplib import FTP
import logging
logger = logging.getLogger(__name__)
class FTPconnector:
    def __init__(
            self,
            host:str,
            port:int = 21,
            username: str="",
            password: str=""
            ):
        
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ftp = None
    
    def connect(self):
        try:
            self.ftp = FTP()
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            logger.info(f"Connected to {self.host}")
        except Exception as e:
            logger.info(f"Error connecting to {self.host}: {e}")
            self.disconnect()

    def disconnect(self):
        if self.ftp:
            self.ftp.quit()
            logger.info(f"Disconnected from {self.host}")
            self.ftp = None

    def list_files(self):
        if self.ftp:
            try:
                files = self.ftp.nlst()
                logger.info(f"Files in current directory: {files}")
            except Exception as e:
                logger.info(f"Error listing files: {e}")
        else:
            logger.error("Not connected to any FTP server.")

    def change_dir(self, path:str):
        if self.ftp:
            try:
                self.ftp.cwd(path)
                logger.info(f"Changed directory to {path}")
            except Exception as e:
                logger.error(f"Error changing directory: {e}")
        else:
            logger.info("Not connected to any FTP server.")
    
    def download_file(self, remote_path:str, local_path:str):
        if self.ftp:
            try:
                self.ftp.retrbinary(f"RETR {remote_path}", open(local_path, 'wb').write)
                logger.info(f"Downloaded {remote_path} to {local_path}")
            except Exception as e:
                logger.error(f"Error downloading file: {e}")
        else:
            logger.info("Not connected to any FTP server.")
    
    def upload_file(self, local_path:str, remote_path:str):
        if self.ftp:
            try:
                with open(local_path, 'rb') as f:
                    self.ftp.storbinary(f"STOR {remote_path}", f)
                logger.info(f"Uploaded {local_path} to {remote_path}")
            except Exception as e:
                logger.info(f"Error uploading file: {e}")
        else:
            logger.info("Not connected to any FTP server.")

    
