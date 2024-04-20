from gen_tb import gen_tb

module_list = ['adder.v', 'fadd.v']
for module in module_list:
    gen_tb.gen_verilog_tb(module)
