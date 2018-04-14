#!/usr/bin/env python3
import sys

import config
from RepoFetcher import RepoFetcher


def main():
    if len(sys.argv) != 2:
        raise ValueError('Usage ./main.py <branch>')
    branch = sys.argv[1]
    rf = RepoFetcher(config, branch)
    rf.check()


if __name__ == '__main__':
    main()
