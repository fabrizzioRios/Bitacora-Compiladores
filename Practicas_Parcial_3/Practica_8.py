import dis

bytecode_print = compile("print('Hola')", "<string>", "exec")
dis.dis(bytecode_print)


def generate_bytecode_for_print():
    yield "LOAD_CONST", ""
    yield "PRINT_EXPR", None
    yield "POP_TOP", None


for opcode, argument in generate_bytecode_for_print():
    print(opcode, argument)

# code_obj = compile(
#     [
#         ("LOAD_CONST", ""),
#         ("PRINT_EXPR", None),
#         ("POP_TOP", None),
#     ],
#     "<string>",
#     "exec"
# )
# exec(code_obj)
