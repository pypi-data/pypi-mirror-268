import time
import binascii
from tokhelper import utils
import requests
import json, sys
from tokhelper import captchaCheck_pb2
from tokhelper.solve_captcha import TikTokCaptchaSolver
from urllib.parse import urlencode
import traceback
URL_SESSION="https://autolive.vip/api/tiktok/commit"

P_VERSION_CODE="0.54.0"
P_WEBCAST_VERSION="540"
P_BROWSER_VERSION="5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TikTokLIVEStudio/0.54.0 Chrome/104.0.5112.102 Electron/20.1.0-tt.8.release.main.35 TTElectron/20.1.0-tt.8.release.main.35 Safari/537.36"
H_USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TikTokLIVEStudio/0.54.0 Chrome/104.0.5112.102 Electron/20.1.0-tt.8.release.main.35 TTElectron/20.1.0-tt.8.release.main.35 Safari/537.36"

def load_tiktok_acc(id):
    url = f"https://autolive.vip/api/tiktok/load?id={id}"
    data = None
    try:
        headers={"platform":"Autolive"}
        res = requests.get(url, headers=headers).json()
        if "status" in res and res['status']=='success':
            data=res['data']
    except:
        pass
    return data
def save_session():
    url = ""
def get_domain(acc, xtype=1):
    cookie_encr=acc['cookie']
    cookies = json.loads(utils.decrypt_data(cookie_encr))
    domain="webcast22-normal-c-useast1a.tiktokv.com"
    url="https://tnc16-platform-useast1a.tiktokv.com/get_domains/v4/"
    if xtype==2:
        url="https://tnc16-platform-useast5.us.tiktokv.com/get_domains/v4/"
    params = {
    'version_code': P_VERSION_CODE,
    'device_id': acc['device_id'],
    'aid': '8311',
    'device_platform': 'win',
    'tnc_src': '6',
    'ttwebview_version': '1130022001',
    }
    headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': H_USER_AGENT,
    'accept-language': 'en-US',
    }
    try:
        response = requests.get(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
        )
        response = response.json()
        data=response['data']
        ttnet_dispatch_actions=data['ttnet_dispatch_actions']
        for action in ttnet_dispatch_actions:
            param =  action['param']
            if 'strategy_info' in param:
                strategy_info=param['strategy_info']
                if 'webcast-normal.tiktokv.com' in strategy_info:
                    domain=strategy_info['webcast-normal.tiktokv.com']
    except:
        if xtype==1:
            return get_domain(acc,2)
        pass
    return domain
def get_proxy_by_region_luna(region):
    return None
    if region=='vn':
        return {"http":"http://user-lu1810112-region-vn:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233",
                       "https":"http://user-lu1810112-region-vn:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233"}
                       
    if region=='us':
        return {"http":"http://user-lu1810112-region-us:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233",
                "https":"http://user-lu1810112-region-us:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233"}
    if region=='gb':
        return {"http":"http://user-lu1810112-region-gb:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233",
                "https":"http://user-lu1810112-region-gb:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233"}
    return {"http":"http://user-lu1810112-region-vn:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233",
                       "https":"http://user-lu1810112-region-vn:D5Bn3O@as.ahnacjtm.lunaproxy.net:12233"}
def get_proxy_by_region(region):
    return None
    if region=='vn':
        return {"http":"http://victor69:dota2hoabt2_country-vn_streaming-1@geo.iproyal.com:12321",
                       "https":"http://victor69:dota2hoabt2_country-vn_streaming-1@geo.iproyal.com:12321"}
                       
    if region=='us':
        return {"http":"http://victor69:dota2hoabt2_country-us_streaming-1@geo.iproyal.com:12321",
                "https":"http://victor69:dota2hoabt2_country-us_streaming-1@geo.iproyal.com:12321"}
    if region=='gb':
        return {"http":"http://victor69:dota2hoabt2_country-gb_streaming-1@geo.iproyal.com:12321",
                "https":"http://victor69:dota2hoabt2_country-gb_streaming-1@geo.iproyal.com:12321"}
    return {"http":"http://victor69:dota2hoabt2_country-vn_streaming-1@geo.iproyal.com:12321",
                       "https":"http://victor69:dota2hoabt2_country-vn_streaming-1@geo.iproyal.com:12321"}
