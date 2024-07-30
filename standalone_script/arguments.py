# Standard library imports
import argparse
import re
import sys
import traceback
# Third party imports
# Local library imports
# Type hint imports
from typing import Tuple


def setup_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Some description")
    parser.add_argument("-i", "--ip", type=str, help="IP address", required=True)
    parser.add_argument("-t", "--type", type=str, help="Command Type", choices=["first_type", "sec_type"], required=True)
    return parser.parse_args()

def parse_arguments(args) -> Tuple[str, str]:
    ip = args.ip
    type = args.type

    # IP regex matching, it's better to have ^ and $ to eliminate unwanted characters.
    ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ip_pattern.fullmatch(ip):
        raise argparse.ArgumentError("illegal IP")

    return ip, type

if __name__ == "__main__":
    try:
        ip, type = parse_arguments(setup_arguments())
    except Exception:
        traceback.print_exc()
        sys.exit(1)
