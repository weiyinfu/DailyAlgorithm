from bes.util import single_pyx
from os.path import *

"""
cython包装
"""
single_pyx.compile_folder(dirname(__file__))
import baga

baga.solve()
# ans = baga.py_judge([[2, 2, 3], [3, 4, 0], [0, 0, 7]])
# print(ans)
