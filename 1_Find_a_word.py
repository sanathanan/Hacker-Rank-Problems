import re

no_of_input = int(input())
st = '\n'.join(['*'+input().strip().replace('_','')+'*' for _ in range(no_of_input)])
for _ in range(int(input())):
    wd = input().strip()
    reg = r'(?<=[\W])'+ wd +'(?=[\W])'
    m = re.findall(reg,st)
    print(len(m))