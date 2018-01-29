# coding:utf-8
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


# 等比例压缩图片
def resizeImg(img_path, dst_w=0, dst_h=0, qua=85):
    """''
    只给了宽或者高，或者两个都给了，然后取比例合适的
    如果图片比给要压缩的尺寸都要小，就不压缩了
    """
    img = Image.open(img_path+'.jpg')
    ori_w, ori_h = img.size
    print('ori_w,ori_h', ori_w, ori_h)
    widthRatio = heightRatio = None
    ratio = 1

    if (ori_w and ori_w > dst_w) or (ori_h and ori_h > dst_h):
        if dst_w and ori_w > dst_w:
            widthRatio = float(dst_w) / ori_w  # 正确获取小数的方式
        if dst_h and ori_h > dst_h:
            heightRatio = float(dst_h) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio

        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    img.resize((newWidth, newHeight), Image.ANTIALIAS).save(img_path + u'@300.jpg', "JPEG", quality=qua)
    print u'等比压缩完成'


if __name__ == "__main__":
    resizeImg('/Users/bingpo/Desktop/python/blog/static/pictures/0x0ss-30.jpg', dst_w=300, qua=85)
