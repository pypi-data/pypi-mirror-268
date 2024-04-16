# 六十四卦编码

六十四卦编码，python实现。
如：“hello，世界”会编码为“䷯䷬䷿䷶䷸䷬䷀䷌䷌䷎䷼䷲䷰䷳䷸䷘䷔䷭䷒〇”。

## all language

* [golang](https://github.com/lizongying/go-gua64)
* [js](https://github.com/lizongying/js-gua64)
* [java](https://github.com/lizongying/java-gua64)
* [php-gua64](https://github.com/lizongying/php-gua64)
* [python](https://github.com/lizongying/pygua64)

## install

```
pip install pygua64
```

## example

```
from pygua64 import gua64
r = gua64.encode('hello，世界'.encode())
print(r.decode())

r = gua64.decode('䷯䷬䷿䷶䷸䷬䷀䷌䷌䷎䷼䷲䷰䷳䷸䷘䷔䷭䷒〇'.encode())
print(r.decode())

r = verify('䷯䷬䷿䷶䷸䷬䷀䷌䷌䷎䷼䷲䷰䷳䷸䷘䷔䷭䷒〇')
print(r)
```