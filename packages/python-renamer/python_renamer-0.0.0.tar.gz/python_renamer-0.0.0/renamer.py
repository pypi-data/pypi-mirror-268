#!/usr/bin/env python3
# coding: utf-8

__author__ = "ChenyangGao <https://chenyanggao.github.io>"
__version__ = (0, 0, 0)
__all__ = ["batch_rename", "rename_by_pairs", "rename_back"]


from itertools import count
from os import rename, fsdecode, PathLike
from os.path import abspath, relpath
from pathlib import Path
from sys import stdout

from filerev import file_reviter
from iterdir import iterdir
from json_write import json_log_gen_write

try:
    from orjson import loads
except ImportError:
    try:
        from ujson import loads
    except ImportError:
        from json import loads


def batch_rename(
    top=None, 
    getnew=None, 
    predicate=lambda p: not p.name.startswith(".") or None, 
    follow_symlinks=False, 
    outfile=stdout, 
    out_relpath=False, 
):
    if getnew is None:
        cnt = count(1).__next__
        getnew = lambda p: p.with_stem(str(cnt()))
    if isinstance(outfile, PathLike) or not hasattr(outfile, "write"):
        outfile = open(outfile, "wb")
    if top is None:
        top = Path().absolute()
    else:
        top = Path(fsdecode(top)).absolute()
    toppath = str(top)
    gen = json_log_gen_write(file=outfile)
    output = gen.send
    for path in iterdir(
        top, 
        topdown=False, 
        max_depth=-1, 
        predicate=predicate, 
        follow_symlinks=follow_symlinks, 
    ):
        try:
            pathold = str(path)
            pathnew = abspath(fsdecode(getnew(path)))
            if pathold != pathnew:
                rename(pathold, pathnew)
                if out_relpath:
                    output((relpath(pathold, top), relpath(pathnew, top)))
                else:
                    output((pathold, pathnew))
        except Exception as e:
            print(e)


def rename_by_pairs(pairs, /):
    for old, new in pairs:
        rename(old, new)


def rename_back(path):
    pairs = map(loads, file_reviter(open(path, "rb")))
    rename_by_pairs((new, old) for old, new in pairs)

