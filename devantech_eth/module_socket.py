import socket

class ModuleSocket:
    """
    This class is the base class of all ETH modules.

    It contains all methods needed to manage a socket connection to an ETH module and also all methods that are common to every module type.

    Attributes:
        ip (string): The IP address of the module
        port (int): The port number of the module
        password (string): The password used to unlock the module
        moduleID (int): The expected module ID.
        socket (socket): The socket used to communicate on.
    """
    
    def __init__(self, ip = "192.168.0.2", port = 17494, password  = None, moduleID = 0):
        """
        The Constructor for the ETHModule class.
        
        Parameters:
                ip (string): The IP address of the module
                port (int): The port number of the module
                password (string): The password used to unlock the module
        """
        self.module_id = moduleID
        self.ip = ip
        self.port = port
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Tries to connect to an ETH module.

        If a connection is established it validates the module ID to make sure that we are talking to the right kind of module and then sends the password.
        """
        try:
            self.socket.connect((self.ip, self.port))
        except:
            raise
            
        if self.checkModuleID() != True:
            self.close()
            raise Exception("Received unexpected ID from module.")
        
        if self.isPasswordEnabled() == True:
            if self.sendPassword() == False:
                self.close()
                raise Exception("Wrong password sent to module.")

    def close(self):
        """
        Closes the connection to a module.
        """
        self.logout()
        self.socket.close()

    def write(self, message):
        """
        Writes data out to a module.

        Parameters:
            message (string): The data to write.
        """
        try:
            self.socket.sendall(message.encode())
        except:
            raise
            
    def read(self, number):
        """
        Reads data back from a module.

        Parameters:
            number (int): The number of bytes to read.

        Returns:
            array: The data received.
        """
        chunks = []
        bytes_received = 0
        while bytes_received < number:
            try:
                chunk = self.socket.recv(2048)
                if chunk == '':
                    raise Exception("Unable to read the expected number of bytes")
                chunks.extend(chunk)
                bytes_received = bytes_received + len(chunk)
            except:
                raise
        return chunks
                    
    def checkModuleID(self):
        """
        Checks the module is of the expected type.

        Returns:
            bool: true if the correct module is found false otherwise.
        """
        self.write("\x10")
        d = self.read(3)
        if d[0] != self.module_id:
            return False
        return True

    def isPasswordEnabled(self):
        """
        Checks to see if the password is enabled.

        Returns:
            bool: True if the password is enabled, false otherwise.
        """
        self.write("\x7a")
        d = self.read(1)
        if d[0] == 0:
            return True
        return False

    def sendPassword(self):
        """
        Sends the password to the module and checks for success.

        Returns:
            bool: True is accepted, false otherwise.
        """
        pw = "\x79" + self.password
        self.write(pw)
        d = self.read(1)
        if d[0] != 1:
            return False
        return True

    def logout(self):
        """
        Logs out of the module.
        """
        self.write("\x7b")
        d = self.read(1)
    
    def getSerialNumber(self):
        """
        Gets the serial number from the module.

        Returns:
            array: The 5 byte mac address read back from the module.
        """
        self.write("\x77")
        return self.read(6)

    def getVolts(self):
        """
        Reads the voltage back from the module.

        Returns:
            float: the voltage.
        """
        self.write("\x78")
        d = self.read(1)
        vl = d[0] / 10
        return vl

    def getModuleInfo(self):
        """
        Gets the module info.

        Returns:
            array: the module ID, hardware and firmware versions.
        """
        self.write("\x10")
        d = self.read(3)
        return d

    def getModuleID(self):
        """
        Get the module ID.

        Returns:
            byte: The module ID
        """
        d = self.getModuleInfo()
        return d[0]

    def getHardwareVersion(self):
        """
        Get the hardware version.

        Returns:
            byte: The hardware version.
        """
        d = self.getModuleInfo()
        return d[1]

    def getFirmwareVersion(self):
        """
        Get the firmware version.

        Returns:
            byte: The firmware version.
        """
        d = self.getModuleInfo()
        return d[2]        
        
    def digitalActive(self, port, pulse):
        """
        Set a digital output active.

        Parameters:
            port (int): The digital io port to set.
            pulse (int): The pulse time for the change.
        """
        message = "\x20"
        message += chr(port)
        message += chr(pulse)
        self.write(message)
        d = self.read(1)
                
    def digitalInactive(self, port, pulse):
        """
        Set a digital output inactive.

        Parameters:
            port (int): The digital io port to set.
            pulse (int): The pulse time for the change.
        """
        message = "\x21"
        message += chr(port)
        message += chr(pulse)
        self.write(message)
        d = self.read(1)

    def setDigitalState(self, port, pulse, state):
        """
        Set the state of a digital output.

        Parameters:
            port (int): The digital output to set.
            pulse (int): The pulse time for the change.
            state (int): The state to set, 0 for inactive, otherwise active.
        """
        if state == 0:
           self. digitalInactive(port, pulse)
        else:
            self.digitalActive(port, pulse)
