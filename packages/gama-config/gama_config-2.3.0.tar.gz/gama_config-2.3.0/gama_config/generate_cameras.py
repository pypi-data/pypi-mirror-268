from typing import List
from math import radians
from greenstream_config import Camera, Offsets
from gama_config.gama_vessel import Mode, Variant


def generate_cameras_armidale(namespace: str, mode: Mode):
    k_intrinsic = [1097.44852, 0.0, 992.544475, 0.0, 1101.33980, 552.247413, 0.0, 0.0, 1.0]

    # Distorion parameters are broken in foxglove :(
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
            camera_frame_topic=None,
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
            camera_frame_topic=None,
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
            camera_frame_topic=None,
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
            camera_frame_topic=None,
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
            camera_frame_topic=None,
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
    elif mode == Mode.SIMULATOR:
        for camera in cameras:
            camera.elements = [
                f"rosimagesrc ros-topic=sensors/cameras/{camera.name}_color/image_raw ros-name='gst_rosimagesrc_{camera.name}' ros-namespace='{namespace}'"
            ]

    return cameras


# Set up all the camera configurations for each mode and variant
def get_camera_configuration_map(namespace: str) -> dict[Mode, dict[Variant, List[Camera]]]:

    # Pre-set video patterns for testing
    cameras_mode_stub: List[Camera] = [
        Camera(
            name="bow",
            type="color",
            order=0,
            elements=[
                "videotestsrc pattern=ball",
                "video/x-raw, format=RGB,width=1280,height=720",
            ],
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/bow_color/image_raw",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
        Camera(
            name="port",
            type="color",
            order=1,
            elements=[
                "videotestsrc pattern=pinwheel",
                "video/x-raw, format=RGB,width=1280,height=720",
            ],
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/port_color/image_raw",
            camera_info_topic="sensors/cameras/port_color/camera_info",
            camera_info_ext_topic="sensors/cameras/port_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
        Camera(
            name="stbd",
            type="color",
            order=2,
            elements=[
                "videotestsrc pattern=spokes",
                "video/x-raw, format=RGB,width=1280,height=720",
            ],
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/stbd_color/image_raw",
            camera_info_topic="sensors/cameras/stbd_color/camera_info",
            camera_info_ext_topic="sensors/cameras/stbd_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
    ]

    # Image stream taken from a published ros image topic
    cameras_mode_simulator: List[Camera] = [
        Camera(
            name="bow",
            type="color",
            order=0,
            elements=[
                f"rosimagesrc ros-topic=sensors/cameras/bow_color/image_raw ros-name='gst_rosimagesrc_bow' ros-namespace='{namespace}'",
            ],
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/bow_color/image_raw",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        )
    ]

    cameras_hardware_single_webcam: List[Camera] = [
        Camera(
            name="bow",
            type="color",
            order=0,
            elements=[
                "v4l2src",
                "video/x-raw, width=1920,height=1080",
            ],
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/bow_color/image_raw",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        )
    ]

    cameras_hardware_triple_cam: List[Camera] = [
        Camera(
            name="bow",
            type="color",
            order=0,
            elements=[
                "aravissrc exposure-auto=on",
                "video/x-raw, format=RGB,width=1920,height=1080",
            ],
            pixel_height=1080,
            pixel_width=1920,
            # TO CHANGE UPON RECEIVING CAMERA SPECS
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/bow_color/image_raw",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
        Camera(
            name="port",
            type="color",
            order=1,
            elements=["v4l2src device=/dev/video2"],
            # TO CHANGE UPON RECEIVING CAMERA SPECS
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/port_color/image_raw",
            camera_info_topic="sensors/cameras/port_color/camera_info",
            camera_info_ext_topic="sensors/cameras/port_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
        Camera(
            name="stbd",
            type="color",
            order=2,
            elements=["v4l2src device=/dev/video0"],
            # TO CHANGE UPON RECEIVING CAMERA SPECS
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/stbd_color/image_raw",
            camera_info_topic="sensors/cameras/stbd_color/camera_info",
            camera_info_ext_topic="sensors/cameras/stbd_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
    ]

    cameras_realsense: List[Camera] = [
        Camera(
            name="bow",
            type="color",
            order=0,
            elements=[
                f"rosimagesrc ros-topic=sensors/cameras/bow_color/color/image_raw ros-name='gst_rosimagesrc_bow' ros-namespace='{namespace}'"
            ],
            # TO CHANGE UPON RECEIVING CAMERA SPECS
            pixel_height=720,
            pixel_width=1280,
            sensor_height_mm=7.2,
            sensor_width_mm=12.8,
            fov=110.0,
            camera_frame_topic="sensors/cameras/bow_color/image_raw",
            camera_info_topic="sensors/cameras/bow_color/camera_info",
            camera_info_ext_topic="sensors/cameras/bow_color/camera_info_ext",
            offsets=Offsets(
                roll=0.0,
                pitch=0.0,
                yaw=0.0,
                forward=0.0,
                left=0.0,
                up=0.0,
            ),
        ),
    ]

    # Map of Mode/Variant to camera configuration
    return {
        Mode.STUBS: {
            Variant.EDUCAT: cameras_mode_stub,
            Variant.WHISKEY_BRAVO: cameras_mode_stub,
            Variant.ORACLE_2_2: cameras_mode_stub,
            Variant.ORACLE_22: cameras_mode_stub,
            Variant.ARMIDALE: generate_cameras_armidale(namespace, Mode.STUBS),
        },
        Mode.SIMULATOR: {
            Variant.EDUCAT: cameras_mode_simulator,
            Variant.WHISKEY_BRAVO: cameras_mode_simulator,
            Variant.ORACLE_2_2: cameras_mode_simulator,
            Variant.ORACLE_22: cameras_mode_simulator,
            Variant.ARMIDALE: generate_cameras_armidale(namespace, Mode.SIMULATOR),
        },
        Mode.HARDWARE: {
            Variant.EDUCAT: cameras_hardware_single_webcam,
            Variant.WHISKEY_BRAVO: cameras_hardware_triple_cam,
            Variant.ORACLE_2_2: cameras_realsense,
            Variant.ORACLE_22: cameras_hardware_triple_cam,
            Variant.ARMIDALE: generate_cameras_armidale(namespace, Mode.HARDWARE),
        },
    }


def generate_cameras(mode: Mode, variant: Variant, namespace: str):

    # return the camera configuration for the specified mode and variant
    camera_configuration = get_camera_configuration_map(namespace)
    return camera_configuration[mode][variant]
