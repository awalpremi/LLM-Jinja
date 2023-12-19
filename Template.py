#%%
from jinja2 import Environment, FileSystemLoader
import ast
import os
from typing import Dict, Any, List

def read_jinja_template(filepath: str, variables: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Reads a Jinja template file, renders it with the given variables, and returns the result as a list.

    Args:
        filepath (str): The path to the Jinja template file.
        variables (dict): The variables to be used for rendering the template.

    Returns:
        list: The rendered template as a list.
    """
    env = Environment(loader=FileSystemLoader('/'))
    template = env.get_template(filepath)
    rendered_template = template.render(variables)
    template_list = ast.literal_eval(rendered_template)
    return template_list

data_vars: Dict[str, Any] = {'name': 'John Doe', 'age': 18}

template_filename: str = 'Template.jinja'
template_filepath: str = os.path.join(os.path.dirname(__file__), template_filename)
template_list: List[Dict[str, Any]] = read_jinja_template(template_filepath, data_vars)

test_case: List[Dict[str, Any]] = [{'role': 'system', 'content': f'You are a helpful assistant to a {data_vars["age"]} y/o person.'}, {'role': 'user', 'content': f'Hello, {data_vars["name"]}!'}]
assert template_list == test_case, "Template list does not match test case"
print(f'{template_list} is a type {type(template_list)}')

print('Add it to any LLM that uses chatLM format like OpenAI api')
# %%
