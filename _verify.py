# Verify the dataset links

import os
import yaml
import re
import csv

datasets = set()

for root, dirs, files in os.walk("datasets"):
    for f in files:
        p = os.path.join(root, f)
        name = os.path.basename(p)

        datasets.add(name)

with open("_data/datasets.yml", "r") as f:
    data = yaml.load(f)

used_datasets = set()


def check_csv(path):
    errors = []

    try:
        with open(path, "rb") as f:
            data = f.read().decode("ascii")
    except:
        errors.append("warning: not ascii")
        pass

    with open(path, "rb") as f:
        data = f.read().decode("utf-8")

    if "\r" in data:
        errors.append("contains \\r")

    with open(path, "r") as f:
        reader = csv.reader(f)
        header = reader.__next__()
        for row in reader:
            if len(header) != len(row):
                errors.append("row length mismatch")

    if len(errors) > 0:
        print(path)
        for err in errors:
            print("  " + err)


for item in data:
    for file in item["files"]:
        if not os.path.exists(file[1:]):
            print("Invalid link: %s" % file)
        check_csv(file[1:])
        used_datasets.add(os.path.basename(file))

for item in datasets:
    if item not in used_datasets:
        print("Unused dataset: %s" % item)
