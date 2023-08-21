#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lớp "Fact" đại diện cho một vị từ logic với các thuộc tính khác nhau như phép toán, đối số và phủ định. 
class Fact:
    def __init__(self, op='', args=[], negated=False):
        self.op = op               # Relation or function
        self.args = args           # Varibles and constants
        self.negated = negated     # Not

    def __repr__(self):
        return '{}({})'.format(self.op, ', '.join(self.args))

    def __lt__(self, rhs):
        if self.op != rhs.op:
            return self.op < rhs.op
        if self.negated != rhs.negated:
            return self.negated < rhs.negated
        return self.args < rhs.args

    def __eq__(self, rhs):
        if self.op != rhs.op:
            return False
        if self.negated != rhs.negated:
            return False
        return self.args == rhs.args

    def __hash__(self):
        return hash(str(self))
   
    def copy(self):
        return Fact(self.op, self.args.copy(), self.negated)

    def negate(self):
        self.negated = not self.negated

    def get_args(self):
        return self.args

    def get_op(self):
        return self.op

    @staticmethod
    def parse_fact(fact_str):
        if '\\' in fact_str:
            # Handle cases like "X\=Y"
            parts = fact_str.split('\\=')
            op = parts[0]
            args = [arg.strip() for arg in parts[1].split(',')]
        else:
            #fact_str = fact_str.strip().rstrip('.').replace(' ', '')
            op_start = 0
            print("Parsing fact_str:", fact_str)
            #sep_idx = fact_str.index('(')
            op_end = fact_str.index('(')
            op = fact_str[op_start:op_end]
            args_start = op_end + 1
            args_end = len(fact_str) - 1
            #op = fact_str[:sep_idx]
            args = fact_str[args_start:args_end].split(',')
        return Fact(op, args)

