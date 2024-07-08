# Flask Math Operations

A simple Python Flask application to perform basic mathematical operations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Perform basic mathematical operations (addition, subtraction, multiplication, division).
- Simple RESTful API using Flask.
- JSON responses for calculation results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-math-operations.git
   ```

2. Navigate into the project directory:

   ```bash
   cd flask-math-operations
   ```

3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. The server will start running at `http://localhost:5000`.

## Endpoints

- **GET /add/<int:a>/<int:b>**  
  Adds two integers `a` and `b`.

- **GET /subtract/<int:a>/<int:b>**  
  Subtracts integer `b` from integer `a`.

- **GET /multiply/<int:a>/<int:b>**  
  Multiplies two integers `a` and `b`.

- **GET /divide/<int:a>/<int:b>**  
  Divides integer `a` by integer `b`. Returns a JSON object with the result.

## Examples

- To add 5 and 3:
  ```
  GET http://localhost:5000/add/5/3
  Response: {"result": 8}
  ```

- To subtract 7 from 10:
  ```
  GET http://localhost:5000/subtract/10/7
  Response: {"result": 3}
  ```

- To multiply 4 and 6:
  ```
  GET http://localhost:5000/multiply/4/6
  Response: {"result": 24}
  ```

- To divide 10 by 2:
  ```
  GET http://localhost:5000/divide/10/2
  Response: {"result": 5.0}
  ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your suggested changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
