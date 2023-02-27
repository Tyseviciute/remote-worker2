from flask import Flask, Response
from imutils.video import WebcamVideoStream
import imutils
import cv2

app = Flask(__name__)
vs = WebcamVideoStream(src=0).start()


@app.route('/')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen():
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, height=720, width=1280)
        ret, jpeg = cv2.imencode('.jpg', frame)
        if ret:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)


# <!--<div>
#     <img style='max-width: 100vh' src="{{ url_for('main.video_feed') }}">
# </div>-->
