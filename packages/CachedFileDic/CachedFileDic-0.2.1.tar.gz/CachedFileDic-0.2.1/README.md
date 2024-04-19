- The explanations in English, Simplified Chinese, and Spanish are provided below.
- 下面提供了英语、简体中文和西班牙语的说明。
- Las explicaciones en inglés, chino simplificado y español se proporcionan a continuación.

---

## 概要
- `CachedFileDic`は、Pythonの辞書のように使えるライブラリです。
- メモリのキャッシュのように、巨大データをファイルに保存しつつメモリにも適宜載せるため、メモリに載り切る量を意識せず巨大データを扱うことができます。

## 特徴
- Pythonの辞書と同様に読み書きができます。 (現状のリリースバージョンではCRUDの「C」「R」のみ実装されていますが、「U」「D」も順次追加予定です。)
- 巨大データを扱う際に自動的に一部データをファイルに退避します。いくつかのデータを同じファイルにまとめて書き込むため、メモリに載せる量が巨大すぎず、かつIOが頻繁すぎないため、比較的高速に読み書き可能です。
- ファイルへの書き込みは基本的には自動で行われますが、プログラム異常終了時等のデータ消失を防ぐために明示的に書き込みを行うことも可能です。

## 使用例
```python
import CachedFileDic

# 対象ディレクトリに接続 [CachedFileDic]
db = CachedFileDic.conn("./data/")

# データ書き込み [CachedFileDic]
db["key1"] = "fuga"
# データ読み出し [CachedFileDic]
print(db["key1"])  # -> fuga
# データの存在確認 [CachedFileDic]
print(("key1" in db))  # -> True

# for文脈での利用
for key in db:
    print(db[key])

# 明示的なファイル書き込み
db.commit()
```

## 注意点
- 複数プロセスからの競合書き込みには対応していません。 (高速化のため)
- セキュリティ的チューニングはされていません。 (信頼できない第三者が作成したDBの読み込みは危険を伴います。)

---

## Overview
- `CachedFileDic` is a library that can be used like a Python dictionary.
- It saves large data sets to a file while also loading them into memory as needed, similar to memory caching. This allows handling large data sets without being constrained by memory capacity.

## Features
- It can be read and written just like a Python dictionary. (The current release version implements only 'Create' and 'Read' in CRUD operations, but 'Update' and 'Delete' will be added progressively.)
- When dealing with large data sets, it automatically backs up part of the data to a file. Several pieces of data are written to the same file, ensuring that the amount of data loaded into memory is not too large, and reducing frequent I/O operations, thus allowing relatively fast read and write speeds.
- While file writing is generally automatic, explicit writing can be performed to prevent data loss in cases of abnormal program termination.

## Usage Example
```python
import CachedFileDic

# Connect to a target directory [CachedFileDic]
db = CachedFileDic.conn("./data/")

# Write data [CachedFileDic]
db["key1"] = "exampleValue"
# Read data [CachedFileDic]
print(db["key1"])  # -> exampleValue
# Check for data existence [CachedFileDic]
print(("key1" in db))  # -> True

# Usage within a for loop
for key in db:
    print(db[key])

# Explicit file writing
db.commit()
```

## Notes
- The library does not support concurrent writing from multiple processes for speed optimization.
- Security tuning is not implemented. (Loading databases created by untrusted third parties can be risky.)

---

## 概要
- `CachedFileDic`是一个可像Python字典一样使用的库。
- 它将大量数据保存在文件中，同时适当地加载到内存中，这样就可以处理大数据而无需担心内存容量限制。

## 特点
- 可以像Python字典那样进行读写操作。（目前的发布版本仅实现了CRUD的“C”和“R”，“U”和“D”将陆续添加。）
- 当处理大数据时，它会自动将部分数据存储到文件中。由于将一些数据汇总到同一个文件中，因此不会使内存负担过重，同时也不会频繁进行IO操作，从而可以相对快速地进行读写。
- 尽管文件写入通常是自动进行的，但为了防止程序异常终止等情况下的数据丢失，也可以明确进行文件写入。

## 使用示例
```python
import CachedFileDic

# 连接目标目录 [CachedFileDic]
db = CachedFileDic.conn("./data/")

# 数据写入 [CachedFileDic]
db["key1"] = "示例文本"
# 数据读取 [CachedFileDic]
print(db["key1"])  # -> 示例文本
# 检查数据是否存在 [CachedFileDic]
print(("key1" in db))  # -> True

# 在for循环中使用
for key in db:
    print(db[key])

# 明确的文件写入
db.commit()
```

## 注意事项
- 不支持多进程间的竞争写入。（为了提高速度）
- 没有进行安全性调整。（加载不可信第三方创建的DB存在风险。）

---

## Resumen
- `CachedFileDic` es una biblioteca que funciona como un diccionario en Python.
- Permite trabajar con grandes volúmenes de datos, almacenándolos en archivos mientras mantiene una copia en memoria, sin la necesidad de preocuparse por el límite de memoria disponible.

## Características
- Ofrece funcionalidades de lectura y escritura similares a los diccionarios de Python. (En la versión actual solo están implementadas las operaciones de 'crear' y 'leer', pero se planea añadir 'actualizar' y 'eliminar' en futuras actualizaciones).
- Al manejar grandes datos, parte de ellos se almacenan automáticamente en archivos. Esto se hace agrupando varios datos en un mismo archivo, lo que minimiza la sobrecarga de memoria y reduce la frecuencia de operaciones de entrada/salida, permitiendo una lectura y escritura relativamente rápida.
- La escritura en archivos se realiza automáticamente, pero también se puede hacer manualmente para prevenir la pérdida de datos en casos de terminación anormal del programa.

## Ejemplos de Uso
```python
import CachedFileDic

# Conexión con el directorio objetivo [CachedFileDic]
db = CachedFileDic.conn("./data/")

# Escritura de datos [CachedFileDic]
db["clave1"] = "ejemplo"
# Lectura de datos [CachedFileDic]
print(db["clave1"])  # -> ejemplo
# Verificar la existencia de datos [CachedFileDic]
print(("clave1" in db))  # -> True

# Uso en bucles for
for clave in db:
    print(db[clave])

# Escritura de archivos explícita
db.commit()
```

## Consideraciones
- No está diseñado para manejar escrituras concurrentes desde múltiples procesos (para optimizar la velocidad).
- No se han implementado medidas de seguridad avanzadas (la carga de bases de datos creadas por terceros no confiables puede ser peligrosa).
