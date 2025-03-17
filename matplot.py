
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    img_file = "img/Lena.png"  # 표시할 이미지 경로 ---①
    # img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 회색으로 읽기
    img_color = cv2.imread(img_file, cv2.IMREAD_COLOR)  # 컬러영상 읽기

    if img is not None:
        plt.imshow(img, cmap='gray')
        plt.show()

        img_rgb= cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.show()

        cv2.imshow('IMG Gray', img)  # 읽은 이미지를 화면에 표시 --- ③
        cv2.waitKey() # 키가 입력될 때 까지 대기 --- ④
        cv2.destroyAllWindows()  # 창 모두 닫기 --- ⑤

    else:
        print('No image file.')

    print('program is terminated')
