import re
import os
import keyword
def highlight(code):
	
    for k in keyword.kwlist:
        k = k + " "
        code = code.replace(k,"<b style='color:yellow' title='hello'>" + k + "</b>")
	# Add title attribute for popover
    #converting text to html
    code = code.replace("\n", "<br>")
    code = code.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
    functions = re.findall("\w*\(", code)
    for function in functions:
        code = code.replace(function[:-1],"<b style='color:blue' title='hello'>" + function[:-1] + "</b>")
        # Add title attribute for popover
    return code