import pgeof
from pgeof import EFeatureID
import laspy


def bench_verticality():
    las_file = laspy.read("/Users/romainjanvier/data/3DFin/mini_bench.las")
    vert = pgeof.compute_features_selected(
        las_file.xyz, 0.1, 50000, [EFeatureID.Verticality, EFeatureID.VerticalityPGEOF]
    )
    out_data = laspy.create(point_format=2, file_version="1.2")
    out_data.xyz = las_file.xyz
    out_data.add_extra_dims(
        [
            laspy.ExtraBytesParams("vert", "float32"),
            laspy.ExtraBytesParams("vert_pgeof", "float32"),
        ]
    )
    out_data.vert = vert[:, 0]
    out_data.vert_pgeof = vert[:, 1]
    out_data.write("vert.las")


if __name__ == "__main__":
    bench_verticality()