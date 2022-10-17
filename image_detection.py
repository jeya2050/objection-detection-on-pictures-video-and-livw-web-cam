import cv2
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
image=cv2.imread("/Users/jeya/Desktop/yolo v5/pexels-tetyana-kovyrina-1439087.jpg")
result=model(image)
df=result.pandas().xyxy[0]
print(df)
for ind in df.index:
    x1,y1=int(df['xmin'][ind]),int(df['ymin'][ind])
    x2,y2=int(df['xmax'][ind]),int(df['ymax'][ind])
    label=df['name'][ind]
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.putText(image,label,(x1,y1-5),cv2.FONT_HERSHEY_PLAIN,5,(255,255,0),2)
cv2.imshow("image",image)
cv2.waitKey()