import sys
if __name__ == '__main__':
    nums = [int(i) for i in input().split('/')]
    numerator, denominator = nums[0], nums[1]
    if numerator == 0:
        sys.stdout.write("0" + '\n')
    result = ""
    d = {}
    if (numerator < 0) ^ (denominator < 0):
        result += '-'
    numerator, denominator = abs(numerator), abs(denominator)
    div, mod = divmod(numerator, denominator)
    if mod == 0:
        result += str(div)
        sys.stdout.write(result + '\n')
    result += str(div) + '.'
    d[mod] = len(result) # 记录余数以及对应的位置，该位置就是要插入括号的位置
    while mod:
        mod *= 10
        div, mod = divmod(mod, denominator)
        result += str(div)
        if mod in d:
            index = d[mod] # 若余数已经存在，则找到该余数所对应的位置，在该余数之前插入（
            result = result[:index] + '(' + result[index:] + ')'
            break
        d[mod] = len(result)

    sys.stdout.write(result + '\n')