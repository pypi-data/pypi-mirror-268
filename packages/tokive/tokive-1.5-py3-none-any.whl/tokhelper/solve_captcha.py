# github.com/angelillija

import random
import time
import cv2
from io import BufferedReader
from numpy import uint8, frombuffer
import requests
import re
class TikTokCaptchaSolver:

    def get_domain(self):
        domain=None
        url="https://www.tiktok.com/foryou?lang=en"
        data=requests.get(url, headers=self.headers, cookies=self.cookies).text
        regex_pattern = r'captcha":"(.+?)"'
        matches = re.findall(regex_pattern, data)
        if matches:
            for match in matches:
                print(match)
                if match and "//" in match:
                    domain = "https:" + match
        return domain


    def __init__(self, device_id: int, install_id: int, cookies, capt, user_agents, browser_version, proxies=None) -> None:
        self.session = requests.Session()
        self.base_url = "https://verification-va.tiktok.com"

        if capt['region'] =='ttp':
            self.base_url = "https://verification.us.tiktok.com"
            # self.base_url = "https://verification.tiktokw.us"
            # "https://us.tiktok.com/captcha/"

        print(self.base_url)
        self.cookies=cookies
        self.proxies=proxies
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': user_agents,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.params = {
              "lang":"en",
              "app_name":"",
              "h5_sdk_version":"2.33.0",
              "h5_sdk_use_type":"cdn",
              "sdk_version":"3.8.13",
              "iid":install_id,
              "did": device_id,
              "device_id":device_id,
              "ch":"web_text",
              "aid":"8311",
              "os_type":"2",
              "mode":"",
              "platform":"pc",
              "webdriver":"false",
              "type":"verify",
               "fp":capt['fp'],
               "detail":capt['detail'],
              "server_sdk_env":capt['server_sdk_env'],
              "subtype":"slide",
              # "challenge_code":"1105",
              "challenge_code":"3058",
              "os_name":"windows",
              "h5_check_version":"3.8.13",
              "region":capt['region'],
              "triggered_region":capt['region'],
              "cookie_enabled":"true",
              "screen_width":"1920",
              "screen_height":"1080",
              "browser_language":"en-US",
              "browser_platform":"Win32",
              "browser_name":"Mozilla",
              "browser_version":browser_version
            }
        # print("prepre get")
        # xx=self.get_domain()
        # print(xx)
        # print("done get")
    @staticmethod
    def process_image(buffer: BufferedReader):
        nparr = frombuffer(buffer, uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        blurred = cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (3, 3), 0)
        return cv2.addWeighted(
            cv2.convertScaleAbs(cv2.Sobel(blurred, cv2.CV_16S, 1, 0, ksize=3)),
            0.5,
            cv2.convertScaleAbs(cv2.Sobel(blurred, cv2.CV_16S, 0, 1, ksize=3)),
            0.5,
            0,
        )

    def solve_captcha(self, retries=1) -> dict:
        # arr=["verification-i18n.tiktok.com","verification-i18n.tiktokv.com","verification-va-useast2a.tiktokv.com","verification-va.tiktok.com","verification-va.tiktokv.com","verification.tiktok.com","verification.us.tiktok.com","verification.us.tiktokv.com","verification16-normal-c-useast1a.tiktokv.com","verification16-normal-c-useast2a.tiktokv.com","verification16-platform-useast5.us.tiktokv.com","verification16-platform-ycru.tiktokv.com","verification16-tmp-normal-useast1a.tiktokv.com"]
        try:
            captcha = self.session.get(
                url=f"{self.base_url}/captcha/get", params=self.params, headers= self.headers, cookies=self.cookies, proxies=self.proxies
            ).json()
            challenge=captcha["data"]['challenges'][0]
        except:
            print("Retries new domain!!")
            if retries>0:
                self.base_url=self.get_domain()
                if self.base_url:
                    print("NewDomain: "+self.base_url)
                    return self.solve_captcha(retries-1)
        puzzle, piece = [
            self.process_image(
                self.session.get(challenge["question"][f"url{url}"]).content
            )
            for url in [1, 2]
        ]

        time.sleep(1)

        randlength = round(random.uniform(50, 100))
        max_loc = cv2.minMaxLoc(cv2.matchTemplate(puzzle, piece, cv2.TM_CCOEFF_NORMED))[
            3
        ][0]
        headers_verify=self.headers
        headers_verify['content-type']="application/json"
        param_verify=self.params
        param_verify['challenge_code']=challenge['challenge_code']
        h,w = puzzle.shape
        return self.session.post(
            url=f"{self.base_url}/captcha/verify",
            params=self.params,
            headers=headers_verify,
            proxies=self.proxies,
            json={
                "modified_img_width": w,
                "id": challenge["id"],
                "mode": "slide",
                "reply": [
                    {
                        "relative_time": (i * randlength),
                        "x": round(max_loc / (randlength / i)),
                        "y": challenge["question"]["tip_y"],
                    }
                    for i in range(1, randlength)
                ],
            },
        ).json()

