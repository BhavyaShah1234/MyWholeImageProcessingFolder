import cv2 as cv

cap = cv.VideoCapture(0)

class_file = 'coco (2).names'
with open(class_file, 'rt') as f:
	class_names = f.read().rstrip('\n').split('\n')

config_path = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weights_path = 'frozen_inference_graph.pb'

net = cv.dnn_DetectionModel(weights_path, config_path)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
	success, img = cap.read()
	class_ids, confidence, bounding_box = net.detect(img, confThreshold=0.6, nmsThreshold=0.3)
	if len(class_ids) != 0:
		for class_id, conf, bbox in zip(class_ids.flatten(), confidence.flatten(), bounding_box):
			cv.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), color=(0, 255, 0), thickness=2)
			cv.putText(img, f'{class_names[class_id-1].upper()} {round(conf * 100, 3)}%', (bbox[0]+10, bbox[1]-10), cv.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)

	cv.imshow('Img', img)
	cv.waitKey(1)
