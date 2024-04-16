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
    from agilicus_api.model.desktop_connection_info import DesktopConnectionInfo
    from agilicus_api.model.desktop_remote_app import DesktopRemoteApp
    from agilicus_api.model.k8s_slug import K8sSlug
    from agilicus_api.model.network_service_config import NetworkServiceConfig
    from agilicus_api.model.resource_config import ResourceConfig
    globals()['DesktopConnectionInfo'] = DesktopConnectionInfo
    globals()['DesktopRemoteApp'] = DesktopRemoteApp
    globals()['K8sSlug'] = K8sSlug
    globals()['NetworkServiceConfig'] = NetworkServiceConfig
    globals()['ResourceConfig'] = ResourceConfig


class DesktopResourceSpec(ModelNormal):
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
        ('desktop_type',): {
            'RDP': "rdp",
            'VNC': "vnc",
        },
        ('session_type',): {
            'USER': "user",
            'ADMIN': "admin",
        },
    }

    validations = {
        ('name',): {
            'max_length': 100,
            'regex': {
                'pattern': r'^[a-zA-Z0-9-_.:]+$',  # noqa: E501
            },
        },
    }

    @property
    def name(self):
       return self.get("name")

    @name.setter
    def name(self, new_value):
       self.name = new_value

    @property
    def address(self):
       return self.get("address")

    @address.setter
    def address(self, new_value):
       self.address = new_value

    @property
    def config(self):
       return self.get("config")

    @config.setter
    def config(self, new_value):
       self.config = new_value

    @property
    def desktop_type(self):
       return self.get("desktop_type")

    @desktop_type.setter
    def desktop_type(self, new_value):
       self.desktop_type = new_value

    @property
    def session_type(self):
       return self.get("session_type")

    @session_type.setter
    def session_type(self, new_value):
       self.session_type = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def connector_id(self):
       return self.get("connector_id")

    @connector_id.setter
    def connector_id(self, new_value):
       self.connector_id = new_value

    @property
    def name_slug(self):
       return self.get("name_slug")

    @name_slug.setter
    def name_slug(self, new_value):
       self.name_slug = new_value

    @property
    def connection_info(self):
       return self.get("connection_info")

    @connection_info.setter
    def connection_info(self, new_value):
       self.connection_info = new_value

    @property
    def remote_app(self):
       return self.get("remote_app")

    @remote_app.setter
    def remote_app(self, new_value):
       self.remote_app = new_value

    @property
    def resource_config(self):
       return self.get("resource_config")

    @resource_config.setter
    def resource_config(self, new_value):
       self.resource_config = new_value

    @property
    def allow_non_domain_joined_users(self):
       return self.get("allow_non_domain_joined_users")

    @allow_non_domain_joined_users.setter
    def allow_non_domain_joined_users(self, new_value):
       self.allow_non_domain_joined_users = new_value

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
            'name': (str,),  # noqa: E501
            'address': (str,),  # noqa: E501
            'desktop_type': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'config': (NetworkServiceConfig,),  # noqa: E501
            'session_type': (str,),  # noqa: E501
            'connector_id': (str,),  # noqa: E501
            'name_slug': (K8sSlug,),  # noqa: E501
            'connection_info': (DesktopConnectionInfo,),  # noqa: E501
            'remote_app': (DesktopRemoteApp,),  # noqa: E501
            'resource_config': (ResourceConfig,),  # noqa: E501
            'allow_non_domain_joined_users': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'address': 'address',  # noqa: E501
        'desktop_type': 'desktop_type',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'config': 'config',  # noqa: E501
        'session_type': 'session_type',  # noqa: E501
        'connector_id': 'connector_id',  # noqa: E501
        'name_slug': 'name_slug',  # noqa: E501
        'connection_info': 'connection_info',  # noqa: E501
        'remote_app': 'remote_app',  # noqa: E501
        'resource_config': 'resource_config',  # noqa: E501
        'allow_non_domain_joined_users': 'allow_non_domain_joined_users',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, address, desktop_type, org_id, *args, **kwargs):  # noqa: E501
        """DesktopResourceSpec - a model defined in OpenAPI

        Args:
            name (str): The name of the DesktopResource. This uniquely identifies the DesktopResource within the organisation. 
            address (str): The hostname or IP of the DesktopResource. A Desktop Gateway will proxy requests from the client through to this address via the Connector associated with this gateway using `connector_id`. 
            desktop_type (str): The type of desktop represented by this DesktopResource. The type identifies which protocol will be used to communicate with it. The possible types are:   - `rdp`: Remote Desktop Protocol (RDP). This allows clients which support RDP to connect to a desktop     running an RDP server.   - 'vnc': Virtual Network Computing protocol (VNC). This allows the clients that support VNC to connect to a     desktop running a VNC server 
            org_id (str): Unique identifier

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
            config (NetworkServiceConfig): [optional]  # noqa: E501
            session_type (str): The internal session type. In Microsoft Remote Desktop, `admin` means console.   - `admin`: Connect to the console (session id = 0)   - `user`: Create a new user session, which might sign out the console depending on setup. . [optional] if omitted the server will use the default value of "user"  # noqa: E501
            connector_id (str): Unique identifier. [optional]  # noqa: E501
            name_slug (K8sSlug): [optional]  # noqa: E501
            connection_info (DesktopConnectionInfo): [optional]  # noqa: E501
            remote_app (DesktopRemoteApp): [optional]  # noqa: E501
            resource_config (ResourceConfig): [optional]  # noqa: E501
            allow_non_domain_joined_users (bool): Whether to allow non-domian-joined users. If true, append relavant properties for user's RDP session . [optional]  # noqa: E501
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

        self.name = name
        self.address = address
        self.desktop_type = desktop_type
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
    def __init__(self, name, address, desktop_type, org_id, *args, **kwargs):  # noqa: E501
        """DesktopResourceSpec - a model defined in OpenAPI

        Args:
            name (str): The name of the DesktopResource. This uniquely identifies the DesktopResource within the organisation. 
            address (str): The hostname or IP of the DesktopResource. A Desktop Gateway will proxy requests from the client through to this address via the Connector associated with this gateway using `connector_id`. 
            desktop_type (str): The type of desktop represented by this DesktopResource. The type identifies which protocol will be used to communicate with it. The possible types are:   - `rdp`: Remote Desktop Protocol (RDP). This allows clients which support RDP to connect to a desktop     running an RDP server.   - 'vnc': Virtual Network Computing protocol (VNC). This allows the clients that support VNC to connect to a     desktop running a VNC server 
            org_id (str): Unique identifier

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
            config (NetworkServiceConfig): [optional]  # noqa: E501
            session_type (str): The internal session type. In Microsoft Remote Desktop, `admin` means console.   - `admin`: Connect to the console (session id = 0)   - `user`: Create a new user session, which might sign out the console depending on setup. . [optional] if omitted the server will use the default value of "user"  # noqa: E501
            connector_id (str): Unique identifier. [optional]  # noqa: E501
            name_slug (K8sSlug): [optional]  # noqa: E501
            connection_info (DesktopConnectionInfo): [optional]  # noqa: E501
            remote_app (DesktopRemoteApp): [optional]  # noqa: E501
            resource_config (ResourceConfig): [optional]  # noqa: E501
            allow_non_domain_joined_users (bool): Whether to allow non-domian-joined users. If true, append relavant properties for user's RDP session . [optional]  # noqa: E501
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

        self.name = name
        self.address = address
        self.desktop_type = desktop_type
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

