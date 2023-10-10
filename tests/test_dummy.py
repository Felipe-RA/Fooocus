import os
import importlib
import pytest

def import_all_modules(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.py'):
                module = os.path.join(root, file).replace('/', '.').replace('.py', '')
                importlib.import_module(module)

def test_dummy():
    import_all_modules('.')
    assert 1 == 1