import pytest

import time
import math


@pytest.mark.parametrize(
    "link",
    ["https://stepik.org/lesson/236895/step/1",
     "https://stepik.org/lesson/236896/step/1",
     "https://stepik.org/lesson/236897/step/1",
     "https://stepik.org/lesson/236898/step/1",
     "https://stepik.org/lesson/236899/step/1",
     "https://stepik.org/lesson/236903/step/1",
     "https://stepik.org/lesson/236904/step/1",
     "https://stepik.org/lesson/236905/step/1",]
)


def test_link(browser, link):

    browser.get(link)
    time.sleep(5)
    answer = str(math.log(int(time.time())))

    browser.find_element_by_css_selector('[placeholder~=Type]').send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(1)
    result_text_elt = browser.find_element_by_class_name("smart-hints__hint")
    result_text = result_text_elt.text
    expected_result = "Correct!"
    assert result_text == expected_result, result_text
