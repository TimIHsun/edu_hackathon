# -*- coding: utf-8 -*-
"""install_ckiptagger.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m_ibuRM0o4hKdxPfAs7O4LB9iChrDktF
"""

!pip install -U ckiptagger[tfgpu,gdown]
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER

print('hello, ckiptagger~')