#!/usr/bin/env python
# coding: utf-8

# In[346]:


def load_file(filename):
    facts = []
    rules = []
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            if not line or line.startswith('%'):
                continue
                
            query_match = re.match(r'^\d+\.\s(.+)$', line)
            predicate_match = re.match(r'^\s(.+)$', line)
            if query_match:
                query = query_match.group(1)
                query = query.rstrip('.')
                questions.append(query)
            else: 
                predicate, arguments = line.split('(', 1)
                arguments = arguments.rstrip(').')

                if ':-' in line:
                    # It's a rule 
                    rule = line.rstrip('.')
                    rules.append(rule)
                else:
                    # It's a fact
                    fact = line.rstrip('.')
                    facts.append(fact)
                
    return facts, rules, questions


# In[347]:


import re

def define_rules(rules):
    defined_rules = []
    
    for rule in rules:
        rule_dict = {}
        match = re.match(r'(\w+)\((.*?)\)', rule)
        predicate = match.group(1)
        args = [arg.strip() for arg in match.group(2).split(',')]

        # Extract conditions
        conditions = []
        if ':-' in rule:
            _, condition_str = rule.split(':-', 1)
            conditions = [cond.strip() for cond in re.split(r',\s*(?![^()]*\))', condition_str)]
            
        existing_rule = next((rule for rule in defined_rules if rule['predicate'] == predicate), None)
        if existing_rule:
            existing_rule['conditions'].append(conditions)
        else:
            defined_rules.append({
                'predicate': predicate,
                'args': args,
                'conditions': [conditions]
            })
    
    return defined_rules


# In[348]:


def define_facts(facts):
    defined_facts = []
    
    for fact in facts:
        predicate, args = fact.split('(')
        args = args[:-1].split(', ')
        defined_facts.append({
            'predicate': predicate,
            'args': args
        })
    
    return defined_facts


# In[349]:


def define_questions(questions):
    defined_questions = []
    
    for question in questions:
        predicate, args = fact.split('(')
        args = args[:-1].split(', ')
        defined_questions.append({
            'predicate': predicate,
            'args': args
        })
    
    return defined_questions


# In[354]:


facts, rules, questions = load_file('Facts.txt')
defined_rules = define_rules(rules)
defined_facts = define_facts(facts)
defined_questions = define_questions(questions)

#show
for fact in defined_facts:
    print(rule)
print()
for rule in defined_rules:
    print(rule)
print()
for question in defined_quess:
    print(rule)
print()


#do query
# for question in questions:
#     print(question)
#     predicate, args = question.split('(')
#     args = args[:-1].split(', ')
    
#     if (len(args) == 1 or (args[0] != 'X' and args[1] != 'X')):
#         check(predicate, args)
#         if (predicate == 'female'):
#             print (female())
#         elif (predicate == 'male'):
#             print (male(args[0]))
#         elif (predicate == 'married'):
#             print (married(args[0],args[1]))        
#     else:
        


# In[ ]:





# In[351]:


# kinship_tree, root_node = build_kinship_tree(facts)
# def build_kinship_tree(facts):
#     person_dict = {}

#     for fact in facts:
#         predicate, args = fact.split('(')
#         args = args[:-1].split(', ')
#         if predicate == 'parent':
#             parent_name, child_name = args
#             parent = person_dict.get(parent_name, Person(parent_name, None))
#             child = person_dict.get(child_name, Person(child_name, None))
#             parent.add_child(child)
#             person_dict[parent_name] = parent
#             person_dict[child_name] = child
#         elif predicate == 'male' or predicate == 'female':
#             person_name = args[0]
#             gender = predicate
#             person = person_dict.get(person_name, Person(person_name, gender))
#             person.gender = gender
#             person_dict[person_name] = person
#         elif predicate == 'married':
#             person1_name, person2_name = args
#             person1 = person_dict.get(person1_name, Person(person1_name, None))
#             person2 = person_dict.get(person2_name, Person(person2_name, None))
#             person1.set_married(person2)
#             person_dict[person1_name] = person1
#         elif predicate == 'divorced':
#             spouse1_name = args[0]
#             spouse2_name = args[1]

#             spouse1 = person_dict.get(spouse1_name, Person(spouse1_name, None))
#             spouse2 = person_dict.get(spouse2_name, Person(spouse2_name, None))

#             spouse1.set_divorce(spouse2)
#             person_dict[spouse1_name] = spouse1
            
#     # Find the root node dynamically
#     root = None
#     for person in person_dict.values():
#         if person.parents is None:
#             root = person
#             break

#     return person_dict, root


# In[352]:


# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#         self.children = []
#         self.married = None
#         self.parents = []
#         self.divorced = []

#     def add_child(self, child):
#         self.children.append(child)
#         child.set_parent(self)

#     def set_parent(self, parent):
#         self.parents.append(parent)

#     def set_married(self, married):
#         self.married = married
        
#     def set_divorce(self, divorce):
#         self.married = None
#         self.divorced.append(divorce) 


# In[353]:


#test rules input
# for rule_dict in defined_rules:
#     print(rule_dict['predicate'])
#     print(rule_dict['args'])
#     print(rule_dict['conditions'])

#test fact input
# for  name, person in kinship_tree.items():
#     married = person.married
#     print("MARRIED: ",married)
#     divorced = person.divorced
#     print("DIVORCED: ",divorced)
#     gender = person.gender
#     print("GENDER: ",person.name, ":", gender)
#     parent = person.parents
#     print("PARENT: ",parent)
#     print(f"{person.name}'s children: {person.children}")
#     print()

