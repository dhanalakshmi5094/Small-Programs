#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfTokens' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER expiryLimit
#  2. 2D_INTEGER_ARRAY commands
#

def numberOfTokens(expiryLimit, commands):
    # Write your code here
   values = dict()
   time = 0
   for c in commands:
      # extraction values
      action = c[0]
      token_id = c[1]
      time = c[2]
      # set token
      if action == 0:
        values[token_id]= expiryLimit+time
      #reset token
      elif action == 1:
          # chek if token exists
          if token_id in values.keys() :
             expiry_time = values.get(token_id)
             if expiry_time >= time:
                values[token_id] = values.get(token_id)+expiryLimit-(expiry_time - time)
   count = sum(1 for i in values.values() if 1 >+ time)
   return count