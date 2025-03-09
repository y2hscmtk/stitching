from stitching import Stitcher
import cv2
import numpy as np

stitcher = Stitcher(detector="sift", crop=True)

cameras = stitcher.get_camera(["01.jpg", "02.jpg", "03.jpg"])

print(cameras)

# 2. 기존 stitch() 함수를 사용하여 파노라마 생성 (내부적으로 매번 호모그래피 계산)
panorama_standard = stitcher.stitch(["01.jpg", "02.jpg"])
cv2.imwrite("panorama_standard.jpg", panorama_standard)
print("save image - sticher : panorama_standard.jpg")

# 3. 미리 계산된 카메라 파라미터로 파노라마 생성
panorama_precomputed = stitcher.stitch(["01.jpg", "02.jpg"], cameras)
cv2.imwrite("panorama_precomputed.jpg", panorama_precomputed)
print("saved image - precomputed : panorama_precomputed.jpg")