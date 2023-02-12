"""
测试环境配置信息
"""

import os
import sys
basedir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
DB_PATH = 'sqlite:///' + os.path.join(basedir, 'test_data.sqlite')
