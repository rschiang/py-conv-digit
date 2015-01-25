# Convert Chinese uppercase numbers to digits

capital_chars = {
    '零': 0,
    '壹': 1,
    '貳': 2,
    '參': 3,
    '肆': 4,
    '伍': 5,
    '陸': 6,
    '柒': 7,
    '捌': 8,
    '玖': 9,
}

digits = { c: d for c, d in capital_chars.items() }

units = {
    '垓': 10 ** 20,
    '京': 10 ** 16,
    '兆': 10 ** 12,
    '億': 10 ** 8,
    '萬': 10 ** 4,
}

single_units = {
    '仟': 1000,
    '佰': 100,
    '拾': 10,
}

def uppercase_to_digits(source):
    # 先宣告所有需要用到的緩衝區
    digit, buf, result = 0, 0, 0

    # 列舉每一個字元
    for char in source:
        # 如果遇到大寫數字，先存起來
        if char in capital_chars:
            digit = capital_chars[char]
        # 如果遇到可重複的單位，存進緩衝區
        elif char in single_units:
            buf += digit * single_units[char]
            digit = 0
        # 不會重複的單位可以直接結算
        else:
            buf += digit
            digit = 0
            if char in units:
                result += buf * units[char]
                buf = 0
            elif char == '元':
                break

    # 結算所有緩衝區的數字
    return result + buf + digit

test_cases = [
    '玖仟伍佰貳拾柒',
    '玖仟伍佰貳拾柒萬捌仟陸佰捌拾玖',
    '陸佰捌拾玖億零貳仟',
    '柒億參仟萬元',
    '壹拾柒萬零參佰元',
    '嗡嗡嗡元',
]

for case in test_cases:
    print(uppercase_to_digits(case))
