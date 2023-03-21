# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import cv2
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    img_file = "img/Lenna.png"  # 표시할 이미지 경로 ---①
    img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②
    #img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 회색으로 읽기

    print(type(img))

    if img is not None:
        #plt.imshow(img, cmap='gray')
        #plt.show()

        cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시 --- ③
        cv2.waitKey() # 키가 입력될 때 까지 대기 --- ④
        cv2.destroyAllWindows()  # 창 모두 닫기 --- ⑤

    else:
        print('No image file.')

    save_file = 'img/Lenna_gray.jpg'
    cv2.imwrite(save_file, img)  # 파일로 저장, 포맷은 확장에 따름

    print('program is terminated')
