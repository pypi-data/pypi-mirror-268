"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.04.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import agilicus_api
from agilicus_api.api.applications_api import ApplicationsApi  # noqa: E501


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_config(self):
        """Test case for add_config

        Add an environment configuration row  # noqa: E501
        """
        pass

    def test_add_role(self):
        """Test case for add_role

        Add a role to the application.  # noqa: E501
        """
        pass

    def test_add_role_to_rule_entry(self):
        """Test case for add_role_to_rule_entry

        Add a rule to a role in the application.  # noqa: E501
        """
        pass

    def test_add_rule(self):
        """Test case for add_rule

        Add a rule to the application.  # noqa: E501
        """
        pass

    def test_create_application(self):
        """Test case for create_application

        Create an application  # noqa: E501
        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        Remove an application  # noqa: E501
        """
        pass

    def test_delete_config(self):
        """Test case for delete_config

        Remove an environment configuration  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Remove a role  # noqa: E501
        """
        pass

    def test_delete_role_to_rule_entry(self):
        """Test case for delete_role_to_rule_entry

        Remove a role_to_rule_entry  # noqa: E501
        """
        pass

    def test_delete_rule(self):
        """Test case for delete_rule

        Remove a rule  # noqa: E501
        """
        pass

    def test_get_all_usage_metrics(self):
        """Test case for get_all_usage_metrics

        Get all resource metrics for the Applications API  # noqa: E501
        """
        pass

    def test_get_application(self):
        """Test case for get_application

        Get a application  # noqa: E501
        """
        pass

    def test_get_application_usage_metrics(self):
        """Test case for get_application_usage_metrics

        Get application metrics  # noqa: E501
        """
        pass

    def test_get_config(self):
        """Test case for get_config

        Get environment configuration  # noqa: E501
        """
        pass

    def test_get_environment(self):
        """Test case for get_environment

        Get an environment  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get a role  # noqa: E501
        """
        pass

    def test_get_role_to_rule_entry(self):
        """Test case for get_role_to_rule_entry

        Get a role_to_rule_entry  # noqa: E501
        """
        pass

    def test_get_rule(self):
        """Test case for get_rule

        Get a rule  # noqa: E501
        """
        pass

    def test_list_application_summaries(self):
        """Test case for list_application_summaries

        List application summaries  # noqa: E501
        """
        pass

    def test_list_applications(self):
        """Test case for list_applications

        Get applications  # noqa: E501
        """
        pass

    def test_list_combined_rules(self):
        """Test case for list_combined_rules

        List rules combined by scope or role  # noqa: E501
        """
        pass

    def test_list_configs(self):
        """Test case for list_configs

        Get all environment configuration  # noqa: E501
        """
        pass

    def test_list_environment_configs_all_apps(self):
        """Test case for list_environment_configs_all_apps

        Get all environment configuration for a given organisation.  # noqa: E501
        """
        pass

    def test_list_role_to_rule_entries(self):
        """Test case for list_role_to_rule_entries

        Get all RoleToRuleEntries  # noqa: E501
        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        Get all roles  # noqa: E501
        """
        pass

    def test_list_rules(self):
        """Test case for list_rules

        Get all rules  # noqa: E501
        """
        pass

    def test_list_runtime_status(self):
        """Test case for list_runtime_status

        Get an environment's runtime status  # noqa: E501
        """
        pass

    def test_replace_application(self):
        """Test case for replace_application

        Create or update an application  # noqa: E501
        """
        pass

    def test_replace_config(self):
        """Test case for replace_config

        Update environment configuration  # noqa: E501
        """
        pass

    def test_replace_environment(self):
        """Test case for replace_environment

        Update an environment  # noqa: E501
        """
        pass

    def test_replace_role(self):
        """Test case for replace_role

        Update a role  # noqa: E501
        """
        pass

    def test_replace_role_to_rule_entry(self):
        """Test case for replace_role_to_rule_entry

        Update a role_to_rule_entry  # noqa: E501
        """
        pass

    def test_replace_rule(self):
        """Test case for replace_rule

        Update a rule  # noqa: E501
        """
        pass

    def test_replace_runtime_status(self):
        """Test case for replace_runtime_status

        update an environemnt's runtime status  # noqa: E501
        """
        pass

    def test_update_patch_application(self):
        """Test case for update_patch_application

        patch application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
