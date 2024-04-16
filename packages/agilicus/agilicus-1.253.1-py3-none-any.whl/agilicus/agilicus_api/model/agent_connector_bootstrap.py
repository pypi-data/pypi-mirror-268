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



class AgentConnectorBootstrap(ModelNormal):
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
        ('api_key',): {
            'max_length': 40,
            'min_length': 1,
            'regex': {
                'pattern': r'[0-9a-zA-Z]+',  # noqa: E501
            },
        },
        ('api_key_user',): {
            'max_length': 100,
            'min_length': 1,
            'regex': {
                'pattern': r'.*',  # noqa: E501
            },
        },
        ('issuer',): {
            'max_length': 1024,
            'min_length': 1,
            'regex': {
                'pattern': r'http(s)?:\/\/.*',  # noqa: E501
            },
        },
        ('org_id',): {
            'max_length': 40,
            'min_length': 1,
            'regex': {
                'pattern': r'[0-9a-zA-Z]+',  # noqa: E501
            },
        },
        ('response_challenge_id',): {
            'max_length': 40,
            'min_length': 1,
            'regex': {
                'pattern': r'[0-9a-zA-Z]+',  # noqa: E501
            },
        },
        ('response_challenge_code',): {
            'max_length': 40,
            'min_length': 1,
            'regex': {
                'pattern': r'[0-9a-zA-Z]+',  # noqa: E501
            },
        },
    }

    @property
    def api_key(self):
       return self.get("api_key")

    @api_key.setter
    def api_key(self, new_value):
       self.api_key = new_value

    @property
    def api_key_user(self):
       return self.get("api_key_user")

    @api_key_user.setter
    def api_key_user(self, new_value):
       self.api_key_user = new_value

    @property
    def issuer(self):
       return self.get("issuer")

    @issuer.setter
    def issuer(self, new_value):
       self.issuer = new_value

    @property
    def connector_id(self):
       return self.get("connector_id")

    @connector_id.setter
    def connector_id(self, new_value):
       self.connector_id = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def join_cluster(self):
       return self.get("join_cluster")

    @join_cluster.setter
    def join_cluster(self, new_value):
       self.join_cluster = new_value

    @property
    def response_challenge_id(self):
       return self.get("response_challenge_id")

    @response_challenge_id.setter
    def response_challenge_id(self, new_value):
       self.response_challenge_id = new_value

    @property
    def response_challenge_code(self):
       return self.get("response_challenge_code")

    @response_challenge_code.setter
    def response_challenge_code(self, new_value):
       self.response_challenge_code = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'api_key': (str,),  # noqa: E501
            'api_key_user': (str,),  # noqa: E501
            'issuer': (str,),  # noqa: E501
            'connector_id': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'join_cluster': (bool,),  # noqa: E501
            'response_challenge_id': (str,),  # noqa: E501
            'response_challenge_code': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'api_key': 'api_key',  # noqa: E501
        'api_key_user': 'api_key_user',  # noqa: E501
        'issuer': 'issuer',  # noqa: E501
        'connector_id': 'connector_id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'join_cluster': 'join_cluster',  # noqa: E501
        'response_challenge_id': 'response_challenge_id',  # noqa: E501
        'response_challenge_code': 'response_challenge_code',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, api_key, api_key_user, issuer, connector_id, org_id, *args, **kwargs):  # noqa: E501
        """AgentConnectorBootstrap - a model defined in OpenAPI

        Args:
            api_key (str): The secret api key that can be used to bootstrap the connector 
            api_key_user (str): The username/email/etc to provide alongside the api key when authenticating using it. 
            issuer (str): The url of the issuer for the connector to log in to 
            connector_id (str): The unique ID of the connector 
            org_id (str): The unique ID of the organisation the connector belongs to. 

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
            join_cluster (bool): Whether to join a cluster or create a new one. If false or not set, a new cluster is created. [optional]  # noqa: E501
            response_challenge_id (str): The ID of a challenge to respond to indicating that the install finished. . [optional]  # noqa: E501
            response_challenge_code (str): The code of a challenge to respond to indicating that the install finished. . [optional]  # noqa: E501
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

        self.api_key = api_key
        self.api_key_user = api_key_user
        self.issuer = issuer
        self.connector_id = connector_id
        self.org_id = org_id
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
    def __init__(self, api_key, api_key_user, issuer, connector_id, org_id, *args, **kwargs):  # noqa: E501
        """AgentConnectorBootstrap - a model defined in OpenAPI

        Args:
            api_key (str): The secret api key that can be used to bootstrap the connector 
            api_key_user (str): The username/email/etc to provide alongside the api key when authenticating using it. 
            issuer (str): The url of the issuer for the connector to log in to 
            connector_id (str): The unique ID of the connector 
            org_id (str): The unique ID of the organisation the connector belongs to. 

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
            join_cluster (bool): Whether to join a cluster or create a new one. If false or not set, a new cluster is created. [optional]  # noqa: E501
            response_challenge_id (str): The ID of a challenge to respond to indicating that the install finished. . [optional]  # noqa: E501
            response_challenge_code (str): The code of a challenge to respond to indicating that the install finished. . [optional]  # noqa: E501
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

        self.api_key = api_key
        self.api_key_user = api_key_user
        self.issuer = issuer
        self.connector_id = connector_id
        self.org_id = org_id
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

