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

from __future__ import annotations

from geoh5py.ui_json.input_file import InputFile


def get_multi_data_from_ui_json(
    input_file: InputFile, to_extract: dict[str, list[str]]
) -> dict:
    """
    Extract the data from an InputFile.

    The InputFile data is obsolete with new widgets containing multiple values.
    This function construct a multilevel dictionary to
    store the values extracted from the ui.json file.

    :param input_file: The input_file containing the parameters.
    :param to_extract: The multilevel widget and values to extract.

    :return: A multilevel dictionary with the extracted values.
    """
    ui_json = input_file.ui_json
    data_to_change = input_file.data

    if data_to_change is None or ui_json is None:
        raise ValueError("No ui.json data was found.")

    for key in to_extract:
        if key in ui_json and isinstance(to_extract[key], list):
            data_to_change[key] = input_file.promote(
                {
                    extract: item
                    for extract, item in ui_json[key].items()
                    if extract in to_extract[key]
                }
            )

    return data_to_change
