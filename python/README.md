問題の入手
acc new abc100

任意のテスト実行
python3 main.py < tests/sample-1.in
pypy3 main.py < tests/sample-1.in

テスト実行
dir = abc/100/a
oj t -c 'python3 main.py' -d tests/
oj t -c 'pypy3 main.py' -d tests/

提出
acc s main.py -- --guess-python-interpreter pypy
