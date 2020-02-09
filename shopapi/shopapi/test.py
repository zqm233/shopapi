import requests
import re
def get_url_from_js(rid):
    # 从播放页源代码中直接匹配地址
    header = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.get('https://www.douyu.com/{}'.format(rid), headers=header).text
        real_url = re.findall(r'live/({}[\d\w]*?)_'.format(rid), response)[0]
    except:
        real_url = '直播间未开播或不存在'
    return "http://tx2play1.douyucdn.cn/live/" + real_url + ".flv?uuid="

print(get_url_from_js('554559'))