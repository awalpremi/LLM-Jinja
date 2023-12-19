# Using Jinja for LLM prompt templating

This project consists of a Python script that uses the Jinja2 library to render a template file with a set of variables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Jinja2 package. Pip or Conda as you like.

### Installing

Clone the repository to your local machine.
```bash
git clone https://github.com/awalpremi/LLM-Jinja.git
```

### Usage

Here's an example of how to use the script:

Put any text in the jinja template with variables in {{}}

```jinja
[
    {"role": "system", "content": "You are a helpful assistant to a {{age}} y/o person."},
    {"role": "user", "content": "Hello, {{name}}!"}
]
```
Load the template in python and populate it with data.

```python
template_filename: str = 'Template.jinja'
template_filepath: str = os.path.join(os.path.dirname(__file__), template_filename)
template_list: List[Dict[str, Any]] = read_jinja_template(template_filepath, data_vars)
```

In this example, the Template.jinja file is rendered with the variables {'name': 'John Doe', 'age': 18}, and the result is stored in template_list.

