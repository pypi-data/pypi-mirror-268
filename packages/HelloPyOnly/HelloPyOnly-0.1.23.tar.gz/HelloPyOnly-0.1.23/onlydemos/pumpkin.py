import pygame,math,cv2,dlib
from hellopy.gameobject.sprite import *
from hellopy.gameobject.circle import circle
from hellopy.gameobject.text import text
from hellopy.window import window

__all__ = ["vA2B","VirtualFace",'distance','find_center','get_face_angle', 'detect_face']

def distance(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
def find_center(points):
    x_sum = 0
    y_sum = 0
    for item in points:
        x_sum += item.x
        y_sum += item.y
    return (x_sum/len(points),y_sum/len(points))

def detect_face(index=0):
    try: p = get_landmarks()[index]
    except: p = False
    return p

def get_face_angle(p):
    p1 = ((p[39].x+p[42].x)/2, (p[39].y+p[42].y)/2)
    p2 = ((p[31].x+p[35].x)/2, (p[31].y+p[35].y)/2)
    return math.degrees(math.atan((p1[0]-p2[0])/(p1[1]-p2[1])))

def draw_landmarks(p):
    # 绘制面部特征点
    if not p:
        text("No face detected.", window.w/2-100,window.h/2,40,"red")
        return
    for n in range(len(p)):
        x = p[n].x
        y = p[n].y
        circle(x,y,1,"red")
        text(str(n),x,y,20,"blue")

def vA2B(A,B):
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    return pygame.math.Vector2(dx,dy)

def get_landmarks():
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    fps = []
    for face in faces:
        # 获取面部特征点
        landmarks = predictor(gray, face)
        fp = []
        for i in range(68):
            fp.append((landmarks.part(i)))
        fps.append(fp)
    return fps

class VirtualFace():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._v2le = (0,0)
        self._v2re = (0,0)
        self._v2m = (0,0)
        self._angle = 0
        self._face = None
        self._left_eye = None
        self._right_eye = None
        self._mouth = None

    @property
    def face(self):
        return self._face
    @face.setter
    def face(self, face):
        self._face = face
        self._x = face.x
        self._y = face.y
        self._angle = face.angle

    @property
    def left_eye(self):
        return self._left_eye
    @left_eye.setter
    def left_eye(self, left_eye):
        self._left_eye = left_eye
        self._v2le = vA2B((self._x,self._y),(left_eye.x,left_eye.y))

    @property
    def right_eye(self):
        return self._right_eye
    @right_eye.setter
    def right_eye(self, right_eye):
        self._right_eye = right_eye
        self._v2re = vA2B((self._x,self._y),(right_eye.x,right_eye.y))
    
    @property
    def mouth(self):
        return self._mouth
    @mouth.setter
    def mouth(self, mouth):
        self._mouth = mouth
        self._v2m = vA2B((self._x,self._y),(mouth.x,mouth.y))
    
    @property
    def angle(self):
        return self._angle
    @mouth.setter
    def angle(self, angle):
        self._angle = angle
        self.face.angle = angle
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x):
        self._x = x
        self.face.x = x
        self.left_eye.x = x + self._v2le[0]
        self.right_eye.x = x + self._v2re[0]
        self.mouth.x = x + self._v2m[0]
    
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        self._y = y
        self.face.y = y
        self.left_eye.y = y + self._v2le[1]
        self.right_eye.y = y + self._v2re[1]
        self.mouth.y = y + self._v2m[1]
    
    def rotate_to(self, angle, r_center=None):
        rc = r_center or (self.x, self.y)
        self.face.rotate_to(angle, rc)
        if self.left_eye:
            self.left_eye.rotate_to(angle, rc)
        if self.right_eye:
            self.right_eye.rotate_to(angle, rc)
        if self.mouth:
            self.mouth.rotate_to(angle, rc)
    
    def draw(self):
        self.face.draw()
        self.left_eye.draw()
        self.right_eye.draw()
        self.mouth.draw()

# 设置摄像头检测器
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 替换为模型文件的路径