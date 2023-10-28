from cairosvg import svg2png
# 设置背景颜色
background_color = 'white'
svg2png(url = 'https://img.zdic.net/xz/swdz/9999_7712.svg', background_color=background_color, output_width=1024, output_height=1024, write_to='output.png')


# cairosvg.svg2png(
#     file_obj=None,     # 输入的 SVG 文件对象，可以是文件名的字符串，文件对象，或 SVG 数据的字符串
#     write_to=None,     # 输出的 PNG 文件名或文件对象，如果为 None，则返回 PNG 数据作为字节字符串
#     parent_width,parent_height       # 指定 SVG 图像在转换为 PNG 图像时的父容器宽度。这个参数是可选的，并且通常情况下，你不需要显式地指定它
#     output_width=None, # 输出图像的宽度，可以是像素数或字符串（如"100px"）
#     output_height=None, # 输出图像的高度，可以是像素数或字符串（如"100px"）
#     scale=None,        # 输出图像的缩放比例
#     dpi=None,          # 输出图像的分辨率（每英寸点数）
#     format=None,       # 输出图像的格式（通常不需要指定）
#     output=None,       # 输出选项，可以是"original"、"rgb"、"rgba"或"alpha"，用于控制输出的颜色通道
#     output_dict=None   # 输出选项的字典，用于更详细的控制输出
#       negate_colors 颜色反转
#   invert_images这个参数的作用与 negate_colors 参数类似，用于创建底片效果的图像。当设置为 True 时，这个参数会将整个 SVG 图像的颜色反转，产生反色的效果。
#       
# )
