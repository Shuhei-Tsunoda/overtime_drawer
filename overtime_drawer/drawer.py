from typing import Tuple, Generator

from matplotlib.figure import Figure
import pandas as pd
import seaborn as sns


def generate_figures(df: pd.DataFrame) -> Generator[Tuple[str, Figure], None, None]:
    """
    DataFrameから残業時間を描画したFigureを生成する。
    DataFrameは以下のような形式でなければならない。

    ==========  ============  =====  ====== =====
    部署         名前          11月    12月   1月
    ==========  ============  =====  ====== =====
    部署A        愛知 大地      30     50     100
    部署B        鹿児島 真島    20     15     0
    ==========  ============  =====  ====== =====
    """
    months = df.columns[df.columns.str.endswith('月')]
    df['合計'] = df[months].T.sum()
    df = df.sort_values(by=['部署', '合計'], ascending=[True, False])
    departments = df['部署'].unique()

    for d in departments:
        df_d = df[df['部署'] == d]

        ax = df_d.set_index('名前')[months].plot(
            kind='bar',
            stacked=True,
            title=f'{d}の残業時間',
            figsize=(10, 5),
        )

        # Draw avg line
        average = df_d[months].sum().sum() / len(df_d.index)
        sns.lineplot(x=[-0.5, len(df_d)+0.5], y=average, ax=ax)
        ax.text(-0.5, average, '{:0.1f}h'.format(average), ha='right', va='center')

        # Draw top text
        for n, total in enumerate(df_d[months].T.sum()):
            ax.text(n, total, '{:0.1f}h'.format(total),
                    rotation=30,
                    ha='left',
                    va='bottom')

        ax.grid(axis='y')
        ax.locator_params(axis='y', nbins=4)

        yield d, ax.get_figure()
