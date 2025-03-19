import cv2
import numpy as np

def cute_cartoonify(image_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 800))  # 크기 조절 
    
    # 색상을 부드럽게 하기 위한 필터 적용
    smooth_color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러 적용 (선 부드럽게)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 적응형 임계값 (윤곽선 추출)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                cv2.THRESH_BINARY, blockSize=9, C=2)

    # 윤곽선을 부드럽게 만들기 위해 모폴로지 변환 적용
    kernel = np.ones((2, 2), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # 색상과 윤곽선 결합 (연한 효과 유지)
    cartoon = cv2.bitwise_and(smooth_color, smooth_color, mask=edges)

    # 결과 출력
    cv2.imshow("Cute Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cute_cartoonify('image1.jpg')  
