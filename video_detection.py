import cv2
import torch
video=cv2.VideoCapture("/Users/jeya/Desktop/yolo v5/Pexels Videos 1721303.mp4")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
while True:
    success,frame=video.read()
    if success==True:
        result=model(frame)
        df=result.pandas().xyxy[0]
        for ind in df.index:
            x1,y1=int(df["xmin"][ind]),int(df["ymin"][ind])
            x2,y2=int(df["xmax"][ind]),int(df["ymax"][ind])
            label=df["name"][ind]
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.putText(frame,label,(x1,y1+5),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),4)
        cv2.imshow("frame",frame)
        cv2.waitKey()
    else:
        print("frame nil")
        break