from __future__ import absolute_import

import pkg_resources

from bmi_dbseabed import BmiDbSeabed as DbSeabedData

DbSeabedData.__name__ = "DbSeabedData"
DbSeabedData.METADATA = pkg_resources.resource_filename(__name__, "data/DbSeabedData")

__all__ = [
    "DbSeabedData",
]
