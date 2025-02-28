import os
from pathlib import Path
import test_path1
from .. import test_flush

os_path = os.path.abspath(__file__)
os_path_1 = os.path.dirname(os.getcwd())
os_path_2 = os.getcwd()

new_path = Path(__file__)
new_path_parents = Path(__file__).parents[1]

print(__name__)
print(f"os path: {os_path}")
print(f"os path: {os_path_1}")
print(f"os path: {os_path_2}")
print(f"new path: {new_path}")
print(f"new path: {new_path_parents}")
