# The generator script of gRPC and Protobuf.
#
# This script calls :module:`grpc_tools.protoc` to compile all the protocol buffers in the
# ../proto folder. Related dependencies (dev dependencies) should be installed.

import pathlib
import runpy
import sys

CURRENT_DIR = pathlib.Path(__file__).parent.absolute()
PROJECT_DIR = CURRENT_DIR.parent
PROTO_DIR = PROJECT_DIR / "proto"
GENERATE_DIR = CURRENT_DIR / "generated" / "api"


class GrpcGenerator(object):
    args: list[str]

    def __init__(
        self,
        proto_dir: pathlib.Path = PROTO_DIR,
        out_dir: pathlib.Path = GENERATE_DIR,
    ):
        if not out_dir.exists():
            out_dir.mkdir(parents=True)
        out_path = str(out_dir)
        include_path = str(proto_dir)
        proto_source = str(proto_dir / "*.proto")
        self.args = [
            f"-I{include_path}",
            proto_source,
            f"--python_out={out_path}",
            f"--pyi_out={out_path}",
            f"--grpc_python_out={out_path}",
        ]

    def run(self) -> None:
        sys.argv = ["", *self.args]
        runpy.run_module("grpc_tools.protoc", run_name="__main__", alter_sys=True)


def main() -> None:
    GrpcGenerator().run()


if __name__ == "__main__":
    main()
