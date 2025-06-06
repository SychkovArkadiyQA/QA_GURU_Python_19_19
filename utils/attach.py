import allure
import requests
import os
from dotenv import load_dotenv


load_dotenv()
user_name = os.getenv("USER_NAME")
access_key = os.getenv("ACCESS_KEY")


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='Screenshot',
                  attachment_type=allure.attachment_type.PNG)


def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump,
                  name='XML screen',
                  attachment_type=allure.attachment_type.XML)


def add_video(browser):
    browserstack_session = requests.get(
        url=f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
        auth=(user_name, access_key)
    ).json()
    video_url = browserstack_session['automation_session'].get('video_url')

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )