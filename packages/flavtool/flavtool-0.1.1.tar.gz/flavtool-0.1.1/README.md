# flavtool

flavtoolは、味覚情報を埋め込み可能なファイル形式:FlavMP4の解析、
編集を可能にするpythonツールキットです。

## インストール方法

```shell
pip install flavtool
```


## 使用方法
ツールキットは、parser, analyzer,codec,composerに分けられます。

### parser
MP4ファイルを構文解析します。

```python
from flavtool.parser import Parser

p = Parser("pathmp4")

box = p.parse()

box = p.parse()
#メディアデータをメモリに読み込まないようにするには、read_mdat_bytes=falseとしてください
box = p.parse(read_mdat_bytes=False)

# boxには構文解析されたBoxの集合が入ります
box.print()
```

### analyzer
パースされた情報を元に、トラック情報、メディア情報などを整理します。

```python
from flavtool.parser import Parser
from flavtool.analyzer import analyze

p = Parser("pathmp4")
box = p.parse(read_mdat_bytes=False)

#解析
flav_mp4 = analyze(box)

#味のトラック情報を取得
taste_track = flav_mp4.tracks["tast"]
#味のデータを取得(Chunk, Sample構造を取っています)
taste_media_data = flav_mp4.tracks["tast"]
```

### codec
味データのデコード/エンコードを行います
```python
from flavtool.codec import get_decoder, get_encoder
import numpy as np


taste = np.array([1,2,3,4,5], dtype=np.uint8)

#非圧縮5次元味データのエンコーダを取得する
encoder = get_encoder("raw5")

#エンコード (5次元 uin8 ndarray -> bytes)
byte_data = encoder(taste)

#デコード (bytes -> 5次元 ndarray uint8)
decoder = get_decoder("raw5")
taste_data = decoder(byte_data)

```

### composer
与えられたFlavMP4構造体の情報を元にMP4データを再合成します

```python
from flavtool.parser import Parser
from flavtool.analyzer import analyze

##サンプルコード準備中
p = Parser("pathmp4")
box = p.parse(read_mdat_bytes=False)

#解析
flav_mp4 = analyze(box)

#味のトラック情報を取得
taste_track = flav_mp4.tracks["tast"]
#味のデータを取得(Chunk, Sample構造を取っています)
taste_media_data = flav_mp4.tracks["tast"]

```