def create_key_live(id):
    acc = load_tiktok_acc(id)
    url_stream = "Error"
    if acc:
        domain = get_domain(acc)
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/room/create/"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version':P_WEBCAST_VERSION,
            'live_mode':6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
       
        #print(json.dumps(cookies));
        data = {
            'title': acc['title'],
            'live_studio': '1',
            'gen_replay': 'true',
            'chat_auth': '0',
            # 'cover_uri': '720x720/tos-maliva-avt-0068/7149784794476806149',
            'close_room_when_close_stream': 'false',
            'hashtag_id': acc['topic'],
            'game_tag_id': '0',
            'screenshot_cover_status': '1',
            'gift_auth': '1',
        }
        proxiex=get_proxy_by_region(acc['priority_region'])
        response = requests.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxiex
        ).json()
        if 'data' in response:
            data_live=response['data']
            #print(data_live)
            if 'stream_url' in data_live:
                url_stream = data_live['stream_url']['rtmp_push_url']
                room_id=data_live['living_room_attrs']['room_id']
            else:
                return json.dumps(response)
        else:
            return json.dumps(response)
        return url_stream+";;"+str(room_id)

def active_live_mobile(id):
    acc = load_tiktok_acc(id)
    if acc:
        domain = get_domain(acc)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/live_permission/apply/"
        _rticket="1" + utils.random_digit(12)
        params={
        "permission_name": "live_by_record",
        "iid": acc['install_id'],
        "device_id": acc['device_id'],
        "ac": "wifi",
        "channel": "googleplay",
        "aid": "1233",
        # "app_name": "musical_ly",
        "app_name": "trill",
        "version_code": "330205",
        "version_name": "33.2.5",
        "device_platform": "android",
        "os": "android",
        "ab_version": "33.2.5",
        "ssmix": "a",
        "device_type": "SM-N950F",
        "device_brand": "samsung",
        "language": "en",
        "os_api": "28",
        "os_version": "9",
        "openudid": utils.random_text_digit(16),
        "manifest_version_code": "2023302050",
        "resolution": "1080*2094",
        "dpi": "420",
        "update_version_code": "2023302050",
        "_rticket": _rticket,
        "is_pad": "0",
        "current_region":  acc['priority_region'].upper(),
        "app_type": "normal",
        "sys_region": acc['priority_region'].upper(),
        "mcc_mnc": "45201",
        "timezone_name": "Asia/Ho_Chi_Minh",
        "residence": acc['priority_region'].upper(),
        "app_language": "en",
        "ac2": "wifi5g",
        "uoo": "0",
        "op_region": acc['priority_region'].upper(),
        "timezone_offset": "25200",
        "build_number": "33.2.5",
        "host_abi": "arm64-v8a",
        "locale": "en",
        "region": acc['priority_region'].upper(),
        "ts": "1" + utils.random_digit(9),
        "cdid": utils.random_cid(),
        "webcast_sdk_version": "3230",
        "webcast_language": "en",
        "webcast_locale": "en_US",
        "effect_sdk_version": "15.8.0",
        "current_network_quality_info": "{\"tcp_rtt\":76,\"quic_rtt\":76,\"http_rtt\":235,\"downstream_throughput_kbps\":1339,\"quic_send_loss_rate\":-1,\"quic_receive_loss_rate\":-1,\"net_effective_connection_type\":4,\"video_download_speed\":8145}"
    }
    headers = {
          'sdk-version': '2',
          'x-bd-kmsv': '0',
          'x-tt-dm-status': 'login=1;ct=1;rt=1',
          'x-ss-req-ticket': _rticket,
          'multi_login': '1',
          'passport-sdk-version': '19',
          'pns_event_id': '906',
          'x-vc-bdturing-sdk-version': '2.3.5.i18n',
          'x-ss-stub': utils.random_text_digit(32).upper(),
          'x-tt-store-region': acc['priority_region'],
          'x-tt-store-region-src': 'uid',
          'x-ss-dp': '1233',
          'x-tt-trace-id': '00-' + utils.random_text_digit(32) + '-' + utils.random_text_digit(16) + '-01',
          'user-agent': 'com.ss.android.ugc.trill/2023302050 (Linux; U; Android 9; en; SM-N950F; Build/PPR1.180610.011; Cronet/TTNetVersion:996128d2 2024-01-12 QuicVersion:ce58f68a 2024-01-12)',
          'content-type': 'application/x-www-form-urlencoded'
        }
    payload = ""
    proxiex = get_proxy_by_region(acc['priority_region'])
    response = requests.post(
        url,
        params= params,
        cookies= cookies,
        headers=headers,
        data=payload,
        proxies=proxiex
    ).json()
    print(response)
