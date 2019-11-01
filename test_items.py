import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button=browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        button=False
    assert (button!=False) & (button.text!=""), "Should contain add to cart button with some text"
