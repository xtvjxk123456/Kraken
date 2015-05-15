"""Kraken - objects.Attributes.IntegerAttribute module.

Classes:
IntegerAttribute - Base Attribute.

"""

from kraken.core.objects.attributes.number_attribute import NumberAttribute
from kraken.core.kraken_system import ks


class IntegerAttribute(NumberAttribute):
    """Float Attribute. Implemented value type checking and limiting."""

    def __init__(self, name, value=0, minValue=None, maxValue=None, keyable=None):
        super(IntegerAttribute, self).__init__(name, value, minValue=minValue,
              maxValue=maxValue)

        assert type(self.value) is int, "Value is not of type 'int'."


    # ==============
    # Value Methods
    # ==============
    def getRTVal(self):
        """Returns and RTVal object for this attribute.

        Return:
        RTVal

        """
        return ks.rtVal('Integer', self.value)


    def validateValue(self, value):
        """Validates the incoming value is the correct type.

        Arguments:
        value -- Type, value to check the type of.

        Return:
        True if successful.

        """

        if type(value) is not int:
            return False

        return True
