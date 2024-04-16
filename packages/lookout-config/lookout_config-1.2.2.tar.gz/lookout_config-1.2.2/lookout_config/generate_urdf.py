from typing import List
from lookout_config import LookoutConfig
from greenstream_config import Camera, Offsets, get_cameras_urdf
from gr_urchin import URDF, Joint, Material, Link, xyz_rpy_to_matrix, Visual, Mesh, Geometry
from math import radians


def generate_urdf(
    config: LookoutConfig,
    cameras: List[Camera],
    ins_offset: Offsets,
    mesh_path: str,
    waterline=0.0,  # meters between the waterline and the base_link
    add_optical_frame: bool = True,
):

    file_path = f"/tmp/vessel_{config.mode.value}.urdf"

    # generate links and joints for all vessel cameras
    camera_links, camera_joints = get_cameras_urdf(
        cameras, config.camera_overrides if config.camera_overrides else [None], add_optical_frame
    )

    urdf = URDF(
        name="origins",
        materials=[
            Material(name="grey", color=[0.75, 0.75, 0.75, 1]),
            Material(name="blue", color=[0, 0, 1, 1]),
        ],
        links=[
            Link(name="ins_link", inertial=None, visuals=None, collisions=None),
            Link(name="waterline_link", inertial=None, visuals=None, collisions=None),
            Link(
                name="base_link",
                inertial=None,
                visuals=[
                    Visual(
                        name="visual",
                        geometry=Geometry(
                            mesh=Mesh(filename=mesh_path, combine=False, lazy_filename=mesh_path)
                        ),
                        origin=xyz_rpy_to_matrix([0, 0, 0, radians(-90), 0, 0]),
                        material=Material(name="grey"),
                    )
                ],
                collisions=None,
            ),
            *camera_links,
        ],
        joints=[
            Joint(
                name="base_to_ins",
                parent="base_link",
                child="ins_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix(
                    [
                        ins_offset.forward,
                        ins_offset.left,
                        ins_offset.up,
                        ins_offset.roll,
                        ins_offset.pitch,
                        ins_offset.yaw,
                    ]
                ),
            ),
            Joint(
                name="base_to_waterline",
                parent="base_link",
                child="waterline_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0, 0, -waterline, 0, 0, 0]),
            ),
            *camera_joints,
        ],
    )

    urdf.save(file_path)

    # stringify urdf response for robot description
    with open(file_path) as infp:
        robot_description = infp.read()

    return robot_description
