# Lesson 1: What is Python and How Do You Run It?

---

## Learning Objective

By the end of this lesson, you will be able to install Python, create your first `.py` file, run it successfully, and recognize the entry point structure used in our thermodynamics simulation script.

---

## 1. What is Python?

Python is a **programming language** — a way of giving instructions to a computer in a format that is close to plain English.

When you write Python, you are writing a set of instructions in a text file. The computer then reads those instructions and executes them one line at a time, from top to bottom.

Here is what makes Python a good first language:

- It reads almost like English sentences
- One line of Python often replaces ten lines in older languages
- It has a massive library of ready-made tools for science, math, and graphics — which is exactly why our thermodynamics simulation uses it
- It is free and runs on Windows, macOS, and Linux

> **What Python is not:** Python is not an app you click on. It is not a website builder by itself. It is a general-purpose tool, like a Swiss Army knife for computation.

---

## 2. Installing Python — Use Anaconda

There are several ways to install Python. For this course, **Anaconda** is strongly recommended.

**Why Anaconda?**

Our script uses three external libraries:

- `numpy` — for fast math and arrays
- `matplotlib` — for plots and interactive graphics

Installing these manually can be frustrating for beginners. Anaconda installs Python _and_ hundreds of scientific libraries all at once, in a single installer. You will not need to install numpy or matplotlib separately.

### Installation Steps

