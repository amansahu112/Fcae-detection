from flask import Flask,render_template,request,session,flash
from PIL import Image
import os

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s', methods = ['POST'])
def s():
    if request.method == 'POST':
        f = request.files['img']
        f.save(f.filename)
        image_boundary(f.filename)
        os.remove(f.filename)
        n='static\{}'.format(f.filename)
    return render_template("s.html", name = n)

def image_boundary(path):
    print(path)
    import cv2
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.imwrite("static\\"+path, img)



if __name__=='__main__':
    app.run(debug=True)
