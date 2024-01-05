import time

def scroll_type(page, id):
    id_selector = f'[id^="{id}"]'
    page.locator(id_selector).scroll_into_view_if_needed()
    time.sleep(1)


def text_type(page, id, value):
    id_selector = f'[id^="{id}"] div.sc-oTZKJ.HHLbu.form-item-control'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    time.sleep(1)


def phone_type(page, id, value):
    id_selector = f'[id^="{id}"] input'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    time.sleep(1)


def select_type(page, id, value):
    id_selector = f'[id^="{id}"] div.sc-pRrUz.dQnepB'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    time.sleep(1)
    page.locator(f"li.ant-select-dropdown-menu-item[name={value}]").click()
    time.sleep(1)


def search_select_type(page, id, value):
    time.sleep(2)
    id_selector = f'[id^="{id}"] div.sc-oTZKJ.HHLbu '
    print('id_selector===>',page.locator(id_selector))
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    time.sleep(2)
    li = page.query_selector_all("li.ant-select-dropdown-menu-item")
    print("li===>", li)

    for child in li:
        if child:
            option = child.query_selector(f'span:has-text("{value}")')
            print("option===>", option)
            if option:
                option.click()
                

common_str = "formItem-_initialRecord__proposed__a0924e88%%package_bmf9g5__c__"

search_select_str = "formItem-_initialRecord__proposed__f72d99b6%%package_bmf9g5__c__"

person_type_str = "formItem-_initialRecord__proposed__58b433c1%%package_bmf9g5__c__"

field_list = [
    {"name": f"{common_str}text_aadeyh2w2oibo077", "value": "自动化输入的法定姓名", "type_fun": "text_type"},
    {"name": f"{common_str}text_aaddip5eeqkho", "value": "自动化输入的常用姓名", "type_fun": "text_type"},
    {"name": f"{common_str}option_aaddip5eeqkio", "value": "男", "type_fun": "select_type"},       
    {"name": f"{search_select_str}lookup_aade3st4fpgay050", "value": "中国大陆", "type_fun": "search_select_type"},
    {"name": f"{common_str}lookup_aaddiqarrfoco", "value": "其他护照", "type_fun": "search_select_type"},
    {"name": f"{common_str}text_aaddiqarrfodo", "value": "4343544429472942", "type_fun": "text_type"},
    {"name": f"{common_str}phone_aaddiqbnrkyd4", "value": "15689763465", "type_fun": "phone_type"},
    {"name": f"{person_type_str}lookup_aaddiugagiidi", "type_fun": "scroll_type"},
    {"name": f"{person_type_str}lookup_aaddiugagiidi", "value": "外包", "type_fun": "search_select_type"},
]

def all_fun(page):
    for item in field_list:
        if item["type_fun"] == "text_type":
            text_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
            )
        if item["type_fun"] == "phone_type":
            phone_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
            )
        if item["type_fun"] == "search_select_type":
            search_select_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
            )
        if item["type_fun"] == "select_type":
            select_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
            )
        if item["type_fun"] == "scroll_type":
            scroll_type(
                page,
                id=f"{item["name"]}",
            )
    time.sleep(2)
