import dis


def translate_to_bytecode(source_code):
    bytecode = compile(source_code, '<string>', 'exec')
    dis.disassemble(bytecode)


source_code = """
def greet(name):
    print("Hello, " + name + "!")

greet("World")
"""

translate_to_bytecode(source_code)
