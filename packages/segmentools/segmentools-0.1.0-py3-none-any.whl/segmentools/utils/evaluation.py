from typing import List, Tuple

import pandas as pd
from xlsxwriter.workbook import Format
from xlsxwriter.worksheet import Worksheet


def get_true_cells_coordinates(bool_data: pd.DataFrame) -> List[Tuple[int]]:
    """Return coordinates of row/columns for each cell of a dataframe/worksheet where boolean values is .

    Args:
        bool_data (pd.DataFrame): dataframe of boolean value.

    Returns:
        List[Tuple[int]]: List of x,y coordinates.
    """
    # get df shape
    h, w = bool_data.shape
    # reindex to have number as index
    bool_data.index = range(0, h)
    bool_data.columns = range(0, w)
    bool_data = bool_data.rename_axis(index="idx", columns="cols")
    # get True cells infos
    indexes = bool_data.stack().reset_index(name="value").query("value == 1")
    coordinates = list(zip(indexes["idx"], indexes["cols"]))
    # return coordinates
    return coordinates


def outlier_mapping(
    data: pd.DataFrame, confidence_level: int = 2
) -> Tuple[List[Tuple[int]]]:
    """Return list of cells coordinates for positive & negatives outliers from metric/image data.
    Mean and std should be at the top of dataframe.

    Args:
        data (pd.DataFrame): Data where to identify outliers.
        confidence_level (int, optional): Level of confidence for thresholding outlieers. Defaults to 2 (sigma deviations).

    Returns:
        Tuple[List[Tuple[int]]]:Lists of coordinates for negatives (< u - 2sigma) & positives (> u + 2sigma) outliers
    """
    # get numerics datas (without images names etc)
    numeric_data = data[data.columns[2:]]
    # extract mean/std
    mean, std = numeric_data.iloc[0], numeric_data.iloc[1]
    # compute threswhold
    threshold_up, threshold_down = mean + (confidence_level * std), mean - (
        confidence_level * std
    )
    # get boolean masks
    down_table = numeric_data < threshold_down
    up_table = numeric_data > threshold_up
    # gather celles coordinates
    down_cells = get_true_cells_coordinates(down_table)
    up_cells = get_true_cells_coordinates(up_table)
    # update coordinates by adding names & link to left
    down_cells = [(x + 1, y + 2) for x, y in down_cells]
    up_cells = [(x + 1, y + 2) for x, y in up_cells]
    # return coordinates
    return down_cells, up_cells


def cell_formatting(
    worksheet: Worksheet, format: Format, coordinates: List[Tuple[int]]
):
    """Format cells with conditionnal formatting for outlier detection.

    Args:
        worksheet (Worksheet): Sheet of xlsxwriter worksheet.
        format (Format): Format of cell.
        coordinates (List[Tuple[int]]): cells coordinates to apply format on.
    """
    for x, y in coordinates:
        # ignore the two first columns and first row, it is table titles.
        if x < 3 or y < 2:
            continue
        worksheet.conditional_format(
            x, y, x, y, {"type": "no_blanks", "format": format}
        )


def path_to_link(path):
    return f'<a href="file:///{path}" target="_blank">Open</a>'
