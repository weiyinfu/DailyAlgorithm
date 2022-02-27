"""
控制台下的树状图显示

node只需要包含left和right两个成员变量就可以
"""


def main(node, son_getter, value_getter, indent_unit=1):
    ans = []
    indent_unit = max(indent_unit, 1)

    def go(node, prefix):
        if not node:
            return
        ans.append(prefix + value_getter(node))
        sons = list(son_getter(node))
        for ind, son in enumerate(sons):
            sep = ('`' if ind == len(sons) - 1 else '|') + ('-' * indent_unit)
            go(son, f"{prefix.replace('-', ' ').replace('`', ' ')}{sep}")

    go(node, '')
    return '\n'.join(ans)


def binary_tree_view(node, indent_unit=1):
    def get_sons(node):
        if not node:
            return []
        return [i for i in [node.left, node.right] if i]

    def get_value(node):
        return str(node.key)

    return main(node, get_sons, get_value, indent_unit)


if __name__ == '__main__':
    a = {
        'value': 1,
        'sons': [
            {'value': 2, 'sons': [{'value': 4}, {'value': 5}], },
            {'value': 3, 'sons': [{'value': 4}, {'value': 5}, {'value': 7}]}
        ]
    }
    ans = main(a, lambda x: x.get('sons', []), lambda x: str(x['value']), 3)
    print(ans)
