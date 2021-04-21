from tests import test_register_code
from tests import test_register_user
from tests import test_home_screen
from tests import test_catalog_sections
from tests import test_confirm_code
from tests import test_register_fields
from tests import test_auth_user
from tests import test_recover_send
from tests import test_recover_change
from tests import test_user_verify_email
from tests import test_personal_area
from tests import test_change_personal_data_user
from tests import test_favorite_product
from tests import test_favorite_product_double
from tests import test_favorite_product_del
from tests import test_favorite_product_all_del
from tests import test_catalog_products_viewed
from tests import test_review_product
from tests import test_question
from tests import test_favorite_list
from environment import yaml_environment
import allure


class Test():
    environment_adapter = yaml_environment.yaml_environment(
        "environment/test_environment.yml")

    @allure.title("Отправка кода подтверждения")
    @allure.description("Отправка кода подтверждения")
    def test_register_code(self):
        test_register_code.TestRegisterCode(
            self.environment_adapter).request().test()

    @allure.title("Проверка кода подтверждения")
    @allure.description("Проверка кода подтверждения")
    def test_confirm_code(self):
        test_confirm_code.TestConfirmCode(
            self.environment_adapter).request().test()

    @allure.title("Получение полей для регистрации")
    @allure.description("Получение полей для регистрации")
    def test_register_fields(self):
        test_register_fields.TestRegisterFields(
            self.environment_adapter).request().test()

    @allure.title("Регистрация пользователя")
    @allure.description("Регистрация пользователя")
    def test_register_user(self):
        test_register_user.TestRegisterUser(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Восстановление пароля")
    @allure.description("Восстановление пароля")
    def test_auth_user(self):
        test_auth_user.TestAuthUser(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Проверка кода подтверждения")
    @allure.description("Проверка кода подтверждения")
    def test_recover_send(self):
        test_recover_send.TestRecoverSend(
            self.environment_adapter).request().test()

    @allure.title("Изменить пароль во время восстановления")
    @allure.description("Изменить пароль во время восстановления")
    def test_recover_change(self):
        test_recover_change.TestRecoverChange(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Подтвердить электронную почту")
    @allure.description("Подтвердить электронную почту")
    def test_user_verify_email(self):
        test_user_verify_email.TestUserVerifyEmail(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Изменение личных данных пользователя")
    @allure.description("Изменение личных данных пользователя")
    def test_change_personal_data_user(self):
        test_change_personal_data_user.TestChangePersonalDataUser(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Личный кабинет")
    @allure.description("Личный кабинет")
    def test_personal_area(self):
        test_personal_area.TestPersonalArea(
            self.environment_adapter).request().rewrite_token().test()

    @allure.title("Добавить в избранное")
    @allure.description("Добавить в избранное")
    def test_favorite_product(self):
        test_favorite_product.TestFavoriteProduct(
            self.environment_adapter).request().test()

    @allure.title("Добавить в избранное дубль")
    @allure.description("Добавить в избранное дубль")
    def test_favorite_product_double(self):
        test_favorite_product_double.TestFavoriteProductDouble(
            self.environment_adapter).request().test()

    @allure.title("Удаление из избранного")
    @allure.description("Удаление из избранного")
    def test_favorite_product_del(self):
        test_favorite_product_del.TestFavoriteProductDel(
            self.environment_adapter).request().test()

    @allure.title("Удалить все из избранного")
    @allure.description("Удалить все из избранного")
    def test_favorite_product_all_del(self):
        test_favorite_product_all_del.TestFavoriteProductAllDel(
            self.environment_adapter).request().test()

    @allure.title("Список избранных")
    @allure.description("Список избранных")
    def test_favorite_list(self):
        test_favorite_list.TestFavoriteList(
            self.environment_adapter).request().test()

    @allure.title("Получение главного экрана")
    @allure.description("Получение главного экрана")
    def test_home_screen(self):
        test_home_screen.TestHomeScreen(
            self.environment_adapter).request().test()

    @allure.title("Получение просмотренных товаров")
    @allure.description("Получение просмотренных товаров")
    def test_catalog_products_viewed(self):
        test_catalog_products_viewed.TestCatalogProductsViewed(
            self.environment_adapter).request().test()

    @allure.title("Добавить отзыв")
    @allure.description("Добавить отзыв")
    def test_review_product(self):
        test_review_product.TestReviewProduct(
            self.environment_adapter).request().test()

    @allure.title("Добавить вопрос")
    @allure.description("Добавить вопрос")
    def test_question(self):
        test_question.TestQuetion(
            self.environment_adapter).request().test()

    # @allure.title("Разделы каталога")
    # @allure.description("Разделы каталога")
    # def test_catalog_sections(self):
    #     test_catalog_sections.TestCatalogSections(
    #         self.environment_adapter).request().print_json_response()
