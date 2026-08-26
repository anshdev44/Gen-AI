from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code ="""
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)

    if len(numbers) == 0:
        return 0

    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]

total = calculate_sum(numbers)
average = calculate_average(numbers)

print("Total:", total)
print("Average:", average),
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, 
    chunk_size=200,          
    chunk_overlap=200         
)

chunks=splitter.split_text(code)

for i,chunk in enumerate(chunks):
    print('chunk number->',i)
    print(chunk)
