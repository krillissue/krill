from krill import Executable, Warning

example = Executable("example", kind='executable')
example.set_property(Warning.ALL)
example.set_language('c++')
example.set_dialect(17)

example.add_sources("src/main.cpp")
