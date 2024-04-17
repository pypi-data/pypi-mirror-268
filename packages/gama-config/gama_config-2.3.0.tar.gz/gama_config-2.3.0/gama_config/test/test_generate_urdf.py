from gama_config.generate_urdf import generate_urdf
from gama_config.gama_vessel import GamaVesselConfig
from greenstream_config import Offsets


def test_generate_urdf():
    config = GamaVesselConfig()
    urdf = generate_urdf(
        config=config,
        cameras=[],
        ins_offset=Offsets(),
        mesh_path="package://some_package/meshes/some_mesh.stl",
    )

    assert """<mesh filename="package://some_package/meshes/some_mesh.stl"/>""" in urdf
