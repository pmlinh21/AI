#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fact import Fact
from unify import unify
from util import Substitution

class Rule:
    def __init__(self, conclusion=Fact(), premises=[]):
        self.conclusion = conclusion        
        self.premises = premises            
        self.operators = self.extract_operators()           
        self.premises.sort()
        self.duplicate_predicate = self.check_duplicate_predicate()

    def __repr__(self):
        return '{} => {}'.format(' & '.join([str(condition) for condition in self.premises]), str(self.conclusion))

    def copy(self):
        return Rule(self.conclusion.copy(), self.premises.copy())

    def get_premise_count(self):
        return len(self.premises)

    def extract_operators(self):
        operators = set()
        for premise in self.premises:
            operators.add(premise.op)
        return operators

    def is_helpful(self, fact_operator):
        return fact_operator in self.operators

    def may_trigger(self, new_facts):
        for new_fact in new_facts:
            for premise in self.premises:
                if unify(new_fact, premise, Substitution()):
                    return True
        return False

    def check_duplicate_predicate(self):
        premise_count = self.get_premise_count()
        for i in range(premise_count - 1):
            if self.premises[i].op == self.premises[i + 1].op:
                return True
        return False

    @staticmethod
    def parse_rule(rule_str):       
        rule_str = rule_str.strip().rstrip('.').replace(' ', '')
        sep_index = rule_str.find(':-')

        conclusion = Fact.parse_fact(rule_str[: sep_index])
        premises = []
        fact_strings = rule_str[sep_index + 2:].split('),')
        # print(fact_strings)
        for idx, fact_str in enumerate(fact_strings):
            if idx != len(fact_strings) - 1:
                fact_str += ')'
            # print(fact_str)
            fact = Fact.parse_fact(fact_str)
            premises.append(fact)
        # print(premises)
        # duplicate_predicate = True
        return Rule(conclusion, premises)

