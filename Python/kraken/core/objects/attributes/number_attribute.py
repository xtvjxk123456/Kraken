"""Kraken - objects.Attributes.NumberAttribute module.

Classes:
NumberAttribute - Base Attribute.

"""

from kraken.core.objects.attributes.attribute import Attribute


class NumberAttribute(Attribute):
    """Number Attributee. Base class for number attribute types"""

    def __init__(self, name, value=0, minValue=None, maxValue=None, parent=None):
        super(NumberAttribute, self).__init__(name, value=value, parent=parent)

        self._min = minValue
        self._max = maxValue
        self._uiMin = minValue
        self._uiMax = maxValue


    # ==============
    # Value Methods
    # ==============
    def setValue(self, value):
        """Sets the value of the attribute.

        Arguments:
        value -- Value to set the attribute to.

        Return:
        True if successful.

        """

        if self.validateValue(value) is False:
            raise TypeError("Value: '" + str(value) + "' has an invalid type!")

        super(NumberAttribute, self).setValue(value)

        return True


    # ==================
    # Min / Max Methods
    # ==================
    def getMin(self):
        """Gets the minimum value for this attribute.

        Return:
        Float / Integer - minimum value.

        """

        return self._min


    def setMin(self, minimum):
        """Sets the minimum value for the attribute.

        Note: Only works on float or integer attributes.

        Arguments:
        minimum -- float / integer, minimum value the attribute can have.

        Return:
        True if successful.

        """

        assert type(minimum) in (int, float) or minimum is not None, "'minimum' is not of type 'int', 'float', or None."

        self._min = minimum

        return True


    def getMax(self):
        """Gets the maximum value for this attribute.

        Return:
        Float / Integer - maximum value.

        """

        return self._max


    def setMax(self, maximum):
        """Sets the maximum value for the attribute.

        Note: Only works on float or integer attributes.

        Arguments:
        maximum -- float / integer, maximum value the attribute can have.

        Return:
        True if successful.

        """

        assert type(maximum) in (int, float) or maximum is not None, "'maximum' is not of type 'int', 'float', or None."

        self._max = maximum

        return True


    def getUIMin(self):
        """Gets the default minimum ui slider value for this attribute.

        Return:
        Float / Integer - default minimum ui slider value.

        """

        return self._uiMin


    def setUIMin(self, minimum):
        """Sets the default minimum ui slider value for the attribute.

        Note: Only works on float or integer attributes.

        Arguments:
        minimum -- float / integer, default minimum ui slider value.

        Return:
        True if successful.

        """

        if self.isTypeOf('IntegerAttribute'):
            if type(minimum) is not int or minimum is not None:
                raise TypeError("UiMin value is not of type 'int' or None.")

        if self.isTypeOf('ScalarAttribute'):
            if type(minimum) not in (int, float) or minimum is not None:
                raise TypeError("UiMin value is not of type 'int', 'float' or None.")

        if minimum is not None and minimum < self._min:
            raise ValueError('UiMin value is less than attribute minimum')

        self._uiMin = minimum

        return True


    def getUIMax(self):
        """Gets the default maximum ui slider value for this attribute.

        Return:
        Float / Integer - default maximum ui slider value.

        """

        return self._uiMax


    def setUIMax(self, maximum):
        """Sets the default maximum ui slider value for the attribute.

        Note: Only works on float or integer attributes.

        Arguments:
        maximum -- float / integer, default maximum ui slider value.

        Return:
        True if successful.

        """

        if self.isTypeOf('IntegerAttribute'):
            if type(maximum) is not int or maximum is not None:
                raise TypeError("UiMax value is not of type 'int' or None.")

        if self.isTypeOf('ScalarAttribute'):
            if type(maximum) not in (int, float) or maximum is not None:
                raise TypeError("UiMax value is not of type 'int','float', or None.")

        if maximum is not None and maximum > self._max:
            raise ValueError('UiMax value is greater than attribute maximum')

        self._uiMax = maximum

        return True
