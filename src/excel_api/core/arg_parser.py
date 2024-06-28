import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", help="host")
    parser.add_argument("--port", default=6238, help="port")
    return parser
