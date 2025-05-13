from typing import Dict, List, Optional

import pandas as pd

from .utils import declare_component

_component_func = declare_component("table")


def table(
    data: pd.DataFrame,
    columns: Optional[List[str]] = None,
    maxHeight: Optional[int] = None,
    key: Optional[str] = None,
):
    """
    Create a table component.

    Args:
        data (pd.DataFrame): The dataframe to display in the table.
        columns (List[str], optional): The columns to display in the table. If not provided, the columns will be the columns of the dataframe.
        maxHeight (int, optional): The maximum height of the table. Defaults to None.
        key (str, optional): The key of the table. Defaults to None.

    Examples:
    ```python
    import streamlit_shadcn_ui as ui
    # Sample data
    data = [
        {"invoice": "INV001", "paymentStatus": "Paid", "totalAmount": 500, "paymentMethod": "Credit Card"},
        {"invoice": "INV002", "paymentStatus": "Unpaid", "totalAmount": 200, "paymentMethod": "Cash"},
        {"invoice": "INV003", "paymentStatus": "Paid", "totalAmount": 150, "paymentMethod": "Debit Card"},
        {"invoice": "INV004", "paymentStatus": "Unpaid", "totalAmount": 350, "paymentMethod": "Credit Card"},
        {"invoice": "INV005", "paymentStatus": "Paid", "totalAmount": 400, "paymentMethod": "PayPal"},
        # Add more records as needed
    ]

    # Creating a DataFrame
    invoice_df = pd.DataFrame(data)
    ui.table(data=invoice_df, maxHeight=300)


        ```

    """
    if columns is None:
        columns = [{"dataKey": col, "title": col} for col in list(data.columns)]
    props = {
        "data": data.to_dict("records"),
        "columns": columns,
        "maxHeight": maxHeight,
    }
    component_value = _component_func(comp="table", props=props, key=key)
    return component_value
