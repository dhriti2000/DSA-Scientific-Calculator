Ultimate DSA Scientific Calculator

A Python-based scientific calculator built using Sympy and Numpy.
It can handle both symbolic and numeric computations and is designed
to simulate real-world DSA-style problem solving in a terminal.

Features:
- Symbolic math like integration, differentiation, solving equations
- Differential equation solving (dsolve)
- Number theory operations (gcd, primes)
- Variable assignments (x = 5)
- Advanced math functions like zeta, gamma
- Works directly in terminal without any UI

Tech Used:
Python 3.9+
Sympy
Numpy

Installation:
git clone https://github.com/<your-username>/Ultimate-DSA-Scientific-Calculator.git
cd Ultimate-DSA-Scientific-Calculator
pip install -r requirements.txt
python scientific_calculator.py

Example Usage:
>> sym:solve(x+y-1, x-y-1, x, y)
→ {x: 1, y: 0}

>> x = pi
Assigned x = 3.141593

>> sym:zeta(2)
→ pi**2/6

>> sym:dsolve(Derivative(y(x), x) - y(x), y(x))
→ Eq(y(x), C1*exp(x))

Future Improvements:
Matrix operations (add, inverse, determinant)
Plotting support using matplotlib
Command history and file saving

Author:
Dhriti Ojha
