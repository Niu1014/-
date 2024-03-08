def check_brackets(strings):
    outputs = []
    for string in strings:
        stack = []
        marked_string = list(string)
        for i, char in enumerate(string):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    marked_string[i] += '?'
        for index in stack:
            marked_string[index] += 'x'
        outputs.append(''.join(marked_string))
    return outputs