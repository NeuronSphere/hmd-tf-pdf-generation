import logging
import sys
import os
import json
from pathlib import Path
import shutil
from typing import Dict

from reportlab.pdfgen import canvas
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
import pandas as pd
import numpy as np


logging.basicConfig(
    stream=sys.stdout,
    format="%(levelname)s %(asctime)s - %(message)s",
    level=logging.ERROR,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def do_transform(
    input_content_path: str,
    output_content_path: str,
    transform_nid: str,
    transform_instance_context: Dict,
) -> int:
    """Function to do the actual Transform work

    Args:
        input_content_path (str): filepath for input files
        output_content_path (str): filepath for output files
        transform_nid (str): NID of running TransformInstance
        transform_instance_context (Dict): context dictionary for the running TransformInstance

    Returns:
        int: exit code
    """
    # Get data into pandas DataFrame
    # Can be from SQL with read_sql() or some other method

    # Random data
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=list("ABC"))
    output_filepath = os.path.join(
        output_content_path, f"{transform_instance_context['filename']}.pdf"
    )

    Title = transform_instance_context["title"]

    # Get PDF Styles
    styles = getSampleStyleSheet()
    styleNormal = styles["Normal"]
    styleHeading = styles["Heading1"]

    doc = SimpleDocTemplate(output_filepath)
    story = []

    # Add Heading
    story.append(Paragraph(Title, style=styleHeading))

    data = [df.columns.tolist(), *df.values.tolist()]

    t = Table(data, style=[("GRID", (0, 0), (-1, -1), 0.5, colors.grey)])
    story.append(t)

    doc.build(story)

    logger.info(f"Transform_nid: {transform_nid}")
    logger.info(f"Transform_instance_context: {transform_instance_context}")

    return 0