def create_key_live_mobile(id):
    acc = load_tiktok_acc(id)
    url_stream = "Error"
    if acc:
        domain = get_domain(acc)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/create/"
        _rticket="1" + utils.random_digit(12)
        params={
        "iid": acc['install_id'],
        "device_id": acc['device_id'],
        "ac": "wifi",
        "channel": "googleplay",
        "aid": "1233",
        # "app_name": "musical_ly",
        "app_name": "trill",
        "version_code": "330205",
        "version_name": "33.2.5",
        "device_platform": "android",
        "os": "android",
        "ab_version": "33.2.5",
        "ssmix": "a",
        "device_type": "SM-N950F",
        "device_brand": "samsung",
        "language": "en",
        "os_api": "28",
        "os_version": "9",
        "openudid": utils.random_text_digit(16),
        "manifest_version_code": "2023302050",
        "resolution": "1080*2094",
        "dpi": "420",
        "update_version_code": "2023302050",
        "_rticket": _rticket,
        "is_pad": "0",
        "current_region":  acc['priority_region'].upper(),
        "app_type": "normal",
        "sys_region": acc['priority_region'].upper(),
        "mcc_mnc": "45201",
        "timezone_name": "Asia/Ho_Chi_Minh",
        "residence": acc['priority_region'].upper(),
        "app_language": "en",
        "ac2": "wifi5g",
        "uoo": "0",
        "op_region": acc['priority_region'].upper(),
        "timezone_offset": "25200",
        "build_number": "33.2.5",
        "host_abi": "arm64-v8a",
        "locale": "en",
        "region": acc['priority_region'].upper(),
        "ts": "1" + utils.random_digit(9),
        "cdid": utils.random_cid(),
        "webcast_sdk_version": "3230",
        "webcast_language": "en",
        "webcast_locale": "en_US",
        "effect_sdk_version": "15.8.0",
        "current_network_quality_info": "{\"tcp_rtt\":76,\"quic_rtt\":76,\"http_rtt\":235,\"downstream_throughput_kbps\":1339,\"quic_send_loss_rate\":-1,\"quic_receive_loss_rate\":-1,\"net_effective_connection_type\":4,\"video_download_speed\":8145}"
    }
    headers = {
          'sdk-version': '2',
          'x-bd-kmsv': '0',
          'x-tt-dm-status': 'login=1;ct=1;rt=1',
          'x-ss-req-ticket': _rticket,
          'multi_login': '1',
          'passport-sdk-version': '19',
          'pns_event_id': '906',
          'x-vc-bdturing-sdk-version': '2.3.5.i18n',
          'x-ss-stub': utils.random_text_digit(32).upper(),
          'x-tt-store-region': acc['priority_region'],
          'x-tt-store-region-src': 'uid',
          'x-ss-dp': '1233',
          'x-tt-trace-id': '00-' + utils.random_text_digit(32) + '-' + utils.random_text_digit(16) + '-01',
          'user-agent': 'com.ss.android.ugc.trill/2023302050 (Linux; U; Android 9; en; SM-N950F; Build/PPR1.180610.011; Cronet/TTNetVersion:996128d2 2024-01-12 QuicVersion:ce58f68a 2024-01-12)',
          'content-type': 'application/x-www-form-urlencoded'
        }
    titlex = {'title': acc['title']}
    en_title = urlencode(titlex, safe=' ')
    payload = f"hashtag_id={acc['topic']}&hold_living_room=1&chat_sub_only_auth=2&screen_shot=1&community_flagged_chat_auth=2&ecom_bc_toggle=3&live_sub_only=0&chat_l_2=1&caption=0&{en_title}&live_sub_only_use_music=0&mobile_binded=0&create_source=0&spam_comments=1&commercial_content_promote_third_party=false&grant_level=0&screenshot_cover_status=2&mobile_validated=0&cover_uri=webcast-sg%2F7323062342785616641&live_agreement=0&orientation=1&commercial_content_promote_myself=false&allow_preview_duration_exp=1&transaction_history=1&chat_auth=1&disable_preview_sub_only=0&grant_group=1&gift_auth=1&star_comment_switch=true&has_commerce_goods=false&open_commercial_content_toggle=false&event_id=-1&star_comment_qualification=false&game_tag_id=0&community_flagged_chat_review_auth=2&age_restricted=0&group_chat_id=0&sdk_key=hd&optout_gift_gallery=false&live_room_mode=4&gen_replay=true&shopping_ranking=1"
    proxiex = get_proxy_by_region(acc['priority_region'])
    response = requests.post(
        url,
        params= params,
        cookies= cookies,
        headers=headers,
        data=payload,
        proxies=proxiex
    ).json()
    if 'data' in response:
        data_live = response['data']
        # print(data_live)
        if 'stream_url' in data_live:
            url_stream = data_live['stream_url']['rtmp_push_url']
            room_id = data_live['living_room_attrs']['room_id']
        else:
            return json.dumps(response)
    else:
        return json.dumps(response)
    return url_stream + ";;" + str(room_id)

