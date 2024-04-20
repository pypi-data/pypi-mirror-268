#  Copyright (c) 2024 Mira Geoscience Ltd.
#
#  This file is part of targeting_workflow package.
#
#  All rights reserved.
#
#  The software and information contained herein are proprietary to, and
#  comprise valuable trade secrets of, Mira Geoscience, which
#  intend to preserve as trade secrets such software and information.
#  This software is furnished pursuant to a written license agreement and
#  may be used, copied, transmitted, and stored only in accordance with
#  the terms of such license and with the inclusion of the above copyright
#  notice.  This software and information or any other copies thereof may
#  not be provided or otherwise made available to any other person.

# pylint: disable=import-error

from __future__ import annotations

from geoh5py.objects import BlockModel, Grid2D, ObjectBase, Octree, Points
from geoh5py.shared.utils import fetch_active_workspace

from ..database.database import Database
from ..shared.utils import get_geoh5py_coordinates


def export_data(
    geoh5py_object: Points | Grid2D | BlockModel | Octree,
    database: Database,
    to_export: list,
):
    """
    Export selected data to geoh5py.
    :param database: The database to export the data from.
    :param to_export: The list of data to export.
    """
    # verify the data to export are in the database and are created==True
    if not set(to_export).issubset(database.created):
        raise KeyError("The data to export have to be 'created' data of the database.")

    if not isinstance(geoh5py_object, ObjectBase):
        raise TypeError("The data must be a geoh5py Object.")

    # open the workspace
    with fetch_active_workspace(geoh5py_object.workspace, mode="r+"):
        # prepare the association of the data
        vertices, association = get_geoh5py_coordinates(geoh5py_object)

        if not vertices.equals(database.get_features(["x", "y", "z"])):
            raise IndexError(
                "The vertices of the geoh5py object do not match the database vertices."
            )

        # Add data to geoh5py object
        for column in to_export:
            geoh5py_object.add_data(
                {
                    column: {
                        "association": association,
                        "values": database.get_features(column).values.flatten(),
                    }
                }
            )

            if column in database.metadata:
                column_metadata = database.metadata[column]
                geoh5py_object.metadata = {column: column_metadata}
