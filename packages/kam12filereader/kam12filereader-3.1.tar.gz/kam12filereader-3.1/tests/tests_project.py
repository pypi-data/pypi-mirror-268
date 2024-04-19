import pandas as pd
import os
import sys
# from hidden_operation import GroupID, Stamp

parent_file = os.path.abspath(__file__)
kam12_baseactions_dir = os.path.abspath(os.path.join(parent_file, "..", "..", "kam12filereader"))
sys.path.append(kam12_baseactions_dir)

sad_file = os.path.abspath(os.path.join(kam12_baseactions_dir, "..", "tests", "real_file", "SAD.xlsx"))       
budget_file = os.path.abspath(os.path.join(kam12_baseactions_dir, "..", "tests", "real_file", "Budget.xlsx")) 

from main_operation import BudgetAccount, SADDetail
from hidden_operation import GroupID, Stamp

budget = BudgetAccount(budget_file)
sad = SADDetail(sad_file)
print(budget.get_data())
print(sad.get_data())