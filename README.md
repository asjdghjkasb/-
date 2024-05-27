## 使用方法

终端运行

```python
poetry build
poetry install
```

然后就可以使用该项目了

## 项目介绍

1. 项目从根目录文件 pKcScan.py 运行,调用./pkcsan/app.py 中为核心操作,可以直接改为多线程
2. 项目核心功能功能放在 core 模块,core.py 中(./core/core.py)

## fingerprint 相关规则

1. fingerprint 放在 module/fingerprint/allFingerprint 目录, 目录位置 ./module/fingerprint/allFingerprint
2. fingerprint 全部为 Json 文件(暂时只支持 Json 文件)
3. fingerprint 文件模板位于 ./module/fingerprint/Template.json (fingerprint 自行添加)

## Poc 相关规则

1. Poc 放在 module/poc 目录, 目录位置 ./module/Poc/
2. Poc 分类名称必须小写, 例如: ./module/Poc/pikachu
3. Poc 版本号位于 Poc 名称下一级, 例如: ./module/Poc/pikachu/1.1.1
4. Poc 全部为 Json 文件(暂时只支持 Json 文件)
5. Poc 文件模板位于 ./module/Poc/Template.json (Poc 自行添加)
