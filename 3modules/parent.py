from subpackage import sub_child
import child
from child import run_child
import sys

# ctrl + space to see possible folders and files when importing

# run_child()
sub_child.run_sub_package()
child.run_child()
run_child()

# Good for debugging
print(sys.path)
print(child.__name__)
print(dir(child))
