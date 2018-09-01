# overtime_drawer

社員の残業時間を記述したcsvファイルから、
残業時間をpngファイルとして描画する。

## 機能

- 部門ごとの描画 - 部門ごとに残業時間を描画する。
- 平均残業時間 - 部門ごとの平均残業時間を描画する。

## 必要なもの

- [Python](https://www.python.org/)
- [Pipenv](https://pipenv-ja.readthedocs.io/)

## インストール方法

1. `$ pipenv install`を実行する

## アンインストール方法

1. `$ pipenv --rm`を実行する
1. このディレクトリを削除する

## 使用方法

1. `$ pipenv run draw <CSVファイルのパス> <画像を保存したいフォルダのパス>`を実行する

## 実行例を見る

1. `$ pipenv run draw_example`を実行する

## License

MIT
