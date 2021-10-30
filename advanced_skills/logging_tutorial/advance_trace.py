import logging
import traceback
""" Helpful 
for troubleshooting
"""

# You the which kind of error would happen
try:
    a = [1, 2, 3]
    val = a[5]
except IndexError as e:
    logging.error(e) # only logging the msg
    logging.error(e, exc_info=True) # include the stack trace


# You have no idea which kind of error would happen
# but you still want to traceback the code
try:
    a = [1, 2, 3]
    val = a[5]
except:
    logging.error("The error is %s", traceback.format_exc()) # include the stack trace