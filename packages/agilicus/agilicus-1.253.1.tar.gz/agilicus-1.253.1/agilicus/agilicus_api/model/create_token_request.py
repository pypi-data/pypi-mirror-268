"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.04.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError


def lazy_import():
    from agilicus_api.model.host_permissions import HostPermissions
    from agilicus_api.model.time_validity import TimeValidity
    from agilicus_api.model.token_scope import TokenScope
    from agilicus_api.model.token_validity import TokenValidity
    globals()['HostPermissions'] = HostPermissions
    globals()['TimeValidity'] = TimeValidity
    globals()['TokenScope'] = TokenScope
    globals()['TokenValidity'] = TokenValidity


class CreateTokenRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('scopes',): {
        },
    }

    @property
    def sub(self):
       return self.get("sub")

    @sub.setter
    def sub(self, new_value):
       self.sub = new_value

    @property
    def org(self):
       return self.get("org")

    @org.setter
    def org(self, new_value):
       self.org = new_value

    @property
    def roles(self):
       return self.get("roles")

    @roles.setter
    def roles(self, new_value):
       self.roles = new_value

    @property
    def audiences(self):
       return self.get("audiences")

    @audiences.setter
    def audiences(self, new_value):
       self.audiences = new_value

    @property
    def time_validity(self):
       return self.get("time_validity")

    @time_validity.setter
    def time_validity(self, new_value):
       self.time_validity = new_value

    @property
    def hosts(self):
       return self.get("hosts")

    @hosts.setter
    def hosts(self, new_value):
       self.hosts = new_value

    @property
    def token_validity(self):
       return self.get("token_validity")

    @token_validity.setter
    def token_validity(self, new_value):
       self.token_validity = new_value

    @property
    def session(self):
       return self.get("session")

    @session.setter
    def session(self, new_value):
       self.session = new_value

    @property
    def scopes(self):
       return self.get("scopes")

    @scopes.setter
    def scopes(self, new_value):
       self.scopes = new_value

    @property
    def inherit_session(self):
       return self.get("inherit_session")

    @inherit_session.setter
    def inherit_session(self, new_value):
       self.inherit_session = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'sub': (str,),  # noqa: E501
            'org': (str,),  # noqa: E501
            'audiences': ([str],),  # noqa: E501
            'time_validity': (TimeValidity,),  # noqa: E501
            'roles': ({str: (str,)},),  # noqa: E501
            'hosts': ([HostPermissions],),  # noqa: E501
            'token_validity': (TokenValidity,),  # noqa: E501
            'session': (str,),  # noqa: E501
            'scopes': ([TokenScope],),  # noqa: E501
            'inherit_session': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'sub': 'sub',  # noqa: E501
        'org': 'org',  # noqa: E501
        'audiences': 'audiences',  # noqa: E501
        'time_validity': 'time_validity',  # noqa: E501
        'roles': 'roles',  # noqa: E501
        'hosts': 'hosts',  # noqa: E501
        'token_validity': 'token_validity',  # noqa: E501
        'session': 'session',  # noqa: E501
        'scopes': 'scopes',  # noqa: E501
        'inherit_session': 'inherit_session',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, sub, org, audiences, time_validity, *args, **kwargs):  # noqa: E501
        """CreateTokenRequest - a model defined in OpenAPI

        Args:
            sub (str): Unique identifier
            org (str): Unique identifier
            audiences ([str]): array of audiences
            time_validity (TimeValidity):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            roles ({str: (str,)}): associative mapping of an application to a role. [optional]  # noqa: E501
            hosts ([HostPermissions]): array of valid hosts. [optional]  # noqa: E501
            token_validity (TokenValidity): [optional]  # noqa: E501
            session (str): Unique identifier. [optional]  # noqa: E501
            scopes ([TokenScope]): The list of scopes requested for the access token. Multiple scopes are seperated by a space character. Ex. urn:agilicus:users urn:agilicus:issuers. An optional is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?. [optional]  # noqa: E501
            inherit_session (bool): When session is not provided, this option controls if the session applied to the token should come from the token making the token create request. This option is normally True, so that all tokens are chained together using the same session. This would normally be set to False when creating system orientated tokens so that they have no session, and subsequently, tokens created with this sessionless token will also not contain an inherited token (unless of course it was created with the session in the payload of the request). . [optional] if omitted the server will use the default value of True  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.sub = sub
        self.org = org
        self.audiences = audiences
        self.time_validity = time_validity
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, sub, org, audiences, time_validity, *args, **kwargs):  # noqa: E501
        """CreateTokenRequest - a model defined in OpenAPI

        Args:
            sub (str): Unique identifier
            org (str): Unique identifier
            audiences ([str]): array of audiences
            time_validity (TimeValidity):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            roles ({str: (str,)}): associative mapping of an application to a role. [optional]  # noqa: E501
            hosts ([HostPermissions]): array of valid hosts. [optional]  # noqa: E501
            token_validity (TokenValidity): [optional]  # noqa: E501
            session (str): Unique identifier. [optional]  # noqa: E501
            scopes ([TokenScope]): The list of scopes requested for the access token. Multiple scopes are seperated by a space character. Ex. urn:agilicus:users urn:agilicus:issuers. An optional is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?. [optional]  # noqa: E501
            inherit_session (bool): When session is not provided, this option controls if the session applied to the token should come from the token making the token create request. This option is normally True, so that all tokens are chained together using the same session. This would normally be set to False when creating system orientated tokens so that they have no session, and subsequently, tokens created with this sessionless token will also not contain an inherited token (unless of course it was created with the session in the payload of the request). . [optional] if omitted the server will use the default value of True  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.sub = sub
        self.org = org
        self.audiences = audiences
        self.time_validity = time_validity
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

