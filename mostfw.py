#!/usr/bin/env python3

import re
import argparse
from collections import Counter


def mostfw(data, max_nitem=0, min_freq=1, max_wsize=7):
    if not max_nitem:
        max_nitem = None
    word_counts = Counter(re.split('\s+|\W+|\d+', data))

    for i, j in word_counts.most_common(max_nitem):
        if 1 < len(i) <= max_wsize and not any_ascii(i) and j >= min_freq:
            yield i, j


def any_ascii(s):
    return any(ord(c) < 128 for c in s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('query_files', type=argparse.FileType('r'),
                        metavar='<file>', nargs='+',
                        help='input dataset')
    parser.add_argument('-n', '-nitem', '--max-nitem', type=int,
                        metavar='<int>', default=0,
                        help='maximum items to output (default: all)')
    parser.add_argument('-f', '-freq', '--min-freq', type=int,
                        metavar='<int>', default=2,
                        help='minimum frequency in counter (default: 2)')
    parser.add_argument('-w', '-wsize', '--max-wordsize', type=int,
                        metavar='<int>', default=7,
                        help='maximum number of Chinese characters (default: 7)')
    args = parser.parse_args()

    data = []
    for f in args.query_files:
        data.append(f.read())

    for i, j in mostfw(''.join(data), args.max_nitem, args.min_freq, args.max_wordsize):
        print('%s\t%s' % (i, j))


if __name__ == '__main__':
    main()
