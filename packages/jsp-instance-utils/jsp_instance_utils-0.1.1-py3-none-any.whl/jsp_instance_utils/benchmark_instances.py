import numpy as np
import pathlib as pl
import importlib.resources
import numpy.typing as npt
import jsp_instance_utils.jsp_instance_parser as parser


def get_benchmark_instance(name="ft06") -> npt.NDArray:
    file_path = importlib.resources.files('jsp_instance_utils').joinpath('resources/jsp_instances/taillard/ft06.txt')
    file_path = pl.Path(file_path)
    print(file_path)
    jsp, _ = parser.parse_jps_taillard_specification(
        instance_path=file_path
    )
