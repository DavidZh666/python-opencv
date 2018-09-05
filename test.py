import cv2
##
def getsaveimg():
	src=cv2.imread('1.jpg',0)  #gray model
	cv2.imshow('image',src)
	k=cv2.waitKey(0)
	if k==27:
		cv2.destroyAllWindows()
		#cv2.destoryWindows('image')
	elif k == ord('s'):
		cv2.imwrite("gray.png",src)
		cv2.destroyWindow('image')

def getvideo():
	cap = cv2.VideoCapture('test.mp4')
	#cap =cv2.VideoCapture(0)
	while cap.isOpened():
		ret,frame = cap.read()##ret =True or false
		gray=cv2.cvtColor(frame,cv2.COLOR2GRAY) ##to gray
		cv2.imshow('frame', gray)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def getvideosize():
	cap = cv2.VideoCapture('output.avi')
	while cap.isOpened():
		ret, frame = cap.read()
		print(frame.shape)
		cv2.imshow('frame', frame)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()


def savevideo():
	cap=cv2.VideoCapture('test.mp4')
	#define the codec and creat VideoWriter object
	### XVID MPEG-4,***.avi;I420 YUV,***.avi;PIMI MPEG-1 ***.avi;
	### THEO Ogg Vorbis,***ogv;FLV1 flash .flv;MJPG    ***.avi/***.mp4
	#fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
	fourcc=cv2.VideoWriter_fourcc(*'XVID')
	out=cv2.VideoWriter("output.avi",fourcc,25.0,(1280,720))
	#out=cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

	while(cap.isOpened):
		ret,frame=cap.read()
		if ret ==True:
			frame=cv2.flip(frame,0)  ##flip image
			out.write(frame)
			cv2.imshow('frame',frame)
			if cv2.waitKey(1)&0xff==ord('q'):
				break
		else:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

getvideosize()
	