# tests all
ta:
	@oj t -c 'python3 main.py' -d tests/

# テスト指定
# make t case=1
case = 1
t:
	@python3 main.py < tests/sample-${case}.in

# submit
s:
	@acc s main.py -- --guess-python-interpreter pypy

t1:
	@make t case=1
t2:
	@make t case=2
t3:
	@make t case=3
t4:
	@make t case=4
