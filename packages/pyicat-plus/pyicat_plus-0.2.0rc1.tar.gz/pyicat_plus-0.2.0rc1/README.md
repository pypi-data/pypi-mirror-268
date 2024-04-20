# PyIcat-Plus

A python client for ICAT+.

## Getting started

Register raw datasets with ICAT

```bash
icat-store-raw --beamline id00 \
    --proposal id002207 \
    --path /data/visitor/path/to/dataset1 \
    --dataset test1 \
    --sample mysample

icat-store-raw --beamline id00 \
    --proposal id002207 \
    --path /data/visitor/path/to/dataset2 \
    --dataset test2 \
    --sample mysample
```

Register processed data with ICAT

```bash
icat-store-processed --beamline id00 \
    --proposal id002207 \
    --path /data/visitor/path/to/processed \
    --dataset testproc \
    --sample mysample \
    --raw /data/visitor/path/to/dataset1 \
    --raw /data/visitor/path/to/dataset2
```

## Test

With threads

```bash
python -m pip install -e .[test]
pytest
```

With gevent

```bash
python -m pip install -e .[test]
python -m pip install gevent
python -m gevent.monkey --module pytest
```

## NeXus

Each ICAT field has a [NeXus](http://www.nexusformat.org/) equivalent. Create a NeXus compliant
HDF5 file with all ICAT fields:

```bash
icat-nexus-definitions [--url https://...]
```

An example can be found [here](https://gitlab.esrf.fr/icat/pyicat-plus/-/jobs/artifacts/main/download?job=build_hdf5)
and opened with [myhdf5](https://myhdf5.hdfgroup.org/).

## Documentation

https://pyicat-plus.readthedocs.io/
