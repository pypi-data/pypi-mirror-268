from sites import Sites


class Browser(Sites):
    def __init__(self):
        super(Browser, self).__init__()
    
    def open_browser(self, url: str):
        self.browser.open_available_browser(url)

    def change_to_frame(self, frame_xpath: str):
        self.browser.unselect_frame()
        self.browser.wait_until_element_is_visible(frame_xpath, timeout=60 * 2)
        iframe = self.browser.find_element(frame_xpath)
        self.browser.select_frame(iframe)