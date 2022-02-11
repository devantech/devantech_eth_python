# devantech_eth

A python3 library for controlling the Devantech ETHxxx range of modules.

This library works with:

* [ETH002-B](https://www.robot-electronics.co.uk/eth002b.html)
* [ETH008-B](https://www.robot-electronics.co.uk/eth008b.html)
* [ETH484-B](https://www.robot-electronics.co.uk/eth484b.html)
* [ETH8020-B](https://www.robot-electronics.co.uk/products/relay-modules/ethernet-relay/eth8020-20-x-16a-ethernet-relay.html)

# Install

You can install the module with pip.

```
pip -m install devantech-eth
```

# Getting started

This example shows creating an instance of the ETH002 class, connecting to the module and toggling relay one.

```python
# import the eth002 module from devantech-eth
from devantech_eth import eth002

# Create an instance of the ETH002 class and try connecting to the module
module = eth002.ETH002(ip = "192.168.0.100", port = 17494, password = "password")
module.connect()

# Toggle digital output 1
module.toggleDO1()

# Close the connection to the module
module.close()
```

This example shows creating an instance of the ETH484 class, connecting to the module and reading the value of an analogue input.

```python
# import the eth484 module
from devantech_eth import eth484

# create an instance of the ETH484 class and connect to the module
module = eth484.ETH484(ip = "192.168.0.100", port = 17494, password = "password")
module.connect()

# Get and print the value of analogue input 1
value = module.getAI1Value()
print(value)

# Close the connection to the module.
module.close()
```
# Source

The source for this library is available on [github](https://github.com/devantech/devantech_eth_python)
