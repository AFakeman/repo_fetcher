#!/usr/bin/env python3
import argparse

import config
from RepoFetcher import RepoFetcher


def main():
    parser = argparse.ArgumentParser(description='Default argument parser')
    parser.add_argument('branch', action='store', type=str, help='Name of the task')
    parser.add_argument('-c', '--check', help='Flag which decides whether to do similarity checking or not',
                        action='store_true')
    args = parser.parse_args()

    rf = RepoFetcher(config, args.branch)
    rf.collect()
    if args.check:
        rf.check()


if __name__ == '__main__':
    main()
