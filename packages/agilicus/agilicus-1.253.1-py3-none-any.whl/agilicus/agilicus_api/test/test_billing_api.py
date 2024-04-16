"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2024.04.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import agilicus_api
from agilicus_api.api.billing_api import BillingApi  # noqa: E501


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self):
        self.api = BillingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_billing_usage_record(self):
        """Test case for add_billing_usage_record

        Add usage records for a billing account  # noqa: E501
        """
        pass

    def test_add_customer_balance_transaction(self):
        """Test case for add_customer_balance_transaction

        Add a customer balance transaction  # noqa: E501
        """
        pass

    def test_add_org_to_billing_account(self):
        """Test case for add_org_to_billing_account

        Add an org to a billing account  # noqa: E501
        """
        pass

    def test_add_org_to_billing_subscription(self):
        """Test case for add_org_to_billing_subscription

        Add an org to a billing subscription  # noqa: E501
        """
        pass

    def test_add_subscription_balance_transaction(self):
        """Test case for add_subscription_balance_transaction

        Add a subscription balance transaction  # noqa: E501
        """
        pass

    def test_create_billing_account(self):
        """Test case for create_billing_account

        Create a billing account  # noqa: E501
        """
        pass

    def test_create_feature(self):
        """Test case for create_feature

        create a feature  # noqa: E501
        """
        pass

    def test_create_product(self):
        """Test case for create_product

        Create a product  # noqa: E501
        """
        pass

    def test_create_subscription(self):
        """Test case for create_subscription

        Create a billing subscription  # noqa: E501
        """
        pass

    def test_delete_billing_account(self):
        """Test case for delete_billing_account

        Delete a billing account  # noqa: E501
        """
        pass

    def test_delete_feature(self):
        """Test case for delete_feature

        Delete a feature  # noqa: E501
        """
        pass

    def test_delete_product(self):
        """Test case for delete_product

        Delete a product  # noqa: E501
        """
        pass

    def test_delete_subscription(self):
        """Test case for delete_subscription

        Delete a billing subscription  # noqa: E501
        """
        pass

    def test_get_billing_account(self):
        """Test case for get_billing_account

        Get a single billing account  # noqa: E501
        """
        pass

    def test_get_billing_account_orgs(self):
        """Test case for get_billing_account_orgs

        Get all orgs in a billing account  # noqa: E501
        """
        pass

    def test_get_billing_subscription_orgs(self):
        """Test case for get_billing_subscription_orgs

        Get all orgs in a billing subscription  # noqa: E501
        """
        pass

    def test_get_customer_balance_transactions(self):
        """Test case for get_customer_balance_transactions

        Get the customers balance transactions  # noqa: E501
        """
        pass

    def test_get_feature(self):
        """Test case for get_feature

        Get a feature by id  # noqa: E501
        """
        pass

    def test_get_product(self):
        """Test case for get_product

        Get a single product  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Get a single billing subscription  # noqa: E501
        """
        pass

    def test_get_subscription_balance_transactions(self):
        """Test case for get_subscription_balance_transactions

        Get the subscription balance transactions  # noqa: E501
        """
        pass

    def test_get_usage_records(self):
        """Test case for get_usage_records

        Get all subscription usage records  # noqa: E501
        """
        pass

    def test_list_billing_accounts(self):
        """Test case for list_billing_accounts

        Get all billing accounts  # noqa: E501
        """
        pass

    def test_list_features(self):
        """Test case for list_features

        Get all features  # noqa: E501
        """
        pass

    def test_list_products(self):
        """Test case for list_products

        Get all products  # noqa: E501
        """
        pass

    def test_list_subscription_features(self):
        """Test case for list_subscription_features

        Get all subscription features  # noqa: E501
        """
        pass

    def test_list_subscriptions(self):
        """Test case for list_subscriptions

        Get all billing subscriptions for a billing account  # noqa: E501
        """
        pass

    def test_list_subscriptions_with_feature(self):
        """Test case for list_subscriptions_with_feature

        Get all subscriptions using feature_id  # noqa: E501
        """
        pass

    def test_remove_org_from_billing_account(self):
        """Test case for remove_org_from_billing_account

        Remove an org from a billing account  # noqa: E501
        """
        pass

    def test_remove_org_from_billing_subscription(self):
        """Test case for remove_org_from_billing_subscription

        Remove an org from a billing subscription  # noqa: E501
        """
        pass

    def test_replace_billing_account(self):
        """Test case for replace_billing_account

        Create or update a billing account  # noqa: E501
        """
        pass

    def test_replace_feature(self):
        """Test case for replace_feature

        update a Feature  # noqa: E501
        """
        pass

    def test_replace_product(self):
        """Test case for replace_product

        Create or update a product  # noqa: E501
        """
        pass

    def test_replace_subscription(self):
        """Test case for replace_subscription

        Create or update a billing subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
