# openCVをインポート
import cv2

# 画像を読み込む
img = cv2.imread("pokemon_rowlet.png")

# RBGのB成分だけを0にする
#img[:,:,0] = 0

# 画像を表示する
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
