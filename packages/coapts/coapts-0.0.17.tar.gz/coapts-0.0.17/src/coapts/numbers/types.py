# SPDX-FileCopyrightText: Christian Amsüss and the aiocoap contributors
#
# SPDX-License-Identifier: MIT

"""List of known values for the CoAP "Type" field.

As this field is only 2 bits, its valid values are comprehensively enumerated
in the `Type` object.
"""

from enum import IntEnum

class Type(IntEnum):
    CON = 1 # Confirmable
    NON = 3 # Non-confirmable
    ACK = 0 # Acknowledgement
    RST = 2 # Reset

    def __str__(self):
        return self.name

CON, NON, ACK, RST = Type.CON, Type.NON, Type.ACK, Type.RST

__all__ = ['Type', 'CON', 'NON', 'ACK', 'RST']
