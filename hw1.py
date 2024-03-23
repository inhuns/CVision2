
import cv2
import matplotlib.pyplot as plt

img_file = "img/Lenna.png"  # 표시할 이미지 경로 ---①
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 회색으로 읽기
img_color = cv2.imread(img_file, cv2.IMREAD_COLOR)  # 컬러영상 읽기

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(img_color)

if img is not None:
    plt.subplot(2, 2, 3)
    plt.imshow(img, cmap='gray')  # cmap = color map

    #img_rgb = cv2.... ?)        # Q)  OpenCV의 색변환 함수를 이용하여 BGR을 RGB로 변경하시오.
    #plt.subplot(2, 2, 4)
    #plt.imshow(img_rgb)
    plt.show()

else:
    print('No image file.')

