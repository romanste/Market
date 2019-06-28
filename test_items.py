import time


def test_basket_button_existing(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_class_name('btn-add-to-basket')
    time.sleep(30)  # for language verification
