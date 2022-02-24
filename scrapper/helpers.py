class ConfigObjectHelper:
    """
    Helper class to set up a configuration object
    """

    @staticmethod
    def is_builtin_attr(attr: str):
        """Checks if the attribute is a python builtin attribute

        Args:
            attr: Attribute name

        Returns:
            Boolean
        """

        return attr.startswith('__') and attr.endswith('__')

    @staticmethod
    def is_method(attr: str, obj: object):
        """Checks if the attribute is a method or a function

        Args:
            attr: Attribute name
            obj: Object to check if the passed attribute is a function/method

        Returns:
            Boolean
        """

        return callable(getattr(obj, attr))

    @staticmethod
    def is_valid_attribute(attr: str, obj: object):
        """Checks if the attribute is not a python builtin attribute
        neither a method or a function

        Args:
            attr: Attribute name
            obj: Object to check if the passed attribute is a valid one

        Returns:
            Boolean
        """

        return not ConfigObjectHelper.is_builtin_attr(attr) and \
               not ConfigObjectHelper.is_method(attr, obj)

    @staticmethod
    def has_required_attributes(obj: object, required_attributes: list = None):
        """Check if the config object has all required attributes
        for the class to work properly

        Args:
            obj: Object to check if it has all required attributes
            required_attributes: List with all required attributes

        Returns:
            'True' if the object has all required attributes
        Raises:
            'AttributeError' if some of the required attributes
            are not present in config object
        """

        if not required_attributes:
            return True

        for attribute in required_attributes:
            if attribute not in dir(obj):
                raise AttributeError(
                    f"'{attribute}' attribute MUST be provided in config object"
                )

        return True
