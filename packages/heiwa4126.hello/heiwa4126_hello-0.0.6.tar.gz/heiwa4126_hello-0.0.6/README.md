# heiwa4126.hello (pip-heiwa4126-hello)

`heiwa4126.fizzbuzz` は Python 用の パッケージです。
'hello' を返す関数 `hello()` を実装します。

## インストール

```sh
pip install heiwa4126.hello
```

(名前空間パッケージなので、それとわかるよう区切りに `.` を使っています)

## 使用方法

このパッケージは、以下のように使用できます:

```python
from heiwa4126.hello import hello

print(hello())
```

このコードは、"hello" を適切に出力します。

またパッケージをインストールすると コマンド `heiwa4126_hello` も
インストールされます。

```sh
heiwa4126_hello
# or
heiwa4126_hello2
```

このコマンドは、"hello" を適切に出力します。2 つの違いは
[pyproject.toml](pyproject.toml)
の project.scripts のところを参照。

## このパッケージはテンプレートです

```sh
YOUR_NAMESPACE="お好みの名前空間"
YOUR_PACKAGE="お好みのパッケージ名"
find . -type f | xargs perl -i.bak -pe "s/heiw4126/$YOUR_NAMESPACE/g;s/hello/$YOUR_PACKAGE/g;"
mv src/heiwa4126 "src/$YOUR_NAMESPACE"
mv "src/$YOUR_NAMESPACE/hello.py" "src/$YOUR_NAMESPACE/$YOUR_PACKAGE"
```

のようにして置き換えて使ってください。
