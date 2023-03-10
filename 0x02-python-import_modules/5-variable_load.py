from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location("variable_load_5", "variable_load_5.py")
module = module_from_spec(spec)
spec.loader.exec_module(module)

print(module.a)
