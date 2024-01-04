from playwright.sync_api import sync_playwright
import json

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
    page.goto('https://apaas-dev1205.aedev.feishuapp.cn/ae/ui/apps/1746381508062253/appPages/wl94sgglide2cx?dataGrid%40k50r6mrrlhoeq=%7B%22snapshotId%22%3A1785230278686746%7D')
   

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

    # 等待表单出现
    form_selector = 'span.sc-fznXWL.dIkGXA.kunlun-clamp:text("新建待入场")'  # 替换为定位表单的选择器
    page.wait_for_selector(form_selector)
    print('打开新建待入场人员表单')


    # XPath 选择器
    xpath_selector = "xpath=//span[contains(text(), '法定姓名')]/ancestor::div[contains(@class, 'form-item-label')]/following-sibling::div[contains(@class, 'form-item-control')]/div[contains(@class, 'form-item-control')]"
  
    
    xpath_element = page.query_selector(xpath_selector)

    # 定位最近的具有contenteditable属性的父元素
    editable_div_selector = xpath_element.query_selector("div[contenteditable='true'].editor-kit-container")

    # 等待可编辑的div出现
    page.wait_for_selector(editable_div_selector)

    # 点击该div以便进行输入
    page.click(editable_div_selector)

    # 输入文本，这里假设您要输入的是"Hello"
    page.keyboard.type('自动化输入的法定姓名')
    print('输入法定姓名')

   # 点击下拉菜单以打开选项列表
    dropdown_selector = 'div.sc-pRrUz.dQnepB'
    page.click(dropdown_selector)

    # 等待下拉选项出现并选择它
    # 这里假设选项可以通过文本内容定位
    option_text = '男'
    page.click(f"text={option_text}")
    print('选择性别')
    # ... 针对其他输入框重复上述步骤 ...

    # 点击提交按钮
    submit_button_selector = 'div.ant-row.ant-form-action-bar button.ant-btn.sc-pQGev.lbdMzz.ant-btn-primary'  # 替换为定位提交按钮的选择器
    page.click(submit_button_selector)
    print('点击保存按钮')
    
    # ...[之前的脚本代码]...

    # 询问用户是否关闭浏览器
    response = input("测试完成。输入'y'来关闭浏览器，或者按任意键保持浏览器打开: ")

    if response.lower() == 'y':
        browser.close()
    else:
        print("浏览器将保持打开状态。手动关闭浏览器以结束会话。")
        # 在这种情况下，脚本将结束，但浏览器会保持打开状态

   

with sync_playwright() as playwright:
    run(playwright)