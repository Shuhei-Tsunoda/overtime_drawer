import os
from logging import getLogger, StreamHandler, INFO
from typing import Optional

import pandas as pd
from matplotlib.figure import Figure
import click

from overtime_drawer import drawer


logger = getLogger(__name__)


@click.command()
# @click.option('--src', type=click.Path(exists=True), help='csvファイルへのパス')
# @click.option('--dist', type=click.Path(), help='画像を出力するディレクトリへのパス')
@click.argument('src', type=click.Path(exists=True))
@click.argument('dist_dir', type=click.Path(dir_okay=True, file_okay=False))
def generate(src: Optional[str], dist_dir: Optional[str]):
    if src is None:
        raise click.BadParameter('srcを指定してください')
    if dist_dir is None:
        raise click.BadParameter('distを指定してください')
    df = pd.read_csv(src)
    os.makedirs(dist_dir, exist_ok=True)
    for d, fig in drawer.generate_figures(df):
        dist = os.path.join(dist_dir, d+'.png')
        logger.info(f'Exporting {dist}')
        fig.savefig(dist)

    logger.info('Complete')


if __name__ == '__main__':
    logger.setLevel(INFO)
    logger.addHandler(StreamHandler())
    generate(None, None)
