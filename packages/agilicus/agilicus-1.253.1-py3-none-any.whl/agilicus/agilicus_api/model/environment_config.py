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
    from agilicus_api.model.environment_config_var import EnvironmentConfigVar
    globals()['EnvironmentConfigVar'] = EnvironmentConfigVar


class EnvironmentConfig(ModelNormal):
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
        ('config_type',): {
            'CONFIGMAP_MOUNT': "configmap_mount",
            'CONFIGMAP_ENV': "configmap_env",
            'SECRET_MOUNT': "secret_mount",
            'SECRET_ENV': "secret_env",
            'FILE_MOUNT': "file_mount",
            'MOUNT_SMB': "mount_smb",
            'MOUNT_GCS': "mount_gcs",
            'MOUNT_TMPDIR': "mount_tmpdir",
        },
    }

    validations = {
        ('maintenance_org_id',): {
            'max_length': 40,
            'min_length': 1,
        },
    }

    @property
    def id(self):
       return self.get("id")

    @id.setter
    def id(self, new_value):
       self.id = new_value

    @property
    def app_id(self):
       return self.get("app_id")

    @app_id.setter
    def app_id(self, new_value):
       self.app_id = new_value

    @property
    def environment_name(self):
       return self.get("environment_name")

    @environment_name.setter
    def environment_name(self, new_value):
       self.environment_name = new_value

    @property
    def maintenance_org_id(self):
       return self.get("maintenance_org_id")

    @maintenance_org_id.setter
    def maintenance_org_id(self, new_value):
       self.maintenance_org_id = new_value

    @property
    def config_type(self):
       return self.get("config_type")

    @config_type.setter
    def config_type(self, new_value):
       self.config_type = new_value

    @property
    def mount_domain(self):
       return self.get("mount_domain")

    @mount_domain.setter
    def mount_domain(self, new_value):
       self.mount_domain = new_value

    @property
    def mount_username(self):
       return self.get("mount_username")

    @mount_username.setter
    def mount_username(self, new_value):
       self.mount_username = new_value

    @property
    def mount_password(self):
       return self.get("mount_password")

    @mount_password.setter
    def mount_password(self, new_value):
       self.mount_password = new_value

    @property
    def mount_hostname(self):
       return self.get("mount_hostname")

    @mount_hostname.setter
    def mount_hostname(self, new_value):
       self.mount_hostname = new_value

    @property
    def mount_share(self):
       return self.get("mount_share")

    @mount_share.setter
    def mount_share(self, new_value):
       self.mount_share = new_value

    @property
    def mount_src_path(self):
       return self.get("mount_src_path")

    @mount_src_path.setter
    def mount_src_path(self, new_value):
       self.mount_src_path = new_value

    @property
    def mount_path(self):
       return self.get("mount_path")

    @mount_path.setter
    def mount_path(self, new_value):
       self.mount_path = new_value

    @property
    def file_store_uri(self):
       return self.get("file_store_uri")

    @file_store_uri.setter
    def file_store_uri(self, new_value):
       self.file_store_uri = new_value

    @property
    def env_config_vars(self):
       return self.get("env_config_vars")

    @env_config_vars.setter
    def env_config_vars(self, new_value):
       self.env_config_vars = new_value

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
            'maintenance_org_id': (str,),  # noqa: E501
            'config_type': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'app_id': (str,),  # noqa: E501
            'environment_name': (str,),  # noqa: E501
            'mount_domain': (str,),  # noqa: E501
            'mount_username': (str,),  # noqa: E501
            'mount_password': (str,),  # noqa: E501
            'mount_hostname': (str,),  # noqa: E501
            'mount_share': (str,),  # noqa: E501
            'mount_src_path': (str,),  # noqa: E501
            'mount_path': (str,),  # noqa: E501
            'file_store_uri': (str,),  # noqa: E501
            'env_config_vars': ([EnvironmentConfigVar],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'maintenance_org_id': 'maintenance_org_id',  # noqa: E501
        'config_type': 'config_type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'app_id': 'app_id',  # noqa: E501
        'environment_name': 'environment_name',  # noqa: E501
        'mount_domain': 'mount_domain',  # noqa: E501
        'mount_username': 'mount_username',  # noqa: E501
        'mount_password': 'mount_password',  # noqa: E501
        'mount_hostname': 'mount_hostname',  # noqa: E501
        'mount_share': 'mount_share',  # noqa: E501
        'mount_src_path': 'mount_src_path',  # noqa: E501
        'mount_path': 'mount_path',  # noqa: E501
        'file_store_uri': 'file_store_uri',  # noqa: E501
        'env_config_vars': 'env_config_vars',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'app_id',  # noqa: E501
        'environment_name',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, maintenance_org_id, config_type, *args, **kwargs):  # noqa: E501
        """EnvironmentConfig - a model defined in OpenAPI

        Args:
            maintenance_org_id (str): The Organisation which is responsibile for maintaining this Environment. 
            config_type (str): configuration type

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
            id (str): Unique identifier. [optional]  # noqa: E501
            app_id (str): Unique identifier. [optional]  # noqa: E501
            environment_name (str): Unique identifier. [optional]  # noqa: E501
            mount_domain (str): mount user domain. [optional]  # noqa: E501
            mount_username (str): mount username. [optional]  # noqa: E501
            mount_password (str): mount password. [optional]  # noqa: E501
            mount_hostname (str): mount hostname. [optional]  # noqa: E501
            mount_share (str): mount share. [optional]  # noqa: E501
            mount_src_path (str): source mount path. [optional]  # noqa: E501
            mount_path (str): destination mount path. [optional]  # noqa: E501
            file_store_uri (str): files API URI where configuration is located. [optional]  # noqa: E501
            env_config_vars ([EnvironmentConfigVar]): It stores an array of env_config_var objects(key & value pairs) in API. It provides environment variables to build configmaps and secrets directly. . [optional]  # noqa: E501
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

        self.maintenance_org_id = maintenance_org_id
        self.config_type = config_type
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
    def __init__(self, maintenance_org_id, config_type, *args, **kwargs):  # noqa: E501
        """EnvironmentConfig - a model defined in OpenAPI

        Args:
            maintenance_org_id (str): The Organisation which is responsibile for maintaining this Environment. 
            config_type (str): configuration type

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
            id (str): Unique identifier. [optional]  # noqa: E501
            app_id (str): Unique identifier. [optional]  # noqa: E501
            environment_name (str): Unique identifier. [optional]  # noqa: E501
            mount_domain (str): mount user domain. [optional]  # noqa: E501
            mount_username (str): mount username. [optional]  # noqa: E501
            mount_password (str): mount password. [optional]  # noqa: E501
            mount_hostname (str): mount hostname. [optional]  # noqa: E501
            mount_share (str): mount share. [optional]  # noqa: E501
            mount_src_path (str): source mount path. [optional]  # noqa: E501
            mount_path (str): destination mount path. [optional]  # noqa: E501
            file_store_uri (str): files API URI where configuration is located. [optional]  # noqa: E501
            env_config_vars ([EnvironmentConfigVar]): It stores an array of env_config_var objects(key & value pairs) in API. It provides environment variables to build configmaps and secrets directly. . [optional]  # noqa: E501
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

        self.maintenance_org_id = maintenance_org_id
        self.config_type = config_type
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

