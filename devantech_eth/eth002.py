from devantech_eth import module_socket

class ETH002(module_socket.ModuleSocket):
    """
    This class provides all the methods needed for easily controlling an ETH002.
                   
    """
    
    def __init__(self, ip = "192.168.0.2", port = 17494, password = None):
        """
        The constructor for the ETH002 class.

        Parameters:
            ip: (string): The IP address of the module
            port (int): The port number of the module
            password (string): The password used to unlock the module. 
        """
        super().__init__( ip = ip, port = port, password = password, moduleID = 18)

    def getDigitalOutputs(self):
        """
        Get an array that represents the states of the digital outputs.

        Returns:
            array: Bytes indicating the states of the outputs.
        """
        self.write("\x24")
        d = self.read(1)
        return d

    def getDO1State(self):
        """
        Get the state of digital output 1.

        Returns:
            int: 1 for active 0 for inactive
        """
        d = self.getDigitalOutputs()
        st = 1 if d[0] & 0b00000001 else 0
        return st

    def getDO2State(self):
        """
        Get the state of digital output 2.

        Returns:
            int: 1 for active 0 for inactive
        """
        d = self.getDigitalOutputs()
        st = 1 if d[0] & 0b00000010 else 0
        return st

    def setDO1Active(self):
        """
        Sets digital output 1 to active.
        """
        self.digitalActive(1, 0)

    def setDO2Active(self):
        """
        Sets digital output 2 to active
        """
        self.digitalActive(2, 0)

    def setDO1Inactive(self):
        """
        Sets digital output 1 to inactive.
        """
        self.digitalInactive(1, 0)
    
    def setDO2Inactive(self):
        """
        Sets digital output 2 to inactive
        """
        self.digitalInactive(2, 0)

    def setDO1State(self, state):
        """
        Sets the state of digital output 1.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(1, 0, state)

    def setDO2State(self, state):
        """
        Sets the state of digital output 2.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(2, 0, state)

    def toggleDO1(self):
        """
        Toggles digital output 1.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00000001 else 1
        self.setDO1State(st)

    def toggleDO2(self):
        """
        Toggles digital output 1.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00000010 else 1
        self.setDO2State(st)
        
