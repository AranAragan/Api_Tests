from tests import test_register_code
from tests import test_register_user
from tests import test_home_screen
from tests import test_catalog_sections
from tests import test_confirm_code
from tests import test_register_fields
from tests import test_catalog_products_viewed
from environment import yaml_environment

environment_adapter = yaml_environment.yaml_environment(
    "environment/test_environment.yml")
test_register_code.test_register_code(
    environment_adapter).request().print_json_response()
test_confirm_code.test_confirm_code(
    environment_adapter).request().print_json_response()
test_register_fields.test_register_fields(
    environment_adapter).request().print_json_response()
test_register_user.test_register_user(
    environment_adapter).request().rewrite_token().print_json_response()
test_home_screen.test_home_screen(
    environment_adapter).request().print_json_response()
test_catalog_products_viewed.test_catalog_products_viewed(
    environment_adapter).request().print_json_response()
test_catalog_sections.test_catalog_sections(
    environment_adapter).request().print_json_response()
