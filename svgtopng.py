from cairosvg import svg2png
import requests

# 发起GET请求
url = 'https://img.zdic.net/xz/swdz/9999_7712.svg'
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    svg_code = response.text
    svg2png(bytestring=svg_code, parent_width=1024, parent_height=1024, write_to='output.png')
else:
    print(f'请求失败，状态码: {response.status_code}')

