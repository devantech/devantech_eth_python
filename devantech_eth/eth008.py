from devantech_eth import module_socket

class ETH008(module_socket.ModuleSocket):
    """
    This class provides all the methods needed for easily controlling an ETH008.
                   
    """
    
    def __init__(self, ip = "192.168.0.2", port = 17494, password = None):
        """
        The constructor for the ETH002 class.

        Parameters:
            ip: (string): The IP address of the module
            port (int): The port number of the module
            password (string): The password used to unlock the module. 
        """
        super().__init__( ip = ip, port = port, password = password, moduleID = 19)

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

    def getDO3State(self):
            """
            Get the state of digital output 3.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b00000100 else 0
            return st

    def getDO4State(self):
            """
            Get the state of digital output 4.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b00001000 else 0
            return st

    def getDO5State(self):
            """
            Get the state of digital output 5.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b00010000 else 0
            return st

    def getDO6State(self):
            """
            Get the state of digital output 6.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b00100000 else 0
            return st

    def getDO7State(self):
            """
            Get the state of digital output 7.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b01000000 else 0
            return st

    def getDO8State(self):
            """
            Get the state of digital output 8.

            Returns:
                int: 1 for active 0 for inactive
            """
            d = self.getDigitalOutputs()
            st = 1 if d[0] & 0b10000000 else 0
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

    def setDO3Active(self):
        """
        Sets digital output 3 to active
        """
        self.digitalActive(3, 0)

    def setDO4Active(self):
        """
        Sets digital output 4 to active
        """
        self.digitalActive(4, 0)

    def setDO5Active(self):
        """
        Sets digital output 5 to active
        """
        self.digitalActive(5, 0)

    def setDO6Active(self):
        """
        Sets digital output 6 to active
        """
        self.digitalActive(6, 0)

    def setDO7Active(self):
        """
        Sets digital output 7 to active
        """
        self.digitalActive(7, 0)

    def setDO8Active(self):
        """
        Sets digital output 8 to active
        """
        self.digitalActive(8, 0)

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
    
    def setDO3Inactive(self):
        """
        Sets digital output 3 to inactive
        """
        self.digitalInactive(3, 0)
    
    def setDO4Inactive(self):
        """
        Sets digital output 4 to inactive
        """
        self.digitalInactive(4, 0)
    
    def setDO5Inactive(self):
        """
        Sets digital output 5 to inactive
        """
        self.digitalInactive(5, 0)
    
    def setDO6Inactive(self):
        """
        Sets digital output 6 to inactive
        """
        self.digitalInactive(6, 0)
    
    def setDO7Inactive(self):
        """
        Sets digital output 7 to inactive
        """
        self.digitalInactive(7, 0)

    def setDO8Inactive(self):
        """
        Sets digital output 8 to inactive
        """
        self.digitalInactive(8, 0)

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

    def setDO3State(self, state):
        """
        Sets the state of digital output 3.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(3, 0, state)

    def setDO4State(self, state):
        """
        Sets the state of digital output 4.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(4, 0, state)

    def setDO5State(self, state):
        """
        Sets the state of digital output 5.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(5, 0, state)

    def setDO6State(self, state):
        """
        Sets the state of digital output 6.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(6, 0, state)

    def setDO7State(self, state):
        """
        Sets the state of digital output 7.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(7, 0, state)

    def setDO8State(self, state):
        """
        Sets the state of digital output 8.

        Parameters: 
            state (int): 0 for inactive, > 0 for active.
        """
        self.setDigitalState(8, 0, state)

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
        Toggles digital output 2.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00000010 else 1
        self.setDO2State(st)

    def toggleDO3(self):
        """
        Toggles digital output 3.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00000100 else 1
        self.setDO3State(st)

    def toggleDO4(self):
        """
        Toggles digital output 4.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00001000 else 1
        self.setDO4State(st)

    def toggleDO5(self):
        """
        Toggles digital output 5.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00010000 else 1
        self.setDO5State(st)

    def toggleDO6(self):
        """
        Toggles digital output 6.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b00100000 else 1
        self.setDO6State(st)

    def toggleDO7(self):
        """
        Toggles digital output 7.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b01000000 else 1
        self.setDO7State(st)

    def toggleDO8(self):
        """
        Toggles digital output 8.

        If the output is active it will become active, if it is active it will become inactive.
        """
        d = self.getDigitalOutputs()
        st = 0 if d[0] & 0b10000000 else 1
        self.setDO8State(st)
        
