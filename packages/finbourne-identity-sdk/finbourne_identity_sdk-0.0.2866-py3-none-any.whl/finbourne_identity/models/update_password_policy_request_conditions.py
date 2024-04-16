# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2866
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_identity.configuration import Configuration


class UpdatePasswordPolicyRequestConditions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'complexity': 'UpdatePasswordPolicyRequestComplexity',
        'age': 'UpdatePasswordPolicyRequestAge',
        'lockout': 'UpdatePasswordPolicyRequestLockout'
    }

    attribute_map = {
        'complexity': 'complexity',
        'age': 'age',
        'lockout': 'lockout'
    }

    required_map = {
        'complexity': 'required',
        'age': 'required',
        'lockout': 'required'
    }

    def __init__(self, complexity=None, age=None, lockout=None, local_vars_configuration=None):  # noqa: E501
        """UpdatePasswordPolicyRequestConditions - a model defined in OpenAPI"
        
        :param complexity:  (required)
        :type complexity: finbourne_identity.UpdatePasswordPolicyRequestComplexity
        :param age:  (required)
        :type age: finbourne_identity.UpdatePasswordPolicyRequestAge
        :param lockout:  (required)
        :type lockout: finbourne_identity.UpdatePasswordPolicyRequestLockout

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._complexity = None
        self._age = None
        self._lockout = None
        self.discriminator = None

        self.complexity = complexity
        self.age = age
        self.lockout = lockout

    @property
    def complexity(self):
        """Gets the complexity of this UpdatePasswordPolicyRequestConditions.  # noqa: E501


        :return: The complexity of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :rtype: finbourne_identity.UpdatePasswordPolicyRequestComplexity
        """
        return self._complexity

    @complexity.setter
    def complexity(self, complexity):
        """Sets the complexity of this UpdatePasswordPolicyRequestConditions.


        :param complexity: The complexity of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :type complexity: finbourne_identity.UpdatePasswordPolicyRequestComplexity
        """
        if self.local_vars_configuration.client_side_validation and complexity is None:  # noqa: E501
            raise ValueError("Invalid value for `complexity`, must not be `None`")  # noqa: E501

        self._complexity = complexity

    @property
    def age(self):
        """Gets the age of this UpdatePasswordPolicyRequestConditions.  # noqa: E501


        :return: The age of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :rtype: finbourne_identity.UpdatePasswordPolicyRequestAge
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this UpdatePasswordPolicyRequestConditions.


        :param age: The age of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :type age: finbourne_identity.UpdatePasswordPolicyRequestAge
        """
        if self.local_vars_configuration.client_side_validation and age is None:  # noqa: E501
            raise ValueError("Invalid value for `age`, must not be `None`")  # noqa: E501

        self._age = age

    @property
    def lockout(self):
        """Gets the lockout of this UpdatePasswordPolicyRequestConditions.  # noqa: E501


        :return: The lockout of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :rtype: finbourne_identity.UpdatePasswordPolicyRequestLockout
        """
        return self._lockout

    @lockout.setter
    def lockout(self, lockout):
        """Sets the lockout of this UpdatePasswordPolicyRequestConditions.


        :param lockout: The lockout of this UpdatePasswordPolicyRequestConditions.  # noqa: E501
        :type lockout: finbourne_identity.UpdatePasswordPolicyRequestLockout
        """
        if self.local_vars_configuration.client_side_validation and lockout is None:  # noqa: E501
            raise ValueError("Invalid value for `lockout`, must not be `None`")  # noqa: E501

        self._lockout = lockout

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePasswordPolicyRequestConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePasswordPolicyRequestConditions):
            return True

        return self.to_dict() != other.to_dict()