def continue_key_live(id):
    acc = load_tiktok_acc(id)
    url_stream = "Error"
    if acc:
        domain=get_domain(acc)
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/room/continue/"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version':P_WEBCAST_VERSION,
            'live_mode':6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
       
        #print(json.dumps(cookies));
        data = {
            'title': acc['title'],
            'live_studio': '1',
            'gen_replay': 'true',
            'chat_auth': '0',
            # 'cover_uri': '720x720/tos-maliva-avt-0068/7149784794476806149',
            'close_room_when_close_stream': 'false',
            'hashtag_id': acc['topic'],
            'game_tag_id': '0',
            'screenshot_cover_status': '1',
            'gift_auth': '1',
        }
        response = requests.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()
        if 'data' in response:
            data_live=response['data']
            #print(data_live)
            if 'stream_url' in data_live:
                url_stream = data_live['stream_url']['rtmp_push_url']
                room_id=data_live['living_room_attrs']['room_id']
        return url_stream+";;"+str(room_id)
def encode_room(room_id, status):
    room = captchaCheck_pb2.Room()
    room.last_id = room_id
    room.cur_id = room_id
    room.status = status
    #print(room)
    encoded_data = room.SerializeToString()
    if status == 0:
        hex_string = binascii.hexlify(encoded_data).decode()
        spaced_hex_string = ' '.join([hex_string[i:i + 2] for i in range(0, len(hex_string), 2)])
        print(spaced_hex_string)
        spaced_hex_string += " 18 00"
        encoded_data = binascii.unhexlify(spaced_hex_string.replace(' ', ''))
    print(encoded_data)
    return encoded_data

def check_captcha_http(acc, id, room_id, cookies, domain):
    url_domain = f"https://{domain}"
    url = f"{url_domain}/webcast/eco/captcha_check/"
    params = {
        "aid": "8311",
        "app_name": "tiktok_live_studio",
        'device_id': acc['device_id'],
        'install_id': acc['install_id'],
        "channel": "studio",
        "version_code": P_VERSION_CODE,
        "device_platform": "windows",
        "timezone_name": "Asia/Bangkok",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "en-US",
        "browser_platform": "Win32",
        "browser_name": "Mozilla",
        "browser_version": P_BROWSER_VERSION,
        "language": "en",
        "app_language": "en",
        "webcast_language": "en",
        "priority_region": acc['priority_region'],
        "webcast_sdk_version": P_WEBCAST_VERSION,
        "live_mode": "6"
    }
    print(params)
    headers = {
        'accept': 'application/x-protobuf',
        'accept-language': 'en-US',
        'content-type': 'application/x-protobuf',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': H_USER_AGENT,
        'x-ss-dp': '',
        'sdk_aid': '8311'
    }
    proxiex = get_proxy_by_region(acc['priority_region'])
    encoded_data = encode_room(room_id, 0)
    response = requests.post(url, params=params, headers=headers, cookies=cookies, data=encoded_data,
                             proxies=proxiex).json()
    print(response)
    rs = None
    if 'data' in response:
        captcha_decision = response['data']['captcha_decision']
        print(captcha_decision)
        if 'fp' in captcha_decision:
            captcha_decision = json.loads(captcha_decision)
            rs = captcha_decision  # fp,detail,server_sdk_env
            return captcha_decision
    return rs

