CRC (Cyclic Redundancy Check) Program in Python

This is a Python implementation of the Cyclic Redundancy Check (CRC) algorithm. CRC is commonly used for error-checking in digital networks and storage devices to detect accidental changes to raw data.

This program computes the CRC checksum for a given input message using a specified CRC polynomial and returns both the checksum and the transmitted message (message with appended checksum).

Features
Supports any CRC polynomial: You can specify the polynomial used for the CRC computation.
Message validation: Verify whether the received message has been transmitted without error.
Customizable CRC width: Adjust the width of the CRC (e.g., 8-bit, 16-bit, 32-bit).
CRC Algorithm
The CRC algorithm takes a binary message and performs division using binary arithmetic with a predetermined generator polynomial. The remainder of this division is the CRC code, which is appended to the original message.

CRC Formula

R(x) = M(x) * x^k % G(x)
Where:

M(x) is the original message.
G(x) is the generator polynomial.
x^k is a power of 2 used to shift the message.
This program simulates the CRC calculation process and checks the integrity of transmitted messages.

Requirements
Python 3.x
No external dependencies are required.

Installation
Clone the repository or download the crc.py file directly:

bash
Copy code
git clone https://github.com/rafailsialakis/Cyclic-Redundancy-Check
cd crc-python
Ensure you have Python 3 installed by running:

bash
Copy code
python3 --version
Usage
You can run the program from the command line or use it within another Python project.

Command-line Usage:
Open a terminal and navigate to the directory where crc.py is located.
Run the Python script:
bash
Copy code
python3 crc.py
By default, the program will ask for a message and a polynomial (in binary format).

Parameters:
Message: The binary input message to calculate the CRC for.
Polynomial: The binary representation of the generator polynomial.
Example:
If your message is 1101011011 and your polynomial is 10011:

bash
Copy code
Enter the message (binary): 1101011011
Enter the CRC polynomial (binary): 10011
