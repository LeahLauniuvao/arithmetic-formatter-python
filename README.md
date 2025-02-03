# Arithmetic Formatter 🧮 
A simple Python script that formats arithmetic problems into a structured layout.

## Features
- Accepts up to **five** arithmetic problems as input.  
- Supports **addition (+) and subtraction (-)** only.  
- Formats problems with correct spacing and alignment.  
- Optionally **displays answers** when requested.  

---

## Example Output 🖥️  
This script takes arithmetic problems as input and arranges them neatly.

### ✅ Python Code:
```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
---
### ✅ Expected Output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172

## How to Run the Script 🚀  
Clone the repository, navigate to the directory, and run the script.

```bash
# Clone the repository
git clone https://github.com/LeahLauniuvao/arithmetic-formatter-python.git

# Navigate to the directory
cd arithmetic-formatter-python

# Run the script
python arithmetic_arranger.py

## 🔬 Unit Testing (Optional but Recommended)
To test the script, run:
```bash
python test_arithmetic_arranger.py

## 🚀 Future Enhancements  
- Add support for **multiplication and division**.  
- Implement a **command-line interface (CLI)** for interactive input.  
- Create a **GUI version using Tkinter**.  
