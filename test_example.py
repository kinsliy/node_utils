from playwright.sync_api import sync_playwright
import json
import time
from create_admission_person import all_fun

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # 尝试加载已保存的cookies
    try:
        with open("cookies.json", "r") as file:
            cookies = json.load(file)
            context.add_cookies(cookies)
    except FileNotFoundError:
        print("Cookies file not found. Will proceed with new login.")

    page = context.new_page()
    page.goto('https://apaas-dev1205.aedev.feishuapp.cn/ae/ui/apps/1746381508062253/appPages/wl94sgglide2cx')
   

    # 检查是否已经登录
    if not page.is_visible('text="待入场"'):
        # 执行登录操作，比如扫描二维码
        # ...

        # 等待特定文本出现，表明登录成功
        page.wait_for_selector('span.sc-fznXWL.cQNMoL.kunlun-clamp:text("待入场")')

        # 保存当前的cookies
        cookies = context.cookies()
        with open("cookies.json", "w") as file:
            json.dump(cookies, file)

    # 执行其他操作...
    page.wait_for_selector('span.sc-fznXWL.cQNMoL.kunlun-clamp:text("待入场")')
    print('进入待入场页面')
        # 点击按钮
    button_selector = 'button.ant-btn.sc-pscky.bAFTxf'  # 替换为实际的按钮选择器
    page.click(button_selector)
    print('点击新建按钮')

    all_fun(page)
    


#    # 点击下拉菜单以打开选项列表
#     dropdown_selector = 'div.sc-pRrUz.dQnepB'
#     page.click(dropdown_selector)

#     # 等待下拉选项出现并选择它
#     # 这里假设选项可以通过文本内容定位
#     option_text = '男'
#     page.click(f"text={option_text}")
#     print('选择性别')
#     # ... 针对其他输入框重复上述步骤 ...
    
    
#     country_selector = '[id^="formItem-_initialRecord__proposed__f72d99b6\\%\\%package_bmf9g5__c__lookup_aade3st4fpgay050-metaFormContainer"] div.sc-oTZKJ.HHLbu.form-item-control'
#     test_x = page.locator(country_selector)
#     test_x.click()
#     page.keyboard.type('中国')
#     # 等待下拉选项出现并选择它
#     # 这里假设选项可以通过文本内容定位
#     time.sleep(1)
#     country_selector_text = '中国大陆'
#     page.click(f"text={country_selector_text}")
#     print('国家/地区')


#     time.sleep(5)
    
    
#     id_type = '[id^="formItem-_initialRecord__proposed__a0924e88\\%\\%package_bmf9g5__c__lookup_aaddiqarrfoco"] div.sc-oTZKJ.HHLbu.form-item-control'
#     page.locator(id_type).click()
#     page.keyboard.type('其他')
#     # 等待下拉选项出现并选择它
#     # 这里假设选项可以通过文本内容定位
#     time.sleep(1)
#     id_type_text = '其他护照'
#     page.click(f"text={id_type_text}")
    
    
    
#     # id_number = '[id^="formItem-_initialRecord__proposed__a0924e88\\%\\%package_bmf9g5__c__text_aaddiqarrfodo"] div.sc-oTZKJ.HHLbu.form-item-control'
#     # page.locator(id_number).click()
#     # page.keyboard.type('34947374382')
    
#     # phone_number = '[id^="formItem-_initialRecord__proposed__a0924e88%%package_bmf9g5__c__phone_aaddiqbnrkyd4"] input'
#     # page.locator(phone_number).click()
#     # page.keyboard.type('15687462735')
    
    
#     person_type = '[id^="formItem-_initialRecord__proposed__58b433c1\\%\\%package_bmf9g5__c__lookup_aaddiugagiidi"] div.sc-oTZKJ.HHLbu.form-item-control'
#     page.locator(person_type).evaluate("""(element) => {
#     element.scrollIntoView(); 
#     }""")
#     page.locator(person_type).click()
#     page.keyboard.type('外包')
#     # 等待下拉选项出现并选择它
#     # 这里假设选项可以通过文本内容定位
#     time.sleep(1)
#     person_type_text = '外包'
#     page.click(f"text={person_type_text}")
    
#     time.sleep(1)
    
    # person_sub_type = '[id^="formItem-_initialRecord__proposed__58b433c1\\%\\%package_bmf9g5__c__lookup_aaddiugawz2aw"] div.sc-oTZKJ.HHLbu.form-item-control'
    # page.locator(person_sub_type).evaluate("""(element) => {
    # element.scrollIntoView(); 
    # }""")
    # page.locator(person_sub_type).click()
    # page.keyboard.type('人员外包')
    # # 等待下拉选项出现并选择它
    # # 这里假设选项可以通过文本内容定位
    # time.sleep(1)
    # person_sub_type_text = '人员外包'
    # page.click(f"text={person_sub_type_text}")
    

    # time.sleep(6)
    # 点击提交按钮
    # submit_button_selector = 'div.ant-row.ant-form-action-bar button.ant-btn.sc-pQGev.lbdMzz.ant-btn-primary'  # 替换为定位提交按钮的选择器
    # page.click(submit_button_selector)
    # print('点击保存按钮')
    
    # ...[之前的脚本代码]...

    # 询问用户是否关闭浏览器
    # response = input("测试完成。输入'y'来关闭浏览器，或者按任意键保持浏览器打开: ")

    # if response.lower() == 'y':
    #     browser.close()
    # else:
    #     print("浏览器将保持打开状态。手动关闭浏览器以结束会话。")
    #     # 在这种情况下，脚本将结束，但浏览器会保持打开状态

   

with sync_playwright() as playwright:
    run(playwright)