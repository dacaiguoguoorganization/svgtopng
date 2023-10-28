from cairosvg import svg2png
# 设置背景颜色
background_color = 'white'
svg2png(url = 'https://img.zdic.net/xz/swdz/9999_7712.svg', background_color=background_color, parent_width=1024, parent_height=1024, write_to='output.png')