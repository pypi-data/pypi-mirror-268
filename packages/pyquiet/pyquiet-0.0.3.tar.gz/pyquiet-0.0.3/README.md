# QUIET-paser

## 环境配置

### ANTLR-Python Runtime
首先， 需要检查Python下的antlr运行环境，quiet-parser使用的版本为antlr4-python3-runtime=4.13.0
```
$ pip show antlr4-python3-runtime

Name: antlr4-python3-runtime
Version: 4.13.0
Summary: ANTLR 4.13.0 runtime for Python 3
Home-page: 
Author: Terence Parr, Sam Harwell
Author-email: Eric Vergnaud <eric.vergnaud@wanadoo.fr>
License: BSD
Location: /home/liudingdong/anaconda3/envs/quingo/lib/python3.8/site-packages
Requires: 
Required-by: pyquiet
```
若已安装其它版本的antlr4-python3-runtime，会在使用pip安装quiet-parser之后卸载并安装4.13.0的antlr4-python3-runtime。

### Parser&Lexer 生成
新版本已经将生成后的文件上传，故无需进行额外的操作

### 测试
```
pip install -e .
pytest
```