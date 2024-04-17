# tasks-loader

The `tasks-loader` module is designed to simplify the process of managing and taking actions based on the rows of an input CSV file. 

![Banner](https://i.imgur.com/RwODhsn.jpeg)

This module enables quick and easy loading and adaptation of any CSV file based on the data management needs encountered in various projects. Whether automating task creation, performing data validation, or preprocessing information for further analysis, `tasks-loader` offers a robust foundation for working with CSV data in Python.


## Table of Contents
- [tasks-loader](#tasks-loader)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Key Features](#key-features)
  - [Task Format Dictionary](#task-format-dictionary)
  - [Examples](#examples)
    - [Example 1: Basic Task Loading](#example-1-basic-task-loading)
    - [Example 2: Advanced Validation with Regex and Lambda](#example-2-advanced-validation-with-regex-and-lambda)
    - [Example 3: Post-processing Data](#example-3-post-processing-data)
    - [Example 4: Ticket / Sneakers Bot-like Validation](#example-4-ticket--sneakers-bot-like-validation)
    - [Example 2: Advanced Validation with Regex and Lambda](#example-2-advanced-validation-with-regex-and-lambda-1)
    - [Example 5: Using Pre-Made Regex Checks with the Patterns Class](#example-5-using-pre-made-regex-checks-with-the-patterns-class)
    - [Example 6: File Check and Creation Handling](#example-6-file-check-and-creation-handling)
  - [Stay in touch with me](#stay-in-touch-with-me)

## Installation

To install `tasks-loader`, run the following command:
```bash
pip install tasks-loader
```

## Key Features

- **Dynamic Task Creation**: Automatically generates tasks from CSV rows, facilitating easy manipulation and processing.
- **Flexible Validation**: Supports extensive validation mechanisms including type checks, regex patterns, lambda functions, and predefined choices.
- **Customizable Default Values**: Enables specifying global or field-specific default values for handling missing or invalid data.
- **Post-processing Hooks**: Allows for data transformation after loading, such as converting units or normalizing strings.
- **Automatic Header Adjustment**: Converts CSV headers to lowercase and replaces spaces with underscores, simplifying attribute access in Python.
- **Iterability and Validation Checks**: Offers built-in support for task validity checks and iteration over tasks, streamlining application control flow.
- **Extensible Design**: Designed for easy extension to include more validation rules, data transformations, or export options.
- **Increasing Task ID**: No need to specify task IDs in the CSV file; the module automatically assigns incremental IDs to each task.

## Task Format Dictionary

The task format dictionary defines how each field in your CSV file is processed. Here’s what you need to know about constructing this dictionary:

- **type**: The expected Python type of the field (e.g., `str`, `int`).
- **required**: If set to `True`, the field must be present and not empty; otherwise, it's considered optional.
- **default**: A default value to use if the field is missing or fails validation.
- **choices**: A list of acceptable values for the field.
- **validation**: A regex pattern or a lambda function for additional validation criteria.
- **post_format**: A function to transform the field value after all other processing steps.

If a task is invalid (e.g., missing required fields, failed validation), it will not be included in the task list. The `global_default` argument in the `Tasks` constructor allows you to specify a fallback value for any field that is not explicitly handled by the task format.

## Examples

Below are examples demonstrating how to use `tasks-loader` with different configurations and CSV files.

### Example 1: Basic Task Loading

**CSV (`basic_tasks.csv`):**

```csv
Name,Email,Price
John Doe,johndoe@example.com,19.99
Jane Smith,,
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "email": {"type": str, "required": True, "default": "no-email@example.com"},
    "price": {"type": float, "required": False, "default": 9.99},
}
```

**Python Code:**

```python
from tasks_loader import Tasks

tasks = Tasks(input_file='basic_tasks.csv', task_format=task_format)

for task in tasks:
    print(task) 
    # Task is going to be a dict like
    # {'id': '001', 'name': 'John Doe', 'email': 'johndoe@example.com', 'price': 19.99}
```

### Example 2: Advanced Validation with Regex and Lambda

**CSV (`advanced_validation.csv`):**

```csv
Name,Email,Role
John Doe,johndoe@example.com,admin
Jane Smith,janesmith@bademail,visitor
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "email": {
        "type": str,
        "required": True,
        "validation": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    "role": {
        "type": str,
        "required": True,
        "choices": ["admin", "user", "guest"],
        "validation": lambda x: x in ["admin", "user", "guest"]
    },
}
```

**Python Code:**

```python
from tasks_loader import Tasks

tasks = Tasks(input_file='advanced_validation.csv', task_format=task_format)

for task in tasks:
    print(task)
```

### Example 3: Post-processing Data

**CSV (`post_processing.csv`):**

```csv
Name,DelaySeconds
John Doe,30
Jane Smith,45
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "delay_seconds": {
        "type": int,
        "required": True,
        "post_format": lambda x: x * 1000  # Convert seconds to milliseconds
    },
}
```

**Python Code:**

```python
from tasks_loader import Tasks

tasks = Tasks(input_file='post_processing.csv', task_format=task_format)

for task in tasks:
    print(task)
```

### Example 4: Ticket / Sneakers Bot-like Validation

This example demonstrates a setup tailored for automated tasks commonly used in ticket purchasing or sneaker bot scenarios. The configuration ensures all necessary information for a purchase is validated against specific criteria before proceeding with a task.

**CSV (`ticket_sneakers_bot.csv`):**

```csv
Name,Surname,Mail,URL,Min Price,Max Price,Error Delay, Monitor Delay,Credit Card Number,Credit Card Month,Credit Card Year,Credit Card CVV
John,Doe,johndoe@example.com,https://example.com,50,500,1000,5000,1234567890123456,01,2024,123
Jane,Smith,janesmith@example.com,https://invalid,0,,500,2000,1234567890123456,12,2023,456
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "delay_seconds": {
        "type": int,
        "required": True,
        "post_format": lambda x: x * 1000  # Convert seconds to milliseconds
    },
}
```

**Task Format:**
This setup includes several validation steps to ensure each field meets the requirements for automated purchasing tasks:
```python
import re

task_format = {
    "name": {"type": str, "required": True, "validation": lambda x: isinstance(x, str) and x.strip() != ""},
    "surname": {"type": str, "required": True, "validation": lambda x: isinstance(x, str) and x.strip() != ""},
    "mail": {
        "type": str,
        "required": True,
        "validation": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    "url": {
        "type": str,
        "required": True,
        "validation": r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9_./-]+)*$"
    },
    "min_price": {"type": float, "required": False, "default": 0},
    "max_price": {"type": float, "required": False, "default": 10000},
    "error_delay": {"type": int, "required": False, "post_format": lambda x: x // 1000},
    "monitor_delay": {"type": int, "required": False, "post_format": lambda x: x // 1000},
    "credit_card_number": {"type": str, "required": True, "validation": lambda x: len(x) == 16 and x.isdigit()},
    "credit_card_month": {"type": str, "required": True, "validation": r"^(0[1-9]|1[0-2])$"},
    "credit_card_year": {"type": str, "required": True, "validation": r"^\d{4}$"},
    "credit_card_cvv": {"type": str, "required": True, "validation": r"^\d{3}$"},
}
```

**Python Code:**

```python
from tasks_loader import Tasks

tasks = Tasks(input_file='ticket_sneakers_bot.csv', task_format=task_format)

for task in tasks:
    StartTask(**task) # Apply the dict of the task as kwargs
```


**Validation Explained:**

- **Name and Surname**: Must be valid strings that are not just whitespace.
- **Mail**: Uses a regex pattern to validate that the email address is in a proper format.
- **URL**: Validates URLs with a regex pattern to ensure they start with http or https and are generally formatted correctly.
- **Min and Max Price**: Validates that these are floats, with defaults of 0 and 10000 respectively if not specified or invalid.
- **Error and Monitor Delay**: These are expected to be integers representing milliseconds; they are post-processed to convert to seconds.
- **Credit Card Number**: Must be a 16-digit string.
- **Credit Card Month**: Validates with a regex pattern that the month is in MM format, allowing only values from 01 to 12.
- **Credit Card Year**: Must be a 4-digit year in YYYY format.
- **Credit Card CVV**: A 3-digit security code validated with a regex pattern.

This setup is an example of an automated module that initiates tasks based on the validated entries from a CSV file, ensuring each task has all the necessary and correctly formatted information before proceeding. This kind of validation is crucial in scenarios where precise and validated data is essential for the success of automated tasks, such as in ticket purchasing or sneaker bot operations.


### Example 2: Advanced Validation with Regex and Lambda

**CSV (`advanced_validation.csv`):**

```csv
Name,Email,Role
John Doe,johndoe@example.com,admin
Jane Smith,janesmith@bademail,visitor
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "email": {
        "type": str,
        "required": True,
        "validation": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    "role": {
        "type": str,
        "required": True,
        "choices": ["admin", "user", "guest"],
        "validation": lambda x: x in ["admin", "user", "guest"]
    },
}
```

**Python Code:**

```python
from tasks_loader import Tasks

tasks = Tasks(input_file='advanced_validation.csv', task_format=task_format)

for task in tasks:
    print(task)
```

### Example 5: Using Pre-Made Regex Checks with the Patterns Class

**CSV (`regex_validation.csv`):**

```csv
Name,Email,Phone,Month
John Doe,johndoe@example.com,+12345678901,January
Jane Smith,janesmith@bademail,+12345,Smarch
```

**Task Format:**

```python
task_format = {
    "name": {"type": str, "required": True},
    "email": {
        "type": str,
        "required": True,
        "validation": Patterns.MAIL
    },
    "phone": {
        "type": str,
        "required": True,
        "validation": Patterns.PHONE
    },
    "month": {
        "type": str,
        "required": True,
        "validation": Patterns.MONTH
    }
}
```

**Python Code:**

```python
from tasks_loader import Patterns

task_format = {
    "name": {"type": str, "required": True},
    "email": {
        "type": str,
        "required": True,
        "validation": Patterns.MAIL
    },
    "phone": {
        "type": str,
        "required": True,
        "validation": Patterns.PHONE
    },
    "month": {
        "type": str,
        "required": True,
        "validation": Patterns.MONTH
    }
}
```

### Example 6: File Check and Creation Handling

If the specified CSV file does not exist, ty can createa new one by calling the function `create_file` with the appropriate headers based on the `task_format` to ensure data consistency.

**Python Code:**

```python
from tasks_loader import Tasks

# Define the CSV file and format
tasks = Tasks(input_file='new_tasks.csv', task_format=task_format)

if tasks.create_file():
    print("File created, please fill it and then restart the script")
    exit(0)
print("File aready created")
```


## Stay in touch with me

For any inquiries or further information, please reach out:

- [GitHub](https://github.com/glizzykingdreko)
- [Twitter](https://mobile.twitter.com/glizzykingdreko)
- [Medium](https://medium.com/@glizzykingdreko)
- [Email](mailto:glizzykingdreko@protonmail.com) 
- [Website](https://glizzykingdreko.github.io)
- [Buy me a coffee ❤️](https://www.buymeacoffee.com/glizzykingdreko)
- Antibot bypass solutions needed? [TakionAPI](https://takionapi.tech/discord)

Feel free to contact for collaborations, questions, or feedback any of my projects.