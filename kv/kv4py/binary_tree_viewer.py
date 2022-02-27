"""
基于dot的二叉树查看器
"""
import logging
import os
import shutil
import tempfile
import webbrowser
from os.path import *
from typing import List, Union
from tqdm import tqdm
import numpy as np


def binarytree_to_father(tree):
    # 把tree转成father数组
    ans = []

    def go(node, father, side: str):
        if not node:
            ans.append((f"{father.key}", f"_{side}_{father.key}"))
            return
        if father:
            ans.append((f"{father.key}", f"{node.key}"))
        if node.left is None and node.right is None:
            return
        go(node.left, node, 'left')
        go(node.right, node, 'right')

    go(tree.root, None, '')
    return ans


def show_svg(father: List, filename: str):
    """
    调用此函数前，必须保证安装graphviz
    mac：brew install graphviz
    :param father:
    :param filename:
    :return:
    """
    if not filename.endswith('.dot'):
        filename += '.dot'
    with open(filename, "w", encoding='utf8') as f:
        f.write("""
digraph mygraph{
    graph [nodesep=0.1];
    node [shape=circle];
    rankdir="UD";
    edge [arrowhead=vee];
""")
        lines = []
        for beg, end in father:
            invisible = False
            if end.startswith('_'):
                invisible = True
            if invisible:
                # 设置不可见的结点
                lines.append(f"""{end}[group={beg}, label="", width=0.3, style=invis];""")
            edge_sufix = "[style=invis]" if invisible else ""
            lines.append(f"{beg}->{end} {edge_sufix};")
        for i in lines:
            f.write(f"""    {i}\n""")
        f.write("}")
    os.system(f"dot -Tsvg -O {filename}")  # -O表示按照当前名称输出


def show_page(file):
    webbrowser.open_new_tab("file:///" + os.path.abspath(file))


def main(t, eles: Union[np.ndarray, List], show_process: bool = True):
    folder = join(tempfile.gettempdir(), 'binary_tree')
    shutil.rmtree(folder, ignore_errors=True)
    os.makedirs(folder)
    lines = []
    for i, v in enumerate(tqdm(eles)):
        t.insert(v, v)
        if not show_process and i < len(eles) - 1:
            continue
        fa = binarytree_to_father(t)
        show_svg(fa, join(folder, f"{i}"))
        lines.append(f"""
<div>
    <span>插入{v}</span>
    <img src='{i}.dot.svg'>
</div>""")
    html = f"""
    <html>
    <head></head>
    <body>
    <div>
        {''.join(lines)}
    </div>
    </body>
    </html>
    """
    html_path = join(folder, "index.html")
    with open(html_path, 'w')as f:
        f.write(html)
    logging.info(html_path)
    show_page(html_path)