**Step 1.** Go to [https://www.anaconda.com/download](https://www.anaconda.com/download)

**Step 2.** Download the installer for your operating system (Windows, macOS, or Linux).

**Step 3.** Run the installer. Accept all default settings. This may take 5–10 minutes.

**Step 4.** When finished, open the program called **Anaconda Navigator** from your Start Menu (Windows) or Applications folder (macOS).

You will see a screen that looks like a launchpad with several tools. You have successfully installed Python.

> **Confirmed fact:** Anaconda is a distribution maintained by Anaconda, Inc. The free Individual Edition includes Python, numpy, matplotlib, and the Spyder and VS Code editors. You do not need to pay for anything in this course.

---

## 3. Choosing Where to Write Code — Your IDE

An **IDE** stands for **Integrated Development Environment**. It is a text editor built specifically for writing code. It colors your code to make it readable, shows you errors before you run anything, and gives you a place to run your script.

Two good options for beginners:

### Option A — VS Code (Recommended)

Visual Studio Code is a free editor made by Microsoft. It is available directly from Anaconda Navigator. It is fast, widely used, and has excellent Python support.

### Option B — Thonny

Thonny is a simpler editor designed specifically for Python beginners. If VS Code feels overwhelming at first, start with Thonny. Download it free at [https://thonny.org](https://thonny.org/).

### Option C — Spyder (also comes with Anaconda)

Spyder is a scientific Python editor similar to MATLAB's layout. It comes pre-installed with Anaconda and works well for our simulation.

> **For this course**, any of the three will work. The code you write is identical regardless of which editor you choose. The editor is just the tool you use to write and run it.

---

## 4. What is a `.py` File?

A `.py` file is simply a **plain text file** that contains Python code and has the file extension `.py`.

There is nothing magical about it. You could write Python code in Notepad and save it as `my_script.py` and it would work.

When you run a `.py` file, Python reads it from the very first line to the very last line and executes each instruction in order.

---

## 5. Your First Python Script — Hello World

This is the tradition in programming: the first program you write in any language prints the words "Hello, World!" to the screen. It confirms that everything is installed and working.

### Step-by-step:

**Step 1.** Open your IDE (VS Code, Thonny, or Spyder).

**Step 2.** Create a new file. In VS Code: `File → New File`. Save it immediately as `hello.py`.

**Step 3.** Type this code exactly:

```python
# This is a comment. Python ignores any line that starts with #.
# Comments are notes you write for yourself and other humans.

print("Hello, World!")
```

**Step 4.** Run the file.

- In **VS Code**: Click the triangle ▶ button in the top right, or press `Ctrl+F5`
- In **Thonny**: Press the green ▶ button or press `F5`
- In **Spyder**: Press `F5`

**Step 5.** Look at the output panel at the bottom. You should see:

```
Hello, World!
```

If you see that, Python is installed and working correctly.

---

### What each part means:

```python
# This is a comment. Python ignores any line that starts with #.
```

The `#` symbol tells Python: _ignore this line entirely_. Comments exist only for human readers. They do not affect what the program does. You will use comments constantly to explain your code.

```python
print("Hello, World!")
```

`print()` is a **function** — a built-in command that tells Python to display something on the screen. The text inside the quotation marks is what gets displayed. The parentheses `()` are how you pass information into a function.

---

## 6. Running a Script from the Terminal

Your IDE handles running scripts automatically, but it helps to understand what is happening underneath. When you click ▶, the IDE is quietly running this command in a terminal:

```
python hello.py
```

You can do this yourself:

**Step 1.** Open a terminal.

- Windows: Search for **Anaconda Prompt** in the Start Menu (use this instead of regular Command Prompt when using Anaconda)
- macOS/Linux: Open **Terminal**

**Step 2.** Navigate to the folder where your `hello.py` file is saved. Use the `cd` command (which stands for "change directory"):

```bash
cd Desktop
```

**Step 3.** Run your script:

```bash
python hello.py
```

You will see:

```
Hello, World!
```

This is exactly what your IDE does when you press ▶. The IDE is a convenience layer on top of this process.

---

## 7. How This Connects to Our Script

Open the thermodynamics simulation script and scroll to the very bottom. You will find this:

```python
# ---- BOTTOM OF THE SCRIPT ----

def main():
    """Main function to run the interactive simulation."""
    print("=" * 70)
    print("IRREVERSIBLE HEAT TRANSFER SIMULATION")
    print("=" * 70)
    print("\nEducational Model: Heat Conduction Between Thermal Reservoirs")
    # ... more print statements ...
    
    visualizer = InteractiveVisualizer()
    visualizer.show()


if __name__ == "__main__":
    main()
```

There are two things here that now make sense to you:

---

### The `print()` calls inside `main()`

```python
print("=" * 70)
print("IRREVERSIBLE HEAT TRANSFER SIMULATION")
```

This is the exact same `print()` function you used in Hello World. When you run the simulation, before any window opens, Python prints a summary of the program to the terminal. The `"=" * 70` is Python's way of printing the `=` character 70 times in a row to create a visual divider line.

---

### The `if __name__ == "__main__":` block

```python
if __name__ == "__main__":
    main()
```

This is one of Python's most common conventions, and it looks confusing at first. Here is what it means in plain English:

> _"If this file is being run directly by the user — not imported by another file — then execute the_ `main()` _function."_

**Why does this matter?**

Python files can be used in two ways:

1. **Run directly** — you click ▶ or type `python simulation.py` in the terminal
2. **Imported** — another Python file borrows code from this file using the `import` keyword

When Python runs a file directly, it sets a special internal variable called `__name__` to the string `"__main__"`. When a file is _imported_ by another file, `__name__` is set to the file's name instead.

The `if __name__ == "__main__":` check lets the file behave differently depending on how it is being used. If you are running it directly, it launches the simulation. If someone imports it to reuse a class or function, the simulation does not launch automatically.

**For now, the practical takeaway is this:** the last two lines of the script are the _starting point_ of the entire program. Everything begins there.

```python
if __name__ == "__main__":   # "Are we running this file directly?"
    main()                   # "If yes, start the program."
```

---

## Practice Exercise

Complete all three tasks below before moving to Lesson 2.

**Task 1.** Create a new file called `practice1.py`. Make it print your name and your city on two separate lines. Example output:

```
Maria
Manila
```

**Task 2.** Add a comment above each print statement explaining what it does.

**Task 3.** At the bottom of `practice1.py`, add this block exactly as written and confirm it still works:

```python
def main():
    print("My name is Maria")
    print("My city is Manila")

if __name__ == "__main__":
    main()
```

Move your print statements inside the `main()` function. Run it. The output should be identical to before.

> **Note:** Make sure your print statements inside `main()` are indented with 4 spaces. Python uses indentation to know which lines belong inside a function. If you get an `IndentationError`, check your spacing. Lesson 7 covers functions in full detail.

---

## Key Takeaways

- Python is a free, general-purpose programming language that reads like plain English and runs instructions from top to bottom.
- Anaconda is the recommended installer for beginners because it includes Python, numpy, and matplotlib in one package.
- A `.py` file is a plain text file containing Python instructions. Your IDE is simply a convenient tool for writing and running these files.
- `print()` is a built-in function that displays text in the terminal. It is used throughout our simulation script to show startup information.
- The `if __name__ == "__main__": main()` pattern at the bottom of a script is the conventional entry point — it is where execution begins when you run the file directly.

---

# Lesson 2: Variables, Numbers, and Basic Math in Python

---

## 1. Plain-English Concept Explanation

Imagine you're a scientist about to run an experiment. Before you start, you write down your starting values on a notepad: the temperature of your hot reservoir, the mass of the material, the time step for your measurements. In Python, **variables** are that notepad.

A **variable** is simply a named container that holds a value. You give it a name, you store a value in it, and you can use or change that value later.

---

### The Two Types of Numbers You'll Use

Python has two main number types relevant to this script:

**Integer (`int`)** — A whole number. No decimal point.

```
5, 100, -3, 2000
```

**Float (`float`)** — A number _with_ a decimal point. Used when you need precision.

```
3.14, 400.0, 0.1, -273.15
```

> 💡 In science and engineering, you'll almost always use **floats**, because temperatures, masses, and rates are rarely perfectly whole numbers.

---

### Assigning a Variable

The `=` sign in Python does **not** mean "equals" the way it does in math. It means **"store this value in this name."**

```python
temperature = 400.0   # Store the number 400.0 in a variable called "temperature"
```

You can read this as: _"temperature gets the value 400.0"_

---

### Arithmetic Operators

|Symbol|Operation|Example|Result|
|---|---|---|---|
|`+`|Addition|`300 + 100`|`400`|
|`-`|Subtraction|`400 - 300`|`100`|
|`*`|Multiplication|`2.0 * 1000`|`2000.0`|
|`/`|Division|`800 / 2`|`400.0`|
|`**`|Exponentiation|`2 ** 3`|`8`|

> 💡 Notice that dividing two integers with `/` in Python 3 **always produces a float**. So `800 / 2` gives `400.0`, not `400`.

---

### Naming Conventions

Python variable names follow a style called **snake_case**: all lowercase letters, with underscores between words. This is the standard convention in Python.

```python
t_hot_initial = 400.0    # ✅ Good: snake_case, descriptive
ThotInitial = 400.0      # ⚠️  Works, but not standard Python style
x = 400.0                # ⚠️  Works, but tells you nothing about what it stores
```

Rules you **must** follow (your code will break if you don't):

- Names cannot start with a number (`1temp` is invalid)
- Names cannot contain spaces (`t hot` is invalid)
- Names are case-sensitive (`T_hot` and `t_hot` are two different variables)

---

## 2. Annotated Code Examples

```python
# --- Integers ---
mass_hot = 1          # An integer: whole number, no decimal
n_steps = 2000        # Another integer: used for counting steps

# --- Floats ---
T_hot_initial = 400.0   # A float: temperature in Kelvin
T_cold_initial = 300.0  # A float: another temperature
c_p = 1000.0            # A float: specific heat capacity in J/(kg·K)
dt = 0.1                # A float: a small time step in seconds

# --- Basic arithmetic ---
T_difference = T_hot_initial - T_cold_initial  # 400.0 - 300.0 = 100.0
energy = mass_hot * c_p * T_hot_initial        # 1 * 1000.0 * 400.0 = 400000.0

# --- Division always returns a float in Python 3 ---
T_average = (T_hot_initial + T_cold_initial) / 2   # (400.0 + 300.0) / 2 = 350.0

# --- You can update a variable by reassigning it ---
T_hot_initial = 450.0   # The old value (400.0) is gone; now it holds 450.0
```

---

### The Equilibrium Temperature Formula

In our script, the final temperature that both reservoirs will reach is calculated like this:

$$T_{eq} = \frac{m_{hot} \cdot c_p \cdot T_{hot} + m_{cold} \cdot c_p \cdot T_{cold}}{m_{hot} \cdot c_p + m_{cold} \cdot c_p}$$

Here's that same formula written in Python, broken down line by line:

```python
# Define our starting values
m_hot = 1.0       # Mass of the hot reservoir in kilograms
m_cold = 1.0      # Mass of the cold reservoir in kilograms
c_p = 1000.0      # Specific heat capacity in J/(kg·K) — same for both reservoirs
T_hot = 400.0     # Starting temperature of hot reservoir in Kelvin
T_cold = 300.0    # Starting temperature of cold reservoir in Kelvin

# Step 1: Calculate the numerator (top of the fraction)
# This is the total thermal energy in the system
numerator = m_hot * c_p * T_hot + m_cold * c_p * T_cold
# = 1.0 * 1000.0 * 400.0  +  1.0 * 1000.0 * 300.0
# = 400000.0 + 300000.0
# = 700000.0

# Step 2: Calculate the denominator (bottom of the fraction)
# This is the total heat capacity of the system
denominator = m_hot * c_p + m_cold * c_p
# = 1.0 * 1000.0  +  1.0 * 1000.0
# = 1000.0 + 1000.0
# = 2000.0

# Step 3: Divide to get the equilibrium temperature
T_eq = numerator / denominator
# = 700000.0 / 2000.0
# = 350.0  ← the temperature both reservoirs will eventually reach
```

> 💡 When both masses are equal, the equilibrium temperature is exactly the average of the two starting temperatures. Try changing `m_hot` to `2.0` and see how the result shifts.

---

## 3. How This Connects to Our Script

These aren't abstract examples — they appear almost word-for-word in the simulation.

### In `__init__()` (the setup section of the simulation):

```python
# From the script — these are the starting values for the simulation
T_hot_initial = 400    # integer here, but treated as a number throughout
T_cold_initial = 300   # initial temperature of the cold reservoir
mass_hot = 1.0         # mass in kg
mass_cold = 1.0        # mass in kg
c_p = 1000             # specific heat capacity in J/(kg·K)

self.h = 50            # heat transfer coefficient in W/K
                       # "self." means this variable belongs to the simulation object
                       # (you'll learn about "self" in a later lesson on classes)

self.dt = 0.1          # time step: how many seconds pass between each calculation
```

### In `_calculate_equilibrium_temp()`:

```python
def _calculate_equilibrium_temp(self):
    # This is exactly the formula we walked through above
    numerator = self.m_hot * self.c_p * self.T_hot_0 + self.m_cold * self.c_p * self.T_cold_0
    denominator = self.m_hot * self.c_p + self.m_cold * self.c_p
    return numerator / denominator   # Returns the result of the division
```

Every variable in this method — `m_hot`, `c_p`, `T_hot_0` — was assigned back in `__init__()`. The formula is just arithmetic on those stored values.

---

## 4. Practice Exercise

**Goal:** Recreate the equilibrium temperature calculation yourself, then experiment with it.

Open a Python environment (IDLE, VS Code, or an online tool like [python.org/shell](https://www.python.org/shell/)) and type the following:

```python
# Step 1: Assign the starting values
m_hot = 1.0
m_cold = 1.0
c_p = 1000.0
T_hot = 400.0
T_cold = 300.0

# Step 2: Calculate equilibrium temperature
numerator = m_hot * c_p * T_hot + m_cold * c_p * T_cold
denominator = m_hot * c_p + m_cold * c_p
T_eq = numerator / denominator

# Step 3: Print the result
print(T_eq)   # You should see: 350.0
```

**Then try these small changes and observe what happens:**

1. Change `m_hot` to `2.0` — does the equilibrium temperature shift toward hot or cold?
2. Change `T_hot` to `500.0` — how does that affect `T_eq`?
3. What happens if `T_hot` and `T_cold` are the same value?

> ✅ There are no wrong answers here — the goal is to build intuition for how the variables interact.

---

## 5. Key Takeaways

- A **variable** is a named container for a value. You create one using `=`, which means _assignment_, not mathematical equality.
- Python uses two number types here: **integers** (`int`) for whole numbers and **floats** (`float`) for decimals. Physics calculations almost always need floats.
- Python's **arithmetic operators** (`+`, `-`, `*`, `/`, `**`) work as expected, and division with `/` always returns a float.
- Python variable names use **snake_case** by convention, are case-sensitive, and cannot start with a number or contain spaces.
- Every named value in our simulation — `T_hot_initial`, `c_p`, `self.dt`, `self.h` — is just a variable storing a number that the simulation's math will use later.

---

# Lesson 3: Strings, Print Statements, and Code Comments

---

## 1. Plain-English Concept Explanation

### What is a String?

A **string** is simply text. In Python, any time you want to work with words, sentences, or characters, you wrap them in quotes. Python then treats everything inside those quotes as text data — not as code to run.

You can use either single quotes `'like this'` or double quotes `"like this"`. Both work the same way. The only rule is that you must open and close with the _same_ type of quote.

---

### What is `print()`?

`print()` is a built-in **function** (a reusable action Python knows how to do) that displays text in your terminal — the black window where Python runs. Whatever you put inside the parentheses gets shown on screen.

Think of it like asking Python: _"Say this out loud."_

---

### What is an f-string?

An **f-string** (short for _formatted string_) is a special kind of string that lets you embed a variable's value directly inside your text. You write the letter `f` right before the opening quote, then use curly braces `{}` to insert a variable anywhere in the text.

This is incredibly useful when you want to display a label like `"Temperature: 400.0 K"` where the number comes from your program, not from you typing it manually.

---

### What is a Comment?

A **comment** is a note you write inside your code _for humans to read_ — Python completely ignores it. You create a comment by starting a line with the `#` symbol. Everything after `#` on that line is skipped by Python.

Comments are how you explain _why_ your code does something, which becomes essential when your programs get longer.

---

## 2. Annotated Code Examples

### Basic Strings and `print()`

```python
# This is a comment — Python ignores this line entirely

# A string stored in a variable called greeting
greeting = "Hello, welcome to thermodynamics!"

# print() displays the string in the terminal
print(greeting)
# Output: Hello, welcome to thermodynamics!

# You can also print text directly, without storing it first
print("Heat flows from hot to cold.")
# Output: Heat flows from hot to cold.

# Printing multiple things separated by a comma adds a space between them
print("Temperature:", 400)
# Output: Temperature: 400
```

---

### The `=` Sign (a Quick Clarification)

The `=` sign in Python does **not** mean "equals" the way it does in math. It means **"store this value in this variable."** So `greeting = "Hello"` means: _create a box called `greeting` and put the text `"Hello"` inside it._

---

### f-strings

```python
# A variable holding a number
temperature = 400.0

# An f-string lets you insert that variable's value into your text
# Notice the f before the opening quote, and {} around the variable name
label = f"Current temperature: {temperature} K"

print(label)
# Output: Current temperature: 400.0 K

# You can also control how many decimal places are shown
# :.1f means "show 1 digit after the decimal point"
print(f"Temperature: {temperature:.1f} K")
# Output: Temperature: 400.0 K

# :.2f means "show 2 digits after the decimal point"
print(f"Temperature: {temperature:.2f} K")
# Output: Temperature: 400.00 K
```

---

### The `\n` Newline Character

Inside a string, `\n` is a special code that means _"start a new line here."_ It is not displayed literally — it acts as an invisible line break.

```python
# \n creates a line break inside a single string
print("HOT\n400.0 K")
# Output:
# HOT
# 400.0 K
```

---

### The `*` Trick with `print()`

You can repeat a string by multiplying it with a number using `*`.

```python
# "=" repeated 70 times, then printed
print("=" * 70)
# Output: ======================================================================
```

---

## 3. How This Connects to Our Script

### The `main()` Function's Print Statements

Near the bottom of the script, the `main()` function prints a welcome message to the terminal when you run the program. Every technique from this lesson appears there directly:

```python
def main():
    # "=" * 70 repeats the "=" character 70 times — a visual divider
    print("=" * 70)

    # A plain string printed directly
    print("IRREVERSIBLE HEAT TRANSFER SIMULATION")

    print("=" * 70)

    # \n at the start adds a blank line before the text
    print("\nEducational Model: Heat Conduction Between Thermal Reservoirs")

    # The bullet point lines are all plain strings
    print("  • Heat flows spontaneously from hot to cold")
```

Every `print()` call here uses a plain string. No variables needed — the labels are fixed text that never changes.

---

### f-strings in Plot Labels and Visual Annotations

The simulation's visual display uses f-strings heavily because the text _does_ change — it reflects live temperature values calculated by the program:

```python
# T_h is a variable holding the hot reservoir's current temperature
# :.1f formats it to 1 decimal place
# \n inserts a line break between "HOT" and the temperature number
self.ax_visual.text(2, 2.7, f'HOT\n{T_h:.1f} K', ...)
```

So if `T_h` is currently `387.3`, this displays:

```
HOT
387.3 K
```

And this one shows the equilibrium temperature:

```python
# T_eq is calculated by the simulation — it changes with slider settings
self.ax_visual.text(5, 0.3, f'Equilibrium: {self.sim.T_eq:.1f} K', ...)
```

Without f-strings, you would have no clean way to insert a calculated number into a text label.

---

## 4. Practice Exercise

Try this in a new Python file. It should take under 10 minutes.

**Task:** Write a short program that:

1. Stores a hot temperature of `400` and a cold temperature of `300` in two variables
2. Prints a divider line made of `-` repeated 40 times
3. Prints a title: `TEMPERATURE REPORT`
4. Prints the hot temperature using an f-string, formatted to 1 decimal place
5. Prints the cold temperature using an f-string, formatted to 1 decimal place
6. Prints the divider again

**Expected output:**

```
----------------------------------------
TEMPERATURE REPORT
Hot Reservoir:  400.0 K
Cold Reservoir: 300.0 K
----------------------------------------
```

**Starter hint:**

```python
T_hot = 400
T_cold = 300

print("-" * 40)
# your code continues here...
```

---

## 5. Key Takeaways

- A **string** is text data in Python, always wrapped in single or double quotes. Python stores and displays it exactly as written.
- `print()` sends text to your terminal. You can print plain strings, variables, or a mix of both.
- An **f-string** starts with `f` before the quote and uses `{}` to embed a variable's value directly into text — essential for dynamic labels like temperature readouts.
- The format code `:.1f` inside `{}` controls decimal precision: `:.1f` gives one decimal place, `:.2f` gives two.
- A **comment** starts with `#` and is completely ignored by Python — it exists only to explain your code to the humans reading it.

---

# Lesson 4: Lists, Arrays, and NumPy

---

## Learning Objective

By the end of this lesson, you will be able to create Python lists and NumPy arrays, understand why NumPy is preferred for scientific computation, use `np.zeros()` and `np.arange()` to build arrays, access values by index, and recognize how the simulation script stores and updates its temperature and entropy data.

---

## 1. The Problem the Simulation Needs to Solve

Before writing any code, think about what the simulation actually needs to do with numbers.

The simulation tracks the temperature of two reservoirs over time. Time runs from `0` to `200` seconds in steps of `0.1` seconds. That means the simulation needs to store:

- **2,000 temperature values** for the hot reservoir
- **2,000 temperature values** for the cold reservoir
- **2,000 time values**
- **2,000 entropy values**
- **2,000 heat flux values**

And at every single step, it needs to do arithmetic on those values — subtracting temperatures, multiplying by mass, dividing by specific heat capacity.

You need a data structure built for this. Start with the most natural one: the Python list.

---

## 2. Python Lists

A **list** is Python's built-in way of storing a sequence of values in a single variable.

```python
# A list is created with square brackets []
# Values inside are separated by commas

temperatures = [400, 395, 390, 385, 380]

# A list can hold any type of value
mixed = [42, "hello", 3.14, True]

# An empty list
empty = []
```

### Accessing Values by Index

Every item in a list has a position number called an **index**. Python starts counting from **zero**, not one. This is one of the most important rules in Python.

```python
temperatures = [400, 395, 390, 385, 380]
#               [0]  [1]  [2]  [3]  [4]   ← index positions

print(temperatures[0])   # Output: 400  (first item)
print(temperatures[1])   # Output: 395  (second item)
print(temperatures[4])   # Output: 380  (last item)
print(temperatures[-1])  # Output: 380  (negative index = count from the end)
print(temperatures[-2])  # Output: 385  (second from the end)
```

### Changing a Value by Index

```python
temperatures = [400, 395, 390, 385, 380]

temperatures[0] = 410    # Replace the first value
print(temperatures)      # Output: [410, 395, 390, 385, 380]
```

### Building a List with a Loop

```python
# Create a list of 2000 zeros using a loop
data = []                        # start with empty list
for i in range(2000):            # repeat 2000 times
    data.append(0.0)             # add a zero to the end each time

print(len(data))                 # Output: 2000
print(data[0])                   # Output: 0.0
```

This works. But it is slow and awkward for math. Here is why.

---

## 3. Why Python Lists Are Slow for Scientific Math

Imagine you want to multiply every temperature in a list by 2.

```python
temperatures = [400, 395, 390, 385, 380]

# This does NOT work the way you might expect
result = temperatures * 2
print(result)
# Output: [400, 395, 390, 385, 380, 400, 395, 390, 385, 380]
# Python repeated the list twice instead of multiplying each value
```

To actually multiply each value, you need a loop:

```python
temperatures = [400, 395, 390, 385, 380]
result = []

for t in temperatures:
    result.append(t * 2)

print(result)
# Output: [800, 790, 780, 770, 760]
```

This works, but there are two real problems:

**Problem 1 — Speed.** Python lists store each value as a separate object in memory with extra information attached. When you loop over 2,000 values doing arithmetic, Python has to unpack each object individually. For a list of 2,000 items this is barely noticeable. For a list of 2,000,000 items — common in real scientific work — it becomes painfully slow.

**Problem 2 — Readability.** Writing a loop just to multiply every element by a number is verbose and hard to read. Scientific formulas written as loops do not look like the math they represent.

NumPy solves both problems.

---

## 4. What is NumPy?

**NumPy** stands for **Numerical Python**. It is a library — a collection of pre-written tools — that you import into your script to gain new capabilities.

NumPy's core feature is the **ndarray** (n-dimensional array), usually just called an **array**. It looks similar to a Python list but is fundamentally different under the hood:

- All values in a NumPy array must be the **same data type** (usually all floats or all integers)
- Values are stored as a single compact block of memory, not as separate objects
- Math operations apply to the **entire array at once**, written as a single expression
- It is implemented in C under the hood, making it dramatically faster than Python loops

NumPy comes pre-installed with Anaconda. To use it, you import it at the top of your script with the conventional alias `np`:

```python
import numpy as np    # "import numpy, and let me refer to it as np"
```

The alias `np` is a universal convention. Every Python programmer in the world uses it. You will see `np.` everywhere.

---

## 5. NumPy Arrays vs Python Lists — A Direct Comparison

```python
import numpy as np

# --- Python list ---
list_temps = [400, 395, 390, 385, 380]

# --- NumPy array ---
array_temps = np.array([400, 395, 390, 385, 380])

# Math on a Python list: need a loop
list_result = [t * 2 for t in list_temps]

# Math on a NumPy array: one clean expression
array_result = array_temps * 2

print(list_result)    # [800, 790, 780, 770, 760]
print(array_result)   # [800 790 780 770 760]
# Same result, but the NumPy version reads like actual math
```

This is called **vectorized operation** — applying a calculation to every element simultaneously with one expression. It is the core reason scientists use NumPy.

```python
import numpy as np

T_hot  = np.array([400.0, 395.0, 390.0])
T_cold = np.array([300.0, 302.0, 304.0])

# Subtract two arrays element by element — one line, no loop needed
delta_T = T_hot - T_cold

print(delta_T)    # [100.  93.  86.]
```

---

## 6. `np.zeros()` — Creating an Array Pre-filled with Zeros

The simulation does not know the temperature values in advance. It calculates them one step at a time. So it needs to **reserve space** first — create an array of the right size, filled with placeholder zeros, and then fill in the real values during the simulation loop.

`np.zeros()` does exactly this.

```python
import numpy as np

# Create an array of 5 zeros
a = np.zeros(5)
print(a)
# Output: [0. 0. 0. 0. 0.]
# Note: the values are floats (0.) not integers (0)
# NumPy defaults to 64-bit floating point numbers

# Create an array of 2000 zeros — the size used in our simulation
temperatures = np.zeros(2000)
print(temperatures.shape)    # Output: (2000,)  ← shape tells you dimensions
print(len(temperatures))     # Output: 2000
```

### Filling in values by index

```python
import numpy as np

T_hot = np.zeros(5)        # [0. 0. 0. 0. 0.]

T_hot[0] = 400.0           # Set the first value (initial condition)
print(T_hot)               # [400.   0.   0.   0.   0.]

T_hot[1] = 398.5           # Set the second value (after first time step)
T_hot[2] = 397.1
print(T_hot)               # [400.  398.5  397.1   0.    0. ]
```

This is precisely how the simulation works. It sets `T_hot[0]` to the initial temperature, then calculates and fills in each subsequent value during the loop.

---

## 7. `np.arange()` — Creating an Array of Evenly Spaced Values

`np.arange()` creates an array of numbers from a start value to a stop value, stepping by a fixed increment. Think of it as a NumPy version of Python's `range()`, but it produces a float array and includes decimal steps.

```python
import numpy as np

# np.arange(start, stop, step)
# Note: stop value is NOT included in the result

time = np.arange(0, 1.0, 0.25)
print(time)
# Output: [0.   0.25 0.5  0.75]

# The simulation uses:
time = np.arange(0, 200, 0.1)
print(len(time))       # Output: 2000
print(time[0])         # Output: 0.0
print(time[1])         # Output: 0.1
print(time[-1])        # Output: 199.9
```

`np.arange(0, 200, 0.1)` creates exactly 2,000 time points: 0.0, 0.1, 0.2, … all the way to 199.9. This becomes the x-axis of every plot in the simulation.

---

## 8. Array Indexing and Slicing

You access NumPy array values the same way you access list values — by index, starting from zero.

```python
import numpy as np

T_hot = np.array([400.0, 398.5, 397.1, 395.8, 394.6])

# Single value access
print(T_hot[0])     # 400.0  — first value
print(T_hot[2])     # 397.1  — third value
print(T_hot[-1])    # 394.6  — last value

# Slicing: get a range of values
# Syntax: array[start:stop]  (stop is not included)
print(T_hot[0:3])   # [400.  398.5  397.1]  — first three values
print(T_hot[1:])    # [398.5  397.1  395.8  394.6]  — everything from index 1 onward
print(T_hot[:3])    # [400.  398.5  397.1]  — everything up to (not including) index 3
```

### Using a variable as an index

This is important for the simulation. The simulation tracks which step it is currently on using a variable called `current_step`. It uses that variable as the index to read and write values:

```python
import numpy as np

T_hot = np.zeros(5)
T_hot[0] = 400.0

current_step = 0        # we are at step zero

# Read the current temperature
T_now = T_hot[current_step]
print(T_now)            # 400.0

# Write the next temperature
T_hot[current_step + 1] = T_now - 1.5
print(T_hot)            # [400.  398.5   0.    0.    0. ]
```

---

## 9. How This Connects to Our Script

Now open the simulation script and look at the `reset_simulation()` method inside the `IrreversibleHeatTransfer` class. Every concept from this lesson appears directly here.

```python
def reset_simulation(self):
    """Reset simulation to initial conditions."""

    # np.arange() creates the time axis: 0.0, 0.1, 0.2, ... 199.9
    # self.t_max = 200, self.dt = 0.1
    self.time = np.arange(0, self.t_max, self.dt)

    # How many time steps are there? Store that number for use in loops
    self.n_steps = len(self.time)          # = 2000

    # np.zeros() reserves space for 2000 values — placeholders for now
    self.T_hot            = np.zeros(self.n_steps)    # hot reservoir temperatures
    self.T_cold           = np.zeros(self.n_steps)    # cold reservoir temperatures
    self.Q_transferred    = np.zeros(self.n_steps)    # cumulative heat transferred
    self.S_gen_cumulative = np.zeros(self.n_steps)    # cumulative entropy generated
    self.heat_flux        = np.zeros(self.n_steps)    # instantaneous heat flow rate

    # Set initial conditions at index [0] — the starting values
    self.T_hot[0]  = self.T_hot_0       # e.g. 400 K
    self.T_cold[0] = self.T_cold_0      # e.g. 300 K

    # Track the current position in the simulation
    self.current_step = 0
```

Six arrays. All created with `np.zeros()`. One time array created with `np.arange()`. Initial values written into index `[0]`.

---

Now look at the `step()` method — this is where the arrays get filled in one index at a time:

```python
def step(self):
    """Advance simulation by one time step."""
    if self.current_step >= self.n_steps - 1:
        return False                    # stop if we have reached the end

    i = self.current_step               # current index, e.g. i = 0

    # Read current temperatures using index i
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])

    self.heat_flux[i] = Q_dot           # write heat flux at current index

    # Calculate how much temperature changes this step
    dT_hot  = -Q_dot * self.dt / (self.m_hot  * self.c_p)
    dT_cold =  Q_dot * self.dt / (self.m_cold * self.c_p)

    # Write new temperatures at the NEXT index: i + 1
    self.T_hot[i+1]  = self.T_hot[i]  + dT_hot
    self.T_cold[i+1] = self.T_cold[i] + dT_cold

    # Accumulate total heat transferred
    self.Q_transferred[i+1] = self.Q_transferred[i] + Q_dot * self.dt

    # Calculate and accumulate entropy generation
    S_gen_dot = self.calculate_entropy_generation_rate(
        Q_dot, self.T_hot[i], self.T_cold[i]
    )
    self.S_gen_cumulative[i+1] = self.S_gen_cumulative[i] + S_gen_dot * self.dt

    self.current_step += 1              # advance the step counter
    return True
```

The pattern repeats for every array:

> **Read from index `i` → calculate → write to index `i + 1`**

By the time `run_full_simulation()` finishes its loop and calls `step()` 2,000 times, every index in every array has been filled. The arrays then become the data for all five plots.

---

Finally, look at how the plotting methods use array slicing to show only the data computed so far during animation:

```python
def plot_temperature(self):
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    # self.sim.time[:idx+1]  ← all time values from index 0 up to current step
    # self.sim.T_hot[:idx+1] ← all hot temperatures computed so far
    self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_hot[:idx+1], 
                     'r-', linewidth=2, label='Hot Reservoir')
```

`self.sim.T_hot[:idx+1]` is a slice. It takes only the filled-in portion of the array and ignores the remaining zeros. This is what makes the animation look like the line is growing across the plot over time — you are progressively revealing more of the array.

---

## Practice Exercise

Complete all three tasks. You do not need the simulation script open — just a new file called `practice4.py`.

**Task 1.** Create a NumPy array of 10 zeros. Set the first value to `400.0` and the last value to `300.0`. Print the full array.

Expected output:

```
[400.   0.   0.   0.   0.   0.   0.   0.   0. 300.]
```

**Task 2.** Create a time array using `np.arange()` that goes from `0` to `10` in steps of `0.5`. Print the array and print its length.

Expected output:

```
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5
  7.   7.5  8.   8.5  9.   9.5]
20
```

**Task 3.** Simulate a simple cooling process. Start with `T = 400.0`. At each step, subtract `5.0` degrees and store the result in a `np.zeros(10)` array. Print the final array.

```python
import numpy as np

T = np.zeros(10)
T[0] = 400.0

for i in range(9):             # fill indices 1 through 9
    T[i+1] = T[i] - 5.0

print(T)
```

Expected output:

```
[400. 395. 390. 385. 380. 375. 370. 365. 360. 355.]
```

Notice that Task 3 is a miniature version of exactly what `step()` does in the simulation — reading from index `i` and writing to index `i + 1`.

---

## Key Takeaways

- A Python list stores a sequence of values and uses zero-based indexing. It works for small tasks but is slow and awkward for mathematical operations on large datasets.
- NumPy provides the array type, which stores all values as a single compact block of memory, supports vectorized math with no loops required, and is dramatically faster than lists for numerical computation.
- `np.zeros(n)` creates an array of `n` floating-point zeros. The simulation uses this to reserve space for temperature, entropy, heat flux, and heat transfer data before the values are calculated.
- `np.arange(start, stop, step)` creates an array of evenly spaced values. The simulation uses `np.arange(0, 200, 0.1)` to produce the 2,000-point time axis.
- Array slicing with `array[:idx+1]` returns only the filled portion of an array, which is how the animation progressively reveals computed data on the plots without showing the placeholder zeros.

---

# Lesson 5: Conditional Logic — `if`, `elif`, `else`

---

## 1. Plain-English Concept Explanation

Every decision you make in daily life follows a simple pattern: _"If this is true, do that. Otherwise, do something else."_

- If the coffee is hot, drink it. Otherwise, microwave it first.
- If the traffic light is green, go. If it's yellow, slow down. If it's red, stop.

Python uses exactly this same pattern. **Conditional logic** lets your program check whether something is true or false, and then choose what to do based on the answer.

---

### Booleans: The True/False Type

Before Python can make a decision, it needs to evaluate a condition. The result is always one of exactly two values:

- `True`
- `False`

These are called **booleans** (named after mathematician George Boole). They are their own data type in Python, distinct from numbers or text.

```python
print(400 > 300)   # True  — 400 is greater than 300
print(400 < 300)   # False — 400 is not less than 300
```

---

### Comparison Operators

These operators compare two values and return a boolean:

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`==`|Equal to|`300 == 300`|`True`|
|`!=`|Not equal to|`300 != 400`|`True`|
|`>`|Greater than|`400 > 300`|`True`|
|`<`|Less than|`400 < 300`|`False`|
|`>=`|Greater than or equal to|`400 >= 400`|`True`|
|`<=`|Less than or equal to|`300 <= 400`|`True`|

> ⚠️ A very common beginner mistake: `=` assigns a value to a variable. `==` _compares_ two values. They are completely different things.

```python
temperature = 400     # Assignment: store 400 in "temperature"
temperature == 400    # Comparison: is temperature equal to 400? → True
```

---

### `if`, `elif`, and `else`

Python gives you three keywords for conditional logic:

- **`if`** — checks the first condition
- **`elif`** — short for "else if" — checks an additional condition if the first was `False`
- **`else`** — runs if _none_ of the above conditions were `True`

The general pattern looks like this:

```
if <condition is True>:
    do this
elif <different condition is True>:
    do this instead
else:
    do this if nothing above was True
```

You can have as many `elif` blocks as you need. The `else` block is optional. Python checks each condition **from top to bottom** and runs only the **first** block whose condition is `True`, then skips the rest.

---

### Indentation: Python's Way of Grouping Code

In many programming languages, curly braces `{}` are used to group blocks of code together. Python does this differently — it uses **indentation** (spaces at the start of a line).

**Indentation** means pressing the Tab key (or adding 4 spaces) before a line of code. Lines that are indented the same amount belong to the same block.

```python
if temperature > 350:
    print("Hot")      # indented: belongs to the if block
    print("Be careful")  # also indented: also belongs to the if block
print("Done")         # NOT indented: runs regardless of the condition
```

> ⚠️ Indentation is not optional in Python. If it's wrong, your code will either crash or behave in unexpected ways. The standard is **4 spaces** per level.

---

## 2. Annotated Code Examples

### Basic `if` / `else`

```python
T_hot = 400.0    # temperature of the hot reservoir
T_cold = 300.0   # temperature of the cold reservoir

if T_hot > T_cold:                        # Is T_hot greater than T_cold?
    print("Heat will flow hot → cold")    # Runs because 400.0 > 300.0 is True
else:
    print("No heat flow")                 # Skipped — the if condition was True
```

---

### `if` / `elif` / `else` with multiple branches

```python
system_type = "Closed"    # a text value (called a "string") describing the system

if system_type == "Isolated":          # Is it exactly equal to "Isolated"?
    print("No energy exchange")        # Only runs if system_type is "Isolated"
elif system_type == "Closed":          # If not Isolated, is it "Closed"?
    print("Energy exchange only")      # Runs because this condition is True
else:                                  # Runs only if neither condition above was True
    print("Mass and energy exchange")
```

> 💡 Notice `==` is used for comparison here, not `=`. Checking whether `system_type` equals `"Closed"` uses `==`.

---

### Returning early from a function using `if`

Sometimes a condition means you can skip all further calculation and return a simple result immediately:

```python
def calculate_heat_rate(T_h, T_c, h, system_type):
    # If the system is isolated, no heat flows at all — return 0 immediately
    if system_type == "Isolated":
        return 0.0                 # Exit the function right here with value 0.0
                                   # Nothing below this line runs in this case

    # If we reach this line, the system is NOT isolated
    return h * (T_h - T_c)        # Calculate and return the heat transfer rate
```

---

### Checking multiple conditions with `and` / `or`

You can combine conditions using the keywords `and` and `or`:

```python
Q_dot = 150.0    # heat transfer rate
T_h = 400.0      # hot temperature
T_c = 400.0      # cold temperature (same as hot — at equilibrium)

# "and" means BOTH conditions must be True
if Q_dot == 0 or T_h == T_c:       # Is Q_dot zero OR are temperatures equal?
    print("No entropy generated")  # Runs if either condition is True
```

---

## 3. How This Connects to Our Script

Conditional logic appears in three important places in the simulation.

---

### In `calculate_heat_transfer_rate()`

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    # Check whether this is an isolated system
    if self.system_type == "Isolated":   # Compare system_type to the string "Isolated"
        return 0.0                       # Isolated systems exchange no heat — return 0
                                         # The line below is skipped entirely

    return self.h * (T_h - T_c)         # For all other systems, calculate heat rate
                                         # A larger temperature gap = larger heat flow
```

This is an early return pattern. The `if` block handles the special case; everything else falls through to the normal calculation.

---

### In `step()` — the core time-step calculation

```python
def step(self):
    # ... earlier code calculates Q_dot (heat transfer rate) ...

    if self.system_type == "Isolated":   # Is this an isolated system?
        dT_hot = 0.0                     # No temperature change for hot reservoir
        dT_cold = 0.0                    # No temperature change for cold reservoir
    else:                                # For Closed or Open systems:
        dT_hot = -Q_dot * self.dt / (self.m_hot * self.c_p)   # Hot side cools down
        dT_cold = Q_dot * self.dt / (self.m_cold * self.c_p)  # Cold side warms up
```

Here the `if/else` structure selects between two completely different sets of calculations depending on the system type. Without this, the simulation would apply physics equations even to systems where no heat is supposed to flow.

---

### In `plot_reservoir_visual()` — the arrow drawing logic

```python
if T_h > T_c:                                    # Is the hot side still hotter?
    arrow = patches.FancyArrowPatch(...)          # Create an arrow object
    self.ax_visual.add_patch(arrow)               # Draw it on the diagram
    self.ax_visual.text(5, 1.8, 'Heat Flow', ...) # Label it
```

This `if` block checks whether it makes physical sense to draw a heat flow arrow. Once the two reservoirs reach equilibrium (`T_h == T_c`), the condition becomes `False` and no arrow is drawn — which correctly reflects that heat no longer flows.

---

### In `calculate_entropy_generation_rate()`

```python
def calculate_entropy_generation_rate(self, Q_dot, T_h, T_c):
    if Q_dot == 0 or T_h == T_c:    # No heat flowing, OR temperatures are equal?
        return 0                     # No irreversibility — entropy generation is zero
    return Q_dot * (1/T_c - 1/T_h)  # Otherwise, calculate entropy generation rate
```

Two conditions are combined with `or`. If _either_ is true, entropy generation is zero. Only if _both_ are false does the calculation proceed.

---

## 4. Practice Exercise

**Goal:** Write a small program that classifies a thermodynamic system and describes heat flow.

```python
# --- Set up your values ---
T_hot = 400.0       # temperature of hot reservoir (K)
T_cold = 300.0      # temperature of cold reservoir (K)
system_type = "Closed"   # try changing to "Isolated" or "Open"

# --- Part 1: Classify the system ---
if system_type == "Isolated":
    print("Isolated system: no heat or mass exchange")
elif system_type == "Closed":
    print("Closed system: heat exchange only")
else:
    print("Open system: heat and mass exchange")

# --- Part 2: Describe heat flow direction ---
if T_hot > T_cold:
    print("Heat flows from hot to cold")
elif T_hot == T_cold:
    print("System is at equilibrium — no heat flow")
else:
    print("Something unexpected: cold is hotter than hot")
```

**Then try these variations:**

1. Change `system_type` to `"Isolated"` — which lines print?
2. Set `T_hot = 300.0` and `T_cold = 300.0` — what does the second block print?
3. Add a third block: if `system_type == "Isolated"`, print `"Arrow should not be drawn"` — where in the logic would you put it?

---

## 5. Key Takeaways

- **Booleans** are Python's `True`/`False` values — the result of any comparison expression.
- **Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) compare two values and return a boolean. Remember: `=` assigns, `==` compares.
- An `if/elif/else` chain checks conditions **top to bottom** and runs only the **first matching block** — the rest are skipped.
- Python uses **indentation** (4 spaces) instead of curly braces to define which lines belong to which block. Correct indentation is mandatory, not optional.
- In our script, conditional logic controls three real behaviors: whether heat flows at all (`system_type == "Isolated"`), whether temperature changes are calculated, and whether the heat flow arrow is drawn on screen.

---

# Lesson 6: Loops — `for` and `while`

---

## 1. Plain-English Concept Explanation

### What is a Loop?

Imagine you need to do the same task 2,000 times — like advancing a simulation one tiny time step at a time until it reaches equilibrium. You would not write the same line of code 2,000 times. Instead, you use a **loop**: an instruction that tells Python _"repeat this block of code a set number of times, or until a condition is no longer true."_

Python has two main types of loops: `for` and `while`.

---

### The `for` Loop

A **`for` loop** repeats a block of code a specific, known number of times — once for each item in a **sequence** (an ordered collection of values).

The most common sequence used with `for` loops is created by `range()`, which generates a sequence of numbers for you automatically.

The general shape looks like this:

```
for variable in sequence:
    do something
```

The word `in` is required syntax. The `variable` (often named `i` by convention, short for _index_) automatically takes on each value in the sequence, one at a time, as the loop runs.

---

### The `while` Loop

A **`while` loop** repeats a block of code _as long as a condition remains true_. You use it when you don't know in advance exactly how many repetitions you need — you just know the condition that should stop the loop.

The general shape looks like this:

```
while condition is True:
    do something
```

As soon as the condition becomes `False`, the loop stops.

---

### `break` — Exiting a Loop Early

Both `for` and `while` loops can be stopped early using the keyword **`break`**. When Python hits a `break` statement, it immediately exits the loop, even if there are steps remaining.

---

## 2. Annotated Code Examples

### `range()` and the `for` Loop

```python
# range(5) generates the sequence: 0, 1, 2, 3, 4
# (it starts at 0 and stops BEFORE 5 — this is important)
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```

```python
# range(start, stop) lets you choose where to begin
# This generates: 1, 2, 3, 4  (stops before 5)
for i in range(1, 5):
    print(i)
```

```python
# range(n - 1) is common in simulations
# If n = 5, this generates: 0, 1, 2, 3  (4 steps total)
n = 5
for i in range(n - 1):
    print(f"Step {i}")
# Output:
# Step 0
# Step 1
# Step 2
# Step 3
```

---

### Iterating Over a List (a Sequence of Values)

A **list** is a simple ordered collection of values, written with square brackets `[]`. A `for` loop can walk through every item in a list automatically.

```python
# A list of strings — square brackets hold the items, commas separate them
concepts = ["Heat", "Temperature", "Entropy"]

# item takes on each value in the list, one per loop pass
for item in concepts:
    print(item)
# Output:
# Heat
# Temperature
# Entropy
```

---

### Iterating Over a NumPy Array

In our script, most sequences are **NumPy arrays** — these behave just like lists for the purpose of looping. (NumPy arrays were introduced in Lesson 4. For now, just know they work the same way as lists inside a `for` loop.)

```python
import numpy as np

# np.arange(0, 1.0, 0.5) generates: [0.0, 0.5]
# (starts at 0, stops before 1.0, steps by 0.5)
time_steps = np.arange(0, 1.0, 0.5)

for t in time_steps:
    print(f"Time: {t:.1f} seconds")
# Output:
# Time: 0.0 seconds
# Time: 0.5 seconds
```

---

### The `while` Loop

```python
temperature = 400  # starting temperature in Kelvin

# Keep cooling until temperature reaches 350 K
while temperature > 350:
    temperature -= 10  # -= means: subtract 10 and store the result back
    print(f"Cooling... {temperature} K")

print("Equilibrium reached.")
# Output:
# Cooling... 390 K
# Cooling... 380 K
# Cooling... 370 K
# Cooling... 360 K
# Cooling... 350 K
# Equilibrium reached.
```

---

### `break` — Stopping a Loop Early

```python
# A for loop that stops early if a condition is met
for i in range(10):
    if i == 4:
        break       # exit the loop immediately when i equals 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
```

---

### A Loop Inside a Loop (Nested Loops)

You can place one loop _inside_ another. The inner loop completes all its repetitions for every single step of the outer loop.

```python
# Outer loop runs 3 times
for frame in range(3):
    # Inner loop runs 5 times per outer loop step
    for step in range(5):
        print(f"Frame {frame}, Step {step}")
# This prints 15 lines total (3 × 5)
```

---

## 3. How This Connects to Our Script

### The `for` Loop in `run_full_simulation()`

This is the most important loop in the entire script. It runs the simulation from start to finish by repeatedly calling `self.step()` — the function that advances the physics by one tiny time increment:

```python
def run_full_simulation(self):
    """Run complete simulation to equilibrium."""

    # Reset all arrays to starting conditions before running
    self.reset_simulation()

    # self.n_steps is the total number of time steps (e.g. 2000)
    # range(n_steps - 1) gives: 0, 1, 2, ..., 1998
    # We use n_steps - 1 because each call to step() fills position i+1
    # — so the last valid index to start from is n_steps - 2
    for i in range(self.n_steps - 1):
        self.step()   # advance the simulation by one time step
```

Without this loop, you would need to call `self.step()` manually thousands of times. The loop does all of that automatically.

---

### The Inner Loop in `animate()`

The `animate()` method is called once per animation frame. To make the animation move at a visible pace, it advances the simulation by **5 steps per frame** using a `for` loop nested inside the animation's logic. It also uses `break` to stop early if the simulation finishes mid-frame:

```python
def animate(self, frame):
    """Animation function — called once per displayed frame."""

    if self.is_playing and self.sim.current_step < self.sim.n_steps - 1:

        # Advance 5 simulation steps each time a new frame is drawn
        # This makes the animation visually faster without skipping data
        for _ in range(5):
            # self.sim.step() returns False when simulation is complete
            if not self.sim.step():
                self.is_playing = False  # stop playing
                break                    # exit the inner loop immediately
```

The variable `_` is a Python convention meaning _"I need a loop counter, but I don't actually use its value."_ It's just a polite way of saying the number of repetitions is what matters, not which repetition you're on.

---

### The Print Statements in `main()`

The terminal output in `main()` uses plain `print()` calls — not technically a `for` loop, but the _concept_ of sequential repetition is the same. Each `print()` runs one after another, top to bottom. If you ever wanted to print a dynamic list of concepts automatically, a loop would replace those manual calls:

```python
# The manual version used in main() — each line written out separately
print("  • Heat flows spontaneously from hot to cold")
print("  • Temperature difference drives irreversible heat transfer")
print("  • Entropy is generated (Second Law of Thermodynamics)")

# The loop version — identical output, less repetition
concepts = [
    "Heat flows spontaneously from hot to cold",
    "Temperature difference drives irreversible heat transfer",
    "Entropy is generated (Second Law of Thermodynamics)",
]

for concept in concepts:
    print(f"  • {concept}")
```

Both produce the same output. The loop version is easier to extend — just add a new item to the list.

---

## 4. Practice Exercise

Try this in a new Python file. It should take under 10 minutes.

**Task:** Write a short program that simulates a cooling process:

1. Start with a variable `temperature` set to `400`
2. Use a `for` loop with `range()` to simulate 10 cooling steps
3. On each step, subtract `8` from the temperature
4. Print the current step number and temperature using an f-string, formatted to `1` decimal place
5. If the temperature drops below `340`, print `"Warning: approaching equilibrium."` and break out of the loop

**Expected output** (may stop early depending on your numbers):

```
Step 1: 392.0 K
Step 2: 384.0 K
Step 3: 376.0 K
Step 4: 368.0 K
Step 5: 360.0 K
Step 6: 352.0 K
Step 7: 344.0 K
Step 8: 336.0 K
Warning: approaching equilibrium.
```

**Starter hint:**

```python
temperature = 400

for i in range(10):
    # your code here
```

> **Note:** The step numbers in the expected output start at `1`, but `range(10)` starts at `0`. Think about how you might adjust `i` in your f-string to display `1` on the first step.

---

## 5. Key Takeaways

- A **`for` loop** repeats a block of code once for each item in a sequence. `range(n)` generates the sequence `0, 1, 2, ..., n-1` and is the most common tool for controlling how many times a loop runs.
- A **`while` loop** repeats as long as a condition stays `True`. Use it when the number of repetitions isn't known in advance.
- **`break`** exits a loop immediately — used in `animate()` to stop advancing the simulation the moment it finishes, even mid-frame.
- **Nested loops** (a loop inside a loop) multiply repetitions: the `animate()` method runs 5 simulation steps per animation frame using exactly this pattern.
- The variable name **`_`** is a Python convention for a loop counter whose value you don't need — a readable signal to anyone reading your code that the count itself is what matters, not its value.

---

# Lesson 7: Functions — Defining and Calling Them

---

## 1. Plain-English Concept Explanation

Imagine you have a recipe for making tea. Instead of rewriting the full recipe every time you want a cup, you just say _"make tea."_ In programming, a **function** is exactly that — a reusable set of instructions you write once and can use as many times as you need, just by calling its name.

### Why bother with functions?

- **Reusability** — write the logic once, use it anywhere
- **Readability** — `calculate_entropy()` tells you far more than 20 raw lines of math would
- **Organization** — each function does one job, making bugs easier to find and fix

### The four things to know

|Term|Plain-English Meaning|
|---|---|
|`def`|The keyword that tells Python _"I'm about to define a function"_|
|**Parameter**|A placeholder variable that receives input when the function is called|
|**Argument**|The actual value you pass in when calling the function|
|**Return value**|The result the function hands back to whoever called it|

---

## 2. Annotated Code Examples

### Example A — The simplest possible function

```python
# "def" tells Python we're defining a function.
# "greet" is the name we're giving it.
# The parentheses hold any inputs (none here).
# The colon ends the function header — required.
def greet():
    # Everything indented under def belongs to the function.
    # This line only runs when the function is called.
    print("Hello! Welcome to thermodynamics.")

# Calling the function — this is what actually runs it.
# Nothing happens until you call it.
greet()
```

**Output:**

```
Hello! Welcome to thermodynamics.
```

---

### Example B — A function with parameters

```python
# "temperature" is a parameter — a placeholder for input.
# When the function is called, Python fills in the real value.
def describe_temperature(temperature):
    # We use the parameter inside the function like a normal variable.
    print("The current temperature is", temperature, "Kelvin.")

# Calling the function with an argument.
# 400 is the argument — the real value that fills the "temperature" placeholder.
describe_temperature(400)
describe_temperature(300)
```

**Output:**

```
The current temperature is 400 Kelvin.
The current temperature is 300 Kelvin.
```

> **Note:** Parameters live _inside_ the function. If you try to use `temperature` outside the function, Python won't know what it is. This is called **scope** — a variable only exists where it was created.

---

### Example C — A function that returns a value

```python
# Two parameters: the hot and cold temperatures.
def calculate_equilibrium(T_hot, T_cold):
    # Do the calculation inside the function.
    result = (T_hot + T_cold) / 2

    # "return" sends the result back to wherever the function was called.
    # Without return, the function does work but hands nothing back.
    return result

# The returned value is caught in a variable called "eq_temp".
eq_temp = calculate_equilibrium(400, 300)

# Now we can use it.
print("Equilibrium temperature:", eq_temp, "K")
```

**Output:**

```
Equilibrium temperature: 350.0 K
```

---

### Example D — What happens without `return`

```python
def add_numbers(a, b):
    total = a + b
    # No return statement — the result disappears when the function ends.

result = add_numbers(10, 5)

# "None" is Python's way of saying "there is no value here."
print(result)
```

**Output:**

```
None
```

> This is a common beginner mistake. If you need the result of a function later, always use `return`.

---

### Example E — Multiple parameters, realistic math

```python
# This mirrors the kind of math in our actual simulation.
# Four parameters, each with a descriptive name.
def calculate_heat_transfer(h, T_hot, T_cold):
    # h is the heat transfer coefficient (a measure of how easily
    # heat moves between the two objects, in Watts per Kelvin).
    # The formula: Q_dot = h * (T_hot - T_cold)
    Q_dot = h * (T_hot - T_cold)

    # Return the result so the caller can use it.
    return Q_dot

# Call it with real values and store the result.
rate = calculate_heat_transfer(50, 400, 300)
print("Heat transfer rate:", rate, "Watts")
```

**Output:**

```
Heat transfer rate: 5000 Watts
```

---

## 3. How This Connects to Our Script

The thermodynamics simulation is built almost entirely out of functions. Each one handles exactly one job. Here are four of them:

---

### `_calculate_equilibrium_temp()`

```python
def _calculate_equilibrium_temp(self):
    # Calculates the temperature both reservoirs will eventually reach.
    # self.m_hot, self.c_p, self.T_hot_0 etc. are all stored values
    # belonging to the class — we'll cover "self" in the Classes lesson.

    numerator = self.m_hot * self.c_p * self.T_hot_0 + self.m_cold * self.c_p * self.T_cold_0
    denominator = self.m_hot * self.c_p + self.m_cold * self.c_p

    # Returns the equilibrium temperature — a single number in Kelvin.
    return numerator / denominator
```

This function is called once at setup and again whenever the user moves a slider. Because it's a function, that calculation is never rewritten — it's just called again.

---

### `calculate_heat_transfer_rate()`

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    # Takes two temperatures as parameters.
    # Returns zero immediately if the system is "Isolated"
    # (no heat can flow in or out of an isolated system).
    if self.system_type == "Isolated":
        return 0.0

    # Otherwise, apply Newton's Law of Cooling:
    # heat flow rate = coefficient × temperature difference
    return self.h * (T_h - T_c)
```

This function is called inside `step()` on every single time step of the simulation — potentially thousands of times. Writing it as a function means that logic lives in one place.

---

### `calculate_entropy_generation_rate()`

```python
def calculate_entropy_generation_rate(self, Q_dot, T_h, T_c):
    # Q_dot is the heat transfer rate (from the function above).
    # Returns zero if there's no heat flow or no temperature difference.
    if Q_dot == 0 or T_h == T_c:
        return 0

    # Entropy generation formula from the Second Law of Thermodynamics.
    # A positive result means the process is irreversible (energy is "wasted").
    return Q_dot * (1/T_c - 1/T_h)
```

Notice how this function _uses the output of another function_ as its input (`Q_dot`). Functions working together like this is the core of how larger programs are organized.

---

### `step()`

```python
def step(self):
    # Advances the simulation by one tiny time interval (dt = 0.1 seconds).
    # Returns False when the simulation is finished, True otherwise.
    if self.current_step >= self.n_steps - 1:
        return False

    i = self.current_step

    # Calls calculate_heat_transfer_rate() — reusing that function here.
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])

    # Calls calculate_entropy_generation_rate() — reusing that one too.
    S_gen_dot = self.calculate_entropy_generation_rate(Q_dot, self.T_hot[i], self.T_cold[i])

    # ... updates temperatures and entropy arrays, then:
    self.current_step += 1
    return True
```

`step()` is the engine of the simulation. It runs up to 2,000 times during one animation. Because the math is isolated inside other functions, `step()` stays readable — it describes _what happens_, not _how the math works_.

---

## 4. Practice Exercise

**Goal:** Write two functions and use one inside the other.

```python
# STEP 1: Write a function called "celsius_to_kelvin"
# It should take one parameter: a temperature in Celsius.
# It should return the temperature in Kelvin.
# (Hint: Kelvin = Celsius + 273.15)

# STEP 2: Write a function called "temp_difference"
# It should take two parameters: T_hot and T_cold (both in Celsius).
# Inside the function, convert BOTH temperatures to Kelvin
# by calling your celsius_to_kelvin function.
# Return the difference: T_hot_kelvin - T_cold_kelvin.

# STEP 3: Call temp_difference(100, 25) and print the result.
# Expected output: 75.0
```

**Starter structure if you get stuck:**

```python
def celsius_to_kelvin(celsius):
    # your code here
    pass  # "pass" is a placeholder — delete it when you add your code

def temp_difference(T_hot, T_cold):
    # your code here
    pass

print(temp_difference(100, 25))
```

---

## 5. Key Takeaways

- **`def` declares a function.** Nothing inside it runs until you call the function by name.
- **Parameters are placeholders;** arguments are the real values you pass in when calling.
- **`return` sends a value back** to the caller. Without it, the function hands back `None`.
- **Functions make code reusable.** In the simulation, `calculate_heat_transfer_rate()` is called thousands of times without ever rewriting the formula.
- **Functions can call other functions.** `step()` calls both `calculate_heat_transfer_rate()` and `calculate_entropy_generation_rate()` — building complex behavior from simple, testable pieces.

---

# Lesson 8: Introduction to Classes and Objects

---

## Learning Objective

By the end of this lesson, you will be able to explain what a class is, create a simple class with an `__init__` method, understand what `self` refers to, instantiate objects from a class, and recognize how `IrreversibleHeatTransfer` and `InteractiveVisualizer` are structured as the two classes that make up the entire simulation.

---

## 1. The Problem Classes Solve

Before introducing any syntax, consider a practical problem.

Your simulation needs to track several pieces of information about a thermal system all at once:

- Initial hot temperature
- Initial cold temperature
- Mass of each reservoir
- Specific heat capacity
- Heat transfer coefficient
- 2,000-element arrays for temperature, entropy, heat flux
- The current simulation step
- The equilibrium temperature

And it needs functions that operate specifically on that data:

- `reset_simulation()`
- `step()`
- `calculate_heat_transfer_rate()`
- `run_full_simulation()`

You could store all the data in separate variables and write all the functions separately. But then nothing would be grouped together. A function like `calculate_heat_transfer_rate()` would need to receive every relevant variable as an argument every time it is called. The code would sprawl in every direction and become very difficult to read or modify.

A **class** solves this by bundling related data and related functions into a single, organized unit.

---

## 2. What is a Class?

A **class** is a blueprint.

It is a definition — written once — that describes:

1. What **data** something should hold
2. What **actions** it can perform

A class by itself does not hold any real data. It is the plan, not the product.

An **object** (also called an **instance**) is a real, concrete thing built from that blueprint. It holds actual data and can perform actual actions.

The relationship is the same as:

|Blueprint|Real Thing|
|---|---|
|Architectural floor plan|An actual house|
|Cookie cutter|An actual cookie|
|Class|Object (instance)|

You define a class once. You can create as many objects from it as you need, each holding its own independent data.

---

## 3. A Simple Analogy — The Dog Class

Start with something completely unrelated to physics. This makes the syntax easier to absorb before connecting it to the simulation.

```python
# The 'class' keyword defines a new class
# By convention, class names start with a Capital Letter
class Dog:
    pass    # 'pass' means "nothing here yet" — a valid empty class
```

This defines a class called `Dog`. It currently does nothing. But you can already create objects from it:

```python
dog1 = Dog()    # create one Dog object, store it in the variable dog1
dog2 = Dog()    # create a second, completely separate Dog object

print(type(dog1))    # Output: <class '__main__.Dog'>
```

`Dog()` — with parentheses — is how you build an object from a class. This action is called **instantiation**. `dog1` and `dog2` are two separate instances. Changing one does not affect the other.

---

## 4. `__init__` — The Constructor

A class with `pass` is useless. Real classes need to set up their data when an object is created. This happens inside a special method called `__init__`.

`__init__` stands for **initialize**. It runs automatically every time you create a new object from the class. Its job is to set up the object's starting data.

```python
class Dog:

    def __init__(self, name, breed, age):
        # 'self' is explained in the next section
        # For now, read these lines as: "store the given values on this object"
        self.name  = name     # store the name
        self.breed = breed    # store the breed
        self.age   = age      # store the age
```

Now create objects by passing values into the parentheses:

```python
dog1 = Dog("Rex",   "Labrador",  3)
dog2 = Dog("Bella", "Poodle",    7)

# Each object holds its own independent data
print(dog1.name)    # Output: Rex
print(dog2.name)    # Output: Bella
print(dog1.age)     # Output: 3
print(dog2.age)     # Output: 7
```

The dot `.` is how you access data stored on an object. `dog1.name` means: _"go to the object stored in `dog1`, and get the value called `name`."_

### What happens when you write `Dog("Rex", "Labrador", 3)`?

Python executes these steps in order:

1. Creates a new, empty Dog object
2. Calls `__init__` automatically, passing the new object as the first argument
3. `__init__` stores `"Rex"`, `"Labrador"`, and `3` on that object
4. Returns the finished object, which you store in `dog1`

You never call `__init__` directly. Python calls it for you.

---

## 5. `self` — What It Is and Why It Exists

`self` is the most confusing thing about Python classes for beginners. Here is a plain-English explanation.

When you write a method inside a class, Python needs a way to refer to _the specific object the method is being called on_. That is what `self` is.

`self` is always the first parameter of every method in a class. When you call a method on an object, Python automatically passes the object itself as the first argument. You do not pass it manually.

```python
class Dog:

    def __init__(self, name, age):
        self.name = name    # "on THIS object, store name"
        self.age  = age     # "on THIS object, store age"

    def describe(self):
        # self.name refers to the name stored on THIS specific object
        print(f"My name is {self.name} and I am {self.age} years old.")


dog1 = Dog("Rex",   3)
dog2 = Dog("Bella", 7)

dog1.describe()    # Output: My name is Rex and I am 3 years old.
dog2.describe()    # Output: My name is Bella and I am 7 years old.
```

When you call `dog1.describe()`, Python translates this internally to `Dog.describe(dog1)` — it passes `dog1` as the `self` argument. The method then uses `self.name` to get `"Rex"` specifically, not `"Bella"`.

### The rule in plain English

> Every time you write `self.something = value` inside a class, you are storing a piece of data on the object. Every time you write `self.something` later, you are reading that data back. `self` is simply the object talking about itself.

---

## 6. Adding Methods — Actions an Object Can Perform

A method is a function defined inside a class. It always takes `self` as its first parameter.

```python
class Dog:

    def __init__(self, name, age):
        self.name      = name
        self.age       = age
        self.is_hungry = True    # dogs start out hungry

    def eat(self):
        self.is_hungry = False   # eating changes the object's state
        print(f"{self.name} has eaten. No longer hungry.")

    def check_hunger(self):
        if self.is_hungry:
            print(f"{self.name} is hungry.")
        else:
            print(f"{self.name} is full.")

    def have_birthday(self):
        self.age += 1            # modify stored data
        print(f"{self.name} is now {self.age} years old.")


# Create an object
dog1 = Dog("Rex", 3)

# Call methods on it
dog1.check_hunger()      # Output: Rex is hungry.
dog1.eat()               # Output: Rex has eaten. No longer hungry.
dog1.check_hunger()      # Output: Rex is full.
dog1.have_birthday()     # Output: Rex is now 4 years old.
print(dog1.age)          # Output: 4  ← the stored value was modified
```

Notice what is happening here:

- The object `dog1` holds data (`name`, `age`, `is_hungry`)
- Methods read and modify that data using `self`
- Calling `dog1.eat()` changes `dog1.is_hungry` permanently for that object
- `dog2` — if it existed — would be completely unaffected

This is the core idea: **an object owns its data, and its methods operate on that data.**

---

## 7. Default Parameter Values in `__init__`

You can give parameters default values so they become optional when creating an object.

```python
class Dog:

    def __init__(self, name, breed="Unknown", age=0):
        self.name  = name
        self.breed = breed
        self.age   = age


dog1 = Dog("Rex", "Labrador", 3)    # all three provided
dog2 = Dog("Bella")                  # only name provided; breed and age use defaults

print(dog1.breed)    # Output: Labrador
print(dog2.breed)    # Output: Unknown
print(dog2.age)      # Output: 0
```

This pattern appears directly in the simulation's `__init__` method.

---

## 8. Transitioning to the Simulation — `IrreversibleHeatTransfer`

Now apply every concept from above to the actual script. Open the simulation and read the beginning of `IrreversibleHeatTransfer`:

```python
class IrreversibleHeatTransfer:
    """
    Simulates irreversible heat transfer between two thermal reservoirs.
    """

    def __init__(self, T_hot_initial=400, T_cold_initial=300,
                 mass_hot=1.0, mass_cold=1.0, c_p=1000, system_type="Closed"):
```

This maps directly onto the Dog analogy:

|Dog class|IrreversibleHeatTransfer class|
|---|---|
|`name`, `breed`, `age`|`T_hot_initial`, `mass_hot`, `c_p`|
|`dog1 = Dog("Rex", 3)`|`sim = IrreversibleHeatTransfer(T_hot_initial=400)`|
|`dog1.name`|`sim.T_hot_0`|
|`dog1.eat()`|`sim.step()`|

All parameters have default values, so you can create a simulation object with no arguments at all and it uses the defaults:

```python
# These three lines all create valid simulation objects:

sim1 = IrreversibleHeatTransfer()                        # all defaults
sim2 = IrreversibleHeatTransfer(T_hot_initial=500)       # one override
sim3 = IrreversibleHeatTransfer(500, 250, 2.0, 1.0,      # all specified
                                 1000, "Closed")
```

Each of `sim1`, `sim2`, `sim3` is a completely independent object with its own arrays, its own temperatures, its own simulation state. Calling `sim1.step()` does not affect `sim2` at all.

---

Now read the full `__init__` method and every line is recognizable:

```python
def __init__(self, T_hot_initial=400, T_cold_initial=300,
             mass_hot=1.0, mass_cold=1.0, c_p=1000, system_type="Closed"):

    # Store input parameters on the object using self
    self.T_hot_0    = T_hot_initial     # initial hot temperature (K)
    self.T_cold_0   = T_cold_initial    # initial cold temperature (K)
    self.m_hot      = mass_hot          # mass of hot reservoir (kg)
    self.m_cold     = mass_cold         # mass of cold reservoir (kg)
    self.c_p        = c_p               # specific heat capacity (J/kg·K)
    self.system_type = system_type      # "Closed", "Open", or "Isolated"

    # Heat transfer coefficient — not a parameter, just set internally
    self.h = 50     # W/K

    # Calculate equilibrium temperature and store it
    # This calls another method on the same object using self.
    self.T_eq = self._calculate_equilibrium_temp()

    # Time parameters
    self.dt    = 0.1    # time step in seconds
    self.t_max = 200    # total simulation time in seconds

    # Create all arrays and set initial conditions
    # This calls another method on the same object using self.
    self.reset_simulation()
```

Every `self.something = value` line is storing a piece of data on the object. Later, when `step()` runs, it reads `self.m_hot`, `self.c_p`, `self.dt` to do its calculations — it does not need those values passed in as arguments because they are already stored on `self`.

---

## 9. The Second Class — `InteractiveVisualizer`

The script contains a second class that handles everything visual:

```python
class InteractiveVisualizer:
    """Interactive visualization with animation and controls."""

    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]

        # Create a simulation object and store it ON the visualizer object
        self.sim = IrreversibleHeatTransfer(system_type="Closed")

        self.setup_figure()      # build the matplotlib window
        self.is_playing = False  # animation starts paused
        self.animation  = None   # no animation object yet
```

There is something new here worth noting carefully:

```python
self.sim = IrreversibleHeatTransfer(system_type="Closed")
```

This line creates a complete `IrreversibleHeatTransfer` object — with all its arrays, temperatures, and physics — and stores it as an attribute called `self.sim` on the `InteractiveVisualizer` object.

One object holding another object as its data. This is how the two classes connect.

Later, every time the visualizer needs to run the simulation or read its data, it uses `self.sim`:

```python
self.sim.run_full_simulation()     # tell the simulation object to run
self.sim.T_hot[idx]                # read temperature data from the simulation
self.sim.current_step              # read the current step from the simulation
self.sim.h = self.slider_h.val     # write a new heat transfer coefficient
```

The dot chain `self.sim.T_hot` reads as: _"on this visualizer object, get `sim`, then on that simulation object, get `T_hot`."_

---

### The two classes and their responsibilities

||`IrreversibleHeatTransfer`|`InteractiveVisualizer`|
|---|---|---|
|**Owns**|Physics data and arrays|Matplotlib figure, axes, widgets|
|**Knows about**|Temperatures, entropy, heat flux|Sliders, buttons, plots, animation|
|**Does not know about**|Plots or visual elements|Physics equations|
|**Analogy**|The engine|The dashboard|

Neither class needs to know how the other works internally. `InteractiveVisualizer` only needs to know that calling `self.sim.step()` advances the physics by one step. It does not care how `step()` is implemented. This clean separation is one of the main reasons classes are used.

---

## 10. The Full Picture — How Objects Are Created and Used

Here is the entire creation chain when you run the script:

```python
# Bottom of the script — the entry point
if __name__ == "__main__":
    main()
```

```python
def main():
    # ...print statements...
    
    visualizer = InteractiveVisualizer()    # Step 1: create the visualizer object
    visualizer.show()                       # Step 2: display the window
```

**Step 1** triggers `InteractiveVisualizer.__init__()`, which:

- Creates `self.sim = IrreversibleHeatTransfer(...)` — triggering `IrreversibleHeatTransfer.__init__()`, which sets up all physics data and arrays
- Calls `self.setup_figure()` — building all five matplotlib axes
- Calls `self.update_simulation()` — running the full simulation once
- Calls `self.plot_all()` — drawing all five plots with the computed data

**Step 2** calls `plt.show()` — opening the interactive window and handing control to the user.

Everything in the simulation flows from those two lines in `main()`.

---

## Practice Exercise

Complete all three tasks in a new file called `practice8.py`. Do not use any physics — keep it simple.

**Task 1.** Define a class called `Reservoir` with an `__init__` method that takes `name` and `temperature` as parameters and stores them on `self`. Create two objects: one called `hot` with temperature `400`, one called `cold` with temperature `300`. Print both temperatures using dot notation.

Expected output:

```
400
300
```

**Task 2.** Add a method called `cool_down` to `Reservoir` that subtracts `10` from `self.temperature` and prints a message. Call it twice on the `hot` object and print `hot.temperature` afterward.

Expected output:

```
Hot reservoir cooling...
Hot reservoir cooling...
380
```

**Task 3.** Add a second class called `System` whose `__init__` takes no parameters but creates two `Reservoir` objects stored as `self.hot` and `self.cold`. Add a method called `describe` that prints both temperatures. Instantiate one `System` object and call `describe` on it.

Expected output:

```
Hot: 400 K
Cold: 300 K
```

This three-task sequence mirrors exactly how the simulation is structured: `IrreversibleHeatTransfer` is like `Reservoir`, and `InteractiveVisualizer` is like `System` — one class holding and managing another.

---

## Key Takeaways

- A class is a blueprint that defines what data an object holds and what actions it can perform. An object is a concrete instance built from that blueprint, holding real data.
- `__init__` is the constructor method. It runs automatically when an object is created and uses `self.attribute = value` to store data on the object.
- `self` always refers to the specific object a method is being called on. It is passed automatically by Python — you never pass it manually when calling a method.
- `IrreversibleHeatTransfer` bundles all physics data (temperatures, arrays, constants) and all physics logic (step, reset, entropy calculation) into one self-contained unit.
- `InteractiveVisualizer` owns the matplotlib figure and widgets, and holds a complete `IrreversibleHeatTransfer` object as `self.sim` — connecting the two classes cleanly without mixing their responsibilities.

---

# Lesson 9: Class Methods and Instance Attributes

---

## 1. Plain-English Concept Explanation

In Lesson 8 (classes and `__init__`), you learned that a class is a blueprint, and that `__init__` sets up the starting state of each object. But a blueprint isn't just a list of measurements — it also describes _behaviours_. A thermostat doesn't just _have_ a temperature setting; it also _does_ things: it reads the room, it turns the heater on, it resets to defaults.

In Python, those behaviours are called **methods**.

---

### Methods vs. Regular Functions

You've already seen regular functions — standalone blocks of code you define with `def` and call by name. **Methods** are functions that belong to a class. The difference isn't just organisational. A method has automatic access to the object it belongs to, through a special parameter called `self`.

```python
# A regular function — standalone, no connection to any object
def calculate_heat(h, T_h, T_c):
    return h * (T_h - T_c)

# A method — lives inside a class, receives self automatically
class HeatSystem:
    def calculate_heat(self):              # self gives access to the object
        return self.h * (self.T_h - self.T_c)
```

When you call a method on an object, Python automatically passes that object in as `self`. You never write `self` yourself when _calling_ a method — only when _defining_ one.

---

### Instance Attributes: Storing Data on `self`

An **instance attribute** is a variable that belongs to a specific object. You create one by writing `self.name = value` inside any method — usually `__init__`, but not always.

Once stored on `self`, that attribute is available to _every other method_ in the same class. This is the key point:

> `self` is the messenger that carries data between methods inside a class.

```python
class HeatSystem:
    def __init__(self):
        self.temperature = 400.0    # stored on self — available everywhere in the class

    def describe(self):
        print(self.temperature)     # can access it here, in a completely different method
```

Without `self`, you would have to pass every value as an argument every time you called a method. With `self`, you store it once and every method can reach it.

---

### Calling One Method from Inside Another

Because every method receives `self`, and `self` is the object itself, you can call any other method on that same object by writing `self.method_name()`.

```python
class HeatSystem:
    def __init__(self):
        self.temperature = 400.0

    def reset(self):
        self.temperature = 400.0          # reset the attribute

    def run(self):
        self.reset()                      # call another method from inside this one
        print("Running from", self.temperature)
```

This lets you build a **chain of method calls** — one method doing its job and then handing off to the next. This is exactly how our simulation is structured.

---

## 2. Annotated Code Examples

### Storing and reading instance attributes

```python
class ThermalReservoir:

    def __init__(self, T_hot, T_cold, mass, c_p):
        # Store every starting value on self
        # These are now "instance attributes" — they belong to this specific object
        self.T_hot = T_hot        # e.g. 400.0 K
        self.T_cold = T_cold      # e.g. 300.0 K
        self.mass = mass          # e.g. 1.0 kg
        self.c_p = c_p            # e.g. 1000.0 J/(kg·K)

    def equilibrium_temp(self):
        # self.mass, self.c_p etc. were set in __init__ — we can use them here freely
        numerator = self.mass * self.c_p * self.T_hot + \
                    self.mass * self.c_p * self.T_cold
        denominator = self.mass * self.c_p + self.mass * self.c_p
        return numerator / denominator    # returns 350.0 for the values above
```

---

### Calling one method from inside another

```python
class ThermalReservoir:

    def __init__(self, T_hot, T_cold, mass, c_p):
        self.T_hot = T_hot
        self.T_cold = T_cold
        self.mass = mass
        self.c_p = c_p
        self.T_eq = self.equilibrium_temp()   # call a method right inside __init__
                                               # result is stored as another attribute

    def equilibrium_temp(self):
        numerator = self.mass * self.c_p * self.T_hot + \
                    self.mass * self.c_p * self.T_cold
        denominator = self.mass * self.c_p + self.mass * self.c_p
        return numerator / denominator

    def report(self):
        # self.T_eq was set in __init__ by calling self.equilibrium_temp()
        # we can use it directly here — no need to recalculate
        print("Equilibrium temperature:", self.T_eq)


# Create an object and call report()
system = ThermalReservoir(400.0, 300.0, 1.0, 1000.0)
system.report()    # prints: Equilibrium temperature: 350.0
```

---

### A method that sets new attributes on `self`

Attributes don't have to be created only in `__init__`. Any method can add or update them:

```python
class ThermalReservoir:

    def __init__(self, T_hot, T_cold):
        self.T_hot = T_hot
        self.T_cold = T_cold
        # Note: self.n_steps does NOT exist yet at this point

    def setup_simulation(self, t_max, dt):
        self.t_max = t_max                       # new attribute created here
        self.n_steps = int(t_max / dt)           # another new attribute
        self.T_hot_array = [0.0] * self.n_steps  # a list with n_steps zeroes

    def describe(self):
        # self.n_steps is available here — it was set by setup_simulation()
        # BUT only if setup_simulation() was called first
        print("Number of steps:", self.n_steps)


system = ThermalReservoir(400.0, 300.0)
system.setup_simulation(200, 0.1)   # must call this before describe()
system.describe()                   # prints: Number of steps: 2000
```

> ⚠️ If you called `system.describe()` _before_ `system.setup_simulation()`, Python would crash with an `AttributeError` because `self.n_steps` wouldn't exist yet. The order in which you call methods matters.

---

## 3. How This Connects to Our Script

The simulation is built almost entirely on chained method calls and shared instance attributes. Here are the key examples.

---

### `reset_simulation()` reads attributes set by `__init__`

```python
def __init__(self, T_hot_initial=400, ...):
    # ...
    self.dt = 0.1       # time step — stored as instance attribute
    self.t_max = 200    # max simulation time — stored as instance attribute

    self.reset_simulation()    # __init__ immediately calls another method


def reset_simulation(self):
    # This method uses self.t_max and self.dt — set above in __init__
    # It does NOT receive them as arguments; it finds them on self
    self.time = np.arange(0, self.t_max, self.dt)   # uses both attributes
    self.n_steps = len(self.time)                    # creates a NEW attribute

    # These arrays are also new attributes, created here using self.n_steps
    self.T_hot = np.zeros(self.n_steps)
    self.T_cold = np.zeros(self.n_steps)
    self.S_gen_cumulative = np.zeros(self.n_steps)
```

`reset_simulation()` doesn't receive `t_max` or `dt` as parameters — it finds them already waiting on `self`, because `__init__` stored them there first.

---

### `step()` reads arrays created by `reset_simulation()`

```python
def step(self):
    # self.T_hot, self.T_cold, self.current_step — all created in reset_simulation()
    # step() can use them because they're on self
    i = self.current_step

    Q_dot = self.calculate_heat_transfer_rate(   # calling another method on self
        self.T_hot[i], self.T_cold[i]
    )

    self.T_hot[i+1] = self.T_hot[i] + ...       # updating the array in place
    self.current_step += 1                        # updating the counter attribute
```

`step()` both _reads_ from `self` and _writes back_ to `self`. Every call to `step()` leaves updated values on the object for the next call to use.

---

### `on_slider_change()` chains two method calls

This is in the `InteractiveVisualizer` class. When the user moves a slider, this method runs:

```python
def on_slider_change(self, val):
    # Step 1: Update instance attributes from the new slider values
    self.sim.T_hot_0 = self.slider_T_hot.val    # update the simulation's attribute
    self.sim.T_cold_0 = self.slider_T_cold.val
    self.sim.h = self.slider_h.val
    self.sim.m_hot = self.slider_mass_ratio.val
    self.sim.m_cold = 1.0

    # Step 2: Recalculate equilibrium temperature (calls a method on self.sim)
    self.sim.T_eq = self.sim._calculate_equilibrium_temp()

    # Step 3: Re-run the simulation with the new values
    self.update_simulation()    # calls a method on self (the visualizer)

    # Step 4: Redraw all the plots
    self.plot_all()             # calls another method on self
```

Notice `self.sim` — the visualizer object _contains_ the simulation object as one of its own attributes. It accesses the simulation's methods via `self.sim.method_name()`.

---

### The full method call chain in `InteractiveVisualizer`

Here's the sequence that runs when the user moves a slider:

```
on_slider_change()
    └── self.update_simulation()
            └── self.sim.run_full_simulation()
                        └── self.sim.reset_simulation()
                        └── self.sim.step()  ← called 2000 times
    └── self.plot_all()
            └── self.plot_reservoir_visual()
            └── self.plot_temperature()
            └── self.plot_heat_transferred()
            └── self.plot_entropy()
            └── self.plot_heat_flux()
```

Each method does one job, then calls the next. No single method tries to do everything. This is one of the main reasons classes and methods are useful — they let you break a complex task into small, named, reusable steps.

---

## 4. Practice Exercise

**Goal:** Build a small two-class system where methods share data through `self` and call each other.

```python
class Reservoir:

    def __init__(self, temperature, mass, c_p):
        # Store starting values as instance attributes
        self.temperature = temperature    # Kelvin
        self.mass = mass                  # kg
        self.c_p = c_p                    # J/(kg·K)
        self.energy = self.calculate_energy()   # call a method inside __init__

    def calculate_energy(self):
        # Uses attributes stored by __init__
        return self.mass * self.c_p * self.temperature   # J

    def describe(self):
        # Uses attributes stored by __init__ and calculate_energy (via self.energy)
        print(f"Temperature: {self.temperature} K")
        print(f"Energy: {self.energy} J")


class TwoReservoirSystem:

    def __init__(self, T_hot, T_cold):
        # Store two Reservoir objects as instance attributes
        self.hot = Reservoir(T_hot, 1.0, 1000.0)
        self.cold = Reservoir(T_cold, 1.0, 1000.0)

    def equilibrium_temp(self):
        # Access the hot and cold reservoirs through self
        total_energy = self.hot.energy + self.cold.energy
        total_capacity = (self.hot.mass * self.hot.c_p +
                          self.cold.mass * self.cold.c_p)
        return total_energy / total_capacity

    def report(self):
        print("--- Hot Reservoir ---")
        self.hot.describe()              # call a method on the nested object
        print("--- Cold Reservoir ---")
        self.cold.describe()
        print(f"Equilibrium temp: {self.equilibrium_temp()} K")   # call own method


# --- Run it ---
system = TwoReservoirSystem(400.0, 300.0)
system.report()
```

**Then try:**

1. Change `T_hot` to `500.0` — how does `equilibrium_temp()` change?
2. Add a method `temperature_gap()` to `TwoReservoirSystem` that returns `self.hot.temperature - self.cold.temperature`, then call it from `report()`.
3. What happens if you call `system.hot.describe()` directly from outside the class?

---

## 5. Key Takeaways

- **Methods** are functions that belong to a class. They always receive `self` as their first parameter, giving them automatic access to the object's data.
- **Instance attributes** are variables stored on `self`. Set them in any method with `self.name = value` — once set, they're accessible in every other method of the same class.
- One method can **call another method** on the same object using `self.method_name()`. This lets you break complex behaviour into small, named steps.
- The **order of method calls matters**. If method B reads an attribute that method A creates, you must call A before B — otherwise Python raises an `AttributeError`.
- In our script, the entire simulation runs through a **chain of method calls**: a slider change triggers `on_slider_change()`, which calls `update_simulation()`, which calls `run_full_simulation()`, which calls `reset_simulation()` and then `step()` thousands of times — each method doing one job and passing results forward via `self`.

---

# Lesson 10: Importing Libraries and Modules

---

## 1. Plain-English Concept Explanation

### What is a Library?

When you install Python, you get the core language — basic tools like variables, loops, and functions. But Python's real power comes from **libraries**: collections of pre-written code that other developers have built, tested, and made available for anyone to use.

Think of a library like a toolbox someone else assembled. Instead of building a hammer from scratch, you open the toolbox and use the one that's already there.

A **module** is a single file of Python code inside a library. A library may contain many modules, each focused on a specific area. You will sometimes hear the words _library_, _module_, and _package_ used interchangeably in casual conversation — the distinction matters more as you advance, but for now, think of them all as _collections of reusable tools_.

---

### What Does `import` Do?

The keyword **`import`** tells Python: _"go find this library and make its tools available in my script."_ Until you import a library, Python has no idea it exists — even if it's installed on your computer.

Importing does not slow your program down meaningfully. It simply loads the tools you need into memory at the start of your script.

---

### `import numpy` vs. `import numpy as np`

When you write `import numpy`, you can use its tools — but you must type the full word `numpy` every time:

```python
import numpy
array = numpy.zeros(5)   # works, but verbose
```

When you write `import numpy as np`, the `as np` part creates a **shorthand alias** — a nickname. Now you type `np` instead of `numpy` every time:

```python
import numpy as np
array = np.zeros(5)      # same result, less typing
```

The alias is just a convenience. `np` for NumPy and `plt` for Matplotlib's pyplot are conventions so widely used that you will see them in virtually every scientific Python script ever written. Using them makes your code immediately recognizable to other Python programmers.

---

### Importing Specific Tools with `from`

Sometimes you only need _one specific tool_ from a large library. Instead of importing the whole thing, you can use `from` to import just that piece:

```python
from matplotlib.animation import FuncAnimation
```

This means: _"go into the `matplotlib` library, find the `animation` module inside it, and from that module bring in only `FuncAnimation`."_

After this line, you use `FuncAnimation` directly — no prefix needed. This keeps your code cleaner when you only need one or two specific tools from a large library.

---

### How to Read Library Documentation

Every major Python library has **documentation** — a website where all its tools are listed and explained. When you encounter a function you don't recognize, the documentation is the authoritative source for understanding what it does and how to use it.

The most useful documentation sites for our script are:

- NumPy: `numpy.org/doc`
- Matplotlib: `matplotlib.org/stable/api`

When reading documentation, focus on three things:

1. **What the function does** — the plain-English description at the top
2. **Parameters** — what inputs it accepts and what each one means
3. **Examples** — working code snippets near the bottom of each entry

You do not need to memorize documentation. Professional programmers look things up constantly. The skill is knowing _where_ to look and _what_ you're reading when you find it.

---

## 2. Annotated Code Examples

### Basic Import Styles

```python
# Style 1: import the whole library, use full name each time
import numpy
array = numpy.zeros(5)        # creates an array of five 0.0 values

# Style 2: import with an alias (shorthand nickname)
import numpy as np
array = np.zeros(5)           # identical result, less typing

# Style 3: import one specific tool from a module
from matplotlib.animation import FuncAnimation
# Now FuncAnimation is available directly — no prefix needed
anim = FuncAnimation(...)
```

---

### What Happens if You Forget to Import

```python
# If you try to use numpy without importing it first:
array = np.zeros(5)
# Python raises: NameError: name 'np' is not defined
# This is one of the most common beginner errors — always check your imports
```

---

### Checking What a Library Gives You

```python
import numpy as np

# dir() lists everything available inside a library or object
# This is a useful exploration tool — output will be long
print(dir(np))

# help() prints the documentation for a specific function right in your terminal
help(np.zeros)
```

> **Note:** `help()` and `dir()` work in any Python environment, but the output is most readable in a terminal. In some environments the output may be very long — that is normal.

---

## 3. How This Connects to Our Script

Here are the exact import lines from the top of the simulation script, explained one by one:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches
```

---

### `import numpy as np`

**NumPy** (Numerical Python) is the foundation of scientific computing in Python. Its most important contribution is the **array** — a fast, efficient list of numbers that supports mathematical operations across all its values at once.

In our script, NumPy is used to:

```python
# Create the time axis — a sequence of evenly spaced time values
# np.arange(start, stop, step) is like range() but for decimal numbers
self.time = np.arange(0, self.t_max, self.dt)
# Result: [0.0, 0.1, 0.2, 0.3, ..., 199.9]

# Create empty arrays to store temperatures and entropy at every time step
self.T_hot = np.zeros(self.n_steps)    # fills an array with 0.0 values
self.T_cold = np.zeros(self.n_steps)   # one slot per time step

# np.clip() keeps a value within a minimum and maximum boundary
normalized = np.clip(normalized, 0, 1)  # used in color calculations
```

Without NumPy, storing and manipulating thousands of temperature values efficiently would require much more complex code.

---

### `import matplotlib.pyplot as plt`

**Matplotlib** is Python's most widely used plotting library. The `pyplot` module inside it provides a collection of functions for creating charts and graphs. The alias `plt` is a universal convention.

In our script, `plt` is used to:

```python
# Create the entire figure (the window) and set its size
self.fig = plt.figure(figsize=(16, 10))

# Create a set of axes (a specific chart area) inside the figure
# add_gridspec divides the figure into a grid for multiple plots
gs = self.fig.add_gridspec(3, 3, ...)

# Add an individual subplot to the grid
self.ax_temp = self.fig.add_subplot(gs[1, :2])

# Create a slider widget (covered more in the widgets import below)
ax_T_hot = plt.axes([0.15, 0.15, 0.25, 0.02], ...)

# Display the completed figure in a window on screen
plt.show()
```

`plt` builds the visual container. The individual plot axes (`ax_temp`, `ax_entropy`, etc.) are then used to draw specific data into specific panels.

---

### `from matplotlib.animation import FuncAnimation`

`FuncAnimation` is a single class inside Matplotlib's `animation` module. It handles the mechanics of animation — repeatedly calling a function at a set time interval to create the appearance of movement.

In our script, it is used in exactly one place:

```python
# FuncAnimation needs:
# - self.fig      → the figure window to animate
# - self.animate  → the function to call on each frame
# - interval=50   → wait 50 milliseconds between frames (~20 frames per second)
# - blit=False    → redraw the entire figure each frame (simpler but slower than True)
self.animation = FuncAnimation(
    self.fig,
    self.animate,
    interval=50,
    blit=False
)
```

Every time the timer ticks, `FuncAnimation` calls `self.animate()`, which advances the simulation by 5 steps and redraws all the plots. This is what makes the temperature curves grow in real time.

---

### `from matplotlib.widgets import Slider, Button`

The `widgets` module inside Matplotlib provides **interactive controls** — graphical elements the user can click or drag to change values while the program is running.

Our script imports two widgets:

```python
# Slider — a draggable bar that produces a number when moved
# Used four times: T_hot, T_cold, heat transfer coefficient, mass ratio
self.slider_T_hot = Slider(
    ax_T_hot,          # the axes region where the slider will appear
    'T_hot (K)',       # label shown next to the slider
    310,               # minimum value
    500,               # maximum value
    valinit=self.sim.T_hot_0,   # starting position
    valstep=10         # snaps to multiples of 10
)

# Button — a clickable button that triggers a function when pressed
# Used twice: Play/Pause and Reset
self.btn_play = Button(ax_play, 'Play/Pause')
self.btn_reset = Button(ax_reset, 'Reset')
```

When the user drags a slider, the slider calls `self.on_slider_change()` automatically, which updates the simulation parameters and reruns everything.

---

### `import matplotlib.patches as patches`

The `patches` module provides **geometric shapes** that can be drawn directly onto a plot — rectangles, circles, arrows, and more.

In our script, it draws the visual representation of the two reservoirs:

```python
# patches.Rectangle(corner_position, width, height, ...)
# Draws a filled rectangle to represent the hot reservoir
hot_rect = patches.Rectangle(
    (1, 0.5),          # (x, y) position of the bottom-left corner
    2,                 # width
    2,                 # height
    facecolor=temp_to_color(T_h),   # fill color based on temperature
    edgecolor='black',
    linewidth=2
)
self.ax_visual.add_patch(hot_rect)   # add the shape to the plot

# patches.FancyArrowPatch draws the heat flow arrow between reservoirs
arrow = patches.FancyArrowPatch(
    (3.2, 1.5),        # arrow start point
    (6.8, 1.5),        # arrow end point
    arrowstyle='->',
    mutation_scale=30,
    color='red'
)
```

Without `patches`, the reservoir visualization would be plain text labels on a blank background.

---

## 4. Practice Exercise

Try this in a new Python file. It should take under 10 minutes.

**Task:** Write a short script that:

1. Imports NumPy as `np` and Matplotlib's pyplot as `plt`
2. Creates a NumPy array of time values from `0` to `10` in steps of `0.5` using `np.arange()`
3. Creates a second array where every value is the time value multiplied by `2` (NumPy lets you do this in one line — no loop needed)
4. Plots time on the x-axis and your second array on the y-axis using `plt.plot()`
5. Adds a title with `plt.title()` and axis labels with `plt.xlabel()` and `plt.ylabel()`
6. Displays the result with `plt.show()`

**Starter hint:**

```python
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.5)
values = time * 2          # NumPy applies * 2 to every element at once

# your plotting code here
```

> **Environment note:** This exercise requires NumPy and Matplotlib to be installed on your computer. If you see `ModuleNotFoundError`, you may need to install them first. In a terminal, run `pip install numpy matplotlib` and try again.

---

## 5. Key Takeaways

- **`import`** makes a library's tools available in your script. Python cannot use a library — even if it's installed — until you import it.
- Writing **`import numpy as np`** creates a shorthand alias. `np` and `plt` are universal conventions in scientific Python — you will see them in nearly every script in this field.
- **`from library import tool`** brings in one specific item without loading everything. It is used in our script for `FuncAnimation`, `Slider`, and `Button` because only those specific tools are needed from their respective modules.
- Our script relies on four libraries with distinct roles: **NumPy** handles numerical arrays, **Matplotlib pyplot** builds the figure and plots, **FuncAnimation** drives the animation loop, and **Widgets** provide the interactive sliders and buttons.
- When you encounter an unfamiliar function, the library's official documentation is the most reliable place to understand it. Focus on the description, parameters, and code examples — you do not need to read everything.

---

# Lesson 11: Introduction to Matplotlib — Making Your First Static Plot

---

## 1. Plain-English Concept Explanation

So far, your Python programs have produced text output. But our thermodynamics simulation is built around _visual_ output — animated charts that update in real time. To get there, we first need to understand the tool that draws them: **Matplotlib**.

### What is Matplotlib?

**Matplotlib** is a Python library (a collection of pre-written code you can borrow) that draws charts and graphs. It is not part of Python itself — it's a separate package that was installed alongside Python on your machine. You bring it into your script with an `import` statement.

The part of Matplotlib we'll use most is called **pyplot**, which provides a straightforward set of functions for building plots. By convention, everyone imports it with the shorthand `plt`:

```python
import matplotlib.pyplot as plt
```

From this point on, `plt.something()` gives you access to all of pyplot's drawing tools.

---

### The Figure and Axes Model

This is the most important mental model in Matplotlib, and it confuses nearly every beginner, so read this slowly.

Matplotlib uses two layers:

|Term|Real-World Analogy|What It Does|
|---|---|---|
|**Figure**|The picture frame, or the whole sheet of paper|The outer container for everything|
|**Axes**|One individual chart drawn on that paper|The actual plot area with its own x-axis, y-axis, title, and data|

One Figure can contain multiple Axes (i.e., multiple charts side by side). Our simulation has **one Figure** containing **five Axes** — one for each chart panel.

```
┌─────────────────── Figure ───────────────────────┐
│  ┌──────────── Axes 1 ────────────┐               │
│  │  Temperature vs Time           │               │
│  └────────────────────────────────┘               │
│  ┌──── Axes 2 ────┐  ┌── Axes 3 ──┐              │
│  │  Heat Transfer │  │  Entropy   │              │
│  └────────────────┘  └────────────┘              │
└──────────────────────────────────────────────────┘
```

---

### The Functions You'll Use

|Function|What It Does|
|---|---|
|`plt.plot()`|Draws a line on the current Axes|
|`plt.xlabel()`|Labels the horizontal (x) axis|
|`plt.ylabel()`|Labels the vertical (y) axis|
|`plt.title()`|Adds a title above the chart|
|`plt.legend()`|Adds a key explaining what each line means|
|`plt.grid()`|Adds faint background gridlines|
|`plt.show()`|Renders and displays the finished figure|

---

## 2. Annotated Code Examples

### Example A — Your very first plot

```python
# Import the pyplot module from the matplotlib library.
# "as plt" means we can type plt instead of matplotlib.pyplot every time.
import matplotlib.pyplot as plt

# Some simple data to plot.
# In Python, a list is a collection of values inside square brackets.
time = [0, 1, 2, 3, 4, 5]          # x-axis values (seconds)
temperature = [400, 375, 355, 340, 330, 322]  # y-axis values (Kelvin)

# plt.plot() draws a line connecting the x and y data points.
# First argument: x values. Second argument: y values.
plt.plot(time, temperature)

# Add a label to the x-axis.
plt.xlabel("Time (s)")

# Add a label to the y-axis.
plt.ylabel("Temperature (K)")

# Add a title above the chart.
plt.title("Hot Reservoir Cooling Down")

# Display the finished plot on screen.
# Without this line, nothing appears.
plt.show()
```

> **Environment note:** `plt.show()` opens an interactive window on your computer. If you are working inside a Jupyter Notebook, you may see the plot appear inline without needing `plt.show()` — but including it never hurts.

---

### Example B — Styling your line and adding a legend

```python
import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5]
T_hot =  [400, 375, 355, 340, 330, 322]
T_cold = [300, 318, 332, 342, 349, 354]

# The third argument is a format string that controls appearance.
# 'r-'  means red  (r) solid line  (-)
# 'b-'  means blue (b) solid line  (-)
# 'g--' means green (g) dashed line (--)
# "label" is the text that will appear in the legend.
plt.plot(time, T_hot,  'r-', linewidth=2, label='Hot Reservoir')
plt.plot(time, T_cold, 'b-', linewidth=2, label='Cold Reservoir')

# Add a horizontal dashed line at the equilibrium temperature.
# axhline draws a line spanning the full width of the chart.
# "linestyle='--'" makes it dashed. "label" adds it to the legend too.
plt.axhline(350, color='green', linestyle='--', linewidth=2, label='Equilibrium')

plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.title("Temperature Evolution")

# plt.legend() reads all the "label" arguments and builds the key automatically.
# loc='best' tells Matplotlib to place it wherever it fits without covering data.
plt.legend(loc='best')

# plt.grid() adds faint background lines to make values easier to read.
# alpha controls transparency: 0.0 is invisible, 1.0 is fully solid.
plt.grid(True, alpha=0.3)

plt.show()
```

---

### Example C — The explicit Figure and Axes approach

The examples above use a shortcut where `plt` manages the Figure and Axes for you behind the scenes. In our simulation, the code is more explicit, creating the Figure and Axes directly. Here is what that looks like and why:

```python
import matplotlib.pyplot as plt

# plt.figure() creates a blank Figure — the outer container.
# figsize=(width, height) controls the size in inches.
fig = plt.figure(figsize=(10, 5))

# fig.add_subplot(rows, cols, position) adds one Axes to the Figure.
# (1, 2, 1) means: a 1-row, 2-column grid — this is the 1st slot.
ax1 = fig.add_subplot(1, 2, 1)

# (1, 2, 2) means: same grid — this is the 2nd slot.
ax2 = fig.add_subplot(1, 2, 2)

# When using explicit Axes objects, you call methods ON the Axes,
# not on plt directly. ax1.plot() instead of plt.plot().
time = [0, 1, 2, 3, 4, 5]
T_hot  = [400, 375, 355, 340, 330, 322]
T_cold = [300, 318, 332, 342, 349, 354]

# Draw on the first Axes (left chart).
ax1.plot(time, T_hot, 'r-', linewidth=2, label='Hot')
ax1.plot(time, T_cold, 'b-', linewidth=2, label='Cold')

# Notice: ax1.set_xlabel() not plt.xlabel() — the "set_" prefix is used
# when working directly with an Axes object.
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (K)")
ax1.set_title("Temperatures")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Draw on the second Axes (right chart).
heat = [0, 250, 450, 610, 730, 820]
ax2.plot(time, heat, 'purple', linewidth=2)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Heat (J)")
ax2.set_title("Heat Transferred")
ax2.grid(True, alpha=0.3)

plt.show()
```

> **Key distinction:** When using `plt.something()` directly, Matplotlib manages one implicit Axes for you. When you create multiple Axes yourself, you call `ax.set_title()`, `ax.set_xlabel()` etc. on each Axes individually. You will see both styles in the simulation.

---

### Example D — Clearing an Axes before redrawing

Our simulation redraws its charts constantly as the animation runs. If you didn't clear first, old lines would pile up on top of new ones. The fix is one line:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # A shorthand that creates Figure + one Axes together.

# First draw.
ax.plot([0, 1, 2], [400, 375, 355], 'r-')
ax.set_title("First Draw")
plt.pause(1)  # Pause for 1 second so you can see it (used in animations).

# Clear the Axes completely before drawing again.
# This wipes all lines, labels, and titles from this Axes only.
ax.clear()

# Second draw on the same (now blank) Axes.
ax.plot([0, 1, 2], [300, 318, 332], 'b-')
ax.set_title("Second Draw — Previous Line Is Gone")

plt.show()
```

---

## 3. How This Connects to Our Script

Every chart panel in the simulation is drawn by a dedicated function. Each one follows the same pattern: **clear → plot → label → style**. Here they are with the concepts from this lesson highlighted:

---

### `plot_temperature()`

```python
def plot_temperature(self):
    # Step 1: Clear — wipe the Axes so old lines don't accumulate.
    self.ax_temp.clear()

    # idx tracks how far through the simulation we currently are.
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    # Step 2: Plot — draw two lines, one red (hot) and one blue (cold).
    # Only data up to the current step is shown: [:idx+1] is a slice.
    self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_hot[:idx+1],
                     'r-', linewidth=2, label='Hot Reservoir')
    self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_cold[:idx+1],
                     'b-', linewidth=2, label='Cold Reservoir')

    # Draw a horizontal dashed green line at the equilibrium temperature.
    self.ax_temp.axhline(self.sim.T_eq, color='green', linestyle='--',
                        linewidth=2, label='Equilibrium')

    # Step 3: Label — x-axis, y-axis, and title using the set_ prefix.
    self.ax_temp.set_xlabel('Time (s)', fontsize=11)
    self.ax_temp.set_ylabel('Temperature (K)', fontsize=11)
    self.ax_temp.set_title('Temperature Evolution (Irreversible Process)', fontsize=12)

    # Step 4: Style — legend, grid, and fixed x-axis range.
    self.ax_temp.legend(loc='best')
    self.ax_temp.grid(True, alpha=0.3)
    self.ax_temp.set_xlim(0, self.sim.t_max)  # Keep x-axis stable during animation.
```

---

### `plot_heat_transferred()`, `plot_entropy()`, `plot_heat_flux()`

These three functions follow the exact same four-step pattern. The only differences are which data array is plotted, the line colour, and the axis labels:

```python
def plot_heat_transferred(self):
    self.ax_heat.clear()
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    # Q_transferred is divided by 1000 to convert Joules → kilojoules.
    self.ax_heat.plot(self.sim.time[:idx+1],
                     self.sim.Q_transferred[:idx+1] / 1000,
                     'purple', linewidth=2)

    self.ax_heat.set_xlabel('Time (s)', fontsize=11)
    self.ax_heat.set_ylabel('Heat (kJ)', fontsize=11)
    self.ax_heat.set_title('Cumulative Heat\nTransferred', fontsize=12)
    self.ax_heat.grid(True, alpha=0.3)
    self.ax_heat.set_xlim(0, self.sim.t_max)

def plot_entropy(self):
    self.ax_entropy.clear()
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    # Entropy generation is plotted in orange.
    self.ax_entropy.plot(self.sim.time[:idx+1],
                        self.sim.S_gen_cumulative[:idx+1],
                        'orange', linewidth=2, label='Total Entropy Generated')

    self.ax_entropy.set_xlabel('Time (s)', fontsize=11)
    self.ax_entropy.set_ylabel('Entropy Generation (J/K)', fontsize=11)
    self.ax_entropy.set_title('Entropy Generation (Irreversibility Measure)', fontsize=12)
    self.ax_entropy.grid(True, alpha=0.3)
    self.ax_entropy.set_xlim(0, self.sim.t_max)

def plot_heat_flux(self):
    self.ax_flux.clear()
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    self.ax_flux.plot(self.sim.time[:idx+1],
                     self.sim.heat_flux[:idx+1],
                     'darkgreen', linewidth=2)

    self.ax_flux.set_xlabel('Time (s)', fontsize=11)
    self.ax_flux.set_ylabel('Heat Flux (W)', fontsize=11)
    self.ax_flux.set_title('Instantaneous\nHeat Transfer Rate', fontsize=12)
    self.ax_flux.grid(True, alpha=0.3)
    self.ax_flux.set_xlim(0, self.sim.t_max)
```

Notice how each function is self-contained. If one chart breaks, it doesn't affect the others — a direct payoff of the function design from Lesson 7.

---

## 4. Practice Exercise

Write a script that produces a single figure with **two side-by-side charts** using the sample data below.

**Left chart:** Plot both temperature arrays on the same Axes. Use red for hot, blue for cold. Add a legend, grid, x-label, y-label, and title.

**Right chart:** Plot heat transferred. Use a purple line. Add a grid, x-label, y-label, and title.

```python
import matplotlib.pyplot as plt

# Sample data — don't change these.
time        = [0, 10, 20, 30, 40, 50]
T_hot       = [400, 378, 360, 346, 335, 326]
T_cold      = [300, 318, 333, 344, 353, 360]
heat_kJ     = [0.0, 1.1, 2.0, 2.7, 3.2, 3.6]

# Your code here.
# Hint: use fig = plt.figure() and fig.add_subplot()
# or look up plt.subplots(1, 2) as a shorthand.
```

**Expected result:** A window with two labelled, titled, gridded charts side by side.

---

## 5. Key Takeaways

- **Matplotlib's pyplot** (`import matplotlib.pyplot as plt`) is the standard tool for drawing charts in Python. It must be imported before use.
- **Figure is the container; Axes is the chart.** One Figure can hold many Axes. This is how the simulation displays five panels in one window.
- **When working with explicit Axes objects**, use `ax.set_xlabel()`, `ax.set_title()` etc. — not `plt.xlabel()`. Both work, but the `ax.set_` style is necessary when you have multiple charts.
- **`ax.clear()` wipes an Axes before redrawing** — essential in animations where charts update continuously, otherwise old lines stack up.
- **Each plot function in the simulation follows the same pattern:** clear → plot → label → style. Recognising this pattern makes the whole script much easier to read.

---

# Lesson 12: Subplots and Figure Layout with GridSpec

---

## 1. Plain-English Concept Explanation

So far, you've likely seen plots that show a single chart in a single window. But our thermodynamics script needs to show **five different charts at the same time** — temperatures, heat flow, entropy, and more — all visible together in one window.

To do this, matplotlib lets you divide a figure (the whole window) into a **grid of cells**, and then place individual charts (called **axes**) into those cells. The tool that controls this grid is called **GridSpec**.

Think of it like designing a newspaper layout:

- The **figure** is the full page
- **GridSpec** draws the invisible grid lines on that page
- Each **subplot** (axes) is an article placed into one or more grid cells

Here are the key terms you'll need:

|Term|What it means|
|---|---|
|**Figure**|The entire window that matplotlib opens|
|**Axes**|A single chart/plot area inside the figure|
|**Subplot**|Another word for an axes placed inside a grid|
|**GridSpec**|A system for dividing the figure into rows and columns|
|**hspace**|Vertical breathing room _between_ rows of plots|
|**wspace**|Horizontal breathing room _between_ columns of plots|
|**left/right/top/bottom**|How close the grid gets to the edges of the figure|

---

## 2. Annotated Code Examples

### Step 1 — Creating a figure

```python
import matplotlib.pyplot as plt  # Import the plotting library, nickname 'plt'

fig = plt.figure(figsize=(16, 10))  # Create a blank window
                                    # figsize=(width, height) in inches
                                    # (16, 10) makes a wide, landscape window
```

> `fig` is a variable that holds the whole window. Nothing is drawn yet — it's a blank canvas.

---

### Step 2 — Creating a GridSpec grid

```python
gs = fig.add_gridspec(
    3,              # Number of ROWS in the grid
    3,              # Number of COLUMNS in the grid
    hspace=0.35,    # Vertical gap between rows (as a fraction of plot height)
    wspace=0.3,     # Horizontal gap between columns (as a fraction of plot width)
    left=0.08,      # How far the grid starts from the LEFT edge (0.0 to 1.0)
    right=0.95,     # How far the grid extends toward the RIGHT edge
    top=0.92,       # How far the grid extends toward the TOP edge
    bottom=0.25     # How far the grid starts from the BOTTOM edge
                    # (leaving space at the bottom for sliders, added later)
)
```

> This creates an invisible 3-row × 3-column grid over your figure. The `left`, `right`, `top`, `bottom` values are **fractions** of the figure size. For example, `bottom=0.25` means: "start the grid 25% up from the bottom" — reserving that 25% for the slider controls.

Here's a visual of what that 3×3 grid looks like:

```
Columns:   0          1          2
         ┌──────────┬──────────┬──────────┐
Row 0    │  [0,0]   │  [0,1]   │  [0,2]   │
         ├──────────┼──────────┼──────────┤
Row 1    │  [1,0]   │  [1,1]   │  [1,2]   │
         ├──────────┼──────────┼──────────┤
Row 2    │  [2,0]   │  [2,1]   │  [2,2]   │
         └──────────┴──────────┴──────────┘
```

---

### Step 3 — Placing subplots into grid cells

```python
# Span ALL three columns of row 0 (one wide plot across the top)
ax_visual = fig.add_subplot(gs[0, :])
#                               ^  ^
#                           row 0  : means ALL columns

# Span columns 0 and 1 of row 1 (a medium-width plot)
ax_temp = fig.add_subplot(gs[1, :2])
#                              ^  ^^
#                          row 1  columns 0 and 1 (NOT column 2)

# Occupy only column 2 of row 1 (a narrow plot)
ax_heat = fig.add_subplot(gs[1, 2])
#                              ^  ^
#                          row 1  column 2 only

# Span columns 0 and 1 of row 2
ax_entropy = fig.add_subplot(gs[2, :2])

# Occupy only column 2 of row 2
ax_flux = fig.add_subplot(gs[2, 2])
```

> The slicing syntax `gs[row, column]` works just like selecting items from a list. A colon `:` means "all of them." `:2` means "up to but not including index 2" — so columns 0 and 1.

Here's what those five axes look like in the grid:

```
         Col 0         Col 1         Col 2
       ┌─────────────────────────────────────┐
Row 0  │           ax_visual (full width)    │
       ├───────────────────────┬─────────────┤
Row 1  │   ax_temp (2 cols)    │   ax_heat   │
       ├───────────────────────┼─────────────┤
Row 2  │  ax_entropy (2 cols)  │   ax_flux   │
       └───────────────────────┴─────────────┘
           [below grid: space for sliders]
```

---

### Step 4 — Adding a title to the whole figure

```python
fig.suptitle(
    'Irreversible Heat Transfer: Hot and Cold Reservoirs',  # Title text
    fontsize=16,        # Text size in points
    fontweight='bold'   # Makes the text bold
)
```

> `suptitle` means "super title" — a title for the _entire figure_, sitting above all subplots. This is different from `ax.set_title()`, which titles just one individual subplot.

---

### Putting it all together — minimal working example

```python
import matplotlib.pyplot as plt  # Import matplotlib

fig = plt.figure(figsize=(16, 10))  # Create the window

fig.suptitle('My Multi-Plot Figure', fontsize=16, fontweight='bold')  # Figure title

# Create a 3x3 grid with spacing and margin settings
gs = fig.add_gridspec(3, 3,
                      hspace=0.35,
                      wspace=0.3,
                      left=0.08, right=0.95,
                      top=0.92, bottom=0.25)

# Place five axes using grid slicing
ax_visual  = fig.add_subplot(gs[0, :])   # Full-width top row
ax_temp    = fig.add_subplot(gs[1, :2])  # Left 2/3 of middle row
ax_heat    = fig.add_subplot(gs[1, 2])   # Right 1/3 of middle row
ax_entropy = fig.add_subplot(gs[2, :2])  # Left 2/3 of bottom row
ax_flux    = fig.add_subplot(gs[2, 2])   # Right 1/3 of bottom row

# Give each axes a simple title so we can see them
ax_visual.set_title('Reservoir Visualization')
ax_temp.set_title('Temperature')
ax_heat.set_title('Heat')
ax_entropy.set_title('Entropy')
ax_flux.set_title('Heat Flux')

plt.show()  # Open the window and display it
```

Run this and you should see five labeled, empty chart areas arranged exactly as described.

---

## 3. How This Connects to Our Script

This is the **exact structure** used in the `setup_figure()` method of the `InteractiveVisualizer` class. Here's that method with fresh eyes:

```python
def setup_figure(self):
    """Create the figure with subplots and controls."""

    # Step 1: Create the window (16 inches wide, 10 inches tall)
    self.fig = plt.figure(figsize=(16, 10))

    # Step 2: Add a title across the whole window
    self.fig.suptitle('Irreversible Heat Transfer: Hot and Cold Reservoirs',
                      fontsize=16, fontweight='bold')

    # Step 3: Build a 3×3 grid
    # bottom=0.25 reserves the bottom 25% for sliders and buttons (Lesson 13)
    gs = self.fig.add_gridspec(3, 3,
                                hspace=0.35, wspace=0.3,
                                left=0.08, right=0.95,
                                top=0.92, bottom=0.25)

    # Step 4: Assign each axes to a grid region
    self.ax_visual  = self.fig.add_subplot(gs[0, :])   # Reservoir diagram (full width)
    self.ax_temp    = self.fig.add_subplot(gs[1, :2])  # Temperature over time
    self.ax_heat    = self.fig.add_subplot(gs[1, 2])   # Total heat transferred
    self.ax_entropy = self.fig.add_subplot(gs[2, :2])  # Entropy generation
    self.ax_flux    = self.fig.add_subplot(gs[2, 2])   # Instantaneous heat flux

    # (slider and button setup continue after this — covered in Lesson 13)
    self.setup_sliders()
    self.setup_buttons()

    # Run and display everything
    self.update_simulation()
    self.plot_all()
```

Notice that all five axes are stored as `self.ax_visual`, `self.ax_temp`, etc. — using `self.` makes them available to _every other method_ in the class. When `plot_temperature()` runs later, it knows exactly which axes to draw on because `self.ax_temp` was defined here.

---

## 4. Practice Exercise

**Goal:** Build the five-panel layout from scratch, without copying from the script.

1. Create a new Python file called `layout_practice.py`
2. Import `matplotlib.pyplot as plt`
3. Create a figure with `figsize=(14, 8)`
4. Add a `suptitle` of your choice
5. Create a `3x3` GridSpec with `hspace=0.4`, `wspace=0.3`, `bottom=0.1`
6. Add these five subplots:
    - `ax_top` → row 0, all columns
    - `ax_mid_left` → row 1, columns 0 and 1
    - `ax_mid_right` → row 1, column 2
    - `ax_bot_left` → row 2, columns 0 and 1
    - `ax_bot_right` → row 2, column 2
7. Give each axes a `set_title()` with a descriptive name
8. Call `plt.show()`

**Stretch challenge:** Try changing `bottom=0.1` to `bottom=0.4` and observe how much space is reserved at the bottom. Then try `hspace=0.0` and see what happens to the spacing between rows.

---

## 5. Key Takeaways

- **`plt.figure()`** creates the blank window; **`figsize`** sets its width and height in inches.
- **`add_gridspec(rows, cols)`** divides the figure into an invisible grid — nothing is drawn until you call `add_subplot()`.
- **`gs[row, col]`** selects a grid cell; the colon `:` lets a subplot span multiple columns (e.g., `gs[0, :]` spans all three columns).
- **`hspace` and `wspace`** add breathing room between plots; **`left`, `right`, `top`, `bottom`** control how close the grid gets to the figure edges — `bottom=0.25` specifically reserves space for the sliders added in the next lesson.
- All five axes are stored as `self.ax_*` attributes inside the class so that every other method can access and draw on them later.

---

# Lesson 13: Drawing Shapes and Annotations with Matplotlib Patches

---

## Learning Objective

By the end of this lesson, you will be able to draw rectangles and arrows on a Matplotlib axes using `matplotlib.patches`, add styled text annotations using `ax.text()` and the `bbox` dictionary, and fully read and modify the `plot_reservoir_visual()` method that renders the animated reservoir diagram in the simulation.

---

## 1. What Are Matplotlib Patches?

So far in this course, Matplotlib has been used to plot data — lines on axes representing numbers changing over time. But Matplotlib can also draw **shapes** directly onto a figure: rectangles, circles, arrows, polygons, ellipses, and more.

These shapes are called **patches**.

The word "patch" in Matplotlib means any 2D artist that fills an area or draws a geometric shape. Patches are not tied to data arrays. You position them using coordinates you specify directly, which makes them ideal for diagrams, illustrations, and visual annotations.

The patches module is imported like this:

```python
import matplotlib.patches as patches
```

After this import, every shape class lives under the `patches.` namespace:

- `patches.Rectangle()`
- `patches.Circle()`
- `patches.FancyArrowPatch()`
- `patches.Ellipse()`
- `patches.Polygon()`

This lesson covers the two that appear in the simulation: `Rectangle` and `FancyArrowPatch`.

---

## 2. Setting Up a Canvas for Drawing

Before drawing any shape, you need a Matplotlib axes to draw on. The key detail for patch-based diagrams is that you usually want to **turn off the axis lines and tick marks** — they are distracting when you are drawing a diagram rather than plotting data.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 4))

# Set the coordinate range of the drawing canvas
ax.set_xlim(0, 10)    # x runs from 0 to 10
ax.set_ylim(0, 4)     # y runs from 0 to 4

# Turn off the axis frame, ticks, and labels
# This gives a clean blank canvas for drawing
ax.axis('off')

plt.show()
```

Running this gives you a blank white rectangle — your canvas. Every patch you add will be positioned using the coordinate system you defined with `set_xlim` and `set_ylim`.

> **Important:** `set_xlim(0, 10)` does not mean the canvas is 10 pixels or 10 inches wide. It defines a **coordinate system**. When you place a rectangle at x=2, that means 2 units in your chosen coordinate system — whatever portion of the figure that turns out to be.

---

## 3. `patches.Rectangle()` — Drawing Filled Rectangles

`Rectangle` is the most straightforward patch. You specify the bottom-left corner, the width, and the height.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# patches.Rectangle( (x, y), width, height )
# (x, y) is the BOTTOM-LEFT corner of the rectangle

rect = patches.Rectangle(
    (1, 1),          # bottom-left corner at x=1, y=1
    3,               # width: extends 3 units to the right → right edge at x=4
    2,               # height: extends 2 units upward → top edge at y=3
    facecolor='red', # fill color
    edgecolor='black', # border color
    linewidth=2        # border thickness
)

# A patch does nothing until you add it to an axes
ax.add_patch(rect)

plt.show()
```

### The `add_patch()` call

This is a step beginners often forget. Creating a patch object does not draw it. You must explicitly add it to an axes using `ax.add_patch(patch)`. Think of it as: you have built the shape, now you are placing it onto the canvas.

### Key parameters

```python
patches.Rectangle(
    (x, y),              # (required) bottom-left corner coordinates
    width,               # (required) horizontal size
    height,              # (required) vertical size
    facecolor='blue',    # fill color — accepts color names, hex codes, RGB tuples
    edgecolor='black',   # border color
    linewidth=2,         # border line thickness in points
    alpha=0.7,           # transparency: 0.0 = invisible, 1.0 = fully opaque
    zorder=2             # drawing order: higher numbers appear on top
)
```

### Colors in Matplotlib

Matplotlib accepts colors in several formats:

```python
facecolor='red'              # named color string
facecolor='#FF5733'          # hex color code
facecolor=(1.0, 0.2, 0.2)   # RGB tuple: values from 0.0 to 1.0
facecolor=(1.0, 0.2, 0.2, 0.5)  # RGBA tuple: fourth value is alpha/transparency
```

The simulation uses RGB tuples to dynamically color the reservoirs based on their current temperature. That logic is covered in Section 7.

---

## 4. `ax.text()` — Adding Text Annotations

Text labels placed directly on the axes — not on the axis labels or title — are added with `ax.text()`.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# ax.text(x, y, string, **options)
# x, y: position in axes coordinates
# The text is centered or aligned based on ha and va

ax.text(
    5,              # x position
    2,              # y position
    'Hello',        # the string to display
    ha='center',    # horizontal alignment: 'left', 'center', 'right'
    va='center',    # vertical alignment: 'top', 'center', 'bottom'
    fontsize=14,    # font size in points
    fontweight='bold',  # 'normal' or 'bold'
    color='navy'    # text color
)

plt.show()
```

### Alignment explained

`ha` (horizontal alignment) and `va` (vertical alignment) control which part of the text block sits at the coordinates you specify:

```
ha='left'    → the LEFT edge of the text sits at x
ha='center'  → the CENTER of the text sits at x
ha='right'   → the RIGHT edge of the text sits at x

va='bottom'  → the BOTTOM of the text sits at y
va='center'  → the CENTER of the text sits at y
va='top'     → the TOP of the text sits at y
```

If you want text centered on a shape, use `ha='center'` and `va='center'` with coordinates at the shape's center point.

### F-strings in `ax.text()`

Since `ax.text()` takes a string, you can use f-strings to embed live values:

```python
temperature = 387.4

ax.text(5, 2, f'Temperature: {temperature:.1f} K',
        ha='center', va='center', fontsize=12)
# Displays: "Temperature: 387.4 K"
# The :.1f format means: float, 1 decimal place
```

This is exactly how the simulation displays the current reservoir temperature, updating it on every animation frame.

---

## 5. The `bbox` Dictionary — Adding a Background Box to Text

Plain text on a colored diagram can be hard to read. The `bbox` parameter adds a styled background box behind the text.

`bbox` takes a Python dictionary of style options:

```python
ax.text(
    5, 1,
    'Equilibrium: 350.0 K',
    ha='center', va='center',
    fontsize=11,
    bbox=dict(
        boxstyle='round',      # shape of the box: 'round', 'square', 'round4'
        facecolor='wheat',     # background fill color
        edgecolor='brown',     # border color of the box
        alpha=0.8              # transparency of the box
    )
)
```

### `boxstyle` options

```python
boxstyle='round'      # rectangle with rounded corners — most common
boxstyle='square'     # plain rectangle with sharp corners
boxstyle='round4'     # very heavily rounded, almost pill-shaped
boxstyle='sawtooth'   # jagged edge — rarely used
boxstyle='rarrow'     # right-pointing arrow shape
```

The simulation uses `boxstyle='round'` with `facecolor='wheat'` for the equilibrium temperature label and `facecolor='lightblue'` for the system type label.

---

## 6. `patches.FancyArrowPatch()` — Drawing Styled Arrows

`FancyArrowPatch` draws an arrow from one point to another with full control over the arrowhead style and line thickness.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

arrow = patches.FancyArrowPatch(
    (2, 2),          # start point (x1, y1)
    (8, 2),          # end point   (x2, y2)
    arrowstyle='->',         # arrow style string
    mutation_scale=30,       # controls the SIZE of the arrowhead
    linewidth=3,             # thickness of the arrow shaft
    color='red'              # color of the entire arrow
)

ax.add_patch(arrow)    # must add to axes, same as Rectangle

plt.show()
```

### `arrowstyle` options

The `arrowstyle` string controls the shape of the arrowhead and tail:

```python
arrowstyle='->'        # simple line with one arrowhead at the end
arrowstyle='<-'        # arrowhead at the start
arrowstyle='<->'       # arrowheads at both ends
arrowstyle='-'         # plain line, no arrowhead
arrowstyle='-|>'       # line with a filled triangular arrowhead
arrowstyle='fancy'     # thick curved arrow with filled head
arrowstyle='simple'    # simple filled arrow
```

The simulation uses `'->'` — a clean line with a standard arrowhead.

### `mutation_scale`

This single parameter scales the entire arrowhead geometry. Increase it to make the arrowhead larger, decrease it for smaller. A value of `30` gives a clearly visible arrowhead at typical figure sizes.

```python
# Small arrowhead
mutation_scale=10

# Medium arrowhead  
mutation_scale=20

# Large arrowhead — used in simulation
mutation_scale=30
```

---

## 7. Dynamic Color Based on Temperature

The simulation does something more sophisticated than a fixed color. It maps temperature to a color dynamically, so the rectangle turns more red as temperature increases and more blue as it decreases. This function lives inside `plot_reservoir_visual()`:

```python
def temp_to_color(T):
    # Normalize temperature to a 0.0–1.0 range
    T_min, T_max = 250, 500
    normalized = (T - T_min) / (T_max - T_min)

    # Clamp to valid range in case T falls outside bounds
    normalized = np.clip(normalized, 0, 1)

    # Build an RGB tuple
    # r (red) increases as temperature increases
    # b (blue) decreases as temperature increases
    # g (green) is fixed at 0.2
    r = normalized          # 0.0 at cold, 1.0 at hot
    b = 1 - normalized      # 1.0 at cold, 0.0 at hot
    return (r, 0.2, b)      # returns an (R, G, B) tuple
```

Walk through two examples:

**At T = 500 K (maximum hot):**

```
normalized = (500 - 250) / (500 - 250) = 1.0
r = 1.0,  g = 0.2,  b = 0.0  → bright red-orange
```

**At T = 250 K (maximum cold):**

```
normalized = (250 - 250) / (500 - 250) = 0.0
r = 0.0,  g = 0.2,  b = 1.0  → bright blue
```

**At T = 375 K (midpoint):**

```
normalized = (375 - 250) / (500 - 250) = 0.5
r = 0.5,  g = 0.2,  b = 0.5  → purple
```

As the simulation runs and temperatures converge toward equilibrium, both rectangles gradually shift toward the same purple color — a visual confirmation that the reservoirs are equalizing.

`np.clip(normalized, 0, 1)` handles the edge case where a temperature slightly overshoots the defined range due to floating point arithmetic, clamping the value so it never produces an invalid RGB value outside 0.0–1.0.

---

## 8. How This Connects to `plot_reservoir_visual()`

Now read the complete method with full understanding of every line:

```python
def plot_reservoir_visual(self):
    """Visual representation of the two reservoirs."""

    # Clear any previous drawing — necessary because this redraws every frame
    self.ax_visual.clear()

    # Define the coordinate system for this axes
    self.ax_visual.set_xlim(0, 10)
    self.ax_visual.set_ylim(0, 3)

    # Remove axes frame, ticks, and labels — clean canvas for diagram
    self.ax_visual.axis('off')

    self.ax_visual.set_title('Thermal Reservoirs', fontsize=14, fontweight='bold')

    # Get temperatures at the current animation step
    # min() prevents the index exceeding array bounds on the final frame
    idx = min(self.sim.current_step, self.sim.n_steps - 1)
    T_h = self.sim.T_hot[idx]     # current hot temperature
    T_c = self.sim.T_cold[idx]    # current cold temperature

    # --- Color function defined inline ---
    def temp_to_color(T):
        T_min, T_max = 250, 500
        normalized = (T - T_min) / (T_max - T_min)
        normalized = np.clip(normalized, 0, 1)
        r = normalized
        b = 1 - normalized
        return (r, 0.2, b)

    # --- Hot reservoir rectangle (left side) ---
    hot_rect = patches.Rectangle(
        (1, 0.5),                       # bottom-left corner
        2,                               # width
        2,                               # height
        facecolor=temp_to_color(T_h),   # dynamic color based on current temp
        edgecolor='black',
        linewidth=2
    )
    self.ax_visual.add_patch(hot_rect)  # place it on the axes

    # Label above the hot rectangle
    self.ax_visual.text(
        2, 2.7,                          # centered above the rectangle
        f'HOT\n{T_h:.1f} K',            # two-line label with current temperature
        ha='center', va='center',
        fontsize=12, fontweight='bold'
    )

    # --- Cold reservoir rectangle (right side) ---
    cold_rect = patches.Rectangle(
        (7, 0.5),                        # bottom-left corner — right side of canvas
        2,                               # same width as hot
        2,                               # same height as hot
        facecolor=temp_to_color(T_c),   # dynamic color based on current temp
        edgecolor='black',
        linewidth=2
    )
    self.ax_visual.add_patch(cold_rect)

    # Label above the cold rectangle
    self.ax_visual.text(
        8, 2.7,
        f'COLD\n{T_c:.1f} K',
        ha='center', va='center',
        fontsize=12, fontweight='bold'
    )

    # --- Heat flow arrow (only drawn when T_hot > T_cold) ---
    if T_h > T_c:
        arrow = patches.FancyArrowPatch(
            (3.2, 1.5),      # start: just right of the hot rectangle's right edge
            (6.8, 1.5),      # end: just left of the cold rectangle's left edge
            arrowstyle='->',
            mutation_scale=30,
            linewidth=3,
            color='red'
        )
        self.ax_visual.add_patch(arrow)

        # Label above the arrow
        self.ax_visual.text(
            5, 1.8,          # centered between the two rectangles
            'Heat Flow',
            ha='center',
            fontsize=11,
            color='red',
            fontweight='bold'
        )

    # --- Equilibrium temperature label at the bottom ---
    self.ax_visual.text(
        5, 0.3,
        f'Equilibrium: {self.sim.T_eq:.1f} K',
        ha='center',
        fontsize=11,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    )

    # --- System type label at the top ---
    self.ax_visual.text(
        5, 2.95,
        f'System: {self.sim.system_type}',
        ha='center',
        fontsize=12,
        fontweight='bold',
        color='black',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
    )
```

### Why `ax.clear()` is called first

Every time the animation advances a frame, `plot_reservoir_visual()` redraws the entire diagram from scratch. If you did not call `self.ax_visual.clear()` first, each new rectangle would stack on top of the previous one. Over 2,000 frames you would have 2,000 overlapping rectangles. Clearing first discards everything and gives a blank canvas.

### Why the arrow is conditional

```python
if T_h > T_c:
```

Heat only flows from hot to cold. Once the temperatures equalize, `T_h` and `T_c` become equal and the arrow disappears — visually communicating that the driving force for heat transfer has gone to zero. This is a direct physical principle expressed through a drawing condition.

---

## 9. Coordinate Planning — How the Layout Was Designed

The canvas runs from `(0,0)` to `(10,3)`. Here is how the elements are arranged across that space:

```
x:  0    1         3    4    5    6    7         9   10
                                                    
y=3 ┌──────────────────────────────────────────────────┐
    │          [System type label at x=5, y=2.95]      │
y=2.7          [HOT label]              [COLD label]
    │                                                  │
y=2 │  ┌─────────────┐  →→→→→→→→→  ┌─────────────┐   │
    │  │             │  Heat Flow   │             │   │
y=1.5  │  HOT RECT   │─────────────│  COLD RECT  │
    │  │  x=1 to 3   │   arrow      │  x=7 to 9   │   │
y=1 │  │             │              │             │   │
    │  └─────────────┘              └─────────────┘   │
y=0.5                                                  
    │        [Equilibrium label at x=5, y=0.3]        │
y=0 └──────────────────────────────────────────────────┘
```

When you design a patch diagram, sketching this grid on paper first saves significant debugging time. Choose your coordinate range, decide where shapes should sit, and work out the positions before writing any code.

---

## Practice Exercise

Create a new file called `practice13.py`. Build a standalone diagram — no simulation required.

**Task 1.** Create a figure with one axes. Set `xlim` to `(0, 10)`, `ylim` to `(0, 5)`, and call `axis('off')`. Draw two rectangles side by side:

- Left rectangle: bottom-left at `(0.5, 1)`, width `3`, height `3`, `facecolor='tomato'`, `edgecolor='black'`
- Right rectangle: bottom-left at `(6.5, 1)`, width `3`, height `3`, `facecolor='steelblue'`, `edgecolor='black'`

**Task 2.** Add a `FancyArrowPatch` going from `(3.7, 2.5)` to `(6.3, 2.5)` with `arrowstyle='->'`, `mutation_scale=25`, `linewidth=3`, `color='darkorange'`.

**Task 3.** Add text labels:

- Centered above the left rectangle at `(2, 4.3)`: `"HOT\n500 K"`, bold, fontsize 12
- Centered above the right rectangle at `(8, 4.3)`: `"COLD\n300 K"`, bold, fontsize 12
- Centered between the rectangles at `(5, 2.8)`: `"Energy Transfer"`, color `'darkorange'`, fontsize 11

**Task 4.** Add a bbox annotation at `(5, 0.5)` reading `"System: Closed"` with `boxstyle='round'`, `facecolor='lightyellow'`, `alpha=0.9`.

The finished diagram should look structurally identical to the reservoir panel in the simulation.

---

## Key Takeaways

- Matplotlib patches are 2D shapes — rectangles, arrows, circles — drawn directly onto an axes using coordinates you define, independent of any data array.
- `patches.Rectangle((x, y), width, height)` creates a rectangle with its bottom-left corner at `(x, y)`. It must be added to an axes with `ax.add_patch()` before it appears.
- `patches.FancyArrowPatch((x1,y1), (x2,y2))` draws a styled arrow between two points. `arrowstyle='->'` and `mutation_scale` control the head shape and size.
- `ax.text(x, y, string)` places a text label at the given coordinates. `ha` and `va` control alignment, and the `bbox` dictionary adds a styled background box behind the text.
- In `plot_reservoir_visual()`, the entire diagram is cleared and redrawn on every animation frame. Rectangle fill colors are computed dynamically from current temperature values, the heat flow arrow appears only when `T_hot > T_cold`, and f-strings embed live temperature readings directly into the labels.

---

# Lesson 14: Interactive Widgets — Sliders, Buttons, and RadioButtons

---

## 1. Plain-English Concept Explanation

So far, the simulation has been a one-way street: Python runs the code, produces a plot, and you look at it. But our script does something more interesting — it lets you _interact_ with the simulation while it's running. You can drag a slider to change the starting temperature, click a button to pause the animation, or select a radio button to switch the system type.

This is made possible by **widgets** — interactive controls that live inside a matplotlib figure.

---

### What Is a Widget?

A **widget** is a graphical control element — a slider, button, checkbox, or similar object — that a user can interact with using a mouse or keyboard. In matplotlib, widgets are provided by the `matplotlib.widgets` module.

The three widgets used in our script are:

- **`Slider`** — a draggable handle on a track; produces a continuous range of values
- **`Button`** — a clickable rectangle that triggers an action once
- **`RadioButtons`** — a set of circular options where exactly one can be selected at a time

---

### The Key Idea: Callbacks

All three widgets work the same way under the hood:

1. You create the widget
2. You write a **callback function** — a regular method that runs when the widget is used
3. You _register_ that function with the widget using `.on_changed()` or `.on_clicked()`

A **callback function** is simply a function that you don't call yourself — you hand it to something else (in this case, a widget), and that something else calls it at the right moment.

> 💡 Think of a callback like leaving your phone number at a restaurant. You don't stand at the counter waiting. You go sit down, and they _call you back_ when your table is ready.

---

### Where Widgets Live: Axes Positioning

In matplotlib, every widget needs its own **axes** — a rectangular region of the figure to live in. You create these with `plt.axes()`, passing a list of four numbers:

```
plt.axes([left, bottom, width, height])
```

All four values are **fractions of the figure size**, between 0.0 and 1.0:

- `left` — how far from the left edge the widget starts
- `bottom` — how far from the bottom edge the widget starts
- `width` — how wide the widget is
- `height` — how tall the widget is

```python
plt.axes([0.15, 0.15, 0.25, 0.02])
# Starts 15% from left, 15% from bottom
# Is 25% of figure width wide, 2% of figure height tall
```

This is how widgets are positioned below the main plots in our script.

---

## 2. Annotated Code Examples

### The `Slider` Widget

```python
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

fig, ax = plt.subplots()             # create a figure with one main plot
plt.subplots_adjust(bottom=0.25)     # make room at the bottom for the slider

# Step 1: Create an axes region for the slider to live in
ax_slider = plt.axes([0.15, 0.10, 0.65, 0.03])   # [left, bottom, width, height]

# Step 2: Create the Slider inside that axes region
slider = Slider(
    ax=ax_slider,        # the axes it lives in
    label='T_hot (K)',   # text label shown to the left of the slider
    valmin=310,          # minimum value (left end of the track)
    valmax=500,          # maximum value (right end of the track)
    valinit=400,         # starting value (where the handle begins)
    valstep=10           # snap to multiples of 10 when dragged (optional)
)

# Step 3: Define the callback — what happens when the slider is moved
def on_change(val):          # val is the new slider value, passed in automatically
    print("New value:", val) # for now, just print it

# Step 4: Register the callback with the slider
slider.on_changed(on_change)  # "when slider changes, call on_change()"

plt.show()
```

> 💡 `valstep` is optional. Without it, the slider moves continuously. With it, the slider snaps to discrete steps — useful for temperatures where you want whole numbers.

---

### The `Button` Widget

```python
from matplotlib.widgets import Button

# Step 1: Create an axes region for the button
ax_button = plt.axes([0.40, 0.02, 0.12, 0.05])   # small rectangle near the bottom

# Step 2: Create the Button inside it
btn = Button(ax_button, 'Reset')   # second argument is the button label text

# Step 3: Define the callback — what happens when clicked
def on_click(event):        # "event" contains info about the click (rarely needed)
    print("Button clicked!")

# Step 4: Register the callback
btn.on_clicked(on_click)    # "when button is clicked, call on_click()"
```

> 💡 The `event` parameter in a Button callback contains details about the mouse click — position, which button was pressed, etc. In most scripts including ours, it's received but ignored.

---

### The `RadioButtons` Widget

```python
from matplotlib.widgets import RadioButtons

# Step 1: Create an axes region — needs to be tall enough to fit all options
ax_radio = plt.axes([0.55, 0.15, 0.12, 0.10])

# Step 2: Create the RadioButtons
#         Second argument is a list of option labels
#         active=0 means the first option is selected at startup
radio = RadioButtons(ax_radio, ['Closed', 'Open', 'Isolated'], active=0)

# Step 3: Define the callback — receives the label of the selected option
def on_select(label):           # label is the text of whichever option was clicked
    print("Selected:", label)   # e.g. "Selected: Isolated"

# Step 4: Register the callback
radio.on_clicked(on_select)     # RadioButtons also uses on_clicked, not on_changed
```

> ⚠️ Despite being a selection widget, `RadioButtons` uses `.on_clicked()`, not `.on_changed()`. This is a minor inconsistency in matplotlib's API — worth noting so it doesn't surprise you.

---

### How a Slider Callback Updates a Plot

Here is a more complete example showing the full pattern — create widget, define callback, update something meaningful:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Initial temperature values
T_hot_init = 400.0
T_cold_init = 300.0
time = np.linspace(0, 100, 500)    # 500 time points from 0 to 100 seconds

# Simple exponential decay toward equilibrium — not our full model, just for illustration
def temperature_curve(T_start, T_eq, time, rate=0.05):
    return T_eq + (T_start - T_eq) * np.exp(-rate * time)

T_eq = (T_hot_init + T_cold_init) / 2                          # 350.0
line_hot, = ax.plot(time, temperature_curve(T_hot_init, T_eq, time), 'r-')
line_cold, = ax.plot(time, temperature_curve(T_cold_init, T_eq, time), 'b-')
ax.set_ylim(250, 500)

# Slider for T_hot
ax_slider = plt.axes([0.15, 0.10, 0.65, 0.03])
slider = Slider(ax_slider, 'T_hot (K)', 310, 500, valinit=T_hot_init, valstep=10)

def on_change(val):
    new_T_hot = slider.val                             # read the current slider value
    new_T_eq = (new_T_hot + T_cold_init) / 2          # recalculate equilibrium
    line_hot.set_ydata(                                # update the plot line
        temperature_curve(new_T_hot, new_T_eq, time)
    )
    fig.canvas.draw_idle()                             # redraw the figure efficiently
                                                       # draw_idle() avoids flickering

slider.on_changed(on_change)
plt.show()
```

---

## 3. How This Connects to Our Script

### `setup_sliders()` — creating all four sliders and the radio buttons

```python
def setup_sliders(self):
    from matplotlib.widgets import RadioButtons

    # --- Radio buttons for system type ---
    # plt.axes() positions the widget in the figure using figure-fraction coordinates
    ax_sys = plt.axes([0.55, 0.15, 0.12, 0.08], facecolor='lightgoldenrodyellow')
    self.radio_system = RadioButtons(ax_sys, self.system_types, active=0)
    # active=0 → "Closed" is selected at startup (first item in self.system_types)
    self.radio_system.on_clicked(self.on_system_type_change)
    # When a radio option is clicked, call self.on_system_type_change()

    slider_color = 'lightgoldenrodyellow'   # background colour for slider areas

    # --- Axes regions for each slider ---
    # Each sits at a different vertical position (bottom value) so they don't overlap
    ax_T_hot  = plt.axes([0.15, 0.15, 0.25, 0.02], facecolor=slider_color)
    ax_T_cold = plt.axes([0.15, 0.11, 0.25, 0.02], facecolor=slider_color)
    ax_h      = plt.axes([0.15, 0.07, 0.25, 0.02], facecolor=slider_color)
    ax_mass   = plt.axes([0.15, 0.03, 0.25, 0.02], facecolor=slider_color)

    # --- Create each Slider ---
    self.slider_T_hot = Slider(
        ax_T_hot, 'T_hot (K)',       # axes region, label
        310, 500,                     # valmin, valmax
        valinit=self.sim.T_hot_0,    # starting position matches simulation's value
        valstep=10                    # snap to 10-degree increments
    )
    self.slider_T_cold = Slider(
        ax_T_cold, 'T_cold (K)',
        250, 400,
        valinit=self.sim.T_cold_0,
        valstep=10
    )
    self.slider_h = Slider(
        ax_h, 'Heat Transfer Coeff (W/K)',
        10, 200,
        valinit=self.sim.h,
        valstep=10
    )
    self.slider_mass_ratio = Slider(
        ax_mass, 'Mass Ratio (m_hot/m_cold)',
        0.2, 5.0,
        valinit=1.0,
        valstep=0.1                   # finer steps for the mass ratio
    )

    # --- Register the same callback for all four sliders ---
    # Any slider movement calls on_slider_change()
    self.slider_T_hot.on_changed(self.on_slider_change)
    self.slider_T_cold.on_changed(self.on_slider_change)
    self.slider_h.on_changed(self.on_slider_change)
    self.slider_mass_ratio.on_changed(self.on_slider_change)
```

> 💡 All four sliders share _one_ callback function — `on_slider_change()`. That function reads the current value of _all_ sliders every time _any_ one of them changes. This is simpler than writing four separate callbacks.

---

### `setup_buttons()` — creating Play/Pause and Reset

```python
def setup_buttons(self):
    # Create axes regions for two buttons side by side (vertically)
    ax_play  = plt.axes([0.55, 0.10, 0.08, 0.04])
    ax_reset = plt.axes([0.55, 0.05, 0.08, 0.04])

    # Create the buttons — second argument is the visible label text
    self.btn_play  = Button(ax_play,  'Play/Pause')
    self.btn_reset = Button(ax_reset, 'Reset')

    # Register callbacks — each button has its own dedicated function
    self.btn_play.on_clicked(self.toggle_animation)   # Play/Pause → toggle_animation
    self.btn_reset.on_clicked(self.reset_animation)   # Reset → reset_animation
```

---

### The three callback functions

```python
def on_slider_change(self, val):
    # val is the new slider value — passed in automatically, but we don't use it
    # Instead, we read ALL current slider values each time ANY slider changes

    self.sim.T_hot_0  = self.slider_T_hot.val        # read .val to get current position
    self.sim.T_cold_0 = self.slider_T_cold.val
    self.sim.h        = self.slider_h.val
    self.sim.m_hot    = self.slider_mass_ratio.val
    self.sim.m_cold   = 1.0

    self.sim.T_eq = self.sim._calculate_equilibrium_temp()  # recalculate equilibrium
    self.update_simulation()   # re-run the full simulation with new values
    self.plot_all()            # redraw all plots


def toggle_animation(self, event):
    # event is the click event — received but not used
    self.is_playing = not self.is_playing   # flip True→False or False→True
                                             # this is how a toggle works

    if self.is_playing:
        if self.animation is None:
            # Create the animation object only on the first play
            self.animation = FuncAnimation(self.fig, self.animate, interval=50, blit=False)
        self.sim.current_step = 0    # restart from the beginning


def reset_animation(self, event):
    self.is_playing = False          # stop the animation
    self.sim.reset_simulation()      # reset all arrays to initial conditions
    self.plot_all()                  # redraw plots showing the reset state
```

---

### How the pieces connect — the full widget interaction flow

```
User drags T_hot slider
    └── matplotlib detects change
    └── calls on_slider_change(val)
            ├── reads self.slider_T_hot.val  (and all others)
            ├── updates self.sim attributes
            ├── calls self.update_simulation()
            │       └── calls self.sim.run_full_simulation()
            └── calls self.plot_all()
                    └── redraws all 5 subplots

User clicks Play/Pause
    └── matplotlib detects click
    └── calls toggle_animation(event)
            └── flips self.is_playing
            └── creates FuncAnimation if needed

User clicks Reset
    └── matplotlib detects click
    └── calls reset_animation(event)
            ├── sets self.is_playing = False
            ├── calls self.sim.reset_simulation()
            └── calls self.plot_all()

User clicks a RadioButton
    └── matplotlib detects click
    └── calls on_system_type_change(label)
            ├── updates self.sim.system_type
            ├── calls self.update_simulation()
            └── calls self.plot_all()
```

---

## 4. Practice Exercise

**Goal:** Build a small standalone figure with one slider, one button, and one set of radio buttons. Each widget should visibly change something on the plot.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.40)    # leave room at bottom for three widget rows
ax.set_ylim(200, 600)
ax.set_xlim(0, 10)
ax.set_title("Widget Practice")

# --- Initial values ---
T_hot_init = 400.0
T_cold_init = 300.0
line_h, = ax.plot([0, 10], [T_hot_init, T_hot_init], 'r-', linewidth=2, label='Hot')
line_c, = ax.plot([0, 10], [T_cold_init, T_cold_init], 'b-', linewidth=2, label='Cold')
ax.legend()

# --- Slider ---
ax_slider = plt.axes([0.15, 0.25, 0.55, 0.03])
slider = Slider(ax_slider, 'T_hot (K)', 310, 500, valinit=T_hot_init, valstep=10)

def on_slider_change(val):
    line_h.set_ydata([slider.val, slider.val])   # move the red line to new temperature
    fig.canvas.draw_idle()                        # redraw without flickering

slider.on_changed(on_slider_change)

# --- Button ---
ax_button = plt.axes([0.15, 0.15, 0.15, 0.05])
btn = Button(ax_button, 'Reset')

def on_reset(event):
    slider.set_val(T_hot_init)               # programmatically reset slider to 400
    line_h.set_ydata([T_hot_init, T_hot_init])
    fig.canvas.draw_idle()

btn.on_clicked(on_reset)

# --- Radio Buttons ---
ax_radio = plt.axes([0.55, 0.10, 0.15, 0.12])
radio = RadioButtons(ax_radio, ['Closed', 'Open', 'Isolated'], active=0)

def on_system_select(label):
    print("System type selected:", label)    # just print for now
    ax.set_title(f"System: {label}")
    fig.canvas.draw_idle()

radio.on_clicked(on_system_select)

plt.show()
```

**Then try these extensions:**

1. Add a second slider for `T_cold` that moves the blue line
2. Make the Reset button restore _both_ lines to their initial positions
3. When `"Isolated"` is selected via radio button, set both lines to the same value (the average of hot and cold) to suggest equilibrium is fixed

---

## 5. Key Takeaways

- Matplotlib widgets (`Slider`, `Button`, `RadioButtons`) are created in two steps: first create an **axes region** with `plt.axes([left, bottom, width, height])` using figure-fraction coordinates, then create the widget inside that region.
- All three widgets use a **callback pattern**: you write a function, then register it with `.on_changed()` or `.on_clicked()`. The widget calls your function automatically when the user interacts with it.
- `Slider` uses `.on_changed(callback)` — the callback receives the new value as its argument. `Button` and `RadioButtons` both use `.on_clicked(callback)` — Button passes a click event, RadioButtons passes the selected label string.
- In our script, **all four sliders share one callback** (`on_slider_change`), which reads `.val` from every slider each time any one changes. This avoids duplicating logic across four separate functions.
- Widgets must be stored as instance attributes (e.g. `self.slider_T_hot`) — if stored in a local variable, matplotlib may garbage-collect them and they will stop responding to interaction. [Inference — this is consistent with documented matplotlib widget behaviour, but exact garbage collection behaviour may vary by environment.]

---

# Lesson 15: Animation with FuncAnimation

---

## 1. Plain-English Concept Explanation

### What is Animation in Matplotlib?

A static plot shows a fixed snapshot of data. An **animation** shows data changing over time — a sequence of frames displayed one after another fast enough that the human eye perceives smooth movement, like a flipbook.

Matplotlib's `FuncAnimation` is the tool that creates this effect. It works by doing one simple thing repeatedly: calling a function you write, waiting a short fixed interval, then calling it again — over and over, updating the display each time.

You write the function that describes _what changes on each frame_. `FuncAnimation` handles the timing and the repetition.

---

### The Core Idea: A Ticking Clock

The clearest mental model for `FuncAnimation` is a **ticking clock**.

Every time the clock ticks, `FuncAnimation` calls your animation function. Your function updates the plot. The display refreshes. Then the clock ticks again.

You control:

- **How fast** the clock ticks — the `interval` parameter (time between ticks, in milliseconds)
- **What happens** on each tick — your animation function
- **Which figure** gets updated — the `fig` parameter

`FuncAnimation` controls everything else.

---

### The `animate(frame)` Function Signature

Your animation function must accept exactly one argument — conventionally called `frame`. This is an integer that `FuncAnimation` passes in automatically, counting up from `0` each time your function is called: `0, 1, 2, 3, ...`

You do not call this function yourself. `FuncAnimation` calls it for you on every tick.

You are not required to _use_ the `frame` number inside your function — in our script, it is received but ignored, because the simulation tracks its own progress internally. The argument must still be there in the function signature, however, because `FuncAnimation` always passes it.

---

### The `interval` Parameter

`interval` is the number of **milliseconds** to wait between frames. It sets the pace of the animation.

- `interval=1000` → one frame per second (very slow)
- `interval=100` → ten frames per second (moderate)
- `interval=50` → twenty frames per second (smooth for most purposes)

> **Important:** `interval` is the _requested_ delay between frames. If your animation function takes longer to run than `interval` milliseconds, frames will be skipped or the animation will run slower than intended. [Inference] Complex plots with many elements may cause this — behavior depends on your hardware and the complexity of your drawing code. This is not guaranteed to occur, but is worth knowing.

---

### The `blit` Parameter

`blit` is a performance option. It stands for **block transfer** — a technique where only the parts of the image that changed are redrawn, rather than the entire figure.

- `blit=True` → only redrawn elements are updated. Faster, but requires your animation function to return a list of the artists (plot elements) that changed.
- `blit=False` → the entire figure is redrawn on every frame. Slower, but simpler to implement correctly.

Our script uses `blit=False` and returns an empty list `[]` from `animate()`. This is a deliberate simplicity trade-off: since the simulation redraws all five plots on every frame, tracking individual changed elements would add complexity without meaningful benefit in this context.

---

### How `FuncAnimation` Fits Together

Here is the complete sequence of events when the animation runs:

1. You create a `FuncAnimation` object, passing it your figure, your function, the interval, and blit setting
2. `FuncAnimation` starts an internal timer
3. The timer fires every `interval` milliseconds
4. On each timer tick, `FuncAnimation` calls your function with the next frame number
5. Your function updates the simulation and redraws the plots
6. The display refreshes
7. Go to step 3 and repeat

This continues until the window is closed, the animation is paused, or your function signals that it is done.

---

## 2. Annotated Code Examples

### The Minimal Working Example

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and a set of axes to draw on
fig, ax = plt.subplots()

# A line object to update on each frame — plot() returns a list, [0] gets the line
line, = ax.plot([], [])         # empty line to start with
ax.set_xlim(0, 10)              # fix the x-axis range
ax.set_ylim(-1, 1)              # fix the y-axis range

def animate(frame):
    # frame is passed in automatically by FuncAnimation — counts 0, 1, 2, 3...
    x = np.linspace(0, 10, 100)           # 100 evenly spaced x values
    y = np.sin(x + frame * 0.2)           # shift the wave slightly each frame
    line.set_data(x, y)                   # update the line with new data
    return [line]                         # return list of changed artists (blit=True)

# Create the FuncAnimation object
# fig       → the figure to animate
# animate   → your function, called once per frame
# interval  → milliseconds between frames (100ms = 10 frames/sec)
# blit      → True means only redraw changed elements
anim = animation.FuncAnimation(fig, animate, interval=100, blit=True)

plt.show()
```

---

### The `frame` Argument — Used vs. Ignored

```python
# Example 1: frame IS used — to index into pre-computed data
data = [10, 20, 30, 40, 50]    # pre-computed values

def animate_with_frame(frame):
    value = data[frame]         # use frame as an index
    print(f"Frame {frame}: value = {value}")
    return []


# Example 2: frame is NOT used — the object tracks its own state
# This is the pattern our simulation uses
class Counter:
    def __init__(self):
        self.count = 0

counter = Counter()

def animate_without_frame(frame):
    # frame is received but never referenced inside the function
    counter.count += 1          # the object tracks progress itself
    print(f"Internal count: {counter.count}")
    return []
```

---

### The `interval` Parameter in Practice

```python
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title("Watching interval change things")

def animate(frame):
    ax.clear()
    ax.set_title(f"Frame: {frame}")
    return []

# Slow animation — 1 frame per second
slow = FuncAnimation(fig, animate, interval=1000, blit=False)

# Fast animation — 20 frames per second  
# fast = FuncAnimation(fig, animate, interval=50, blit=False)

plt.show()
```

---

### `blit=False` with an Empty Return

```python
def animate(frame):
    # Clear and redraw everything — simple but redraws all elements
    ax.clear()
    ax.plot([0, 1, 2], [frame, frame + 1, frame + 2])

    # blit=False means this return value is not used by FuncAnimation
    # but the return statement must still be present
    return []
```

---

## 3. How This Connects to Our Script

### The `animate()` Method

Here is the full `animate()` method from `InteractiveVisualizer`, with every line explained:

```python
def animate(self, frame):
    # self is the InteractiveVisualizer object — gives access to all its data
    # frame is passed in by FuncAnimation automatically — not used here
    # because self.sim.current_step tracks simulation progress internally

    # Only advance the simulation if the Play button has been pressed
    # AND there are still steps left to compute
    if self.is_playing and self.sim.current_step < self.sim.n_steps - 1:

        # Advance 5 simulation steps per animation frame
        # This makes the animation visually faster — each screen update
        # corresponds to 5 time steps of physics, not just 1
        for _ in range(5):

            # self.sim.step() advances the simulation by one time step
            # It returns False when the simulation has finished
            if not self.sim.step():

                # Simulation is complete — stop the animation
                self.is_playing = False

                # Exit the inner loop immediately — no more steps to take
                break

        # Redraw all five plots with the latest simulation data
        self.plot_all()

    # blit=False is used, so this return value is ignored by FuncAnimation
    # The empty list is returned to satisfy the expected function signature
    return []
```

Two things are worth noting here. First, `frame` is accepted but never referenced inside the function — the simulation's own `current_step` counter is the source of truth for progress. Second, the inner `for _ in range(5)` loop means each clock tick of `FuncAnimation` advances the physics by 5 steps, making the animation run at a pace fast enough to be visually interesting without requiring an extremely small `interval`.

---

### The `toggle_animation()` Method

`FuncAnimation` is not created when the program starts. It is created the first time the user clicks **Play** — and only created once, even if Play is clicked multiple times:

```python
def toggle_animation(self, event):
    # event is passed in by the Button widget — not used here
    # Flip the playing state: if True → False, if False → True
    self.is_playing = not self.is_playing

    if self.is_playing:

        # Only create a new FuncAnimation if one doesn't already exist
        # This prevents multiple animation timers running simultaneously
        if self.animation is None:

            # Create the FuncAnimation object
            # self.fig        → the figure window to animate
            # self.animate    → the function called on each tick
            # interval=50     → 50ms between frames (~20 frames per second)
            # blit=False      → redraw entire figure each frame
            self.animation = FuncAnimation(
                self.fig,
                self.animate,
                interval=50,
                blit=False
            )

        # Reset to the beginning of the simulation each time Play is pressed
        self.sim.current_step = 0
```

The `if self.animation is None` guard is important. `FuncAnimation` starts its internal timer the moment it is created — not when you call a separate start method. If `toggle_animation()` created a new `FuncAnimation` every time Play was clicked, multiple timers would run simultaneously and the simulation would advance several times faster than intended. [Inference] This is a common source of unexpected behavior in Matplotlib animation code — though the exact effect depends on the environment and is not guaranteed to manifest identically in all cases.

---

### The Full Animation Lifecycle in Our Script

Here is the complete sequence from program launch to animation playing:

```
1. Program starts → InteractiveVisualizer.__init__() runs
2. Figure is created, sliders and buttons are drawn
3. self.animation = None  ← no FuncAnimation yet
4. self.is_playing = False ← simulation is paused

5. User clicks Play
6. toggle_animation() runs
7. self.is_playing becomes True
8. self.animation is None → FuncAnimation is created for the first time
9. FuncAnimation starts its internal 50ms timer
10. Every 50ms → animate(frame) is called
11. animate() checks is_playing → True → advances 5 steps → redraws plots
12. Display updates

13. User clicks Play again
14. toggle_animation() runs
15. self.is_playing becomes False
16. animate() is still called every 50ms (timer keeps running)
17. But the if self.is_playing check fails → nothing happens → plots freeze

18. User clicks Play again → is_playing becomes True → simulation resumes
```

The timer never actually stops after the first Play click — but when `is_playing` is `False`, the `animate()` function does nothing on each tick, which creates the appearance of pausing.

---

## 4. Practice Exercise

Try this in a new Python file. It should take under 10 minutes.

**Task:** Build a minimal animation that shows a value increasing over time:

1. Create a figure and axes with `plt.subplots()`
2. Write an `animate(frame)` function that:
    - Clears the axes with `ax.clear()`
    - Sets the y-axis limit to `0` and `100` with `ax.set_ylim(0, 100)`
    - Draws a horizontal line at `y = frame` using `ax.axhline(frame, color='red')`
    - Sets a title showing the current frame number using an f-string
    - Returns `[]`
3. Create a `FuncAnimation` with `interval=100` and `blit=False`
4. Display with `plt.show()`

**Starter hint:**

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def animate(frame):
    ax.clear()
    ax.set_ylim(0, 100)
    # your code here
    return []

anim = FuncAnimation(fig, animate, interval=100, blit=False)
plt.show()
```

> **Environment note:** Matplotlib animations require a display environment to render. If you are running Python in a basic terminal without a graphical interface, `plt.show()` may not open a window. This exercise works as expected in standard desktop environments and in Jupyter notebooks with the appropriate magic command (`%matplotlib notebook`).

---

## 5. Key Takeaways

- **`FuncAnimation`** animates a Matplotlib figure by calling your function repeatedly on a fixed timer. You write _what changes_; it handles _when_ to call you.
- Your animation function **must accept a `frame` argument** — an integer that increments automatically. You are not required to use it, but it must be present in the function signature.
- **`interval`** sets the milliseconds between frames. `interval=50` requests approximately 20 frames per second. [Inference] If your drawing code takes longer than `interval` to execute, the animation may run slower than requested — actual behavior depends on your hardware and plot complexity.
- **`blit=False`** redraws the entire figure on every frame. It is simpler to implement than `blit=True` and is the right choice when multiple subplots are all updated simultaneously, as in our script.
- **`FuncAnimation` starts its timer the moment it is created.** Our script delays creation until the first Play click and uses a `None` guard to prevent duplicate timers from being created on subsequent clicks.

---

# Lesson 16: The Physics Model — What the Equations Actually Mean

---

## 1. Plain-English Concept Explanation

Before this lesson, you have been learning _how_ to write Python. This lesson steps back and asks a different question: **what is the simulation actually modelling?**

Understanding the physics will make the code make sense at a deeper level. You will no longer be copying formulas — you will know _why_ each one is there.

We will cover four ideas:

1. Why heat flows at all, and in which direction
2. How fast it flows (Newton's Law of Cooling)
3. Where it stops (the equilibrium temperature)
4. What is lost along the way (entropy generation)

No calculus is required. Where equations appear, every symbol will be explained in plain English first.

---

### Idea 1 — Why Does Heat Flow?

Heat always flows **from hotter to cooler**. This is not a rule someone invented — it is one of the most reliably observed facts in all of science, formalised as the **Second Law of Thermodynamics**.

Think of it like water flowing downhill. Water doesn't need to be pushed downhill — it just goes. Temperature difference is the "hill" for heat. The bigger the hill, the faster the flow.

In our simulation, one reservoir starts hot (default 400 K) and one starts cold (default 300 K). Heat flows from the hot one to the cold one. As it does, the hot one cools down and the cold one warms up — until they reach the same temperature and flow stops.

> **Kelvin (K):** The temperature scale used in thermodynamics. 0 K is absolute zero — the coldest anything can ever be. To convert from Celsius: K = °C + 273.15. Our simulation uses Kelvin throughout because the entropy formula requires it.

---

### Idea 2 — How Fast Does Heat Flow? (Newton's Law of Cooling)

The rate at which heat flows depends on two things:

- **How different the temperatures are** — a large gap drives faster flow
- **How easily heat can move between the objects** — a copper rod transfers heat faster than a piece of wood

This relationship is captured by **Newton's Law of Cooling**:

```
Q̇ = h × (T_hot − T_cold)
```

Let's read every symbol:

|Symbol|Name|Plain-English Meaning|
|---|---|---|
|`Q̇`|Heat transfer rate|How many Joules of heat move per second (Watts)|
|`h`|Heat transfer coefficient|A number describing how easily heat crosses the boundary between the two reservoirs|
|`T_hot`|Hot reservoir temperature|Current temperature of the hot side, in Kelvin|
|`T_cold`|Cold reservoir temperature|Current temperature of the cold side, in Kelvin|
|`(T_hot − T_cold)`|Temperature difference|The "driving force" — the bigger this gap, the faster heat flows|

> **Joule (J):** The unit of energy. **Watt (W):** The unit of power, meaning energy per second. 1 W = 1 J/s. So Q̇ is measured in Watts — it is _not_ the total heat moved, it is the _rate_ at which heat is moving right now.

#### What this means in practice

At the start of the simulation, T_hot = 400 K and T_cold = 300 K. With h = 50 W/K:

```
Q̇ = 50 × (400 − 300) = 50 × 100 = 5000 W
```

That is a large flow rate — 5000 Joules per second. But as the temperatures converge, the gap shrinks:

```
At T_hot = 360, T_cold = 340:  Q̇ = 50 × 20 = 1000 W
At T_hot = 351, T_cold = 349:  Q̇ = 50 × 2  = 100 W
At T_hot = 350, T_cold = 350:  Q̇ = 50 × 0  = 0 W  ← flow stops
```

The simulation captures this slowdown beautifully — the heat flux chart starts high and decays toward zero as equilibrium approaches.

---

### Idea 3 — Where Does It Stop? (The Equilibrium Temperature)

The system reaches equilibrium when both reservoirs are at the same temperature and no more heat flows. But what temperature will that be?

The answer comes from a simple principle: **energy is conserved**. Whatever energy the hot reservoir loses, the cold reservoir gains. None is created or destroyed — it just moves.

This gives us the **energy balance equation**:

```
Energy lost by hot = Energy gained by cold
m_hot × c_p × (T_hot_initial − T_eq) = m_cold × c_p × (T_cold_initial − T_eq)
                                                               (note: this is negative, meaning a gain)
```

Solving for T_eq (the equilibrium temperature):

```
T_eq = (m_hot × c_p × T_hot_initial + m_cold × c_p × T_cold_initial)
       ──────────────────────────────────────────────────────────────
                    (m_hot × c_p) + (m_cold × c_p)
```

Let's read every symbol:

|Symbol|Name|Plain-English Meaning|
|---|---|---|
|`m_hot`|Mass of hot reservoir|How much material is in the hot reservoir (kg). More mass = more energy stored|
|`m_cold`|Mass of cold reservoir|How much material is in the cold reservoir (kg)|
|`c_p`|Specific heat capacity|How much energy (Joules) it takes to raise 1 kg of the material by 1 Kelvin|
|`T_eq`|Equilibrium temperature|The final temperature both reservoirs settle at|

#### The mass ratio matters

When both masses are equal (m_hot = m_cold = 1 kg), the equation simplifies to a straight average:

```
T_eq = (400 + 300) / 2 = 350 K
```

But if the hot reservoir has more mass — say m_hot = 3 kg, m_cold = 1 kg — it carries more thermal energy and pulls the equilibrium temperature upward:

```
T_eq = (3 × 400 + 1 × 300) / (3 + 1) = 1500 / 4 = 375 K
```

This is why the "Mass Ratio" slider in the simulation moves the green equilibrium line — you are directly changing the energy balance.

---

### Idea 4 — What Is Lost Along the Way? (Entropy Generation)

This is the most subtle of the four ideas, but also the most important for understanding why the simulation is called _irreversible_.

#### What is entropy?

**Entropy** is a measure of how spread out or dispersed energy has become. When heat flows from a hot object to a cold one, the energy becomes more evenly distributed — and entropy increases. The universe, left to itself, always tends toward states where energy is more spread out, not less.

> A useful everyday intuition: a hot cup of coffee in a cold room will always cool down. You will never see a cold cup spontaneously get hotter while the room cools — even though that would conserve energy just as well. The direction nature actually takes is the one that increases entropy.

#### What does "irreversible" mean?

A process is **reversible** if it could, in principle, run backwards without leaving any trace. Reversible processes are theoretical ideals — they require infinitely slow, infinitely gentle changes with no friction, no temperature gaps.

A process is **irreversible** if it cannot run backwards on its own. Heat flowing across a temperature difference is irreversible. Once the two reservoirs reach 350 K, they will not spontaneously separate back into a 400 K reservoir and a 300 K reservoir — even though that would conserve energy. The entropy generated during the process cannot be undone.

#### The entropy generation formula

```
Ṡ_gen = Q̇ × (1/T_cold − 1/T_hot)
```

|Symbol|Name|Plain-English Meaning|
|---|---|---|
|`Ṡ_gen`|Entropy generation rate|How many Joules per Kelvin of entropy are being created per second (J/K·s)|
|`Q̇`|Heat transfer rate|The same heat flow rate from Newton's Law of Cooling|
|`1/T_cold − 1/T_hot`|Thermal asymmetry|This term is always positive when T_hot > T_cold, which guarantees Ṡ_gen is always positive|

#### Why is it always positive?

When T_hot > T_cold, the cold reservoir temperature is lower, so 1/T_cold is a larger number than 1/T_hot. Therefore:

```
1/T_cold − 1/T_hot > 0    (always, when T_hot > T_cold)
```

And since Q̇ is also positive (heat is flowing in the positive direction), their product is always positive. **Entropy generation is never negative for a spontaneous, irreversible process.** A negative value would mean entropy was being destroyed — something that does not occur naturally.

#### What does it feel like?

Entropy generation is "lost potential." Before heat transfer, you could theoretically run a heat engine between 400 K and 300 K and extract useful work. After both reservoirs reach 350 K, that opportunity is gone — the energy still exists, but it is now spread too evenly to do useful work. That lost opportunity is what entropy generation measures.

---

## 2. Code: Every Formula in `IrreversibleHeatTransfer`

Now let's look at exactly where each physical idea lives in the code:

---

### Newton's Law of Cooling → `calculate_heat_transfer_rate()`

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    # If the system is Isolated, no heat can cross any boundary.
    # Q_dot = 0 by definition — the formula does not apply.
    if self.system_type == "Isolated":
        return 0.0

    # Newton's Law of Cooling: Q_dot = h * (T_hot - T_cold)
    # self.h  : heat transfer coefficient (W/K) — set by the slider
    # T_h     : current temperature of the hot reservoir (K)
    # T_c     : current temperature of the cold reservoir (K)
    # Result  : heat flow rate in Watts (Joules per second)
    return self.h * (T_h - T_c)
    # As T_h and T_c converge, (T_h - T_c) → 0, so Q_dot → 0.
    # This is why the heat flux chart decays toward zero over time.
```

---

### Energy Balance → `_calculate_equilibrium_temp()`

```python
def _calculate_equilibrium_temp(self):
    # Numerator: total thermal energy in the system at the start.
    # Each reservoir contributes: mass × specific_heat × initial_temperature.
    # This is the total energy that must be conserved.
    numerator = (self.m_hot  * self.c_p * self.T_hot_0 +
                 self.m_cold * self.c_p * self.T_cold_0)

    # Denominator: total thermal "capacity" of the system.
    # A larger denominator means the same energy is spread across
    # more material, producing a lower equilibrium temperature.
    denominator = self.m_hot * self.c_p + self.m_cold * self.c_p

    # T_eq: the single temperature at which all energy is balanced.
    # This is the green dashed line in the temperature chart.
    return numerator / denominator
    # Note: c_p cancels out here because both reservoirs use the
    # same material. If they were different materials, c_p would
    # need to be tracked separately for each.
```

---

### Entropy Generation → `calculate_entropy_generation_rate()`

```python
def calculate_entropy_generation_rate(self, Q_dot, T_h, T_c):
    # Guard clause: if no heat is flowing, or if temperatures are
    # already equal, there is no irreversibility to measure.
    if Q_dot == 0 or T_h == T_c:
        return 0

    # Entropy generation formula: S_gen_dot = Q_dot * (1/T_c - 1/T_h)
    # Q_dot       : heat transfer rate (W), calculated just before this call
    # (1/T_c - 1/T_h) : always positive when T_h > T_c
    #
    # The result is always positive — confirming the Second Law.
    # Units: Watts × (1/Kelvin) = J/(K·s), i.e. entropy per second.
    return Q_dot * (1/T_c - 1/T_h)
    # As temperatures converge, (1/T_c - 1/T_h) → 0.
    # Entropy generation rate drops to zero at equilibrium —
    # the process becomes less irreversible as it slows down.
```

---

### Applying the Physics Each Timestep → `step()`

```python
def step(self):
    # Stop if the simulation has run its full course.
    if self.current_step >= self.n_steps - 1:
        return False

    i = self.current_step

    # ── NEWTON'S LAW OF COOLING ──────────────────────────────────────
    # How much heat is moving right now, at this instant?
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
    self.heat_flux[i] = Q_dot

    # ── ENERGY BALANCE (per timestep) ───────────────────────────────
    # The hot reservoir loses energy: its temperature drops.
    # dT_hot is the temperature change this timestep.
    # Q_dot * dt = energy transferred this step (Joules)
    # Dividing by (m * c_p) converts Joules back to a temperature change.
    dT_hot  = -Q_dot * self.dt / (self.m_hot  * self.c_p)
    dT_cold =  Q_dot * self.dt / (self.m_cold * self.c_p)
    # Note the signs: hot loses energy (negative), cold gains it (positive).
    # The magnitude of energy lost = magnitude of energy gained.
    # Energy is conserved every single timestep.

    self.T_hot[i+1]  = self.T_hot[i]  + dT_hot
    self.T_cold[i+1] = self.T_cold[i] + dT_cold

    # Cumulative heat transferred so far (Joules).
    self.Q_transferred[i+1] = self.Q_transferred[i] + Q_dot * self.dt

    # ── ENTROPY GENERATION ──────────────────────────────────────────
    # How much entropy was created during this tiny timestep?
    S_gen_dot = self.calculate_entropy_generation_rate(
        Q_dot, self.T_hot[i], self.T_cold[i]
    )
    # Accumulate: add this step's entropy to the running total.
    # This is why the entropy chart always rises — it can never decrease.
    self.S_gen_cumulative[i+1] = self.S_gen_cumulative[i] + S_gen_dot * self.dt

    self.current_step += 1
    return True
```

---

## 3. The Four Ideas as One Story

Here is the complete physical story the simulation tells, from start to finish:

```
START
  T_hot = 400 K, T_cold = 300 K
  Large temperature gap → large Q_dot → fast heat flow
  Entropy being generated rapidly

       ↓  time passes  ↓

MIDDLE
  T_hot ≈ 370 K, T_cold ≈ 330 K
  Smaller temperature gap → slower Q_dot → slower heat flow
  Entropy still being generated, but more slowly

       ↓  time passes  ↓

END
  T_hot = T_cold = T_eq ≈ 350 K
  No temperature gap → Q_dot = 0 → no more heat flow
  Entropy generation stops — but total entropy is now permanently higher
  The process cannot reverse itself
```

Every chart in the simulation illustrates one part of this story:

|Chart|What It Shows|
|---|---|
|Temperature vs Time|The gap closing as both reservoirs approach T_eq|
|Heat Flux|Q̇ starting large and decaying to zero|
|Cumulative Heat Transferred|Total energy moved, levelling off at equilibrium|
|Entropy Generation|Always rising, never falling — the signature of irreversibility|

---

## 4. Practice Exercise

This exercise uses only arithmetic — no coding required. Work through it by hand or with a calculator.

**Setup:** Two reservoirs with the following properties:

```
T_hot_initial  = 500 K
T_cold_initial = 250 K
m_hot          = 2 kg
m_cold         = 1 kg
c_p            = 1000 J/(kg·K)    (same for both)
h              = 100 W/K
```

**Answer these four questions:**

1. What is the equilibrium temperature T_eq? _(Use the energy balance formula.)_
2. What is the initial heat transfer rate Q̇? _(Use Newton's Law of Cooling.)_
3. Is (1/T_cold − 1/T_hot) positive or negative at the start? What does that tell you?
4. If the mass of the hot reservoir doubled to 4 kg (everything else unchanged), would T_eq go up, down, or stay the same? Why, in one sentence?

---

## 5. Key Takeaways

- **Newton's Law of Cooling** (`Q̇ = h × (T_hot − T_cold)`) says heat flow rate is proportional to the temperature difference. As the gap closes, flow slows — which is why both the heat flux chart and the rate of temperature change decay over time.
- **The equilibrium temperature** is set by energy conservation — whatever the hot reservoir loses, the cold reservoir gains. Mass ratio shifts T_eq: more mass on the hot side pulls it higher.
- **Entropy generation** (`Ṡ_gen = Q̇ × (1/T_cold − 1/T_hot)`) is always positive for irreversible heat transfer. It measures lost potential — the useful work that could have been extracted but wasn't.
- **"Irreversible" means the process has a direction.** Once 400 K and 300 K become 350 K and 350 K, entropy has been generated and the original state cannot be recovered spontaneously. This is the Second Law of Thermodynamics in action.
- **Every formula in `IrreversibleHeatTransfer` maps directly to a physical principle.** `calculate_heat_transfer_rate()` is Newton's Law of Cooling. `_calculate_equilibrium_temp()` is energy conservation. `calculate_entropy_generation_rate()` is the Second Law. `step()` is where they all run together, 2,000 times per simulation.

---

# Lesson 17: The Architecture of the Full Script — How Everything Connects

---

## 1. Plain-English Concept Explanation

### What is "architecture"?

When a script grows beyond a few lines, you need to make decisions about **how to organize the code**. Which code goes where? Who is responsible for what? These decisions, taken together, are called the **architecture** of the program.

Our thermodynamics script has two classes. Understanding _why_ there are two — and not one, not five — is the most important architectural insight in the whole script.

---

### The single most important idea: Separation of Concerns

**"Separation of concerns"** means: each piece of code should have **one clear job**, and should not trespass into another piece's job.

Think of a hospital:

- A **doctor** diagnoses and decides treatment. They don't mop floors.
- A **cleaner** maintains the building. They don't prescribe medication.
- Both are essential. Neither does the other's job. If one calls in sick, the other can still function.

Our script follows the same principle:

|Class|Its one job|What it does NOT do|
|---|---|---|
|`IrreversibleHeatTransfer`|Own the physics and data|Nothing about plots, sliders, or windows|
|`InteractiveVisualizer`|Own the visual interface|No physics equations, no raw data arrays|

---

### The relationship between the two classes

`InteractiveVisualizer` **contains** an `IrreversibleHeatTransfer` object. It stores it as `self.sim`. This is called **composition** — one object holding a reference to another.

This is a one-way relationship:

- `InteractiveVisualizer` knows about `IrreversibleHeatTransfer` (via `self.sim`)
- `IrreversibleHeatTransfer` knows **nothing** about `InteractiveVisualizer`

That one-way dependency is intentional and important. More on why shortly.

---

## 2. Annotated Code Examples

### How `self.sim` is created

```python
class InteractiveVisualizer:

    def __init__(self):                          # Called when visualizer is created
        self.sim = IrreversibleHeatTransfer(     # Create the physics object
            system_type="Closed"                 # Pass in initial settings
        )                                        # self.sim now holds the entire
                                                 # physics engine
```

> From this point on, anywhere inside `InteractiveVisualizer`, `self.sim` gives access to all of the physics data — temperatures, entropy, time arrays, and so on.

---

### How slider callbacks update `self.sim` then re-run the simulation

```python
def on_slider_change(self, val):        # 'val' is the new slider value
                                        # matplotlib passes it automatically

    # Step 1: Push new values INTO the physics object
    self.sim.T_hot_0 = self.slider_T_hot.val   # Update hot temperature
    self.sim.T_cold_0 = self.slider_T_cold.val  # Update cold temperature
    self.sim.h = self.slider_h.val              # Update heat transfer coefficient
    self.sim.m_hot = self.slider_mass_ratio.val # Update mass of hot reservoir
    self.sim.m_cold = 1.0                       # Keep cold mass fixed at 1.0 kg

    # Step 2: Recalculate the equilibrium temperature with new values
    self.sim.T_eq = self.sim._calculate_equilibrium_temp()

    # Step 3: Re-run the full simulation with updated parameters
    self.update_simulation()   # This calls self.sim.run_full_simulation()

    # Step 4: Redraw all five plots with the new data
    self.plot_all()
```

> Notice the direction of information flow: Slider → `InteractiveVisualizer` method → `self.sim` parameters → simulation runs → plots update. The physics object never touches the slider. The slider never touches the physics directly.

---

### How the animation loop calls the physics then redraws

```python
def animate(self, frame):               # Called repeatedly by FuncAnimation
                                        # 'frame' is a counter matplotlib provides

    if self.is_playing and \            # Only run if the Play button is active
       self.sim.current_step < self.sim.n_steps - 1:  # And simulation isn't finished

        for _ in range(5):              # Advance 5 physics steps per animation frame
                                        # Makes the animation run at visible speed

            if not self.sim.step():     # Ask the physics object for one time step
                                        # step() returns False when done
                self.is_playing = False # Stop playing if simulation is complete
                break                   # Exit the loop early

        self.plot_all()                 # After advancing physics, redraw all plots

    return []                           # Required by FuncAnimation (can be empty)
```

> `self.sim.step()` is doing the physics math. `self.plot_all()` is doing the drawing. These two lines are the heartbeat of the animation — physics first, then visuals.

---

### How `main()` starts everything

```python
def main():
    # Create the visualizer — this also creates self.sim internally
    visualizer = InteractiveVisualizer()

    # Open the matplotlib window and hand control to the event loop
    # (The event loop listens for slider moves, button clicks, animation frames)
    visualizer.show()
```

> `main()` is intentionally simple. Its only job is to be the entry point — the "on switch" for the whole program. All real logic lives inside the classes.

---

## 3. The Dependency Map

Read the arrows as **"depends on"** or **"calls"**:

```
┌─────────────────────────────────────────────────────────────────┐
│                          main()                                 │
│                             │                                   │
│              creates and calls .show()                          │
│                             │                                   │
│                             ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              InteractiveVisualizer                       │   │
│  │                                                          │   │
│  │  Owns:  self.fig, self.ax_*, sliders, buttons            │   │
│  │                                                          │   │
│  │  ┌─────────────────────────────────────────────────┐    │   │
│  │  │  setup_figure()  ──────────────► draws layout   │    │   │
│  │  │  setup_sliders() ──────────────► creates widgets│    │   │
│  │  │  setup_buttons() ──────────────► creates buttons│    │   │
│  │  │                                                  │    │   │
│  │  │  on_slider_change()                              │    │   │
│  │  │    │  updates self.sim.*                         │    │   │
│  │  │    │  calls update_simulation()                  │    │   │
│  │  │    └─────────────────────────────┐               │    │   │
│  │  │                                  │               │    │   │
│  │  │  animate()                       │               │    │   │
│  │  │    │  calls self.sim.step()  ◄───┘               │    │   │
│  │  │    │  calls self.plot_all()                      │    │   │
│  │  │    └──────────────────────────────────────────►  │    │   │
│  │  │             redraws ax_visual, ax_temp,           │    │   │
│  │  │             ax_heat, ax_entropy, ax_flux          │    │   │
│  │  └─────────────────────────────────────────────────┘    │   │
│  │                        │                                 │   │
│  │              self.sim  │  (one-way reference)            │   │
│  │                        ▼                                 │   │
│  │  ┌───────────────────────────────────────────────────┐  │   │
│  │  │         IrreversibleHeatTransfer                  │  │   │
│  │  │                                                   │  │   │
│  │  │  Owns:  T_hot[], T_cold[], S_gen[], Q[], time[]   │  │   │
│  │  │                                                   │  │   │
│  │  │  __init__()   ── sets up parameters               │  │   │
│  │  │  reset_simulation() ── zeroes all arrays          │  │   │
│  │  │  step()       ── advances physics one timestep    │  │   │
│  │  │  run_full_simulation() ── calls step() in a loop  │  │   │
│  │  │  _calculate_equilibrium_temp() ── energy balance  │  │   │
│  │  │  calculate_heat_transfer_rate() ── Q_dot = h·ΔT   │  │   │
│  │  │  calculate_entropy_generation_rate() ── S_gen_dot │  │   │
│  │  │                                                   │  │   │
│  │  │  ✗ Knows NOTHING about plots, sliders, or figures │  │   │
│  │  └───────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### Information flow at each key moment

```
USER MOVES A SLIDER
        │
        ▼
on_slider_change() fires
        │
        ├──► writes new values into self.sim.*
        │
        ├──► calls self.sim.run_full_simulation()
        │         (recomputes all physics arrays)
        │
        └──► calls self.plot_all()
                  (redraws all five axes)


USER CLICKS PLAY
        │
        ▼
toggle_animation() fires
        │
        └──► sets self.is_playing = True
             starts FuncAnimation loop
                  │
                  ▼ (every 50 milliseconds)
             animate(frame) fires
                  │
                  ├──► self.sim.step() × 5
                  │         (advances physics)
                  │
                  └──► self.plot_all()
                            (redraws plots)


USER CLICKS RESET
        │
        ▼
reset_animation() fires
        │
        ├──► self.is_playing = False
        │
        ├──► self.sim.reset_simulation()
        │         (zeroes arrays, resets step counter)
        │
        └──► self.plot_all()
                  (redraws empty/initial plots)


PROGRAM STARTS
        │
        ▼
main() runs
        │
        └──► InteractiveVisualizer()
                  │
                  ├──► creates self.sim (IrreversibleHeatTransfer)
                  ├──► setup_figure()
                  ├──► setup_sliders()
                  ├──► setup_buttons()
                  ├──► update_simulation() → self.sim.run_full_simulation()
                  └──► plot_all()
                            │
                            └──► .show() opens the window
```

---

## 4. How This Connects to Our Script

Every connection in the map above is a real line of code in the script. Here are the three most important ones to find and re-read now that you have the full picture:

**Connection 1 — The visualizer creates the simulator:**

```python
# Inside InteractiveVisualizer.__init__()
self.sim = IrreversibleHeatTransfer(system_type="Closed")
# This single line creates the entire physics engine and stores it.
```

**Connection 2 — The slider callback bridges both classes:**

```python
# Inside on_slider_change() — this is where the two classes "talk"
self.sim.T_hot_0 = self.slider_T_hot.val  # Visualizer writes into simulator
self.update_simulation()                   # Visualizer asks simulator to recompute
self.plot_all()                            # Visualizer redraws its own axes
```

**Connection 3 — The animation heartbeat:**

```python
# Inside animate() — physics first, visuals second, every single frame
if not self.sim.step():     # Physics object does one unit of work
    self.is_playing = False
self.plot_all()             # Visual object redraws everything
```

---

## 5. Why Are the Two Classes Separated? What Breaks If You Merge Them?

### The case for separation

The physics of heat transfer is **the same regardless of how you display it**. You could display it as:

- An animated matplotlib window (what we do)
- A web page
- A printed table of numbers
- A different library entirely

If the physics equations live in their own class, you can swap the display layer without touching a single line of physics code. The physics doesn't care.

Equally, the display code is **the same regardless of what physics you're simulating**. Sliders, axes, and animation loops are generic tools. If tomorrow you wanted to simulate fluid dynamics instead of heat transfer, you could reuse `InteractiveVisualizer`'s structure almost entirely.

Separation also makes **debugging far easier**. If your entropy values are wrong, you know to look in `IrreversibleHeatTransfer`. If your slider isn't responding, you know to look in `InteractiveVisualizer`. The bug cannot be in both places at once.

### What would break if you merged them

Imagine a single merged class called `HeatSimulatorApp`. It would contain:

- Temperature arrays sitting next to slider definitions
- Physics equations tangled up with `ax.plot()` calls
- `reset_simulation()` also having to know about axis labels

Concretely, these problems would emerge:

```
PROBLEM 1 — Untestable physics
   To test whether your entropy equation is correct, you'd have
   to create a full matplotlib window first. You couldn't run
   the math on its own.

PROBLEM 2 — Unmaintainable size
   The merged class would have 15+ methods with no clear grouping.
   Finding the bug in "the entropy calculation" would mean searching
   through slider code, animation code, and plot code first.

PROBLEM 3 — Fragile changes
   Changing the number of plots would force you to check whether
   anything in the physics equations accidentally depended on
   the figure layout. With separation, that's impossible.

PROBLEM 4 — No reusability
   You couldn't reuse the physics logic in a different project
   (say, a command-line version) without dragging along all the
   matplotlib dependencies.
```

---

## 6. Practice Exercise

No new code to write for this one — this lesson is about reading and understanding.

**Task:** Open the script and trace these three paths manually, line by line.

**Path A — Slider drag:** Starting from `self.slider_T_hot.on_changed(self.on_slider_change)`, follow exactly what happens when a user drags the T_hot slider to a new value. Write down (in plain English, not code) every method that gets called, in order.

**Path B — One animation frame:** Starting from the `FuncAnimation` call in `toggle_animation()`, trace what happens during a single animation frame. Write down every method called and what each one does.

**Path C — Cold start:** Starting from the last two lines of the script (`if __name__ == "__main__": main()`), trace every method called before the window becomes visible. Write the chain as a numbered list.

**Stretch challenge:** Find one place in the script where `IrreversibleHeatTransfer` is given information _from_ `InteractiveVisualizer`, and one place where `InteractiveVisualizer` reads data _from_ `IrreversibleHeatTransfer`. What does each transfer?

---

## 7. Key Takeaways

- **`IrreversibleHeatTransfer`** owns all physics data and equations; it has no knowledge of plots, sliders, or figures — and that ignorance is intentional.
- **`InteractiveVisualizer`** owns the entire visual layer; it accesses the physics exclusively through `self.sim`, a reference created in `__init__`.
- The **information flow is one-way**: the visualizer writes into and reads from the simulator; the simulator never calls back into the visualizer.
- **Separation of concerns** means each class has one job; this makes bugs easier to locate, code easier to reuse, and changes less likely to cause unexpected side-effects.
- **`main()`** is intentionally minimal — its only job is to create the visualizer and open the window; all real logic lives inside the two classes.

---

# Lesson 18: Building the Script From Scratch

---

> 💡 **How to use this lesson:** Follow each step in order. Do not move to the next step until the current one works. Every step ends with a "What you should see" check. If you don't see that, something needs fixing before continuing.

> ⚠️ **Environment note:** This script requires matplotlib and numpy to be installed. If you haven't installed them yet, run this in your terminal before starting:
> 
> ```
> pip install matplotlib numpy
> ```

---

## Step 1: Create the File and Run a Print Statement

**What you're doing:** Confirming that Python is working and you can run a file.

Create a new file called `heat_transfer.py`. Type this exactly:

```python
# heat_transfer.py

def main():
    print("Heat transfer simulation starting...")   # confirm the file runs

if __name__ == "__main__":
    main()    # call main() when the file is run directly
```

Run it from your terminal:

```
python heat_transfer.py
```

**What you should see:**

```
Heat transfer simulation starting...
```

If you see this, Python is working and your file is set up correctly. ✅

---

## Step 2: Add the Imports

**What you're doing:** Loading the external libraries the script depends on. All imports go at the very top of the file, before anything else.

```python
# heat_transfer.py

import numpy as np                            # numerical arrays and math
import matplotlib.pyplot as plt               # plotting
from matplotlib.animation import FuncAnimation  # animation loop
from matplotlib.widgets import Slider, Button   # interactive controls
import matplotlib.patches as patches          # shapes (rectangles, arrows)

def main():
    print("Imports loaded successfully")

if __name__ == "__main__":
    main()
```

Run it again.

**What you should see:**

```
Imports loaded successfully
```

If you see an `ImportError` instead, numpy or matplotlib is not installed. Run `pip install matplotlib numpy` in your terminal and try again. ✅

---

## Step 3: Build `IrreversibleHeatTransfer.__init__()` and Test It

**What you're doing:** Creating the simulation class and its setup method. You're not calculating anything yet — just storing the starting values.

```python
# heat_transfer.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches


class IrreversibleHeatTransfer:
    """Simulates heat transfer between two thermal reservoirs."""

    def __init__(self, T_hot_initial=400, T_cold_initial=300,
                 mass_hot=1.0, mass_cold=1.0, c_p=1000, system_type="Closed"):

        # Store all starting values as instance attributes
        self.T_hot_0    = T_hot_initial    # initial hot reservoir temperature (K)
        self.T_cold_0   = T_cold_initial   # initial cold reservoir temperature (K)
        self.m_hot      = mass_hot         # mass of hot reservoir (kg)
        self.m_cold     = mass_cold        # mass of cold reservoir (kg)
        self.c_p        = c_p             # specific heat capacity (J/kg·K)
        self.system_type = system_type    # "Closed", "Open", or "Isolated"

        # Heat transfer coefficient — controls how fast heat flows
        self.h  = 50     # W/K

        # Time parameters
        self.dt    = 0.1   # time step in seconds
        self.t_max = 200   # total simulation time in seconds


def main():
    # Create a simulation object with default values
    sim = IrreversibleHeatTransfer()

    # Print attributes to confirm they were stored correctly
    print("T_hot_0:     ", sim.T_hot_0)       # should print 400
    print("T_cold_0:    ", sim.T_cold_0)      # should print 300
    print("system_type: ", sim.system_type)   # should print Closed
    print("dt:          ", sim.dt)            # should print 0.1
    print("t_max:       ", sim.t_max)         # should print 200


if __name__ == "__main__":
    main()
```

**What you should see:**

```
T_hot_0:      400
T_cold_0:     300
system_type:  Closed
dt:           0.1
t_max:        200
```

✅

---

## Step 4: Add `_calculate_equilibrium_temp()` and Verify the Math

**What you're doing:** Adding the first real calculation — the temperature both reservoirs will eventually reach.

Add this method inside the class, directly after `__init__`:

```python
    def _calculate_equilibrium_temp(self):
        """Calculate final equilibrium temperature using energy conservation."""
        # Numerator: total thermal energy in the system
        numerator = (self.m_hot  * self.c_p * self.T_hot_0 +
                     self.m_cold * self.c_p * self.T_cold_0)

        # Denominator: total heat capacity of the system
        denominator = self.m_hot * self.c_p + self.m_cold * self.c_p

        return numerator / denominator    # equilibrium temperature in Kelvin
```

Now update `__init__` to call it and store the result, and update `main()` to check it:

```python
    def __init__(self, T_hot_initial=400, T_cold_initial=300,
                 mass_hot=1.0, mass_cold=1.0, c_p=1000, system_type="Closed"):

        self.T_hot_0     = T_hot_initial
        self.T_cold_0    = T_cold_initial
        self.m_hot       = mass_hot
        self.m_cold      = mass_cold
        self.c_p         = c_p
        self.system_type = system_type
        self.h           = 50
        self.dt          = 0.1
        self.t_max       = 200

        # Calculate and store the equilibrium temperature
        self.T_eq = self._calculate_equilibrium_temp()   # calls the new method
```

```python
def main():
    sim = IrreversibleHeatTransfer()
    print("T_eq (equal masses, 400/300):", sim.T_eq)   # should print 350.0

    # Test with unequal masses
    sim2 = IrreversibleHeatTransfer(mass_hot=2.0, mass_cold=1.0)
    print("T_eq (m_hot=2, m_cold=1):   ", sim2.T_eq)   # should be above 350
```

**What you should see:**

```
T_eq (equal masses, 400/300): 350.0
T_eq (m_hot=2, m_cold=1):    366.666...
```

✅

---

## Step 5: Add `reset_simulation()` and Confirm Arrays Are Created

**What you're doing:** Creating the empty arrays that will store temperature, entropy, and heat values at every time step.

Add this method to the class after `_calculate_equilibrium_temp()`:

```python
    def reset_simulation(self):
        """Create empty arrays and set initial conditions."""

        # Build the time axis: values from 0 to t_max, spaced dt apart
        self.time    = np.arange(0, self.t_max, self.dt)
        self.n_steps = len(self.time)    # how many time steps total

        # Create zero-filled arrays — one slot per time step
        self.T_hot             = np.zeros(self.n_steps)   # hot temperature over time
        self.T_cold            = np.zeros(self.n_steps)   # cold temperature over time
        self.Q_transferred     = np.zeros(self.n_steps)   # cumulative heat
        self.S_gen_cumulative  = np.zeros(self.n_steps)   # cumulative entropy generated
        self.heat_flux         = np.zeros(self.n_steps)   # instantaneous heat rate

        # Fill in the starting values at index 0
        self.T_hot[0]  = self.T_hot_0
        self.T_cold[0] = self.T_cold_0

        # Track which step we're on (used by the animation)
        self.current_step = 0
```

Also add a call to `reset_simulation()` at the bottom of `__init__`:

```python
        # (at the end of __init__, after self.T_eq = ...)
        self.reset_simulation()
```

Update `main()`:

```python
def main():
    sim = IrreversibleHeatTransfer()

    print("n_steps:       ", sim.n_steps)       # should print 2000
    print("T_hot[0]:      ", sim.T_hot[0])      # should print 400.0
    print("T_cold[0]:     ", sim.T_cold[0])     # should print 300.0
    print("T_hot length:  ", len(sim.T_hot))    # should print 2000
```

**What you should see:**

```
n_steps:        2000
T_hot[0]:       400.0
T_cold[0]:      300.0
T_hot length:   2000
```

✅

---

## Step 6: Add the Two Rate Calculation Methods

**What you're doing:** Adding the physics — the formulas that calculate how fast heat flows and how much entropy is generated at any given moment.

Add both methods to the class:

```python
    def calculate_heat_transfer_rate(self, T_h, T_c):
        """Return heat transfer rate (W). Returns 0 for isolated systems."""
        if self.system_type == "Isolated":
            return 0.0                  # isolated: no heat exchange at all

        return self.h * (T_h - T_c)    # rate proportional to temperature gap


    def calculate_entropy_generation_rate(self, Q_dot, T_h, T_c):
        """Return entropy generation rate (W/K). Always >= 0."""
        if Q_dot == 0 or T_h == T_c:
            return 0                    # no heat flow = no irreversibility

        return Q_dot * (1/T_c - 1/T_h) # Second Law formula
```

Update `main()` to test both:

```python
def main():
    sim = IrreversibleHeatTransfer()

    # Test heat transfer rate
    Q = sim.calculate_heat_transfer_rate(400.0, 300.0)
    print("Heat rate (400→300):", Q)      # should print 5000.0  (50 * 100)

    Q_zero = sim.calculate_heat_transfer_rate(350.0, 350.0)
    print("Heat rate (equal T):", Q_zero) # should print 0.0

    # Test entropy generation rate
    S = sim.calculate_entropy_generation_rate(5000.0, 400.0, 300.0)
    print("Entropy gen rate:   ", round(S, 4))  # should print a positive number
```

**What you should see:**

```
Heat rate (400→300): 5000.0
Heat rate (equal T): 0.0
Entropy gen rate:    4.1667
```

✅

---

## Step 7: Add `step()` and `run_full_simulation()`, Print First and Last Values

**What you're doing:** Adding the engine of the simulation — `step()` advances time by one increment, and `run_full_simulation()` calls it until the arrays are full.

```python
    def step(self):
        """Advance the simulation by one time step. Returns False when finished."""
        if self.current_step >= self.n_steps - 1:
            return False      # no more steps to take

        i = self.current_step

        # Calculate heat flow at this moment
        Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
        self.heat_flux[i] = Q_dot

        # Calculate temperature changes
        if self.system_type == "Isolated":
            dT_hot  = 0.0
            dT_cold = 0.0
        else:
            dT_hot  = -Q_dot * self.dt / (self.m_hot  * self.c_p)  # hot cools down
            dT_cold =  Q_dot * self.dt / (self.m_cold * self.c_p)  # cold warms up

        # Store new temperatures in the next array slot
        self.T_hot[i+1]  = self.T_hot[i]  + dT_hot
        self.T_cold[i+1] = self.T_cold[i] + dT_cold

        # Accumulate heat transferred
        self.Q_transferred[i+1] = self.Q_transferred[i] + Q_dot * self.dt

        # Calculate and accumulate entropy generation
        S_dot = self.calculate_entropy_generation_rate(Q_dot, self.T_hot[i], self.T_cold[i])
        self.S_gen_cumulative[i+1] = self.S_gen_cumulative[i] + S_dot * self.dt

        self.current_step += 1
        return True


    def run_full_simulation(self):
        """Reset and run all steps to completion."""
        self.reset_simulation()
        for i in range(self.n_steps - 1):
            self.step()
```

Update `main()`:

```python
def main():
    sim = IrreversibleHeatTransfer()
    sim.run_full_simulation()

    print("T_hot  first:", round(sim.T_hot[0], 2))     # should print 400.0
    print("T_hot  last: ", round(sim.T_hot[-1], 2))    # should be near 350.0
    print("T_cold first:", round(sim.T_cold[0], 2))    # should print 300.0
    print("T_cold last: ", round(sim.T_cold[-1], 2))   # should be near 350.0
    print("Total entropy generated:", round(sim.S_gen_cumulative[-1], 4))
```

**What you should see:**

```
T_hot  first: 400.0
T_hot  last:  350.02   ← close to 350, not exact due to discrete time steps
T_cold first: 300.0
T_cold last:  349.98
Total entropy generated: 57.5   ← a positive number confirming irreversibility
```

> 💡 The exact values may differ slightly — the important check is that T_hot fell toward 350, T_cold rose toward 350, and entropy generated is positive. ✅

---

## Step 8: Build a Minimal Static Plot to Confirm the Data

**What you're doing:** Before building the full interactive figure, confirm the simulation data is correct by drawing one simple plot.

```python
def main():
    sim = IrreversibleHeatTransfer()
    sim.run_full_simulation()

    # One simple plot — temperature vs time
    plt.figure(figsize=(8, 4))
    plt.plot(sim.time, sim.T_hot,  'r-', label='Hot Reservoir')
    plt.plot(sim.time, sim.T_cold, 'b-', label='Cold Reservoir')
    plt.axhline(sim.T_eq, color='green', linestyle='--', label='Equilibrium')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature vs Time — Sanity Check')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
```

**What you should see:** A window with two curves converging — red falling from 400, blue rising from 300, both meeting near the green dashed line at 350. ✅

---

## Step 9: Build `setup_figure()` with All Five Axes

**What you're doing:** Creating the `InteractiveVisualizer` class and laying out the five subplot regions. No data yet — just the empty frame.

Add this new class below `IrreversibleHeatTransfer` and above `main()`:

```python
class InteractiveVisualizer:
    """Manages the interactive figure, widgets, and animation."""

    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]
        self.sim = IrreversibleHeatTransfer(system_type="Closed")  # simulation object
        self.is_playing = False     # animation state flag
        self.animation  = None      # will hold the FuncAnimation object later
        self.setup_figure()

    def setup_figure(self):
        """Create figure and all subplot axes."""
        self.fig = plt.figure(figsize=(16, 10))
        self.fig.suptitle('Irreversible Heat Transfer: Hot and Cold Reservoirs',
                          fontsize=16, fontweight='bold')

        # Grid layout: 3 rows, 3 columns
        # hspace/wspace: vertical/horizontal spacing between plots
        # left/right/top/bottom: margins around the whole grid
        gs = self.fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3,
                                   left=0.08, right=0.95,
                                   top=0.92,  bottom=0.25)

        # Assign each subplot to an attribute
        self.ax_visual  = self.fig.add_subplot(gs[0, :])   # full top row
        self.ax_temp    = self.fig.add_subplot(gs[1, :2])  # middle-left (wide)
        self.ax_heat    = self.fig.add_subplot(gs[1, 2])   # middle-right (narrow)
        self.ax_entropy = self.fig.add_subplot(gs[2, :2])  # bottom-left (wide)
        self.ax_flux    = self.fig.add_subplot(gs[2, 2])   # bottom-right (narrow)

    def show(self):
        plt.show()
```

Update `main()`:

```python
def main():
    viz = InteractiveVisualizer()
    viz.show()
```

**What you should see:** A large empty figure with five blank subplot regions and a title at the top. No data yet — that's expected. ✅

---

## Step 10: Add Each Plot Method — Temperature, Heat, Entropy, Flux

**What you're doing:** Filling the four data subplots. Add all four methods to `InteractiveVisualizer`, and add a `plot_all()` method to call them together. Also call `run_full_simulation()` at the end of `__init__`.

First, update `__init__` to run the simulation and call `plot_all()` after `setup_figure()`:

```python
    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]
        self.sim = IrreversibleHeatTransfer(system_type="Closed")
        self.is_playing = False
        self.animation  = None
        self.setup_figure()
        self.sim.run_full_simulation()   # run simulation before plotting
        self.plot_all()                  # draw all plots with initial data
```

Now add the plot methods:

```python
    def plot_all(self):
        """Redraw all subplots."""
        self.plot_temperature()
        self.plot_heat_transferred()
        self.plot_entropy()
        self.plot_heat_flux()
        self.fig.canvas.draw_idle()    # refresh the figure without flickering


    def plot_temperature(self):
        self.ax_temp.clear()    # wipe previous content before redrawing

        idx = min(self.sim.current_step, self.sim.n_steps - 1)

        self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_hot[:idx+1],
                          'r-', linewidth=2, label='Hot Reservoir')
        self.ax_temp.plot(self.sim.time[:idx+1], self.sim.T_cold[:idx+1],
                          'b-', linewidth=2, label='Cold Reservoir')
        self.ax_temp.axhline(self.sim.T_eq, color='green', linestyle='--',
                             linewidth=2, label='Equilibrium')
        self.ax_temp.set_xlabel('Time (s)')
        self.ax_temp.set_ylabel('Temperature (K)')
        self.ax_temp.set_title('Temperature Evolution (Irreversible Process)')
        self.ax_temp.legend(loc='best')
        self.ax_temp.grid(True, alpha=0.3)
        self.ax_temp.set_xlim(0, self.sim.t_max)


    def plot_heat_transferred(self):
        self.ax_heat.clear()

        idx = min(self.sim.current_step, self.sim.n_steps - 1)

        self.ax_heat.plot(self.sim.time[:idx+1],
                          self.sim.Q_transferred[:idx+1] / 1000,   # convert J → kJ
                          'purple', linewidth=2)
        self.ax_heat.set_xlabel('Time (s)')
        self.ax_heat.set_ylabel('Heat (kJ)')
        self.ax_heat.set_title('Cumulative Heat\nTransferred')
        self.ax_heat.grid(True, alpha=0.3)
        self.ax_heat.set_xlim(0, self.sim.t_max)


    def plot_entropy(self):
        self.ax_entropy.clear()

        idx = min(self.sim.current_step, self.sim.n_steps - 1)

        self.ax_entropy.plot(self.sim.time[:idx+1],
                             self.sim.S_gen_cumulative[:idx+1],
                             'orange', linewidth=2)
        self.ax_entropy.set_xlabel('Time (s)')
        self.ax_entropy.set_ylabel('Entropy Generation (J/K)')
        self.ax_entropy.set_title('Entropy Generation (Irreversibility Measure)')
        self.ax_entropy.grid(True, alpha=0.3)
        self.ax_entropy.set_xlim(0, self.sim.t_max)

        if idx > 0:
            total_S = self.sim.S_gen_cumulative[idx]
            self.ax_entropy.text(
                0.98, 0.95, f'Total: {total_S:.2f} J/K',
                transform=self.ax_entropy.transAxes,
                ha='right', va='top',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7)
            )


    def plot_heat_flux(self):
        self.ax_flux.clear()

        idx = min(self.sim.current_step, self.sim.n_steps - 1)

        self.ax_flux.plot(self.sim.time[:idx+1],
                          self.sim.heat_flux[:idx+1],
                          'darkgreen', linewidth=2)
        self.ax_flux.set_xlabel('Time (s)')
        self.ax_flux.set_ylabel('Heat Flux (W)')
        self.ax_flux.set_title('Instantaneous\nHeat Transfer Rate')
        self.ax_flux.grid(True, alpha=0.3)
        self.ax_flux.set_xlim(0, self.sim.t_max)
```

**What you should see:** The figure now has four populated plots. The top row is still blank — that's the visual reservoir diagram, coming next. ✅

---

## Step 11: Add `plot_reservoir_visual()` with Rectangles and Arrow

**What you're doing:** Adding the reservoir diagram — two coloured rectangles with an arrow showing heat direction.

Add this method and include it in `plot_all()`:

```python
    def plot_reservoir_visual(self):
        self.ax_visual.clear()
        self.ax_visual.set_xlim(0, 10)
        self.ax_visual.set_ylim(0, 3)
        self.ax_visual.axis('off')     # hide axis ticks and borders
        self.ax_visual.set_title('Thermal Reservoirs', fontsize=14, fontweight='bold')

        idx = min(self.sim.current_step, self.sim.n_steps - 1)
        T_h = self.sim.T_hot[idx]
        T_c = self.sim.T_cold[idx]

        def temp_to_color(T):
            """Map temperature to a red-blue colour."""
            T_min, T_max = 250, 500
            normalized = np.clip((T - T_min) / (T_max - T_min), 0, 1)
            return (normalized, 0.2, 1 - normalized)   # (red, green, blue)

        # --- Hot reservoir rectangle (left side) ---
        hot_rect = patches.Rectangle(
            (1, 0.5), 2, 2,              # (x, y), width, height
            facecolor=temp_to_color(T_h),
            edgecolor='black', linewidth=2
        )
        self.ax_visual.add_patch(hot_rect)
        self.ax_visual.text(2, 2.7, f'HOT\n{T_h:.1f} K',
                            ha='center', fontsize=12, fontweight='bold')

        # --- Cold reservoir rectangle (right side) ---
        cold_rect = patches.Rectangle(
            (7, 0.5), 2, 2,
            facecolor=temp_to_color(T_c),
            edgecolor='black', linewidth=2
        )
        self.ax_visual.add_patch(cold_rect)
        self.ax_visual.text(8, 2.7, f'COLD\n{T_c:.1f} K',
                            ha='center', fontsize=12, fontweight='bold')

        # --- Heat flow arrow (only if hot is still hotter than cold) ---
        if T_h > T_c:
            arrow = patches.FancyArrowPatch(
                (3.2, 1.5), (6.8, 1.5),   # from, to
                arrowstyle='->', mutation_scale=30,
                linewidth=3, color='red'
            )
            self.ax_visual.add_patch(arrow)
            self.ax_visual.text(5, 1.8, 'Heat Flow',
                                ha='center', fontsize=11,
                                color='red', fontweight='bold')

        # --- Equilibrium label ---
        self.ax_visual.text(
            5, 0.3, f'Equilibrium: {self.sim.T_eq:.1f} K',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8)
        )

        # --- System type label ---
        self.ax_visual.text(
            5, 2.95, f'System: {self.sim.system_type}',
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
        )
```

Update `plot_all()` to include the new method:

```python
    def plot_all(self):
        self.plot_reservoir_visual()     # add this line at the top
        self.plot_temperature()
        self.plot_heat_transferred()
        self.plot_entropy()
        self.plot_heat_flux()
        self.fig.canvas.draw_idle()
```

**What you should see:** The top panel now shows two coloured rectangles (red-ish left, blue-ish right) with a red arrow between them and temperature labels. ✅

---

## Step 12: Add `setup_sliders()` and Confirm They Appear

**What you're doing:** Adding the four sliders and radio buttons below the plots.

Add the method to `InteractiveVisualizer`:

```python
    def setup_sliders(self):
        from matplotlib.widgets import RadioButtons

        slider_color = 'lightgoldenrodyellow'

        # Radio buttons for system type
        ax_sys = plt.axes([0.55, 0.15, 0.12, 0.08], facecolor=slider_color)
        self.radio_system = RadioButtons(ax_sys, self.system_types, active=0)
        self.radio_system.on_clicked(self.on_system_type_change)

        # Axes regions for sliders — each at a different vertical position
        ax_T_hot  = plt.axes([0.15, 0.15, 0.25, 0.02], facecolor=slider_color)
        ax_T_cold = plt.axes([0.15, 0.11, 0.25, 0.02], facecolor=slider_color)
        ax_h      = plt.axes([0.15, 0.07, 0.25, 0.02], facecolor=slider_color)
        ax_mass   = plt.axes([0.15, 0.03, 0.25, 0.02], facecolor=slider_color)

        # Create sliders
        self.slider_T_hot = Slider(ax_T_hot, 'T_hot (K)',
                                   310, 500, valinit=self.sim.T_hot_0, valstep=10)
        self.slider_T_cold = Slider(ax_T_cold, 'T_cold (K)',
                                    250, 400, valinit=self.sim.T_cold_0, valstep=10)
        self.slider_h = Slider(ax_h, 'Heat Transfer Coeff (W/K)',
                               10, 200, valinit=self.sim.h, valstep=10)
        self.slider_mass_ratio = Slider(ax_mass, 'Mass Ratio (m_hot/m_cold)',
                                        0.2, 5.0, valinit=1.0, valstep=0.1)

        # Register the same callback for all four sliders
        self.slider_T_hot.on_changed(self.on_slider_change)
        self.slider_T_cold.on_changed(self.on_slider_change)
        self.slider_h.on_changed(self.on_slider_change)
        self.slider_mass_ratio.on_changed(self.on_slider_change)
```

Add a placeholder callback (so the script doesn't crash when a slider is moved) and the system type callback:

```python
    def on_slider_change(self, val):
        pass    # placeholder — will be filled in next step

    def on_system_type_change(self, label):
        self.sim.system_type = label
        self.sim.T_eq = self.sim._calculate_equilibrium_temp()
        self.update_simulation()
        self.plot_all()

    def update_simulation(self):
        self.sim.run_full_simulation()
```

Update `__init__` to call `setup_sliders()` after `setup_figure()`:

```python
    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]
        self.sim = IrreversibleHeatTransfer(system_type="Closed")
        self.is_playing = False
        self.animation  = None
        self.setup_figure()
        self.setup_sliders()             # add this line
        self.sim.run_full_simulation()
        self.plot_all()
```

**What you should see:** Four labelled sliders and a set of three radio buttons appear below the plots. Dragging a slider does nothing visible yet — that's expected. ✅

---

## Step 13: Wire the `on_slider_change()` Callback

**What you're doing:** Replacing the placeholder with the real callback so sliders actually update the simulation.

Replace the `pass` placeholder in `on_slider_change()`:

```python
    def on_slider_change(self, val):
        # Read current position of every slider
        self.sim.T_hot_0  = self.slider_T_hot.val
        self.sim.T_cold_0 = self.slider_T_cold.val
        self.sim.h        = self.slider_h.val
        self.sim.m_hot    = self.slider_mass_ratio.val
        self.sim.m_cold   = 1.0

        # Recalculate equilibrium and re-run
        self.sim.T_eq = self.sim._calculate_equilibrium_temp()
        self.update_simulation()
        self.plot_all()
```

**What you should see:** Dragging any slider immediately redraws all five plots with updated data. The reservoir colours change, the equilibrium line moves, and the entropy total updates. ✅

---

## Step 14: Add `setup_buttons()` and the Button Callbacks

**What you're doing:** Adding Play/Pause and Reset buttons.

```python
    def setup_buttons(self):
        ax_play  = plt.axes([0.55, 0.10, 0.08, 0.04])
        ax_reset = plt.axes([0.55, 0.05, 0.08, 0.04])

        self.btn_play  = Button(ax_play,  'Play/Pause')
        self.btn_reset = Button(ax_reset, 'Reset')

        self.btn_play.on_clicked(self.toggle_animation)
        self.btn_reset.on_clicked(self.reset_animation)


    def toggle_animation(self, event):
        self.is_playing = not self.is_playing    # flip the playing state

        if self.is_playing:
            if self.animation is None:
                # Create the animation the first time Play is pressed
                self.animation = FuncAnimation(
                    self.fig, self.animate,
                    interval=50,    # milliseconds between frames
                    blit=False
                )
            self.sim.current_step = 0    # restart from the beginning


    def reset_animation(self, event):
        self.is_playing = False
        self.sim.reset_simulation()
        self.plot_all()
```

Add a placeholder `animate()` method for now:

```python
    def animate(self, frame):
        pass    # placeholder — will be completed in Step 15
        return []
```

Update `__init__` to call `setup_buttons()`:

```python
    def __init__(self):
        self.system_types = ["Closed", "Open", "Isolated"]
        self.sim = IrreversibleHeatTransfer(system_type="Closed")
        self.is_playing = False
        self.animation  = None
        self.setup_figure()
        self.setup_sliders()
        self.setup_buttons()             # add this line
        self.sim.run_full_simulation()
        self.plot_all()
```

**What you should see:** Two buttons appear below the radio buttons. Clicking them doesn't animate yet, but they should not cause any errors. ✅

---

## Step 15: Add `animate()` and Complete `FuncAnimation`

**What you're doing:** Replacing the placeholder `animate()` with the real version that advances the simulation frame by frame.

```python
    def animate(self, frame):
        """Called repeatedly by FuncAnimation. Advances simulation and redraws."""
        if self.is_playing and self.sim.current_step < self.sim.n_steps - 1:
            # Advance several steps per frame so the animation isn't too slow
            for _ in range(5):
                if not self.sim.step():    # step() returns False when finished
                    self.is_playing = False
                    break
            self.plot_all()    # redraw all plots after advancing

        return []    # required return value for FuncAnimation
```

**What you should see:** Clicking Play/Pause now animates the simulation from start to equilibrium. The temperature curves draw progressively, the reservoir colours shift, and the entropy plot fills in from left to right. Clicking Play/Pause again pauses it. Clicking Reset returns everything to the initial state. ✅

---

## Final `main()` Function

Replace any test code in `main()` with the final version:

```python
def main():
    print("Starting Irreversible Heat Transfer Simulation...")
    visualizer = InteractiveVisualizer()
    visualizer.show()

if __name__ == "__main__":
    main()
```

---

## Complete Build Checklist

|Step|What was built|Check|
|---|---|---|
|1|File runs, print works|✅|
|2|All imports load|✅|
|3|`__init__` stores attributes|✅|
|4|Equilibrium formula correct|✅|
|5|Arrays created, `T_hot[0]` = 400|✅|
|6|Heat rate and entropy rate return correct values|✅|
|7|`T_hot[-1]` ≈ 350 after full run|✅|
|8|Static plot shows converging curves|✅|
|9|Empty figure with five axes appears|✅|
|10|Four data plots filled with simulation results|✅|
|11|Reservoir diagram shows rectangles and arrow|✅|
|12|Sliders and radio buttons appear|✅|
|13|Dragging a slider updates all plots|✅|
|14|Buttons appear and don't crash|✅|
|15|Play animates; Pause stops; Reset restarts|✅|

---

# Lesson 19: Reading Error Messages and Debugging

---

## 1. Plain-English Concept Explanation

### Errors Are Normal

Every programmer — beginner and expert alike — encounters error messages constantly. An error does not mean you have failed. It means Python found something it could not execute and is telling you exactly where and why.

The skill is not avoiding errors. The skill is **reading them calmly and extracting the information they contain**.

---

### What is a Traceback?

When Python encounters an error it cannot recover from, it stops running and prints a **traceback** — a structured error report. The word _traceback_ refers to Python tracing back through the chain of function calls that led to the problem.

A traceback always has the same anatomy:

```
Traceback (most recent call last):          ← always the first line
  File "simulation.py", line 47, in step    ← where the error occurred
    dT_hot = -Q_dot * self.dt               ← the actual line of code
NameError: name 'Q_dot' is not defined      ← error type: plain English message
```

Reading a traceback from **bottom to top** is often easier:

1. **Bottom line** — the error type and message. Start here.
2. **Middle lines** — the file name, line number, and code that caused it.
3. **Top** — the chain of calls that led there (most useful in longer programs).

---

### The Five Parts of Any Error Line

```
NameError: name 'Q_dot' is not defined
^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
│          │
│          └─ The message — plain English explanation of what went wrong
└─ The error type — a category name that tells you what kind of problem it is
```

Python has many error types. The five you will encounter most often while building this script each have a distinct cause and a reliable fix.

---

## 2. The Five Most Common Errors

---

### Error 1: `NameError` — Using a Name Python Doesn't Know

**What it means:** You referenced a variable, function, or module that Python has not seen yet. Either it was never defined, it was spelled wrong, or it was not imported.

**Realistic example from our script:**

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    # Imagine you accidentally wrote 'coeff' instead of 'self.h'
    return coeff * (T_h - T_c)
```

```
Traceback (most recent call last):
  File "simulation.py", line 89, in calculate_heat_transfer_rate
    return coeff * (T_h - T_c)
NameError: name 'coeff' is not defined
```

**How to fix it:**

- Check the spelling against where the variable was defined
- Check whether it should be `self.h` (an attribute of the class) rather than a standalone name
- Check whether an `import` statement is missing at the top of the file

```python
# Correct version
def calculate_heat_transfer_rate(self, T_h, T_c):
    return self.h * (T_h - T_c)   # self.h was defined in __init__
```

---

### Error 2: `AttributeError` — Asking an Object for Something It Doesn't Have

**What it means:** You tried to access a method or property on an object that does not have it. This usually means a typo in the attribute name, or using the wrong object entirely.

**Realistic example from our script:**

```python
def update_simulation(self):
    # Imagine typing run_simulation() instead of run_full_simulation()
    self.sim.run_simulation()
```

```
Traceback (most recent call last):
  File "simulation.py", line 203, in update_simulation
    self.sim.run_simulation()
AttributeError: 'IrreversibleHeatTransfer' object has no attribute 'run_simulation'
```

**How to fix it:**

- Read the message carefully — it tells you both the object type and the missing attribute name
- Check the class definition for the correct method name
- Watch for plural vs. singular, underscores vs. no underscores, capitalisation differences

```python
# Correct version — the method is called run_full_simulation
def update_simulation(self):
    self.sim.run_full_simulation()
```

**Another common form** — forgetting `self.` entirely inside a class:

```python
def reset_simulation(self):
    # Missing self. — Python looks for a local variable named 'n_steps'
    T_hot = np.zeros(n_steps)
```

```
NameError: name 'n_steps' is not defined
# (Sometimes surfaces as NameError rather than AttributeError
#  depending on exactly where the missing self. appears)
```

```python
# Correct version
def reset_simulation(self):
    self.T_hot = np.zeros(self.n_steps)   # self.n_steps is the attribute
```

---

### Error 3: `IndentationError` — Misaligned Code Blocks

**What it means:** Python uses indentation (the spaces at the start of a line) to define which lines belong to which block — a function body, a loop, a conditional, a class. If your indentation is inconsistent, Python cannot parse the structure and raises this error before running a single line.

**Realistic example from our script:**

```python
def step(self):
    if self.current_step >= self.n_steps - 1:
        return False
    i = self.current_step
      Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
#   ^ two extra spaces — this line does not align with the line above it
```

```
  File "simulation.py", line 112
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
    ^
IndentationError: unexpected indent
```

**How to fix it:**

- Make sure every line inside a function is indented by exactly the same amount
- The Python convention is **4 spaces** per level of indentation
- Never mix tabs and spaces — they look identical visually but Python treats them differently. Most code editors have a setting to convert tabs to spaces automatically.

```python
# Correct version — all lines at the same level use exactly 4 spaces
def step(self):
    if self.current_step >= self.n_steps - 1:
        return False
    i = self.current_step
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
```

> **Editor tip:** If your code editor shows indentation guides (faint vertical lines), use them. They make misalignment immediately visible.

---

### Error 4: `TypeError` — The Wrong Kind of Value

**What it means:** You passed a value of the wrong _type_ to a function or operation. Python is strict about types in certain situations — for example, you cannot multiply a string by a float, or pass a string where a number is expected.

**Realistic example from our script:**

```python
# Imagine the slider returns its value as a string instead of a number
# (This can happen when reading input from certain external sources)
def on_slider_change(self, val):
    self.sim.T_hot_0 = "400"   # accidentally a string, not a number
    self.sim.T_eq = self.sim._calculate_equilibrium_temp()
```

Inside `_calculate_equilibrium_temp()`:

```python
def _calculate_equilibrium_temp(self):
    numerator = self.m_hot * self.c_p * self.T_hot_0
    # self.T_hot_0 is "400" (a string) — you can't multiply a string by a float
```

```
Traceback (most recent call last):
  File "simulation.py", line 58, in _calculate_equilibrium_temp
    numerator = self.m_hot * self.c_p * self.T_hot_0
TypeError: can't multiply sequence by non-int of type 'float'
```

**How to fix it:**

- Read the message — it describes the incompatible types
- Trace back to where the value was assigned and check its type
- Use `print(type(variable))` to inspect a value's type when unsure

```python
# Correct version — ensure the value is stored as a float
def on_slider_change(self, val):
    self.sim.T_hot_0 = float(val)   # float() converts to a decimal number
```

**Another common form** — passing the wrong number of arguments:

```python
# calculate_entropy_generation_rate expects 3 arguments (plus self)
self.calculate_entropy_generation_rate(Q_dot)   # missing T_h and T_c
```

```
TypeError: calculate_entropy_generation_rate() missing 2 required
positional arguments: 'T_h' and 'T_c'
```

---

### Error 5: `IndexError` — Reaching Outside an Array

**What it means:** You tried to access an element of an array or list using an index number that does not exist. Arrays in Python are **zero-indexed** — a 5-element array has valid indices `0, 1, 2, 3, 4`. Index `5` does not exist and raises this error.

**Realistic example from our script:**

```python
def step(self):
    i = self.current_step

    # Imagine current_step is 2000 but n_steps is 2000
    # Valid indices are 0 through 1999 — index 2000 does not exist
    Q_dot = self.calculate_heat_transfer_rate(
        self.T_hot[i],    # self.T_hot has 2000 slots: indices 0-1999
        self.T_cold[i]    # index 2000 is out of bounds
    )
```

```
Traceback (most recent call last):
  File "simulation.py", line 115, in step
    Q_dot = self.calculate_heat_transfer_rate(self.T_hot[i], self.T_cold[i])
IndexError: index 2000 is out of bounds for axis 0 with size 2000
```

**How to fix it:**

- Check the guard condition at the top of `step()` — it exists specifically to prevent this
- Remember that an array of size `n` has valid indices `0` through `n-1`
- `range(n - 1)` in `run_full_simulation()` stops one step early for exactly this reason

```python
# The guard that prevents this — already in the script
def step(self):
    # Stop before current_step can equal n_steps
    if self.current_step >= self.n_steps - 1:
        return False            # exit safely before touching out-of-bounds memory
    i = self.current_step
    # Now i is guaranteed to be a valid index
```

---

## 3. A Simple Debugging Workflow Using `print()`

When Python does not raise an error but your simulation _behaves wrongly_ — temperatures going negative, entropy decreasing, plots showing flat lines — you need to investigate. The most reliable beginner tool is **strategic `print()` statements**.

### The Four-Step Workflow

```
1. Form a hypothesis — "I think the heat transfer rate is wrong"
2. Add a print() statement at the relevant point to observe the value
3. Run the program and read the output
4. Remove the print() statement once you understand what is happening
```

---

### Step 1: Confirm Your Inputs Are What You Think

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    # Add this line temporarily to inspect incoming values
    print(f"DEBUG: T_h = {T_h:.2f}, T_c = {T_c:.2f}")

    return self.h * (T_h - T_c)
```

Output:

```
DEBUG: T_h = 400.00, T_c = 300.00   ← first call looks right
DEBUG: T_h = 399.50, T_c = 300.50   ← second call, temperatures converging
DEBUG: T_h = -12.30, T_c = 850.20   ← something went wrong by here
```

If the values look wrong at step 3, the bug is upstream — in whatever feeds values to this function.

---

### Step 2: Track State Inside a Loop

```python
def run_full_simulation(self):
    self.reset_simulation()
    for i in range(self.n_steps - 1):

        # Print every 200 steps so the output isn't overwhelming
        if i % 200 == 0:
            print(f"DEBUG step {i}: "
                  f"T_hot={self.T_hot[i]:.1f}, "
                  f"T_cold={self.T_cold[i]:.1f}, "
                  f"S_gen={self.S_gen_cumulative[i]:.4f}")
        self.step()
```

Output:

```
DEBUG step 0:    T_hot=400.0, T_cold=300.0, S_gen=0.0000
DEBUG step 200:  T_hot=364.2, T_cold=335.8, S_gen=12.4300
DEBUG step 400:  T_hot=351.1, T_cold=348.9, S_gen=18.7650
DEBUG step 600:  T_hot=350.1, T_cold=349.9, S_gen=19.2100
```

This tells you the simulation is converging correctly toward equilibrium at 350 K.

---

### Step 3: Check a Value's Type When Behaviour Seems Impossible

```python
def on_slider_change(self, val):
    # val comes from the slider — is it definitely a number?
    print(f"DEBUG: val = {val}, type = {type(val)}")
    self.sim.T_hot_0 = val
```

Output:

```
DEBUG: val = 400.0, type = <class 'float'>   ← good, it is a float
```

or:

```
DEBUG: val = 400.0, type = <class 'numpy.float64'>
```

Both `float` and `numpy.float64` work fine for arithmetic in this script — this just shows you that `print(type(...))` is a fast way to rule out type confusion.

---

### Step 4: Trace Which Branch a Conditional Takes

```python
def calculate_heat_transfer_rate(self, T_h, T_c):
    if self.system_type == "Isolated":
        print("DEBUG: Isolated branch taken — returning 0")
        return 0.0

    print(f"DEBUG: Active branch — h={self.h}, dT={T_h - T_c:.2f}")
    return self.h * (T_h - T_c)
```

This confirms whether the `"Isolated"` radio button is correctly routing execution. If you see the isolated branch firing when you expected active heat transfer, the `system_type` attribute was set incorrectly somewhere.

---

### Cleaning Up

Once the bug is found, remove your debug print statements. A clean way to handle this during development is to prefix them all consistently:

```python
print("DEBUG: ...")    # easy to search for and delete when done
```

Some developers use `# TODO: remove debug` comments to mark temporary lines. Either approach works — the goal is to leave no stray print statements in finished code, since they will appear in the terminal every time the program runs.

---

### Quick Reference: Error → Likely Cause → First Place to Look

|Error|Likely Cause|First Place to Look|
|---|---|---|
|`NameError`|Variable not defined or misspelled|The line the error points to — check spelling and `self.`|
|`AttributeError`|Wrong method or property name|The class definition — check exact method names|
|`IndentationError`|Misaligned spaces or mixed tabs/spaces|The line above the flagged line — check alignment|
|`TypeError`|Wrong value type or wrong number of arguments|Where the value was last assigned|
|`IndexError`|Array access beyond its length|The guard condition — check `n_steps` vs `current_step`|

---

## 4. Practice Exercise

Try this in a new Python file. It should take under 10 minutes.

**The file below contains five bugs — one of each error type from this lesson.** Your task is to read each error message, identify the error type, and fix it.

```python
import numpy as np

# --- Bug 1 ---
T_hot = 400
T_cold = 300
delta_T = T_hot - t_cold        # something is wrong here
print(f"Temperature difference: {delta_T}")

# --- Bug 2 ---
time = np.arange(0, 10, 0.5)
print(f"Number of steps: {time.lenght}")   # something is wrong here

# --- Bug 3 ---
def calculate_rate(h, T_h, T_c):
    rate = h * (T_h - T_c)
      return rate                 # something is wrong here

# --- Bug 4 ---
def add_temperatures(T1, T2):
    return T1 + T2

result = add_temperatures("400", 300)   # something is wrong here
print(result)

# --- Bug 5 ---
temperatures = np.zeros(5)       # array has 5 elements: indices 0-4
print(temperatures[5])           # something is wrong here
```

**What to do:**

1. Run the file
2. Read the traceback for the first error Python reports
3. Identify the error type from the bottom line
4. Fix that line
5. Run again and repeat until all five bugs are resolved

> **Note:** Python stops at the first error it encounters and reports only that one. Fix them one at a time, top to bottom.

---

## 5. Key Takeaways

- A **traceback** is Python's structured error report. Read it from the **bottom up**: the last line gives the error type and message; the lines above give the file name, line number, and code that caused it.
- **`NameError`** means Python does not recognise a name — check spelling, missing `self.`, and missing imports. **`AttributeError`** means an object does not have the method or property you asked for — check the class definition for the correct name.
- **`IndentationError`** is caught before your code runs at all. Use 4 spaces consistently per level and never mix tabs and spaces.
- **`TypeError`** signals a mismatch between what a function expects and what it received — wrong type, or wrong number of arguments. **`IndexError`** means you tried to access an array slot that does not exist — remember arrays are zero-indexed and size `n` means valid indices `0` through `n-1`.
- **`print()` debugging** is a reliable, beginner-friendly workflow: form a hypothesis, add a targeted `print()` to observe the value, run the program, read the output, and remove the `print()` once the bug is understood. Prefix all debug prints with `"DEBUG:"` so they are easy to find and remove.

---

# Lesson 20: How to Extend the Script — Suggested Next Projects

---

## Plain-English Introduction

You have built a working, interactive thermodynamic simulation from scratch. That is a genuinely significant achievement for someone who started with no programming experience.

This final lesson is different from the ones before it. There are no exercises to complete, no key takeaways to memorise. Instead, it is a **roadmap** — three clearly signposted paths you could follow if you want to keep going.

Each extension is described at two levels:

- **The physics:** what new behaviour you would be modelling
- **The Python:** which new concepts you would need to learn, and exactly which parts of the existing code you would need to change

None of these extensions require you to throw away what you have built. Each one grows _out of_ the existing script. That is the payoff of writing clean, well-organised code.

---

## Extension 1 — Add a Third Reservoir

### Difficulty: ⭐☆☆ Beginner–Intermediate

---

### What This Would Do

Currently the simulation models two reservoirs: one hot, one cold. Heat flows between them until they reach equilibrium.

A third reservoir introduces a more realistic scenario. Imagine a **warm intermediate body** sitting between the hot and cold reservoirs — like a metal plate separating two fluids. Heat flows from the hot reservoir into the intermediate body, and simultaneously from the intermediate body into the cold reservoir. The intermediate body's temperature is not fixed — it rises and falls depending on how much heat it is gaining versus losing.

This is closer to how real heat exchangers, building walls, and industrial processes actually work.

Physically, you would observe:

- Three temperature curves converging instead of two
- A new equilibrium temperature determined by the energy balance of all three masses
- A higher total entropy generation than the two-reservoir case, because there are now two irreversible heat transfer processes happening simultaneously

---

### New Python Concepts Required

**No entirely new concepts are needed.** This extension is valuable precisely because it can be built using only what you already know: variables, lists, functions, loops, and Matplotlib. What it will sharpen is your ability to _organise_ existing concepts cleanly when the problem becomes more complex.

You would encounter one new practical skill: **managing related variables in groups**. Right now the script has `T_hot`, `T_cold`, `m_hot`, `m_cold` as separate variables. With three reservoirs, you will feel the pull toward storing them in a list or a dictionary so you can loop over them rather than copying code three times.

```python
# Current approach — works for two, becomes unwieldy for three or more.
self.T_hot  = np.zeros(self.n_steps)
self.T_cold = np.zeros(self.n_steps)

# A more scalable approach for three reservoirs.
# A list of arrays — one array per reservoir.
# You can loop over this regardless of how many reservoirs there are.
self.temperatures = [
    np.zeros(self.n_steps),   # index 0: hot reservoir
    np.zeros(self.n_steps),   # index 1: intermediate reservoir
    np.zeros(self.n_steps),   # index 2: cold reservoir
]
```

---

### Which Existing Methods Would Need to Change

**`__init__()`** Add three new parameters: `T_intermediate_initial`, `mass_intermediate`, and `h_intermediate_to_cold` (the heat transfer coefficient between the intermediate and cold reservoir — it may differ from the hot-to-intermediate coefficient). Initialise the new temperature and entropy arrays.

**`_calculate_equilibrium_temp()`** The two-reservoir formula extends naturally. The numerator gains a third term, and the denominator gains a third capacity term:

```python
# Extended energy balance for three reservoirs.
# The logic is identical — just one more term on each side.
numerator = (self.m_hot   * self.c_p * self.T_hot_0   +
             self.m_mid   * self.c_p * self.T_mid_0   +
             self.m_cold  * self.c_p * self.T_cold_0)

denominator = (self.m_hot + self.m_mid + self.m_cold) * self.c_p

return numerator / denominator
```

**`calculate_heat_transfer_rate()`** This method currently calculates one heat flow rate. You would call it _twice_ per timestep: once for the hot-to-intermediate boundary, and once for the intermediate-to-cold boundary. The method signature itself does not need to change — you just call it with different temperature pairs.

**`step()`** This is where the most careful thinking is required. The intermediate reservoir receives heat from the hot side _and_ loses heat to the cold side simultaneously. Its temperature change per timestep must account for both flows:

```python
# Two separate heat flow rates, calculated at the same instant.
Q_dot_hot_to_mid  = self.calculate_heat_transfer_rate(T_hot, T_mid)
Q_dot_mid_to_cold = self.calculate_heat_transfer_rate(T_mid, T_cold)

# The intermediate reservoir's temperature changes due to BOTH flows.
# It gains energy from the hot side and loses energy to the cold side.
# The net change is the difference between what comes in and goes out.
dT_mid = ((Q_dot_hot_to_mid - Q_dot_mid_to_cold) * self.dt
          / (self.m_mid * self.c_p))
```

**`plot_temperature()`** Add a third `ax.plot()` call in a new colour (orange is a natural choice for an intermediate reservoir) and update the legend.

**`setup_sliders()`** Add two new sliders: one for `T_intermediate` and one for `mass_intermediate`.

---

## Extension 2 — Real-Time Carnot Efficiency Display

### Difficulty: ⭐⭐☆ Intermediate

---

### What This Would Do

Right now the simulation shows _what happens_ during irreversible heat transfer. This extension would show _how wasteful_ each moment of that process is, by comparing it against the theoretical best-case scenario.

**Carnot efficiency** is the maximum possible efficiency of any heat engine operating between a hot reservoir at temperature T_hot and a cold reservoir at temperature T_cold. It is a theoretical ceiling — no real device can exceed it, and most fall well short. The formula is:

```
η_Carnot = 1 − (T_cold / T_hot)
```

**Actual efficiency** in our simulation is not straightforward to define in the same terms, because our model is not a heat engine — it is pure heat transfer with no work being extracted. The meaningful comparison is instead between the entropy generated in our irreversible process versus zero (the entropy that _would_ be generated in a perfectly reversible process between the same two temperatures).

A practical metric the simulation could display is the **Second Law efficiency**, sometimes called the **exergy efficiency**. [Inference — the exact formulation of Second Law efficiency varies by textbook and context; the version below is one common approach]:

```
η_II = 1 − (S_gen_actual / S_gen_maximum_possible)
```

Where S_gen_maximum_possible is the entropy that would be generated if all the available work potential (exergy) were destroyed — i.e., if you simply mixed the two reservoirs with no attempt at doing useful work. An η_II of 1.0 means perfectly reversible (no waste). An η_II of 0.0 means all work potential was destroyed.

Displaying both metrics in real time — updating as the animation plays — would give the student a live readout of how far the current state is from the thermodynamic ideal.

---

### New Python Concepts Required

**Matplotlib `Text` objects and `ax.text()` updating**

You already know how to draw lines on an Axes. Displaying a number that updates every animation frame requires a slightly different approach. Rather than clearing and redrawing the entire Axes, you can create a `Text` object once and update its content each frame:

```python
# Create the text object once, during setup.
# The text starts as an empty string — it will be filled in during animation.
self.efficiency_text = self.ax_efficiency.text(
    0.05, 0.90,          # x, y position in Axes coordinates (0 to 1)
    '',                  # starting content — empty
    transform=self.ax_efficiency.transAxes,  # position relative to Axes, not data
    fontsize=13,
    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
)

# Later, inside plot_all() or animate(), update the content:
carnot = 1 - (T_cold / T_hot)
self.efficiency_text.set_text(f'Carnot efficiency: {carnot:.1%}')
# The :.1% format converts 0.654 to "65.4%" automatically.
```

**f-strings with format specifiers**

You have used f-strings for basic variable insertion. This extension would introduce format specifiers — the part after the colon inside the curly braces — to control how numbers are displayed:

```python
value = 0.7348

# :.1%  → displays as a percentage with 1 decimal place
print(f'{value:.1%}')    # Output: 73.5%

# :.3f  → displays as a float with 3 decimal places
print(f'{value:.3f}')    # Output: 0.735

# :.2e  → displays in scientific notation
print(f'{value:.2e}')    # Output: 7.35e-01
```

**A new sixth Axes panel**

The current layout uses a 3×3 grid with five panels. Adding a sixth panel for the efficiency display would require revisiting `setup_figure()` and adjusting the `gridspec` layout — good practice in Matplotlib layout management.

---

### Which Existing Methods Would Need to Change

**`IrreversibleHeatTransfer.__init__()`** Add a new array to store the Carnot efficiency at each timestep:

```python
# Store Carnot efficiency at each timestep for plotting.
self.carnot_efficiency = np.zeros(self.n_steps)
```

**`step()`** Calculate and store the Carnot efficiency at each step. Add these lines after the temperature update:

```python
# Carnot efficiency at the current temperatures.
# Guard against division by zero if T_hot ever equals T_cold.
if self.T_hot[i] > self.T_cold[i]:
    self.carnot_efficiency[i] = 1 - (self.T_cold[i] / self.T_hot[i])
else:
    self.carnot_efficiency[i] = 0.0
```

**`setup_figure()` in `InteractiveVisualizer`** Adjust the `gridspec` call to accommodate a sixth Axes panel, and create `self.ax_efficiency` to hold it.

**`plot_all()`** Add a call to a new method `plot_efficiency()` so it updates alongside the other charts.

**New method: `plot_efficiency()`** Write this new method following the exact same clear → plot → label → style pattern you already know from `plot_temperature()` and the others:

```python
def plot_efficiency(self):
    self.ax_efficiency.clear()
    idx = min(self.sim.current_step, self.sim.n_steps - 1)

    # Plot Carnot efficiency over time.
    # It starts high (large temperature gap = high potential)
    # and falls toward zero as temperatures converge.
    self.ax_efficiency.plot(
        self.sim.time[:idx+1],
        self.sim.carnot_efficiency[:idx+1],
        color='teal', linewidth=2, label='Carnot Efficiency'
    )

    # Display the current value as on-chart text.
    current = self.sim.carnot_efficiency[idx]
    self.ax_efficiency.text(
        0.97, 0.95, f'Now: {current:.1%}',
        transform=self.ax_efficiency.transAxes,
        ha='right', va='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
    )

    self.ax_efficiency.set_xlabel('Time (s)', fontsize=11)
    self.ax_efficiency.set_ylabel('Efficiency', fontsize=11)
    self.ax_efficiency.set_title('Carnot Efficiency Over Time', fontsize=12)
    self.ax_efficiency.set_ylim(0, 1)   # Efficiency is always between 0 and 1.
    self.ax_efficiency.grid(True, alpha=0.3)
    self.ax_efficiency.legend(loc='best')
```

---

## Extension 3 — A True Open System with Mass Flow

### Difficulty: ⭐⭐⭐ Advanced

---

### What This Would Do

Currently the radio button offers three system types — Closed, Open, and Isolated — but the Open option is noted in the code itself as unimplemented: _"for now, treat as closed, can extend."_ This extension makes Open mean something real.

In thermodynamics, an **open system** is one where both energy _and_ mass can cross the boundary. A practical example: a hot fluid flowing through a pipe into a cold tank. As the hot fluid enters, it carries thermal energy with it (called **enthalpy**). The cold fluid leaving carries energy out. The temperature of the tank changes not just because of heat conduction, but because of the composition of fluid inside it changing over time.

Modelling this requires introducing **mass flow rate** (how many kg/s of fluid enter and leave) and **enthalpy** (the energy carried by a moving fluid, which includes both its internal thermal energy and the work done pushing it through the boundary).

The governing equation for an open system energy balance becomes:

```
dU/dt = Q̇ − Ẇ + ṁ_in × h_in − ṁ_out × h_out
```

|Symbol|Meaning|
|---|---|
|`dU/dt`|Rate of change of internal energy inside the system|
|`Q̇`|Heat transfer rate (same as before)|
|`Ẇ`|Work rate (shaft work — can be set to zero if no pump/turbine)|
|`ṁ_in`|Mass flow rate entering (kg/s)|
|`h_in`|Specific enthalpy of the incoming fluid (J/kg)|
|`ṁ_out`|Mass flow rate leaving (kg/s)|
|`h_out`|Specific enthalpy of the outgoing fluid (J/kg)|

For a simplified model, you can assume `ṁ_in = ṁ_out` (steady mass — the system does not fill up or drain) and `Ẇ = 0` (no mechanical work), which makes the equation tractable for the existing structure of the script.

This extension is rated advanced not because any single new concept is dramatically harder, but because it requires you to hold more interacting ideas in mind simultaneously and to restructure parts of the simulation more substantially than the previous two extensions.

---

### New Python Concepts Required

**Class inheritance (optional but natural here)**

The cleanest way to implement this is to create a new class `OpenSystemHeatTransfer` that _inherits_ from `IrreversibleHeatTransfer`. Inheritance means the new class automatically has all the methods and attributes of the original, and you only write code for the parts that change. This avoids duplicating the closed-system logic:

```python
# OpenSystemHeatTransfer inherits everything from IrreversibleHeatTransfer.
# The "(IrreversibleHeatTransfer)" tells Python about the parent class.
class OpenSystemHeatTransfer(IrreversibleHeatTransfer):

    def __init__(self, mass_flow_rate=0.5, h_in=None, **kwargs):
        # super().__init__() calls the parent class's __init__ first,
        # setting up all the existing attributes.
        super().__init__(**kwargs)

        # Then we add the new attributes specific to open systems.
        self.mass_flow_rate = mass_flow_rate  # kg/s
        self.h_in = h_in if h_in is not None else self.c_p * self.T_hot_0

    # Override only the step() method — everything else is inherited.
    def step(self):
        # New open-system step logic here.
        pass
```

**`**kwargs` — passing keyword arguments flexibly**

The `**kwargs` pattern (the double asterisk is part of the syntax) allows a function to accept any number of keyword arguments and pass them along to another function. It is used above so that `OpenSystemHeatTransfer` can accept all the same setup arguments as `IrreversibleHeatTransfer` without listing them all again:

```python
# Without **kwargs, you would need to repeat every parameter.
# With **kwargs, any keyword argument not explicitly listed
# is bundled into a dictionary and forwarded automatically.

def __init__(self, mass_flow_rate=0.5, **kwargs):
    super().__init__(**kwargs)  # forwards T_hot_initial, mass_hot, etc.
```

**Array resizing or a new tracked variable for system mass**

In a true open system, if inflow and outflow rates differ, the mass inside the system changes over time. Tracking this requires a new array alongside the temperature and entropy arrays:

```python
# Track the total mass inside the cold reservoir at each timestep.
self.mass_cold_over_time = np.zeros(self.n_steps)
self.mass_cold_over_time[0] = self.m_cold
```

---

### Which Existing Methods Would Need to Change

**`__init__()`** Add `mass_flow_rate`, `T_inlet` (the temperature of the incoming fluid), and arrays to store mass and enthalpy flow over time. The slider setup would need two new sliders: one for mass flow rate and one for inlet temperature.

**`step()` — the most significant rewrite**

The closed-system `step()` updates temperature using:

```python
dT_cold = Q_dot * dt / (m_cold * c_p)
```

The open-system version must also account for the enthalpy carried in by the incoming mass:

```python
# Enthalpy flow rate into the cold reservoir (W = J/s).
# The incoming fluid carries energy proportional to its temperature.
H_dot_in  = self.mass_flow_rate * self.c_p * self.T_inlet

# Enthalpy flow rate out (fluid leaves at the current cold reservoir temperature).
H_dot_out = self.mass_flow_rate * self.c_p * self.T_cold[i]

# Net enthalpy contribution this timestep.
delta_H = (H_dot_in - H_dot_out) * self.dt

# Updated temperature change: now includes both conduction (Q_dot)
# and the enthalpy carried by the flowing mass.
# Note: if mass_flow_rate is zero, delta_H = 0 and this reduces
# exactly to the closed system equation — a good way to test your work.
dT_cold = (Q_dot * self.dt + delta_H) / (self.m_cold * self.c_p)
```

**`calculate_entropy_generation_rate()`** Open system entropy generation includes an additional term for the irreversibility of mixing fluids at different temperatures. [Inference — the exact form depends on modelling assumptions; verifying against a thermodynamics textbook such as Çengel & Boles is recommended before implementing.]

**`setup_sliders()` in `InteractiveVisualizer`** Add two new sliders — mass flow rate and inlet temperature — that only become active when the Open system radio button is selected. You would use the slider's `ax.set_visible()` method to show and hide them depending on the selected system type.

**`on_system_type_change()`** Currently this method just swaps `self.sim.system_type`. With a true open system model, it would need to swap the simulation object itself — replacing an `IrreversibleHeatTransfer` instance with an `OpenSystemHeatTransfer` instance (if you used the inheritance approach) — then re-run the simulation and redraw all plots.

---

## A Final Note

These three extensions form a natural progression:

```
Extension 1 — Add a Third Reservoir
  More of the same concepts, applied to a more complex physical setup.
  Best first step. Confirms you truly understand the existing code.

Extension 2 — Carnot Efficiency Display
  Introduces new Matplotlib skills (live text, layout adjustment)
  and a new physical quantity, with minimal structural change to the model.

Extension 3 — True Open System
  Requires restructuring the class hierarchy, new physics, new sliders,
  and careful management of interacting state. A genuine intermediate
  Python project.
```

Each one will teach you something the lessons in this course could not — because the best way to consolidate programming knowledge is to encounter a problem you have not seen before and work through it. The script you have built is a solid foundation. Where you take it from here is entirely up to you.
