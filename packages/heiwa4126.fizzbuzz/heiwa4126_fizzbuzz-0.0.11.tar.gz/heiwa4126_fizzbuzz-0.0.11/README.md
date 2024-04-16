# heiwa4126.fizzbuzz (pip-heiwa4126-fizzbuzz)

`heiwa4126.fizzbuzz` は Python 用の FizzBuzz ジェネレータパッケージです。

このプロジェクトは PyPI と GitHub Copilot の練習です。

## インストール

```sh
pip install heiwa4126.fizzbuzz
```

(名前空間パッケージなので、それとわかるよう区切りに `.` を使っています)

## 使用方法

このパッケージは、FizzBuzz のジェネレータを提供します。以下のように使用できます:

```python
from heiwa4126.fizzbuzz import fizzbuzz

for item in fizzbuzz(15):
    print(item)

# or
print("\n".join(fizzbuzz(15)))
```

このコードは、1 から始まり、"Fizz"、"Buzz"、または "FizzBuzz" を適切に出力します。

## GitHub Copilot

このコードのひな形は GitHub Copilot を使って以下のプロンプトで作りました。

```text
@workspace /new fizzbuzzを生成するpythonプロジェクト。pypiで配布可能なディレクトリ構成で、プロジェクト名はheiwa4126_fizzbuzz。fizzbuzzはジェネレータで実装。
```

## 開発メモ

[煩雑な開発メモは GitHub で](https://github.com/heiwa4126/pip-heiwa4126-fizzbuzz/blob/main/docs/development-note.md) 見てね。
