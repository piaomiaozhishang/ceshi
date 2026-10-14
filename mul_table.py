#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ceshi - 打印九九乘法表，最简单的测试脚本之一"""


def main():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j}", end="\t")
        print()


if __name__ == "__main__":
    main()
