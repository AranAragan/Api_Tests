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
from tests import test_product_card
from tests import test_products_viewed
from tests import test_delete_user
from tests import test_catalog_categories
from tests import test_sliders
from tests import test_vue_catalog
from tests import test_catalog
from tests import test_catalog_panel
from tests import test_catalog_banners
from tests import test_catalog_paths
from tests import test_user_orders
from tests import test_user_exist
from tests import test_oauth_token
from tests import test_get_basket
from tests import test_quantity_basket
from tests import test_order_payment
from tests import test_order_delivery
from tests import test_order_gifts
from tests import test_order_coupon
from tests import test_del_order_coupon
from tests import test_del_basket_productid
from tests import test_del_basket_all
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

    @allure.title("Карточка товара")
    @allure.description("Карточка товара")
    def test_product_card(self):
        test_product_card.TestProductCard(
            self.environment_adapter).request().test()

    @allure.title("Просмотренные товары")
    @allure.description("Просмотренные товары")
    def test_products_viewed(self):
        test_products_viewed.TestProductViewed(
            self.environment_adapter).request().test()

    @allure.title("Список категорий")
    @allure.description("Список категорий")
    def test_catalog_categories(self):
        test_catalog_categories.TestCatalogCategories(
            self.environment_adapter).request().test()

    @allure.title("Слайдеры")
    @allure.description("Слайдеры")
    def test_sliders(self):
        test_sliders.TestSliders(
            self.environment_adapter).request().test()

    @allure.title("Vue каталог")
    @allure.description("Vue каталог")
    def test_vue_catalog(self):
        test_vue_catalog.TestVueCatalog(
            self.environment_adapter).request().test()

    @allure.title("Каталог")
    @allure.description("Каталог")
    def test_catalog(self):
        test_catalog.TestCatalog(
            self.environment_adapter).request().test()

    @allure.title("Панель каталога")
    @allure.description("Панель каталога")
    def test_catalog_panel(self):
        test_catalog_panel.TestCatalogPanel(
            self.environment_adapter).request().test()

    @allure.title("Список баннеров")
    @allure.description("Список баннеров")
    def test_catalog_banners(self):
        test_catalog_banners.TestCatalogBanners(
            self.environment_adapter).request().test()

    @allure.title("Получить все ссылки")
    @allure.description("Получить все ссылки")
    def test_catalog_paths(self):
        test_catalog_paths.TestCatalogPaths(
            self.environment_adapter).request().test()

    @allure.title("Получить заказы")
    @allure.description("Получить заказы")
    def test_user_orders(self):
        test_user_orders.TestUserOrders(
            self.environment_adapter).request().test()

    @allure.title("Проверка существования Пользователя")
    @allure.description("Проверка существования Пользователя")
    def test_user_exist(self):
        test_user_exist.TestUserExist(
            self.environment_adapter).request().test()

    @allure.title("Получить информацию о токене")
    @allure.description("Получить информацию о токене")
    def test_oauth_token(self):
        test_oauth_token.TestOauthToken(
            self.environment_adapter).request().test()

    @allure.title("Получить корзину")
    @allure.description("Получить корзину")
    def test_get_basket(self):
        test_get_basket.TestGetBasket(
            self.environment_adapter).request().test()

    @allure.title("Установить количество товара в коризне")
    @allure.description("Установить количество товара в коризне")
    def test_quantity_basket(self):
        test_quantity_basket.TestQuantityBasket(
            self.environment_adapter).request().test()

    @allure.title("Получить способы оплаты")
    @allure.description("Получить способы оплаты")
    def test_order_payment(self):
        test_order_payment.TestOrderPayment(
            self.environment_adapter).request().test()

    @allure.title("Получить данные доставки")
    @allure.description("Получить данные доставки")
    def test_order_delivery(self):
        test_order_delivery.TestOrderDelivery(
            self.environment_adapter).request().test()

    @allure.title("Получить подарки")
    @allure.description("Получить подарки")
    def test_order_gifts(self):
        test_order_gifts.TestOrderGifts(
            self.environment_adapter).request().test()

    @allure.title("Добавить промокод")
    @allure.description("Добавить промокод")
    def test_order_coupon(self):
        test_order_coupon.TestOrderCoupon(
            self.environment_adapter).request().test()

    @allure.title("Удалить промокод")
    @allure.description("Удалить промокод")
    def test_del_order_coupon(self):
        test_del_order_coupon.TestDelOrderCoupon(
            self.environment_adapter).request().test()

    @allure.title("Удалить товар из корзины")
    @allure.description("Удалить товар из корзины")
    def test_del_basket_productid(self):
        test_del_basket_productid.TestDelBasketProductId(
            self.environment_adapter).request().test()

    @allure.title("Удалить товар из корзины")
    @allure.description("Удалить товар из корзины")
    def test_del_basket_all(self):
        test_del_basket_all.TestDelBasketAll(
            self.environment_adapter).request().test()

    # @allure.title("Удаление пользователя")
    # @allure.description("Удаление пользователя")
    # def test_delete_user(self):
        # test_delete_user.TestDeleteUser(
        # self.environment_adapter).request().test()

    # @allure.title("Разделы каталога")
    # @allure.description("Разделы каталога")
    # def test_catalog_sections(self):
        # test_catalog_sections.TestCatalogSections(
        # self.environment_adapter).request().print_json_response()
