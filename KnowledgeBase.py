


# KnowledgeBase chịu trách nhiệm lưu trữ các sự kiện và quy tắc đại diện cho các mối quan hệ và thông tin trong cơ sở tri thức. 

# Các phương thức "add_fact" và "add_rule" cho phép đưa vào cơ sở kiến thức các sự kiện và quy tắc. 

# Phương thức "query" sử dụng forward chaining để trả lời các truy vấn. 

# Phương thức "get_potential_facts" giúp xác định các dữ kiện liên quan để áp dụng quy tắc. 

# Phương thức "populate" đọc các câu và điền vào cơ sở tri thức.

# Lớp Sentence có các phương pháp để phân loại câu là sự kiện, quy tắc hoặc nhận xét. 
# Nó cũng giúp lấy câu tiếp theo từ chuỗi đầu vào.

from fact import Fact
from rule import Rule
from forward_chaining import forward_chaining
class Sentence:
    @staticmethod
    def classify(sentence_str):
        # print("sentence_str: ", sentence_str)
        sentence_str = sentence_str.strip()
        if not sentence_str:
            return 'blank'
        if sentence_str.startswith('%'):
            return 'comment'
        if ':-' in sentence_str:
            return 'rule'
        return 'fact'

    @staticmethod
    def fetch_next(input_str):
        index = 0
        next_str = input_str[index].strip()   
        while not next_str.endswith('.'):
            index += 1
            next_str += input_str[index].strip()
        return next_str, input_str[index + 1:]
    
class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        # print(fact)
        self.facts.add(fact)

    def add_rule(self, rule):
        # print(rule)
        self.rules.append(rule)

    def query(self, alpha):
        return forward_chaining(self, alpha)

    def get_potential_facts(self, rule):
        facts = []
        print("rule:",rule, "\n", rule.operators)
        for fact in self.facts:
            # print("*")
            # print(fact)
            # print(fact.op)
            # print("*")
            if rule.is_helpful(fact.op):
                # print("*")
                # print(fact)
                # print(rule)
                # print("*")
                facts.append(fact)
        # print(facts)
        return facts

    @staticmethod
    def populate(kb, list_sentence_str):
        while list_sentence_str:
            sentence_str, list_sentence_str = Sentence.fetch_next(list_sentence_str)
            sentence_type = Sentence.classify(sentence_str)
            if sentence_type == 'fact':
                fact = Fact.parse_fact(sentence_str)
                kb.add_fact(fact)
            elif sentence_type == 'rule':
                rule = Rule.parse_rule(sentence_str)
                kb.add_rule(rule)

# Các phần còn lại của tệp forward_chaining, fact, main, rule
# ...



