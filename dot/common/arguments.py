import argparse

def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--task",
        help=('Use the task argument to run a default task with configuration values. Example -t connect')
    )

    return parser.parse_args()
