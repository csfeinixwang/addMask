import cv2
import base64
import requests
import numpy as np



def  get_mouth(dst_pic):
     with open(dst_pic, 'rb') as f:
         base64_data = base64.b64encode(f.read())
     url='https://api-cn.faceplusplus.com/facepp/v1/face/thousandlandmark'
     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
     data={ # api_key,api_secret需自己申请
           'api_key':'5qiqI4LvEgImt30iMs2OfMO2fkSbSUxa',
           'api_secret':'84q3sEfJumnJwweojbNMFkX3ZoL3hXji',
           'return_landmark': 'mouth',
           'image_base64': base64_data
           }
     r=requests.post(url,headers=headers,data=data)
     mouth=r.json()['face']['landmark']['mouth']
     x,y=[],[]
     for i in mouth.values():
         y.append(i['y'])
         x.append(i['x'])
     y_max=max(y)
     y_min=min(y)
     x_max=max(x)
     x_min=min(x)
     middle_x=int((x_max+x_min)/2)
     middle_y=int((y_max+y_min)/2)
     size=(int(3*(x_max-x_min)),int(5*(y_max-y_min)))
     return (middle_x,middle_y),size

def  add_mask(img_path,img_outPath):
     src_pic="c://Users//mac//Pictures//iphone_se//mask.png"
     center,size=get_mouth(img_path)
     src=cv2.imread(src_pic)
     src=cv2.resize(src,size)
     dst=cv2.imread(img_path)
     # 掩膜mask
     mask=255*np.ones(src.shape, src.dtype)
     output=cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
     cv2.imwrite(img_outPath, output)

if __name__ == "__main__":
    add_mask("C://Users//mac//Pictures//iphone_se//fei.jpg","C://Users//mac//Pictures//iphone_se//fei1.jpg")