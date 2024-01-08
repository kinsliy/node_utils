import time
from playwright.sync_api import Locator

def is_non_empty_list(li):
    if not isinstance(li, Locator):
        return False
    
    lis = li.all_text_contents()
    return len(lis) > 0

def scroll_type(page, id):
    id_selector = f'[id^="{id}"]'
    element= page.locator(id_selector)
    
    box = element.bounding_box()
    viewport_height = page.viewport_size["height"]

    element_middle = box["y"] + box["height"] / 2
    viewport_middle = viewport_height / 2

    if element_middle != viewport_middle:
        offset = element_middle - viewport_middle
        page.mouse.wheel(0, offset)
        
    time.sleep(1)


def text_type(page, id, value):
    id_selector = f'[id^="{id}"] div.sc-oTZKJ.HHLbu.form-item-control'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    # time.sleep(1)
    
def form_submit_type(page,):
    time.sleep(5)
    id_selector = 'div.ant-row.ant-form-item.ant-form-action-bar button.ant-btn.ant-btn-primary'
   # 直接使用 JavaScript 执行点击操作
    page.evaluate(f"""() => {{
        const element = document.querySelector('{id_selector}');
        console.log('element==>',element)
        if (element) element.click();
    }}""")
    time.sleep(5)


def phone_type(page, id, value):
    id_selector = f'[id^="{id}"] input'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    # time.sleep(1)

def date_select_type(page, id, value):
    time.sleep(2)
    id_selector = f'[id^="{id}"] div.sc-oTZKJ.HHLbu '
    print('id_selector===>',page.locator(id_selector))
    page.locator(id_selector).click()

    time.sleep(3)
    li = page.query_selector_all("div.ant-picker-date-panel")
    print("li===>", li)

    for child in li:
        if child:
            option = child.query_selector(f'div.ant-picker-cell-inner:has-text("{value}")')
            print("option===>", option)
            if option:
                option.click()


def select_type(page, id, value):
    id_selector = f'[id^="{id}"] div.sc-pRrUz.dQnepB'
    page.locator(id_selector).click()
    page.keyboard.type(f"{value}")
    time.sleep(1)
    page.locator(f"div.kunlun-ui-select-dropdown:not(.ant-select-dropdown-hidden) li.ant-select-dropdown-menu-item[name={value}]").click()
    # time.sleep(1)


def search_select_type(page, id, value,search_value = False):
    time.sleep(2)
    id_selector = f'[id^="{id}"] div.sc-oTZKJ.HHLbu'
    print('id_selector===>',page.locator(id_selector))
    page.locator(id_selector).click()
    write_value = value
    if search_value:
         write_value = search_value
   
    page.keyboard.type(f"{write_value}")
    time.sleep(3)
    li =  page.locator("div.kunlun-ui-select-dropdown:not(.ant-select-dropdown-hidden) li.ant-select-dropdown-menu-item")
    print("li===>", li)
    if is_non_empty_list(li):
       li.first.click()
    else:
       li.click()
        
    
    # print("value===>", value)
    # for child in li:
    #     if child:
    #         option = child.query_selector(f'span:has-text("{value}")')
    #         print("option===>", option)
    #         if option:
    #             option.click()
                

common_str = "formItem-_initialRecord__proposed__a0924e88%%package_bmf9g5__c__"

search_select_str = "formItem-_initialRecord__proposed__f72d99b6%%package_bmf9g5__c__"

person_type_str = "formItem-_initialRecord__proposed__58b433c1%%package_bmf9g5__c__"

company_str = "formItem-_initialRecord__proposed__93741d8b%%package_bmf9g5__c__"

lark_str = "formItem-_initialRecord__proposed__8b47b50%%package_bmf9g5__c__"

onboard_str = "formItem-_initialRecord__proposed__57b24732%%package_bmf9g5__c__"
field_list = [
    {"name": f"{common_str}text_aadeyh2w2oibo077", "value": "py自动化输入的法定姓名", "type_fun": "text_type"},
    {"name": f"{common_str}text_aaddip5eeqkho", "value": "py自动化输入的常用姓名", "type_fun": "text_type"},
    {"name": f"{common_str}option_aaddip5eeqkio", "value": "男", "type_fun": "select_type"},       
    {"name": f"{search_select_str}lookup_aade3st4fpgay050", "value": "中国大陆", "type_fun": "search_select_type"},
    {"name": f"{common_str}lookup_aaddiqarrfoco", "value": "其他护照", "type_fun": "search_select_type"},
    {"name": f"{common_str}text_aaddiqarrfodo", "value": "4343544428472942", "type_fun": "text_type"},
    {"name": f"{common_str}phone_aaddiqbnrkyd4", "value": "15689763465", "type_fun": "phone_type"},
    {"name": f"{person_type_str}lookup_aaddiugagiidi", "type_fun": "scroll_type"},
    {"name": f"{person_type_str}lookup_aaddiugagiidi", "value": "外包", "type_fun": "search_select_type"},
    {"name": f"{person_type_str}lookup_aaddiugawz2aw", "value": "人员外包", "type_fun": "search_select_type"},
    {"name": f"{person_type_str}option_aaddiugawz2bw", "value": "否", "type_fun": "select_type"},
    {"name": f"{person_type_str}lookup_aaddiugawz4aw", "value": "测试工程师-F", "type_fun": "search_select_type"},
    {"name": f"{person_type_str}lookup_aaddiugawz4bw", "search_value":"A-","value": "A", "type_fun": "search_select_type"},
    {"name": f"{person_type_str}lookup_aaddjzuzqkcai", "type_fun": "scroll_type"},
    {"name": f"{person_type_str}lookup_aaddjzuzqkcai", "value": "曾二004", "type_fun": "search_select_type"},
    {"name": f"{company_str}lookup_aaddiukcrykbg", "type_fun": "scroll_type"},
    {"name": f"{person_type_str}lookup_aaddlhnw3zyaq", "value": "北京市", "type_fun": "search_select_type"},
    {"name": f"{company_str}lookup_aaddiukcrykbg", "value": "赵花瑞-业务演示专用", "type_fun": "search_select_type"},
    # {"name": f"{person_type_str}lookup_aaddiukcrygdg", "value": "中国大陆北京北京市海淀区意思意思", "type_fun": "search_select_type"},
    {"name": f"{lark_str}option_aaddiuav226d4", "type_fun": "scroll_type"},
    {"name": f"{lark_str}option_aaddiuav226d4", "value": "否", "type_fun": "select_type"},
    {"name": f"{lark_str}option_aaddiuav226a4", "value": "否", "type_fun": "select_type"},
    {"name": f"{lark_str}option_aaddiutnremjw", "value": "否", "type_fun": "select_type"},
    {"name": f"{lark_str}option_aadfoqhnsrifs93e", "value": "否", "type_fun": "select_type"},
    {"name": f"{onboard_str}option_aaddiutnreokw", "type_fun": "scroll_type"},
    {"name": f"{onboard_str}option_aaddiutnreokw", "value": "远程", "type_fun": "select_type"},
    {"name": f"{onboard_str}date_aaddiu2le56f2", "value": "26", "type_fun": "date_select_type"},
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
            local_search_value = False
            if item.get("search_value"):
                local_search_value= item["search_value"]
                
            search_select_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
                search_value =local_search_value
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
        if item["type_fun"] == "date_select_type":
            date_select_type(
                page,
                id=f"{item["name"]}",
                value = item["value"],
            )
    form_submit_type(page)
    time.sleep(5)
