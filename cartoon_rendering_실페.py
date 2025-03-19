import cv2
import numpy as np

def cartoonify_fail(image_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 800))  # 크기 조절
    
    # 색상 필터 적용 (너무 강하게 적용하여 디테일 손실)
    smooth_color = cv2.bilateralFilter(img, d=30, sigmaColor=150, sigmaSpace=150)

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 적용 (너무 강하게 설정하여 디테일 손실)
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 10)
    
    # 윤곽선 검출 (임계값 조절 실패)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, blockSize=3, C=10
    )

    # 윤곽선을 더 강조하기 위해 과도한 모폴로지 연산 적용 (경계선이 깨짐)
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # 색상과 윤곽선 결합 (너무 강한 효과 적용)
    cartoon = cv2.bitwise_and(smooth_color, smooth_color, mask=edges)

    # 결과 출력
    cv2.imshow("Failed Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cartoonify_fail('image1.jpg')
