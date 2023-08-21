

# Phương thức KnowledgeBase.declare xử lý các câu từ tệp đầu vào và điền vào cơ sở tri thức các sự kiện và quy tắc.
# Đối với mỗi query trong tệp truy vấn, hàm main truy xuất đối tượng Fact tương ứng đại diện cho truy vấn. 
# Hàm forward_chaining được gọi với truy vấn làm đầu vào và nó trả về một tập hợp các dữ kiện (sự thay thế) đáp ứng truy vấn. 
# Những kết quả này sau đó được định dạng và ghi vào output.

from KnowledgeBase import KnowledgeBase
from fact import Fact

def main():
    # đọc các input chứa dữ kiện kiến thức, truy vấn và output path mong muốn.
    input_file = 'BritishRoyalFamily.pl'
    query_file = 'queries.txt'
    output_file = 'answers.txt'

    kb = KnowledgeBase()
    with open(input_file, 'r') as f_input:
        sentences = f_input.readlines()
        KnowledgeBase.populate(kb, sentences)

    print('Initialized knowledge base from {}.'.format(input_file))
    # for fact in kb.facts:
    #     print(fact)


    with open(query_file, 'r') as f_query:
        with open(output_file, 'w') as f_output:
            for query_str in f_query.readlines():
                alpha = Fact.parse_fact(query_str)
                alpha_str = str(alpha)
                substitutions = set(kb.query(alpha))
                print(alpha_str)
                
                print(substitutions)
                print()
                # subst_str = ' ;\n'.join([str(subst) for subst in substitutions]) + '.\n'
                # print(subst_str)
                # f_output.write(alpha_str + '\n')
                # f_output.write(subst_str + '\n')

    print('Query results from {} written to {}.'.format(query_file, output_file))

if __name__ == "__main__":
    main()