def check_captcha(acc, id, room_id):
    if acc:
        domain=get_domain(acc)
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/eco/captcha_check/"
        print(url)
        params = {
            "aid": "8311",
            "app_name": "tiktok_live_studio",
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            "channel": "studio",
            "version_code": P_VERSION_CODE,
            "device_platform": "windows",
            "timezone_name": "Asia/Bangkok",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": "en-US",
            "browser_platform": "Win32",
            "browser_name": "Mozilla",
            "browser_version": P_BROWSER_VERSION,
            "language": "en",
            "app_language": "en",
            "webcast_language": "en",
            "priority_region": acc['priority_region'],
            "webcast_sdk_version": P_WEBCAST_VERSION,
            "live_mode": "6"
        }
        print(params)
        headers = {
            'accept': 'application/x-protobuf',
            'accept-language': 'en-US',
            'content-type': 'application/x-protobuf',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '',
            'sdk_aid': '8311'
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        encoded_data=encode_room(room_id, 0)
        response = requests.post(url, params=params, headers=headers, cookies=cookies, data=encoded_data, proxies=proxiex).json()
        print(response)
        rs=None
        if 'data' in response:
            captcha_decision=response['data']['captcha_decision']
            print(captcha_decision)
            if 'fp' in captcha_decision:
                captcha_decision=json.loads(captcha_decision)
                rs = captcha_decision #fp,detail,server_sdk_env
                return captcha_decision
        return rs

def room_ping(id, room_id, stream_id):
    acc = load_tiktok_acc(id)
    if acc:
        domain = get_domain(acc)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/ping/anchor/"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version': P_WEBCAST_VERSION,
            'live_mode': 6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        data = {
            'status': '2',
            'room_id': room_id,
            'stream_id': stream_id,
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        while True:
            print(f"ping--{time.time()}")
            try:
                response = requests.post(
                    url,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                    proxies=proxiex
                ).json()
                print(response)
            except:
                pass
            time.sleep(5)

def get_room_ping_info(acc, domain, room_id, stream_id):
    if acc:
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/ping/anchor/"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version': P_WEBCAST_VERSION,
            'live_mode': 6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        data = {
            'status': '2',
            'room_id': room_id,
            'stream_id': stream_id,
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        return url, params, headers, data, proxiex, cookies
    return None

def room_poll(id, room_id):
    acc = load_tiktok_acc(id)
    if acc:
        domain = get_domain(acc)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/poll/latest"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version': P_WEBCAST_VERSION,
            'live_mode': 6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        data = {
            'room_id': room_id,
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        while True:
            print(f"poll--{time.time()}")
            try:
                response = requests.post(
                    url,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                    proxies=proxiex
                ).json()
                print(response)
            except:
                pass
            time.sleep(10)

def get_room_poll_info(acc, domain, room_id):
    if acc:
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain = f"https://{domain}"
        url = f"{url_domain}/webcast/room/poll/latest"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version': P_WEBCAST_VERSION,
            'live_mode': 6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        data = {
            'room_id': room_id,
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        return url, params, headers, data, proxiex, cookies
    return None

def check_captcha_finish_http(acc, id, room_id, cookies, domain):
    if acc:
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/eco/captcha_check/"
        params = {
            "aid": "8311",
            "app_name": "tiktok_live_studio",
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            "channel": "studio",
            "version_code": P_VERSION_CODE,
            "device_platform": "windows",
            "timezone_name": "Asia/Bangkok",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": "en-US",
            "browser_platform": "Win32",
            "browser_name": "Mozilla",
            "browser_version": P_BROWSER_VERSION,
            "language": "en",
            "app_language": "en",
            "webcast_language": "en",
            "priority_region": acc['priority_region'],
            "webcast_sdk_version": P_WEBCAST_VERSION,
            "live_mode": "6"
        }
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US',
            'content-type': 'application/x-protobuf',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '',
            'sdk_aid': '8311'
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        encoded_data=encode_room(room_id, 1)
        response = requests.post(url, params=params, headers=headers, cookies=cookies, data=encoded_data, proxies=proxiex).json()
        print(response)

def check_captcha_finish(acc, id, room_id):
    if acc:
        domain=get_domain(acc)
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/eco/captcha_check/"
        params = {
            "aid": "8311",
            "app_name": "tiktok_live_studio",
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            "channel": "studio",
            "version_code": P_VERSION_CODE,
            "device_platform": "windows",
            "timezone_name": "Asia/Bangkok",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": "en-US",
            "browser_platform": "Win32",
            "browser_name": "Mozilla",
            "browser_version": P_BROWSER_VERSION,
            "language": "en",
            "app_language": "en",
            "webcast_language": "en",
            "priority_region": acc['priority_region'],
            "webcast_sdk_version": P_WEBCAST_VERSION,
            "live_mode": "6"
        }
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US',
            'content-type': 'application/x-protobuf',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '',
            'sdk_aid': '8311'
        }
        proxiex = get_proxy_by_region(acc['priority_region'])
        encoded_data=encode_room(room_id, 1)
        response = requests.post(url, params=params, headers=headers, cookies=cookies, data=encoded_data, proxies=proxiex).json()
        print(response)
        rs=None
        if 'data' in response:
            captcha_decision=response['data']['captcha_decision']
            print(captcha_decision)
            if 'fp' in captcha_decision:
                captcha_decision=json.loads(captcha_decision)
                rs = captcha_decision #fp,detail,server_sdk_env
                rs={
                "fp":captcha_decision['fp'],
                "detail":captcha_decision['detail'],
                "server_sdk_env":captcha_decision['server_sdk_env'],
                }
        return rs

def fp_solve_captcha(acc, id, room_id, cookies, domain):
    try:
        capt = check_captcha_http(acc, id, room_id, cookies, domain)
        if capt:
            print("capt--------check-verify")
            print(capt)
            print(TikTokCaptchaSolver(
                device_id=acc['device_id'], install_id=acc['install_id'], cookies=cookies, capt=capt,
                user_agents=H_USER_AGENT, browser_version=P_BROWSER_VERSION, proxies=None
            ).solve_captcha())
            check_captcha_finish_http(acc, id, room_id, cookies, domain)
    except:
        traceback.print_exc()
        pass
def fp_ping(ping_url, ping_params, ping_cookies, ping_headers, ping_data, ping_proxiex):
    try:
        print(f"ping--{time.time()}")
        response = requests.post(
            ping_url,
            params=ping_params,
            cookies=ping_cookies,
            headers=ping_headers,
            data=ping_data,
            proxies=ping_proxiex
        ).text
        print(response)
        if "room has finished" in response:
            return False
    except:
        pass
    return True
def fp_poll(poll_url, poll_params, poll_cookies, poll_headers, poll_data, poll_proxiex):
    try:
        print(f"poll--{time.time()}")
        response = requests.post(
            poll_url,
            params=poll_params,
            cookies=poll_cookies,
            headers=poll_headers,
            data=poll_data,
            proxies=poll_proxiex
        ).text
        print(response)
        if "room has finished" in response:
            return False
    except:
        pass
    return True
def solve_ping_poll_captcha_auto(id, room_id, stream_id, retries=3):
    try:
        id = int(id)
        room_id = int(room_id)
        print(f"solve_ping_poll_captcha_auto {id}--{room_id}--{stream_id}")
        acc = load_tiktok_acc(id)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        domain=get_domain(acc)
        ping_url, ping_params, ping_headers, ping_data, ping_proxiex, ping_cookies = get_room_ping_info(
            acc, domain, room_id, stream_id)
        poll_url, poll_params, poll_headers, poll_data, poll_proxiex, poll_cookies = get_room_poll_info(
            acc, domain, room_id)
        cnt_poll=3
        cnt_captcha=6
        is_running=True
        while is_running:
            cnt_poll+=1
            cnt_captcha+=1
            is_running=fp_ping(ping_url, ping_params, ping_cookies, ping_headers, ping_data, ping_proxiex)
            if cnt_poll>1:
                fp_poll(poll_url, poll_params, poll_cookies, poll_headers, poll_data, poll_proxiex)
                cnt_poll=0
            if cnt_captcha>5:
                fp_solve_captcha(acc, id, room_id, cookies, domain)
                cnt_captcha=0
            time.sleep(5)
    except:
        traceback.print_exc()
        time.sleep(1)
        if retries>1:
            solve_ping_poll_captcha_auto(id, room_id, stream_id, retries-1)
def solve_captcha_auto(id, room_id, retries=3):
    try:
        id = int(id)
        room_id = int(room_id)
        print(f"solve_captcha_auto {id}--{room_id}")
        acc = load_tiktok_acc(id)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        domain=get_domain(acc)
        while True:
            try:
                capt = check_captcha_http(acc, id, room_id, cookies, domain)
                if capt:
                    print("capt--------check-verify")
                    print(capt)
                    print(TikTokCaptchaSolver(
                        device_id=acc['device_id'], install_id=acc['install_id'], cookies=cookies, capt=capt, user_agents= H_USER_AGENT, browser_version=P_BROWSER_VERSION, proxies=None
                    ).solve_captcha())
                    check_captcha_finish_http(acc, id, room_id, cookies, domain)
            except:
                traceback.print_exc()
                pass
            time.sleep(30)
    except:
        traceback.print_exc()
        time.sleep(1)
        if retries>1:
            solve_captcha_auto(id, room_id, retries-1)

def solve_captcha(id, room_id):
    id=int(id)
    room_id=int(room_id)
    print(f"solve_captcha {id}--{room_id}")
    acc = load_tiktok_acc(id)
    capt=check_captcha(acc, id, room_id)
    cookie_encr = acc['cookie']
    cookies = json.loads(utils.decrypt_data(cookie_encr))
    proxiex = get_proxy_by_region(acc['priority_region'])
    if capt:
        print("capt--------check-verify")
        print(capt)
        print(TikTokCaptchaSolver(
            device_id=acc['device_id'], install_id=acc['install_id'], cookies=cookies, capt=capt, user_agents= H_USER_AGENT, browser_version=P_BROWSER_VERSION, proxies=proxiex
        ).solve_captcha())
        check_captcha_finish(acc, id, room_id)
def finish_live(id):
    acc = load_tiktok_acc(id)
    if acc:
        domain=get_domain(acc)
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url_domain=f"https://{domain}"
        url=f"{url_domain}/webcast/room/finish_abnormal/"
        params = {
            'aid': '8311',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version':P_WEBCAST_VERSION,
            'live_mode':6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        proxiex=get_proxy_by_region(acc['priority_region'])
        data = {
            'title': 'Luong live test',
            'live_studio': '1',
            'gen_replay': 'true',
            'chat_auth': '1',
            # 'cover_uri': '720x720/tos-maliva-avt-0068/7149784794476806149',
            'close_room_when_close_stream': 'false',
            'hashtag_id': '44',
            'game_tag_id': '0',
            'screenshot_cover_status': '1',
            'gift_auth': '1',
        }
        response = requests.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxiex,
        ).json()
        return response

def check_violation(id):
    #violation_list_type = 1: history
    #violation_list_type = 0: active
    acc = load_tiktok_acc(id)
    if acc:
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url="https://webcast.tiktok.com/webcast/eco/violation_list/"
        params = {
                'violation_list_type': '0',
                'last_id': '',
                'language': 'en',
                'aid': '304449',
                'app_language': 'en',
                'webcast_language': 'en',
                'app_name': 'tiktok_web',
                'browser_language': 'en-US',
                'msToken': '',
                'X-Bogus': '',
                '_signature': '',
            }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'origin': 'https://livecenter.tiktok.com',
            'referer': 'https://livecenter.tiktok.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TikTokLIVEStudio/0.48.2 Chrome/104.0.5112.102 Electron/20.1.0-tt.7.release.mssdk.27 TTElectron/20.1.0-tt.7.release.mssdk.27 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-argus': 'dBLjFcyYWHm3xubH3s28qd5c+gJDWznHEyuia9sTQRAZw2VOhdstVjG6/vX87L5YHxxvPiQj/tcDUGVRcuoLBO+B82bknIg9QR36jA3cubFQgeBOmNqi87mY9LApW6X+4Tos6I5Q88OrmaCrsFG+LDMpH7dQrOWtzUReKiI7+j7/z4y3nw6VC46GgcANZXtAvtNRqd0erjxAw6vGAfQmpNOr29utwG724+U2RMYAK6gkUXOKPqtrsr5D+rpNdc+PCiM=',
            'x-khronos': '1704439285',
            'x-ladon': 'SBwAACwIE5AGn4YRX2TzorkFMWvkLqLOzIKYUTwcNWEVkqGY',
        }
        response = requests.get(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            
        ).text
        print(response)

def product_check(id, url_check):
    acc = load_tiktok_acc(id)
    results=None
    if acc:
        url="https://shop.tiktok.com/api/v1/streamer_desktop/product_link/check"
        params = {
            'aid': '253642',
            'app_name': 'i18n_ecom_alliance',
            'device_id': 0,
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': '0.17.0',
            'device_platform': 'web',
            'cookie_enabled':'true',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en'
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }
        cookie_encr=acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        data = {
            "urls": [
                url_check
            ]
        }
        response = requests.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()
        if 'data' in response:
            product_info=response['data']['results'][0]['product_info']
            results={
                'product_id': product_info['closed_loop_product']['product_id'],
                'main_plan_id': product_info['closed_loop_product']['affiliate_info']['plan_id_list'][0],
                'product_type': product_info['product_type'],
                'source': product_info['source'],
                'source_from': product_info['source_from']

            }
        return results

def product_add(id_user, room_id, product_data):

    acc = load_tiktok_acc(id_user)
    if acc:
        sess = requests.Session()
        csrf=get_csrf(acc, sess)
        url = "https://shop.tiktok.com/api/v1/streamer_desktop/live_product/add?user_language=en&locale=en&aid=253642&app_name=i18n_ecom_alliance&device_id=0&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36&browser_online=true&timezone_name=Asia%2FSaigon&carrier_region=vn"
        params = {
            'aid': '253642',
            'app_name': 'i18n_ecom_alliance',
            'device_id': 0,
            'channel': 'studio',
            'version_code': '0.17.0',
            'device_platform': 'web',
            'cookie_enabled': 'false',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en'
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-secsdk-csrf-token':csrf
        }
        data = {"room_id":room_id, "product_info": [{"product_id": product_data['product_id'],"product_type":  product_data['product_type'],
                                                   "source": product_data['source'],
                                                   "source_from": product_data['source_from'], "main_plan_id": product_data['main_plan_id']}]}

        data=json.dumps(data)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        response = sess.post(
            url,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        print(response.text)
        response=response.json()
        return response

def product_pin(id_user, room_id, product_id):
    acc = load_tiktok_acc(id_user)
    if acc:
        sess = requests.Session()
        csrf=get_csrf(acc, sess)
        url = "https://shop.tiktok.com/api/v1/streamer_desktop/live_product/pin"
        params = {
            'aid': '253642',
            'app_name': 'i18n_ecom_alliance',
            'device_id': 0,
            'channel': 'studio',
            'version_code': '0.17.0',
            'device_platform': 'web',
            'cookie_enabled': 'false',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en'
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-secsdk-csrf-token':csrf
        }
        data = {"room_id": room_id, "product_id": product_id,"op":1}
        data=json.dumps(data)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        response = sess.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        print(response.text)
        # response=response.json()
        # if 'message' in response and response['message'] == "success":
        #     print("ok!!!!!!!")
        # return response
def product_delete(id_user, product_id):
    acc = load_tiktok_acc(id_user)
    if acc:
        sess = requests.Session()
        csrf=get_csrf(acc, sess)
        url = "https://shop.tiktok.com/api/v1/streamer_desktop/live_product/delete"
        params = {
            'aid': '253642',
            'app_name': 'i18n_ecom_alliance',
            'device_id': 0,
            'channel': 'studio',
            'version_code': '0.17.0',
            'device_platform': 'web',
            'cookie_enabled': 'false',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en'
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-secsdk-csrf-token':csrf
        }
        data = {"product_ids": [product_id]}
        #print(sess.cookies)
        data=json.dumps(data)
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        response = sess.post(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        print(response.text)
        # response=response.json()
        # if 'message' in response and response['message'] == "success":
        #     print("ok!!!!!!!")
        # return response
def product_list(id_user):
    acc = load_tiktok_acc(id_user)
    if acc:
        sess = requests.Session()
        url = "https://shop.tiktok.com/api/v1/streamer_desktop/live_product/list"
        params = {
            'aid': '253642',
            'app_name': 'i18n_ecom_alliance',
            'device_id': 0,
            'channel': 'studio',
            'version_code': '0.17.0',
            'device_platform': 'web',
            'cookie_enabled': 'false',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': '5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F110.0.0.0+Safari%2F537.36',
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en'
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        response = sess.get(
            url,
            params=params,
            cookies=cookies,
            headers=headers
        )
        print(response.text)

def get_csrf(acc, sess):
    headers = {
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'x-secsdk-csrf-version': '1.2.7',
        'x-secsdk-csrf-request': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shop.tiktok.com/streamer/live/product/list',
        'accept-language': 'en-US,en;q=0.9',
    }
    cookie_encr = acc['cookie']
    cookies = json.loads(utils.decrypt_data(cookie_encr))
    response = sess.head('https://shop.tiktok.com/api/v1/streamer_desktop/live_product/pin', cookies=cookies,
                             headers=headers)
    csrf = response.headers['x-ware-csrf-token']
    return csrf.split(',')[1]


def get_account_info(id):
    acc = load_tiktok_acc(id)
    if acc:
        cookie_encr = acc['cookie']
        cookies = json.loads(utils.decrypt_data(cookie_encr))
        url = f"https://shop.tiktok.com/api/v1/streamer_desktop/account_info/get"
        params = {
            'aid': '253642',
            'app_name': 'tiktok_live_studio',
            'device_id': acc['device_id'],
            'install_id': acc['install_id'],
            'channel': 'studio',
            'version_code': P_VERSION_CODE,
            'device_platform': 'windows',
            'timezone_name': 'Asia/Saigon',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'en-US',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': P_BROWSER_VERSION,
            'language': 'en',
            'app_language': 'en',
            'webcast_language': 'en',
            'priority_region': acc['priority_region'],
            'webcast_sdk_version': P_WEBCAST_VERSION,
            'live_mode': 6
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': H_USER_AGENT,
            'x-ss-dp': '8311',
            'sdk_aid': '8311'
        }

        proxiex = get_proxy_by_region(acc['priority_region'])
        response = requests.get(
            url,
            params=params,
            cookies=cookies,
            headers=headers,
            proxies=proxiex
        ).text
        return response
    else:
        return json.dumps({"mess":"account doesn't exists"})
    return json.dumps({"mess":"Error"})


# url_pro="https://shop.tiktok.com/view/product/1729578638513506709?region=VN&local=en"
# room_id="7209941296000092955"
# product_list(240)
# product_data=product_check(240, url_pro)
# product_add(240, room_id, product_data)
# product_pin(240,room_id,product_id)
# product_delete(240,"1729578638513506709")
#solve_captcha(user_id, room_id)
if __name__ == '__main__':
    solve_captcha(12864, 7351362532396108587)
    if len(sys.argv) < 1:
        print("Error: need Id")
    if sys.argv[1] == "live_create":
        finish_live(sys.argv[2])
        x=create_key_live(sys.argv[2])
        print(x)
    if sys.argv[1] == "active_live_mobile":
        active_live_mobile(sys.argv[2])
    if sys.argv[1] == "live_create_mobile":
        finish_live(sys.argv[2])
        x=create_key_live_mobile(sys.argv[2])
        print(x)
    if sys.argv[1] == "solve_captcha":
        print("solve_captcha")
        solve_captcha(sys.argv[2], sys.argv[3])
    if sys.argv[1] == "room_ping":
        room_ping(sys.argv[2], sys.argv[3], sys.argv[4])
    if sys.argv[1] == "room_poll":
        room_poll(sys.argv[2], sys.argv[3])

    if sys.argv[1] == "live_finish":
        finish_live(sys.argv[2])
    if sys.argv[1] == "check_violation":
        check_violation(sys.argv[2])        
    if sys.argv[1] == "product_list":
        product_list(sys.argv[2])
    if sys.argv[1] == "product_add":
        url_pro= str(sys.argv[4])
        product_data= product_check(sys.argv[2], url_pro)
        product_add(sys.argv[2], sys.argv[3], product_data)
    if sys.argv[1] == "product_pin":
        product_id = sys.argv[4]
        product_pin(sys.argv[2], sys.argv[3], product_id)
    if sys.argv[1] == "product_delete":
        product_id = sys.argv[3]
        product_delete(sys.argv[2], product_id)
    if sys.argv[1] == "get_account_info":
        acc_id = sys.argv[2]
        x=get_account_info(acc_id)
        print(x)



