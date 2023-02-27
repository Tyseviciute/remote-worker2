# import cv2
# import imutils
from flask import Blueprint, render_template, Response, jsonify
from flask_login import login_required, current_user
# from imutils.video import WebcamVideoStream

from models import ActiveUsers


from robots.robot_2 import move_forward, move_backward, turn_left, turn_right, stop_robot

main = Blueprint('main', __name__)

# vs = WebcamVideoStream(src=0).start()


# pagrindinis puslapis
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required  # login_required - vartotojas gali tai matyti tik prisijungęs
def profile():
    first_active_user = ActiveUsers.query.order_by(ActiveUsers.login_timestamp.asc()).first()
    print(current_user.email)
    print(first_active_user.email)
    if first_active_user.email == current_user.email:
        return render_template('control_profile.html', name=current_user.email)
    else:
        return render_template('view_profile.html', name=current_user.email)


@main.route('/check-availabality')
@login_required
def check():
    first_active_user = ActiveUsers.query.order_by(ActiveUsers.login_timestamp.asc()).first()
    print("checking")
    print(current_user.email)
    print(first_active_user.email)
    if first_active_user.email == current_user.email:
        return "available"
    else:
        return "unavailable"


# @main.route('/camera')
# @login_required
# def video_feed():
#     return Response(gen(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# def gen():
#     while True:
#         frame = vs.read()
#         frame = imutils.resize(frame, height=720, width=1280)
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         if ret:
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


# calling robot motion functions
@main.route('/forward/<int:speed>')
@login_required
def forward(speed):
    print("Moving forward speed:", speed)
    move_forward(speed)
    return jsonify(message=f"Moving forward {speed}")


@main.route('/backward/<int:speed>')
@login_required
def backward(speed):
    print("Moving backward speed:", speed)
    move_backward(speed)
    return jsonify(message=f"Moving backward {speed}")


@main.route('/left/<int:speed>')
@login_required
def left(speed):
    print("Turn left speed:", speed)
    turn_left(speed)
    return jsonify(message=f"Turning left {speed}")


@main.route('/right/<int:speed>')
@login_required
def right(speed):
    print("Turn right speed:", speed)
    turn_right(speed)
    return jsonify(message=f"Turning right {speed}")


@main.route('/stop')
@login_required
def stop():
    print("stop")
    stop_robot()
    return jsonify(message=f"Stopping")
