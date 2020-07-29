# -*- coding: utf-8 -*-
__author__ = 'miro'
__date__ = '2020/2/11'

"""
1. Fetch upstream table in order to get src&target path
2. PathFilter will do the size check and insert filtered results into downstream table
3. Fetch downstream table in order to get src&target path
4. Start distcp job
5. Update the states in 2 tables
"""

class Scheduler:
    def __init__(self):
        pass

