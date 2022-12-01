from config.Config import TestData
from tests import BaseTest
import pytest
import requests
import json
from utils import generateRequestBody
from config.Config import TestData



class TestApi(BaseTest):
    BASE_URL = "https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io"

    @pytest.mark.parametrize('validity', ["Valid"])
    def test_register(self, validity):
        generateRequestBody.RequestBody.generate_register_body(validity)
        request_dict = TestData.requestBodies[-1]  # Use the last appended request body
        endpoint = "/users"
        response = self.Wrappers.post_wrapper(self.BASE_URL + endpoint, request_dict)
        responseJson = json.loads(response.content)
        self.EnsureThat.is_same(response.status_code, 201)  # Status code is expected as 201 when the request has succeeded and has led to the creation of a resource.
        #print(f"\n{responseJson}")
        """      
        self.assertEqual(testJson["id"], expectedId, "Id: " + str(testJson["id"]) + " did not match expected ID: "+ str(expectedId))



        print("Apple Automation is Working For This Country:", country)
        assertion_values = TestData.ASSERTIONS.get(country)

        main_page = MainPage(self.driver, lang_code=shortcode)

        self.EnsureThat.is_same(main_page.get_title(), assertion_values.get("main_title"))
        self.EnsureThat.is_same(main_page.get_element_text(main_page.IPHONE), assertion_values.get("menu_text"))
        iphone_page = main_page.click_to_iphone()

        self.EnsureThat.is_same(iphone_page.get_title(), assertion_values.get("iphone_title"))
        self.EnsureThat.is_same(iphone_page.get_element_text(iphone_page.XIII_PRO), assertion_values.get("menu_iphone_text"))
        pro_page = iphone_page.select_xiii_pro()

        self.EnsureThat.is_same(pro_page.get_title(), assertion_values.get("pro_title"))
        self.EnsureThat.is_same(pro_page.get_element_text(pro_page.BUY_BUTTON), assertion_values.get("buy_button"))
        self.EnsureThat.is_true(pro_page.is_clickable(pro_page.BUY_BUTTON))
        conf_page = pro_page.click_purchase_button()

        conf_page.configure_iphone_specs()
        conf_page.configure_additional_options(country)
        rev_bag_page = conf_page.go_to_bag()

        rev_bag_page.remove_iphone()
        """