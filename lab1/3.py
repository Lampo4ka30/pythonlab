from sys import argv

# checklist for numbers and expression symbols
nums = '0123456789'
signs = '-+*%'


def assay(t):
    ind = 1
    for q in t:
        if (ind == 3) and (q == '0'):
            return False
        elif q in nums:
            ind = 1
        elif ind and (q == '/'):
            ind = 3
        elif ind and q in signs:
            ind = 0
        else:
            return False
    return ind


exp = ''
for i in range(1, len(argv)):
    exp += argv[i]
if assay(exp):
    print('(True, {})'.format(eval(exp)))
else:
    print('(False, None)')
