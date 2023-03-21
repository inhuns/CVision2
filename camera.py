
import cv2

cap = cv2.VideoCapture(0) 	        # 카메라 device 캡쳐객체 생성 ---①
if cap.isOpened(): 			        # 캡쳐 객체 초기화 확인
    while cv2.waitKey(33)<0:
    # while True:
        ret, frame = cap.read()       # 다음 프레임 읽기 --- ②
        if ret:                     # 프레임 읽기 정상
            cv2.imshow("videoFrame", frame) # 화면에 표시 --- ③
            cv2.waitKey(25)
        else:                       # 다음 프레임 읽을 수 없슴,
            break                   # 재생 완료
else:
    print("can't open camera.") # 캡쳐 객체 초기화 실패

cap.release()                   # 캡쳐 자원 반납
cv2.destroyAllWindows()
print('program is terminated')