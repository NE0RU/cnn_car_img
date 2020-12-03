from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os, glob, numpy as np
from keras.models import load_model

app = Flask(__name__)

def cnn():
   caltech_dir = "uploads"
   image_w = 64
   image_h = 64

   pixels = image_h * image_w * 3

   X = []  
   filenames = []
   files = glob.glob(caltech_dir+"/*.*")
   for i, f in enumerate(files):
      img = Image.open(f)
      img = img.convert("RGB")
      img = img.resize((image_w, image_h))
      data = np.asarray(img)
      filenames.append(f)
      X.append(data)

   X = np.array(X)
   model = load_model('./model/multi_img_classification.model')

   prediction = model.predict(X)
   np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
   cnt = 0

   #이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.
   for i in prediction:
      pre_ans = i.argmax()  # 예측 레이블
      print(i)
      print(pre_ans)
      pre_ans_str = ''
      if pre_ans == 0: pre_ans_str = "g80"
      elif pre_ans == 1: pre_ans_str = "gv70"
      elif pre_ans == 2: pre_ans_str = "gv80"
      else: pre_ans_str = "kia stinger"
      if i[0] >= 0.8 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
      if i[1] >= 0.8: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
      if i[2] >= 0.8: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
      if i[3] >= 0.8: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
      r = pre_ans_str
      cnt += 1
      # print(i.argmax()) #얘가 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
      # 즉 얘랑, 나중에 카테고리 데이터 불러와서 카테고리랑 비교를 해서 같으면 맞는거고, 아니면 틀린거로 취급하면 된다.
      # 이걸 한 것은 _4.py에.
   return r

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return render_template('upload.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save("uploads/" + secure_filename(f.filename))
      res = cnn()
      os.remove("uploads/" + secure_filename(f.filename))
      return res

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True)
