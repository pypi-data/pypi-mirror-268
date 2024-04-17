import argparse
import sys

from sglang.srt.server import ServerArgs, launch_server

if __name__ == "__main__":
    sys.setrecursionlimit(8000) # limit recursion, see https://github.com/sgl-project/sglang/issues/154#issuecomment-2014321726
    parser = argparse.ArgumentParser()
    ServerArgs.add_cli_args(parser)
    args = parser.parse_args()
    server_args = ServerArgs.from_cli_args(args)

    launch_server(server_args, None)
