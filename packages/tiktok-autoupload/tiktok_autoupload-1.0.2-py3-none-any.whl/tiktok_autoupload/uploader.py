import os
import pickle
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

class Uploader:
    """
    Class representing a TikTok video uploader.

    Args:
        title (str): The title of the video.
        video_filename (str): The filename of the video to upload.

    Attributes:
        title (str): The title of the video.
        video_filename (str): The filename of the video to upload.
        driver (WebDriver): The Chrome webdriver instance.

    Methods:
        load_cookies(): Loads cookies for the TikTok uploader.
        upload(): Uploads the video to TikTok.

    """

    def __init__(self, title, video_filename):
        self.title = title
        self.video_filename = video_filename

        # Initialize Chrome webdriver
        service = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)

    def load_cookies(self):
        """
        Loads cookies for the TikTok uploader.

        If cookies are found in the 'cookies.txt' file, they are loaded into the webdriver.
        Otherwise, the uploader page is loaded and cookies are saved for future use.

        """
        cookie_file = os.path.join(os.getcwd(), "cookies.txt")
        if os.path.exists(cookie_file):
            with open(cookie_file, "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            print("No cookies found")
            self.driver.get("https://www.tiktok.com/creator-center/upload?lang=en-EN")
            sleep(10)
            while "/creator-center/upload" not in self.driver.current_url:
                sleep(0.5)
            print("Upload page loaded")
            cookies = self.driver.get_cookies()
            with open(cookie_file, "wb") as f:
                pickle.dump(cookies, f)
            print("Cookies saved")

    def upload(self):
        """
        Uploads the video to TikTok.

        This method navigates to the TikTok uploader page, loads cookies, selects the video file,
        adds a caption, and clicks the upload button.

        """
        self.driver.get("https://www.tiktok.com/creator-center/upload?lang=en-EN")
        self.load_cookies()

        iframe_selector = EC.presence_of_element_located((By.XPATH, "//iframe"))
        iframe = WebDriverWait(self.driver, 10).until(iframe_selector)
        self.driver.switch_to.frame(iframe)
        print("Switched to iframe")

        upload_box_selector = EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        upload_box = WebDriverWait(self.driver, 10).until(upload_box_selector)
        video_path = os.path.abspath(os.path.join(os.getcwd(), self.video_filename))
        upload_box.send_keys(video_path)
        print("File uploaded")

        upload_button_selector = EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'btn-post')]/button"))
        upload_button = WebDriverWait(self.driver, 100).until(upload_button_selector)
        print("Upload finished")

        caption = self.driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        caption.send_keys(len(caption.text) * Keys.BACKSPACE + len(caption.text) * Keys.CANCEL)
        caption.send_keys(self.title)
        print("Caption added")

        sleep(1)
        upload_button.click()
        print("Upload button clicked")
        sleep(5)

if __name__ == "__main__":
    uploader = Uploader("video", "video.mp4")
    uploader.upload()
