import cv2
import face_recognition
#读入已知人脸
shuangyong=cv2.imread('C:\\Users\\Administrator\\Desktop\\G2$C(9Q}M9TKN6YRWHUMWZE.png')
#人脸编码为128维向量
known_face_encoding=face_recognition.face_encodings(shuangyong)[0]
#人脸编码放入列表计数
known_face_encodings=[known_face_encoding]
#与编码对应的人脸的代号
known_face_name=['1']
#打开摄像头
#vc=cv2.VideoCapture("http://admin:admin@192.168.0.101:8081/")
vc=cv2.VideoCapture(0)
while True:
	#获取图片
	ret,img=vc.read()
	#获取人脸

	locations=face_recognition.face_locations(img)
	#编码
	face_encodings=face_recognition.face_encodings(img,locations)

	for (top,right,bottom,left),face_encoding in zip(locations,face_encodings):
		#与列表中的人脸比较,如果没有匹配到则存入到列表
		matchs=face_recognition.compare_faces(known_face_encodings,face_encoding)

		name='uk'

		for match,known_name in zip(matchs,known_face_name):
			if match==False:
				continue
			else:
				name=known_name
		if name=='uk':

			known_face_encodings.append(face_encoding)
			known_face_name.append(str(len(known_face_encodings)))
		cv2.rectangle(img,(left,top),(right,bottom),(0,0,255),2)
		cv2.putText(img,name,(left,top-20),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,255),2)

	cv2.imshow('video',img)

	if cv2.waitKey(1)!=-1:
		vc.release()
		cv2.destroyAllWindows()

		break
#输出列表人脸的个数
print(len(known_face_encodings)-1)
print(known_face_name)


