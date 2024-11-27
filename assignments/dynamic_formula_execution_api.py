"""
Hackathon

Problem Statement


In the fast-evolving landscape of data-driven applications, the ability to dynamically process and analyze complex datasets is paramount. This Hackathon challenges participants to develop a Python-based Web API capable of interpreting and executing mathematical expressions on datasets containing diverse data types such as numbers, strings, booleans, dates, and currencies. The API should also handle formula chaining, where the output of one mathematical expression serves as the input for another.

Your Solution
Develop a 'Dynamic Formula Execution API' that:

1. Accepts JSON payloads containing structured data along with a series of mathematical expressions.

2. Validates each expression to ensure it is mathematically correct and executes it dynamically on the provided data.

3. Supports formula chaining by allowing the output from one expression to be used in subsequent expressions.

4. Outputs the calculated results as an HTTP response.



The API should be capable of performing arithmetic and logical operations efficiently across various data types.


Technical Requirements
--------------------------

API Compliance: Ensure the solution adheres to the provided API contract, which includes:

Endpoint URL: `/api/execute-formula`

JSON Schema and Examples: 
Each formula must declare its required inputs, specifying variable names and types to ensure correct execution and data handling. There can be any number of input variables in the data set.

Formula Validation: 
Implement a robust mechanism to validate that each submitted expression is a valid mathematical expression. This includes syntax checks and verification of operation feasibility based on the provided inputs. The formula expression should have variable literals defined in the inputs and which are present in the data. If it doesn’t the formula should raise an error.

Formula Chaining: A formula can take input from another formula’s output and this can be a chain. The API needs to validate that this chain isn’t broken. The order of execution of each formula needs to be arrived at based on this dependency chain.

Data Types: The formulas should support numeric types, percentages, boolean, datetime and currency. Currencies can be mentioned in ISO format or with the currency symbol e.g. USD 100, 100 USD, $ 100, $100, $100,000 etc.

Formula Expression: Expressions should support all mathematical operators, and formula evaluation should honor BODMAS rule.

Performance Requirements
------------------------

Response Time: The API must maintain sub-second response times for all operations, even under high load.
Infinite Loop Detection: Implement mechanisms to detect potential infinite loops or excessively complex computation chains and abort them within sub-second.


Evaluation Criteria
-------------------

Functional Correctness: The solution must meet all functional requirements as outlined in the technical specifications.

Performance: The API must handle requests efficiently under varying loads.

Algorithm Efficiency: Optimization of the expression parsing and execution algorithms for speed and minimal resource usage.

Coding Standards: Adherence to best practices in coding, ensuring clarity, maintainability, and use of appropriate design patterns.

Design Patterns: Effective use of design patterns suitable for API development and real-time data processing.

Test Case Writing: Write suitable test cases covering maximum possible cases for your API.


Samples
-------


1. Simple Addition

Request 1:

{
  "data": [
    {
      "id": 1,
      "fieldA": 10
    },
    {
      "id": 2,
      "fieldA": 20
    }
  ],
  "formulas": [
    {
      "outputVar": "result",
      "expression": "fieldA + 10",
      "inputs": [
        {
          "varName": "fieldA",
          "varType": "number"
        }
      ]
    }
  ]
}

Expected response:

Request body:

{
  "results": {
    "result": [
      20,
      30
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully."
}

----------------------------------------------------------

2. Formula Chaining
Request body:

{
  "data": [
    {
      "id": 1,
      "fieldA": 10,
      "fieldB": 2
    },
    {
      "id": 2,
      "fieldA": 20,
      "fieldB": 3
    }
  ],
  "formulas": [
    {
      "outputVar": "sumResult",
      "expression": "fieldA + fieldB",
      "inputs": [
        {
          "varName": "fieldA",
          "varType": "number"
        },
        {
          "varName": "fieldB",
          "varType": "number"
        }
      ]
    },
    {
      "outputVar": "finalResult",
      "expression": "sumResult * 2 + fieldA",
      "inputs": [
        {
          "varName": "sumResult",
          "varType": "number"
        },
        {
          "varName": "fieldA",
          "varType": "number"
        }
      ]
    }
  ]
}
Expected response:

{
  "results": {
    "sumResult": [
      12,
      23
    ],
    "finalResult": [
      32,
      63
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully with variable-based chaining."
}

----------------------------------------

3. Sales Revenue
Suppose a dataset contains sales data for multiple products, including unit prices and quantities sold. Users might want to calculate the total sales revenue for a product, adjusting for a discount percentage that varies per item.



Request body:

{
  "data": [
    {
      "id": 1,
      "product": "Laptop",
      "unitPrice": "1000 USD",
      "quantity": 5,
      "discount": "10%"
    },
    {
      "id": 2,
      "product": "Smartphone",
      "unitPrice": "500 USD",
      "quantity": 10,
      "discount": "5%"
    },
    {
      "id": 3,
      "product": "Tablet",
      "unitPrice": "300 USD",
      "quantity": 15,
      "discount": "0%"
    }
  ],
  "formulas": [
    {
      "outputVar": "revenue",
      "expression": "((unitPrice * quantity) - (unitPrice * quantity * (discount / 100)))",
      "inputs": [
        {
          "varName": "unitPrice",
          "varType": "currency"
        },
        {
          "varName": "quantity",
          "varType": "number"
        },
        {
          "varName": "discount",
          "varType": "percentage"
        }
      ]
    }
  ]
}


Expected response:

{
  "results": {
    "revenue": [
      4500,
      4750,
      4500
    ]
  },
  "status": "success",
  "message": "The formulas were executed successfully."
}
"""