from glob import glob
import cv2
import mtcnn



tous = glob('./*.jpg')

for j in tous:
    img = cv2.imread(j)
    face_detector = mtcnn.MTCNN()
    CONF_T = 0.05
    img_rgb = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
    results = face_detector.detect_faces(img_rgb)
	# print(results)
    for res in results:
        x1, y1, width, height = res['box']
        x1, y1 = abs(x1), abs (y1)
        x2, y2 = x1 + width, y1 + height
        confidence = res['confidence']
        if confidence < CONF_T:
            continue
        key_points = res['keypoints'].values()
        img[y1:y2, x1:x2] = cv2.blur(img[y1:y2, x1:x2],(200, 200))
		# img[y1:y2, x1:x2] = cv2.rectangle(img[y1:y2, x1:x2],1, 10)
	# cv2.imshow(j, img)
    k =  j[:-4]
    l = k+'.png'
    cv2.imwrite(l,img)
    cv2.waitKey(0)

