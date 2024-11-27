import ast
import astor
from anthropic import AnthropicBedrock


def generate_docstring(function_code):
    prompt = f"""
You are an expert in writing docstring for functions.

Generate docstring for the following functions:\n\n{function_code}.
The docstring should only mention following things:
- the functionality
- the arguments
- the response


Sample Format of Docstring:
    Description:
         Adds two numbers.
    Arguments:
        a (int or float): The first number.
        b (int or float): The second number.
    Response:
        int or float: The sum of the two numbers.

        
Note: Strictly follow the above the sample format, do not include any other explanation.

Instructions:
    - Do not mention anything regarding the programming language in docstring.
    - Do not include any code or part of the function code in the docstring
    - Strictly do not include any other thing in the docstring
    - Also keep it concise and well formatted.
"""

    google_prompt = f'''
For this Python function:

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        raise ZeroDivisionError("Cannot calculate the average of an empty list.")
    return total / count
```

The function docstring using Google style is:


"""
Calculate the average of a list of numbers.

Args:
    numbers (list): A list of numeric values.

Returns:
    float: The average of the input numbers.

Raises:
    ZeroDivisionError: If the input list is empty.
"""

For this Python function:

```python
{function_code}
```

The function docstring using Google style is:
'''

    numpy_prompt = f'''

Python Function: 
```
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        raise ZeroDivisionError("Cannot calculate the average of an empty list.")
    return total / count
```

DocString:
"""
Calculate the average of a list of numbers.

Parameters
----------
numbers : list
    A list of numeric values.

Returns
-------
float
    The average of the input numbers.

Raises
------
ZeroDivisionError
    If the input list is empty.
"""


Python Function:
```
{function_code}
```

DocString:

'''

    client = AnthropicBedrock(
        aws_access_key="",
        aws_secret_key="",
        aws_region="us-east-1",
    )

    response = client.messages.create(
        model="anthropic.claude-3-sonnet-20240229-v1:0",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt},{"role": "assistant", "content": "you help to find information"}]
    )
    return response.content[0].text.strip()


class DocstringGenerator(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        function_code = astor.to_source(node)
        docstring = generate_docstring(function_code)
        node.body.insert(0, ast.Expr(value=ast.Str(s=docstring)))
        return node


def add_docstrings_to_file(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())

    generator = DocstringGenerator()
    tree = generator.visit(tree)

    with open(file_path, 'w') as file:
        file.write(astor.to_source(tree))


# Example usage
add_docstrings_to_file('test_code_doc.py')
