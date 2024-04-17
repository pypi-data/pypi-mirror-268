#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_dbseabed").version


from .bmi import DbSeabedData

__all__ = [
    "DbSeabedData",
]
