"""Command line entry point for nighgravy_0u_kit."""
import argparse

from .core import Nighgravy0uTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="organize files by type")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    sorter = Nighgravy0uTool(args.path)
    if args.dry_run:
        for name, folder in sorter.plan():
            print(f"{name} -> {folder}/")
        return 0
    for name, folder in sorter.apply():
        print(f"{name} -> {folder}/")
    return 0
