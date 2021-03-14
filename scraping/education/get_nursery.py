#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraping_utils import scraping_from_navitime, scraping_from_mapfan  # nopep8


if __name__ == '__main__':
    # # Get nursery kindergarten info from navitime
    # category_id = "0504006"
    # pref_code_list = [i for i in range(11, 15)]
    # df_nursery_kindergarten = scraping_from_navitime(
    #     category_id, pref_code_list)

    # Get nursery kindergarten info from mapfan
    category_id = "1705"
    pref_code_list = [i for i in range(11, 15)]
    df_nursery = scraping_from_mapfan(
        category_id, pref_code_list)

    # Save nursery info
    directory_path = "/home/vagrant/share/data/education/"
    os.makedirs(directory_path, exist_ok=True)
    df_nursery.to_csv(
        directory_path + "nursery.csv", index=False)
    print("Done!")