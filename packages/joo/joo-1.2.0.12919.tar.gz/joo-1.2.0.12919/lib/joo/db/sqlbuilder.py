"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
def equation(left, right, **kwargs):
    """equation: format(left)=format(right)"""
    format_left = kwargs.get("format_left", "{}")
    format_right = kwargs.get("format_right", "{}")
    return format_left.format(left) + "=" + format_right.format(right)

def part_fn(key, value, **kwargs):
    """field name: `key`"""
    return "`" + key + "`"

def part_fp(key, value, **kwargs):
    """field value placeholder: {key}"""
    return "{" + key + "}"

def part_fv(key, value, **kwargs):
    """field value: value"""
    return value

def part_fn_fn(key, value, **kwargs):
    """field name pairs: format(`key`)=format(`key`)"""
    fn_v = fn(key, value)
    return equation(fn_v, fn_v, **kwargs)

def part_fn_fp(key, value, **kwargs):
    """field name/field value placeholder pairs: format(`key`)=format({key})"""
    fn_v = fn(key, value)
    fp_v = fp(key, value)
    return equation(fn_v, fp_v, **kwargs)

fn = part_fn
fp = part_fp
fv = part_fv
fn_fn = part_fn_fn
fn_fp = part_fn_fp

def parts_list(part_proc, data_record, excludings=[], **kwargs):
    parts = []
    for key, value in data_record.items():
        if key in excludings: continue
        parts.append(part_proc(key, value, **kwargs))
    return parts

def parts_str(part_proc, data_record, excludings=[], join_with=",", **kwargs):
    return join_with.join(parts_list(part_proc, data_record, excludings, **kwargs))

