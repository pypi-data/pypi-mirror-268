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
    from agilicus_api.model.email import Email
    from agilicus_api.model.group import Group
    from agilicus_api.model.group_member import GroupMember
    from agilicus_api.model.inheritable_user_config import InheritableUserConfig
    from agilicus_api.model.roles import Roles
    from agilicus_api.model.upstream_user_identity import UpstreamUserIdentity
    from agilicus_api.model.user import User
    from agilicus_api.model.user_attribute import UserAttribute
    from agilicus_api.model.user_attributes import UserAttributes
    from agilicus_api.model.user_identity import UserIdentity
    from agilicus_api.model.user_status_enum import UserStatusEnum
    globals()['Email'] = Email
    globals()['Group'] = Group
    globals()['GroupMember'] = GroupMember
    globals()['InheritableUserConfig'] = InheritableUserConfig
    globals()['Roles'] = Roles
    globals()['UpstreamUserIdentity'] = UpstreamUserIdentity
    globals()['User'] = User
    globals()['UserAttribute'] = UserAttribute
    globals()['UserAttributes'] = UserAttributes
    globals()['UserIdentity'] = UserIdentity
    globals()['UserStatusEnum'] = UserStatusEnum


class Group(ModelNormal):
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
        ('type',): {
            'USER': "user",
            'GROUP': "group",
            'SYSGROUP': "sysgroup",
            'BIGROUP': "bigroup",
            'SERVICE_ACCOUNT': "service_account",
        },
    }

    validations = {
        ('external_id',): {
            'max_length': 100,
            'min_length': 0,
        },
        ('first_name',): {
            'max_length': 100,
            'min_length': 0,
        },
        ('last_name',): {
            'max_length': 100,
            'min_length': 0,
        },
        ('full_name',): {
            'max_length': 201,
            'min_length': 0,
        },
        ('display_name',): {
            'max_length': 100,
            'min_length': 0,
        },
        ('provider',): {
            'max_length': 100,
            'min_length': 1,
        },
    }

    @property
    def members(self):
       return self.get("members")

    @members.setter
    def members(self, new_value):
       self.members = new_value

    @property
    def member_of(self):
       return self.get("member_of")

    @member_of.setter
    def member_of(self, new_value):
       self.member_of = new_value

    @property
    def id(self):
       return self.get("id")

    @id.setter
    def id(self, new_value):
       self.id = new_value

    @property
    def external_id(self):
       return self.get("external_id")

    @external_id.setter
    def external_id(self, new_value):
       self.external_id = new_value

    @property
    def enabled(self):
       return self.get("enabled")

    @enabled.setter
    def enabled(self, new_value):
       self.enabled = new_value

    @property
    def status(self):
       return self.get("status")

    @status.setter
    def status(self, new_value):
       self.status = new_value

    @property
    def first_name(self):
       return self.get("first_name")

    @first_name.setter
    def first_name(self, new_value):
       self.first_name = new_value

    @property
    def last_name(self):
       return self.get("last_name")

    @last_name.setter
    def last_name(self, new_value):
       self.last_name = new_value

    @property
    def full_name(self):
       return self.get("full_name")

    @full_name.setter
    def full_name(self, new_value):
       self.full_name = new_value

    @property
    def email(self):
       return self.get("email")

    @email.setter
    def email(self, new_value):
       self.email = new_value

    @property
    def display_name(self):
       return self.get("display_name")

    @display_name.setter
    def display_name(self, new_value):
       self.display_name = new_value

    @property
    def provider(self):
       return self.get("provider")

    @provider.setter
    def provider(self, new_value):
       self.provider = new_value

    @property
    def roles(self):
       return self.get("roles")

    @roles.setter
    def roles(self, new_value):
       self.roles = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def type(self):
       return self.get("type")

    @type.setter
    def type(self, new_value):
       self.type = new_value

    @property
    def created(self):
       return self.get("created")

    @created.setter
    def created(self, new_value):
       self.created = new_value

    @property
    def updated(self):
       return self.get("updated")

    @updated.setter
    def updated(self, new_value):
       self.updated = new_value

    @property
    def auto_created(self):
       return self.get("auto_created")

    @auto_created.setter
    def auto_created(self, new_value):
       self.auto_created = new_value

    @property
    def upstream_user_identities(self):
       return self.get("upstream_user_identities")

    @upstream_user_identities.setter
    def upstream_user_identities(self, new_value):
       self.upstream_user_identities = new_value

    @property
    def cascade(self):
       return self.get("cascade")

    @cascade.setter
    def cascade(self, new_value):
       self.cascade = new_value

    @property
    def configured_attributes(self):
       return self.get("configured_attributes")

    @configured_attributes.setter
    def configured_attributes(self, new_value):
       self.configured_attributes = new_value

    @property
    def attributes(self):
       return self.get("attributes")

    @attributes.setter
    def attributes(self, new_value):
       self.attributes = new_value

    @property
    def inheritable_config(self):
       return self.get("inheritable_config")

    @inheritable_config.setter
    def inheritable_config(self, new_value):
       self.inheritable_config = new_value

    @property
    def inheritable_status(self):
       return self.get("inheritable_status")

    @inheritable_status.setter
    def inheritable_status(self, new_value):
       self.inheritable_status = new_value

    @property
    def disabled_at_time(self):
       return self.get("disabled_at_time")

    @disabled_at_time.setter
    def disabled_at_time(self, new_value):
       self.disabled_at_time = new_value

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
            'members': ([GroupMember],),  # noqa: E501
            'member_of': ([UserIdentity],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'external_id': (str, none_type,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'status': (UserStatusEnum,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'full_name': (str,),  # noqa: E501
            'email': (Email,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'provider': (str, none_type,),  # noqa: E501
            'roles': (Roles,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'auto_created': (bool,),  # noqa: E501
            'upstream_user_identities': ([UpstreamUserIdentity],),  # noqa: E501
            'cascade': (bool,),  # noqa: E501
            'configured_attributes': (UserAttributes,),  # noqa: E501
            'attributes': ([UserAttribute],),  # noqa: E501
            'inheritable_config': (InheritableUserConfig,),  # noqa: E501
            'inheritable_status': (InheritableUserConfig,),  # noqa: E501
            'disabled_at_time': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'bigroup': Group,
            'group': Group,
            'service_account': User,
            'sysgroup': Group,
            'user': User,
        }
        if not val:
            return None
        return {'type': val}


    attribute_map = {
        'members': 'members',  # noqa: E501
        'member_of': 'member_of',  # noqa: E501
        'id': 'id',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'status': 'status',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'full_name': 'full_name',  # noqa: E501
        'email': 'email',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'provider': 'provider',  # noqa: E501
        'roles': 'roles',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'auto_created': 'auto_created',  # noqa: E501
        'upstream_user_identities': 'upstream_user_identities',  # noqa: E501
        'cascade': 'cascade',  # noqa: E501
        'configured_attributes': 'configured_attributes',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'inheritable_config': 'inheritable_config',  # noqa: E501
        'inheritable_status': 'inheritable_status',  # noqa: E501
        'disabled_at_time': 'disabled_at_time',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'enabled',  # noqa: E501
        'display_name',  # noqa: E501
        'type',  # noqa: E501
        'created',  # noqa: E501
        'updated',  # noqa: E501
        'upstream_user_identities',  # noqa: E501
        'attributes',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Group - a model defined in OpenAPI

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
            members ([GroupMember]): List of members in the group. [optional]  # noqa: E501
            member_of ([UserIdentity]): List of groups that the user is a member of. [optional]  # noqa: E501
            id (str): Unique identifier. [optional]  # noqa: E501
            external_id (str, none_type): External unique identifier. [optional]  # noqa: E501
            enabled (bool): Indicates if the user is enabled or disabled. This field is managed by the backend based on the users configured status, along with the disabled_at_time property if that is set. . [optional]  # noqa: E501
            status (UserStatusEnum): [optional]  # noqa: E501
            first_name (str): User's first name. [optional]  # noqa: E501
            last_name (str): User's last name. [optional]  # noqa: E501
            full_name (str): User's full name, combination of first and last name. [optional]  # noqa: E501
            email (Email): [optional]  # noqa: E501
            display_name (str): A suitable, simplified name of the user that can be used to identify a user. For users of type \"user\", this would be the users email. For other user types (group), the first_name would be used as the display_name. This does introduce the possiblity that multiple users may have identical display names. In this situation, it would be up to the consumer of this to de-duplicate the users (such as also display the users email alongside).  examples:     display_name: user@example.com     display_name: all_users_group . [optional]  # noqa: E501
            provider (str, none_type): Upstream IdP name. [optional]  # noqa: E501
            roles (Roles): [optional]  # noqa: E501
            org_id (str): Unique identifier. [optional]  # noqa: E501
            type (str): Type of user. [optional]  # noqa: E501
            created (datetime): Creation time. [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
            auto_created (bool): Whether the user was automatically created as part of another process such as logging in. On creation, this flag being true serves to trigger any behaviour tied to automatically created users, such as addition to special groups. On read, it can serve to indicate whether the user was automatically created. On update it will ensure that the automatically triggered behaviour still holds true. . [optional] if omitted the server will use the default value of False  # noqa: E501
            upstream_user_identities ([UpstreamUserIdentity]): The upstream identities this user can use to log in to the system. When a user logs in, their identity in this system will be determined by matching against this list. Note that this implies that entries in this list are globally unique. . [optional]  # noqa: E501
            cascade (bool): Whether the user will be added to sub organisations automatically. When set for a user that is a member of a particular organisation, subsequent creations of sub organisations will add this user to that suborgansation. . [optional] if omitted the server will use the default value of False  # noqa: E501
            configured_attributes (UserAttributes): [optional]  # noqa: E501
            attributes ([UserAttribute]): The live attributes of the user, as determined from all sources of attributes. A user's attributes flow from all of their upstream_user_identities as well as the `configured_attributes` field. Attributes are merged by name. If two sources of attributes have an attribute with the same name, that attribute will be merged. For cases where a merge is not possible -- e.g. two attributes with different types -- the oldest source of identity will be used. The `configured_attributes` field is always considered the oldest, so it has priority. Further, the resulting items will be sorted in ascending order of name.  For example, considering a user with following two sources of attributes:  ``` older_upstream:   - name: manager     value: best-manager   - name: groups     value: [\"A\", \"B\"] newer_upstream:   - name: manager     value: other-manager   - name: groups     value: [\"C\"]   - name: age     value 32 ```  The resulting attributes will be:  ``` attributes:   - name: age     value 32   - name: groups     value: [\"A\", \"B\", \"C\"]   - name: manager     value: best-manager ``` . [optional]  # noqa: E501
            inheritable_config (InheritableUserConfig): [optional]  # noqa: E501
            inheritable_status (InheritableUserConfig): [optional]  # noqa: E501
            disabled_at_time (datetime, none_type): Optionally configure a user to be automatically disabled at a specific point in time. Any retrieval of the user object record past the disabled_at_time will result in the enabled property be set to false. . [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Group - a model defined in OpenAPI

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
            members ([GroupMember]): List of members in the group. [optional]  # noqa: E501
            member_of ([UserIdentity]): List of groups that the user is a member of. [optional]  # noqa: E501
            id (str): Unique identifier. [optional]  # noqa: E501
            external_id (str, none_type): External unique identifier. [optional]  # noqa: E501
            enabled (bool): Indicates if the user is enabled or disabled. This field is managed by the backend based on the users configured status, along with the disabled_at_time property if that is set. . [optional]  # noqa: E501
            status (UserStatusEnum): [optional]  # noqa: E501
            first_name (str): User's first name. [optional]  # noqa: E501
            last_name (str): User's last name. [optional]  # noqa: E501
            full_name (str): User's full name, combination of first and last name. [optional]  # noqa: E501
            email (Email): [optional]  # noqa: E501
            display_name (str): A suitable, simplified name of the user that can be used to identify a user. For users of type \"user\", this would be the users email. For other user types (group), the first_name would be used as the display_name. This does introduce the possiblity that multiple users may have identical display names. In this situation, it would be up to the consumer of this to de-duplicate the users (such as also display the users email alongside).  examples:     display_name: user@example.com     display_name: all_users_group . [optional]  # noqa: E501
            provider (str, none_type): Upstream IdP name. [optional]  # noqa: E501
            roles (Roles): [optional]  # noqa: E501
            org_id (str): Unique identifier. [optional]  # noqa: E501
            type (str): Type of user. [optional]  # noqa: E501
            created (datetime): Creation time. [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
            auto_created (bool): Whether the user was automatically created as part of another process such as logging in. On creation, this flag being true serves to trigger any behaviour tied to automatically created users, such as addition to special groups. On read, it can serve to indicate whether the user was automatically created. On update it will ensure that the automatically triggered behaviour still holds true. . [optional] if omitted the server will use the default value of False  # noqa: E501
            upstream_user_identities ([UpstreamUserIdentity]): The upstream identities this user can use to log in to the system. When a user logs in, their identity in this system will be determined by matching against this list. Note that this implies that entries in this list are globally unique. . [optional]  # noqa: E501
            cascade (bool): Whether the user will be added to sub organisations automatically. When set for a user that is a member of a particular organisation, subsequent creations of sub organisations will add this user to that suborgansation. . [optional] if omitted the server will use the default value of False  # noqa: E501
            configured_attributes (UserAttributes): [optional]  # noqa: E501
            attributes ([UserAttribute]): The live attributes of the user, as determined from all sources of attributes. A user's attributes flow from all of their upstream_user_identities as well as the `configured_attributes` field. Attributes are merged by name. If two sources of attributes have an attribute with the same name, that attribute will be merged. For cases where a merge is not possible -- e.g. two attributes with different types -- the oldest source of identity will be used. The `configured_attributes` field is always considered the oldest, so it has priority. Further, the resulting items will be sorted in ascending order of name.  For example, considering a user with following two sources of attributes:  ``` older_upstream:   - name: manager     value: best-manager   - name: groups     value: [\"A\", \"B\"] newer_upstream:   - name: manager     value: other-manager   - name: groups     value: [\"C\"]   - name: age     value 32 ```  The resulting attributes will be:  ``` attributes:   - name: age     value 32   - name: groups     value: [\"A\", \"B\", \"C\"]   - name: manager     value: best-manager ``` . [optional]  # noqa: E501
            inheritable_config (InheritableUserConfig): [optional]  # noqa: E501
            inheritable_status (InheritableUserConfig): [optional]  # noqa: E501
            disabled_at_time (datetime, none_type): Optionally configure a user to be automatically disabled at a specific point in time. Any retrieval of the user object record past the disabled_at_time will result in the enabled property be set to false. . [optional]  # noqa: E501
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

