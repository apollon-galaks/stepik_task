link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button')
    x_el = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button')
    x = x_el.text
    assert x is not None, "Should be a button 'Add to cart'!"
    """
    Проверяющий! Для Вашего удобства я добавил функцию print, чтоб проверить наличие фразы 'Ajouter au panier' на французском.
    Запустите пожалуйста код добавив в конец -s,
    Люблю, уважаю

    """
    print(x)