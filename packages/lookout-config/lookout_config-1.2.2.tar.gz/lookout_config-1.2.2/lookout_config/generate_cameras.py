from typing import List
from greenstream_config import Camera, Offsets
from lookout_config import Mode
from math import radians


def generate_cameras_armidale(mode: Mode, namespace: str):
    # !! IMPORTANT !!
    # Changes here should probably be made in gama also

    k_intrinsic = [1097.44852, 0.0, 992.544475, 0.0, 1101.33980, 552.247413, 0.0, 0.0, 1.0]
    # Distortion parameters are broken in foxglove :(
    # distortion_parameters = [
    #     -0.388772321,
    #     0.194568646,
    #     -0.000662550588,
    #     0.000224063281,
    #     -0.0503775800,
    # ]

    cameras: List[Camera] = [
        Camera(
            name="port",
            type="color",
            order=0,
            elements=[
                "rtspsrc location=rtsp://admin:@192.168.2.21:554/live/0/MAIN latency=10",
                "rtph264depay",
                "h264parse",
                "avdec_h264",
                "videoconvert",
            ],
            pixel_height=1080,
            pixel_width=1920,
            sensor_height_mm=2.21,
            sensor_width_mm=3.92,
            fov=125.0,
            camera_frame_topic="perception/frames/port_color",
            camera_info_topic="sensors/cameras/port_color/camera_info",
            camera_info_ext_topic="sensors/cameras/port_color/camera_info_ext",
            k_intrinsic=k_intrinsic,
            # distortion_parameters=distortion_parameters,
            offsets=Offsets(
                roll=0.0,
                pitch=radians(20.0),
                yaw=radians(45.0),
                forward=2.275,
                left=2.850,
                up=-0.155,
            ),
        ),
        Camera(
            name="bow",
            type="color",
            order=1,
            elements=[
                "rtspsrc location=rtsp://admin:@192.168.2.22:554/live/0/MAIN latency=10",
                "rtph264depay",
                "h264parse",
                "avdec_h264",
                "videoconvert",
            ],
            pixel_height=1080,
            pixel_width=1920,
            sensor_height_mm=2.21,
            sensor_width_mm=3.92,
            fov=125.0,
            camera_frame_topic="perception/frames/bow_color",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            k_intrinsic=k_intrinsic,
            # distortion_parameters=distortion_parameters,
            offsets=Offsets(
                roll=radians(2.0),
                pitch=radians(5.85),
                yaw=0.0,
                forward=3.190,
                left=0.015,
                up=-0.205,
            ),
        ),
        Camera(
            name="stbd",
            type="color",
            order=2,
            elements=[
                "rtspsrc location=rtsp://admin:@192.168.2.23:554/live/0/MAIN latency=10",
                "rtph264depay",
                "h264parse",
                "avdec_h264",
                "videoconvert",
            ],
            pixel_height=1080,
            pixel_width=1920,
            sensor_height_mm=2.21,
            sensor_width_mm=3.92,
            fov=125.0,
            camera_frame_topic="perception/frames/stbd_color",
            camera_info_topic="sensors/cameras/stbd_color/camera_info",
            camera_info_ext_topic="sensors/cameras/stbd_color/camera_info_ext",
            k_intrinsic=k_intrinsic,
            # distortion_parameters=distortion_parameters,
            offsets=Offsets(
                roll=0.0,
                pitch=radians(20.0),
                yaw=radians(-45.0),
                forward=2.275,
                left=-2.850,
                up=-0.155,
            ),
        ),
        Camera(
            name="stern_port",
            type="color",
            order=3,
            elements=[
                "rtspsrc location=rtsp://admin:@192.168.2.24:554/live/0/MAIN latency=10",
                "rtph264depay",
                "h264parse",
                "avdec_h264",
                "videoconvert",
            ],
            pixel_height=1080,
            pixel_width=1920,
            sensor_height_mm=2.21,
            sensor_width_mm=3.92,
            fov=125.0,
            camera_frame_topic="perception/frames/stern_port_color",
            camera_info_topic="sensors/cameras/stern_port_color/camera_info",
            camera_info_ext_topic="sensors/cameras/stern_port_color/camera_info_ext",
            k_intrinsic=k_intrinsic,
            # distortion_parameters=distortion_parameters,
            offsets=Offsets(
                roll=0.0,
                pitch=radians(20.0),
                yaw=radians(135.0),
                forward=-4.980,
                left=2.850,
                up=-0.155,
            ),
        ),
        Camera(
            name="stern_stbd",
            type="color",
            order=4,
            elements=[
                "rtspsrc location=rtsp://admin:@192.168.2.25:554/live/0/MAIN latency=10",
                "rtph264depay",
                "h264parse",
                "avdec_h264",
                "videoconvert",
            ],
            pixel_height=1080,
            pixel_width=1920,
            sensor_height_mm=2.21,
            sensor_width_mm=3.92,
            fov=125.0,
            camera_frame_topic="perception/frames/stern_stbd_color",
            camera_info_topic="sensors/cameras/stern_stbd_color/camera_info",
            camera_info_ext_topic="sensors/cameras/stern_stbd_color/camera_info_ext",
            k_intrinsic=k_intrinsic,
            # distortion_parameters=distortion_parameters,
            offsets=Offsets(
                roll=0.0,
                pitch=radians(20.0),
                yaw=radians(-135.0),
                forward=-4.980,
                left=-2.850,
                up=-0.155,
            ),
        ),
    ]

    if mode == Mode.STUBS:
        for camera in cameras:
            camera.elements = [
                "videotestsrc pattern=ball",
                "video/x-raw, format=RGB,width=1920,height=1080",
            ]
    elif mode == Mode.SIMULATOR or mode == Mode.ROSBAG:
        for camera in cameras:
            camera.elements = [
                f"rosimagesrc ros-topic=sensors/cameras/{camera.name}_{camera.type}/image_raw ros-name='gst_rosimagesrc_{camera.name}_{camera.type}' ros-namespace='{namespace}'"
            ]

    return cameras


def generate_cameras(mode: Mode, namespace: str):
    return generate_cameras_armidale(mode, namespace)
