# PIE Examples and Tutorials

Practical examples and sample programs to help you learn PIE programming.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Programs](#basic-programs)
3. [Working with Variables](#working-with-variables)
4. [Control Flow Examples](#control-flow-examples)
5. [Functions and Recursion](#functions-and-recursion)
6. [Array Examples](#array-examples)
7. [String Processing](#string-processing)
8. [Dictionary Examples](#dictionary-examples)
9. [File I/O Examples](#file-io-examples)
10. [Complete Programs](#complete-programs)

---

## Getting Started

### Hello World

The simplest PIE program:

```pie
output("Hello, World!", string);
```

**Compile and run:**
```bash
python3 src/main.py hello.pie
./program
```

**Output:**
```
Hello, World!
```

---

### Basic Input and Output

Reading user input and displaying results:

```pie
// Get user's name
string name;
output("Enter your name: ", string);
input(name, string);

// Greet the user
output("Hello, " + name + "!", string);
```

---

## Basic Programs

### Calculator

A simple calculator program:

```pie
int a, b;
output("Enter first number: ", string);
input(a, int);

output("Enter second number: ", string);
input(b, int);

int sum = a + b;
int difference = a - b;
int product = a * b;
int quotient = a / b;

output("Sum: ", string);
output(sum, int);

output("Difference: ", string);
output(difference, int);

output("Product: ", string);
output(product, int);

output("Quotient: ", string);
output(quotient, int);
```

---

### Temperature Converter

Convert between Celsius and Fahrenheit:

```pie
float celsius;
output("Enter temperature in Celsius: ", string);
input(celsius, float);

float fahrenheit = (celsius * 9.0 / 5.0) + 32.0;

output("Temperature in Fahrenheit: ", string);
output(fahrenheit, float, 2);
```

**Example Run:**
```
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.00
```

---

### Area Calculator

Calculate areas of different shapes:

```pie
float radius, width, height;

// Circle area
output("Enter circle radius: ", string);
input(radius, float);
float circleArea = 3.14159 * radius * radius;
output("Circle area: ", string);
output(circleArea, float, 2);

// Rectangle area
output("Enter rectangle width: ", string);
input(width, float);
output("Enter rectangle height: ", string);
input(height, float);
float rectArea = width * height;
output("Rectangle area: ", string);
output(rectArea, float, 2);
```

---

## Working with Variables

### Variable Scope Example

```pie
int global = 100;

int testScope() {
    int local = 50;
    output("Global in function: ", string);
    output(global, int);
    output("Local in function: ", string);
    output(local, int);
    return local + global;
}

int main() {
    output("Global in main: ", string);
    output(global, int);
    
    int result = testScope();
    output("Function returned: ", string);
    output(result, int);
    
    return 0;
}
```

---

### Constants and Calculations

```pie
// Mathematical constants
float PI = 3.14159265;
float E = 2.71828183;

// Calculate circle properties
float radius = 5.0;
float circumference = 2.0 * PI * radius;
float area = PI * radius * radius;

output("Radius: ", string);
output(radius, float, 2);
output("Circumference: ", string);
output(circumference, float, 2);
output("Area: ", string);
output(area, float, 2);
```

---

## Control Flow Examples

### Grade Calculator

```pie
float score;
output("Enter your score (0-100): ", string);
input(score, float);

if (score >= 90.0) {
    output("Grade: A", string);
} else if (score >= 80.0) {
    output("Grade: B", string);
} else if (score >= 70.0) {
    output("Grade: C", string);
} else if (score >= 60.0) {
    output("Grade: D", string);
} else {
    output("Grade: F", string);
}
```

---

### Number Guessing Game

```pie
// Seed random number generator
srand(time_now());

// Generate random number between 1 and 100
int target = rand_range(1, 100);
int guess = 0;
int attempts = 0;

output("Guess the number (1-100)!", string);

while (guess != target) {
    output("Enter your guess: ", string);
    input(guess, int);
    attempts++;
    
    if (guess < target) {
        output("Too low!", string);
    } else if (guess > target) {
        output("Too high!", string);
    } else {
        output("Correct!", string);
        output("Attempts: ", string);
        output(attempts, int);
    }
}
```

---

### Multiplication Table

```pie
int number;
output("Enter a number: ", string);
input(number, int);

output("Multiplication table:", string);
for (int i = 1; i <= 10; i++) {
    int result = number * i;
    output(number, int);
    output(" x ", string);
    output(i, int);
    output(" = ", string);
    output(result, int);
}
```

---

### Countdown Timer

```pie
int seconds;
output("Enter countdown seconds: ", string);
input(seconds, int);

output("Starting countdown...", string);
for (int i = seconds; i > 0; i--) {
    output(i, int);
    sleep(1000);  // Wait 1 second
}
output("Time's up!", string);
```

---

## Functions and Recursion

### Factorial Function

```pie
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int num;
    output("Enter a number: ", string);
    input(num, int);
    
    int result = factorial(num);
    output("Factorial: ", string);
    output(result, int);
    
    return 0;
}
```

---

### Fibonacci Sequence

```pie
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    output("First 10 Fibonacci numbers:", string);
    for (int i = 0; i < 10; i++) {
        int fib = fibonacci(i);
        output(fib, int);
    }
    return 0;
}
```

**Output:**
```
First 10 Fibonacci numbers:
0
1
1
2
3
5
8
13
21
34
```

---

### Prime Number Checker

```pie
int isPrime(int n) {
    if (n <= 1) {
        return 0;
    }
    if (n == 2) {
        return 1;
    }
    if (n % 2 == 0) {
        return 0;
    }
    
    for (int i = 3; i * i <= n; i = i + 2) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int num;
    output("Enter a number: ", string);
    input(num, int);
    
    if (isPrime(num) == 1) {
        output("Prime", string);
    } else {
        output("Not prime", string);
    }
    
    return 0;
}
```

---

### GCD (Greatest Common Divisor)

```pie
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    int x = 48;
    int y = 18;
    
    int result = gcd(x, y);
    output("GCD of ", string);
    output(x, int);
    output(" and ", string);
    output(y, int);
    output(" is ", string);
    output(result, int);
    
    return 0;
}
```

---

## Array Examples

### Working with Arrays

```pie
// Create and populate an array
int[] numbers = [10, 20, 30, 40, 50];

// Print all elements
output("Array elements:", string);
for (int i = 0; i < arr_size(numbers); i++) {
    output(numbers[i], int);
}

// Calculate sum
int sum = 0;
for (int i = 0; i < arr_size(numbers); i++) {
    sum = sum + numbers[i];
}
output("Sum: ", string);
output(sum, int);

// Calculate average
float avg = arr_avg(numbers);
output("Average: ", string);
output(avg, float, 2);
```

---

### Finding Maximum and Minimum

```pie
int[] numbers = [45, 12, 78, 23, 91, 34, 67];

// Find maximum
int max = numbers[0];
for (int i = 1; i < arr_size(numbers); i++) {
    if (numbers[i] > max) {
        max = numbers[i];
    }
}
output("Maximum: ", string);
output(max, int);

// Find minimum
int min = numbers[0];
for (int i = 1; i < arr_size(numbers); i++) {
    if (numbers[i] < min) {
        min = numbers[i];
    }
}
output("Minimum: ", string);
output(min, int);
```

---

### Dynamic Array Operations

```pie
// Create empty dynamic array
int[] scores = [];

// Add scores
arr_push(scores, 85);
arr_push(scores, 92);
arr_push(scores, 78);
arr_push(scores, 95);
arr_push(scores, 88);

output("Number of scores: ", string);
output(arr_size(scores), int);

// Check if specific score exists
int searchScore = 92;
if (arr_contains(scores, searchScore) == 1) {
    int index = arr_indexof(scores, searchScore);
    output("Score found at index: ", string);
    output(index, int);
}

// Calculate average
float average = arr_avg(scores);
output("Average score: ", string);
output(average, float, 2);
```

---

### Reversing an Array

```pie
int[] numbers = [1, 2, 3, 4, 5];
int size = arr_size(numbers);

output("Original array:", string);
for (int i = 0; i < size; i++) {
    output(numbers[i], int);
}

// Reverse using swap
for (int i = 0; i < size / 2; i++) {
    int temp = numbers[i];
    numbers[i] = numbers[size - 1 - i];
    numbers[size - 1 - i] = temp;
}

output("Reversed array:", string);
for (int i = 0; i < size; i++) {
    output(numbers[i], int);
}
```

---

## String Processing

### String Manipulation

```pie
string text = "  Hello, World!  ";

// Trim whitespace
string trimmed = string_trim(text);
output("Trimmed: ", string);
output(trimmed, string);

// Convert to uppercase
string upper = string_to_upper(trimmed);
output("Uppercase: ", string);
output(upper, string);

// Convert to lowercase
string lower = string_to_lower(trimmed);
output("Lowercase: ", string);
output(lower, string);

// Reverse string
string reversed = string_reverse(trimmed);
output("Reversed: ", string);
output(reversed, string);
```

---

### Word Counter

```pie
string sentence = "The quick brown fox jumps over the lazy dog";
int spaces = string_count_char(sentence, ' ');
int wordCount = spaces + 1;

output("Sentence: ", string);
output(sentence, string);
output("Word count: ", string);
output(wordCount, int);

// Character statistics
int letterA = string_count_char(sentence, 'a');
int letterE = string_count_char(sentence, 'e');
int letterO = string_count_char(sentence, 'o');

output("Letter 'a' count: ", string);
output(letterA, int);
output("Letter 'e' count: ", string);
output(letterE, int);
output("Letter 'o' count: ", string);
output(letterO, int);
```

---

### Password Validator

```pie
string password;
output("Enter a password: ", string);
input(password, string);

int length = strlen(password);
bool isValid = true;

// Check minimum length
if (length < 8) {
    output("Password must be at least 8 characters", string);
    isValid = false;
}

// Check for uppercase
if (string_to_upper(password) == password) {
    output("Password must contain lowercase letters", string);
    isValid = false;
}

// Check for lowercase
if (string_to_lower(password) == password) {
    output("Password must contain uppercase letters", string);
    isValid = false;
}

if (isValid == true) {
    output("Password is valid!", string);
}
```

---

### String Search and Replace

```pie
string text = "The quick brown fox";
string search = "quick";
string replace = "slow";

// Check if substring exists
if (string_contains(text, search) == 1) {
    int index = string_index_of(text, search);
    output("Found '", string);
    output(search, string);
    output("' at index ", string);
    output(index, int);
}

// Replace spaces with underscores
string filename = "my document file.txt";
string safeName = string_replace_char(filename, ' ', '_');
output("Safe filename: ", string);
output(safeName, string);
```

---

## Dictionary Examples

### Student Record System

```pie
// Create student records
dict student1 = {
    "name": "Alice Johnson",
    "id": 12345,
    "gpa": 3.8,
    "major": "Computer Science"
};

dict student2 = {
    "name": "Bob Smith",
    "id": 12346,
    "gpa": 3.5,
    "major": "Mathematics"
};

// Display student info
string name1 = dict_get(student1, "name");
int id1 = dict_get(student1, "id");
float gpa1 = dict_get(student1, "gpa");
string major1 = dict_get(student1, "major");

output("Student Information:", string);
output("Name: " + name1, string);
output("ID: ", string);
output(id1, int);
output("GPA: ", string);
output(gpa1, float, 2);
output("Major: " + major1, string);
```

---

### Configuration Management

```pie
// Application configuration
dict config = {
    "app_name": "PIE App",
    "version": 1,
    "debug": 1,
    "max_users": 100,
    "timeout": 30.5
};

// Read configuration
string appName = dict_get(config, "app_name");
int version = dict_get(config, "version");
int debugMode = dict_get(config, "debug");

output("Application: " + appName, string);
output("Version: ", string);
output(version, int);

if (debugMode == 1) {
    output("Debug mode: ON", string);
} else {
    output("Debug mode: OFF", string);
}

// Update configuration
dict_set(config, "version", 2);
dict_set(config, "debug", 0);
```

---

### Shopping Cart

```pie
dict cart = {};

// Add items (using quantity as value)
dict_set(cart, "apple", 5);
dict_set(cart, "banana", 3);
dict_set(cart, "orange", 7);

// Display cart
output("Shopping Cart:", string);

int apples = dict_get(cart, "apple");
output("Apples: ", string);
output(apples, int);

int bananas = dict_get(cart, "banana");
output("Bananas: ", string);
output(bananas, int);

int oranges = dict_get(cart, "orange");
output("Oranges: ", string);
output(oranges, int);

// Calculate total items
int total = apples + bananas + oranges;
output("Total items: ", string);
output(total, int);
```

---

## File I/O Examples

### Writing to a File

```pie
// Create and write to file
file f = file_open("output.txt", "w");
file_write(f, "Hello, File I/O!");
file_write(f, "This is the second line.");
file_write(f, "PIE language is awesome!");
file_close(f);

output("File written successfully!", string);
```

---

### Reading from a File

```pie
// Read entire file
file f = file_open("output.txt", "r");
string content = file_read_all(f);
file_close(f);

output("File contents:", string);
output(content, string);
```

---

### Log File Example

```pie
// Append to log file
file log = file_open("app.log", "a");

// Get current time
int timestamp = time_now();
string timeStr = time_to_local(timestamp);

// Write log entry
file_write(log, "[" + timeStr + "] Application started");
file_flush(log);

// Simulate some work
sleep(1000);

// Write another entry
int timestamp2 = time_now();
string timeStr2 = time_to_local(timestamp2);
file_write(log, "[" + timeStr2 + "] Processing complete");

file_close(log);
output("Log file updated", string);
```

---

## Complete Programs

### Student Grade Manager

```pie
// Arrays to store student data
string[] names = ["Alice", "Bob", "Charlie", "Diana", "Eve"];
float[] grades = [95.5, 87.3, 91.2, 78.9, 88.5];

int studentCount = arr_size(names);

// Display all students
output("=== Student Grades ===", string);
for (int i = 0; i < studentCount; i++) {
    output(names[i], string);
    output(": ", string);
    output(grades[i], float, 1);
}

// Calculate class average
float classAvg = arr_avg(grades);
output("\nClass Average: ", string);
output(classAvg, float, 2);

// Find highest grade
float highest = grades[0];
string topStudent = names[0];
for (int i = 1; i < studentCount; i++) {
    if (grades[i] > highest) {
        highest = grades[i];
        topStudent = names[i];
    }
}

output("Top Student: " + topStudent, string);
output("Grade: ", string);
output(highest, float, 1);

// Count students above average
int aboveAverage = 0;
for (int i = 0; i < studentCount; i++) {
    if (grades[i] > classAvg) {
        aboveAverage++;
    }
}
output("Students above average: ", string);
output(aboveAverage, int);
```

---

### Simple Banking System

```pie
// Account balance
float balance = 1000.0;

int running = 1;
while (running == 1) {
    output("\n=== Banking Menu ===", string);
    output("1. Check Balance", string);
    output("2. Deposit", string);
    output("3. Withdraw", string);
    output("4. Exit", string);
    output("Choose option: ", string);
    
    int choice;
    input(choice, int);
    
    if (choice == 1) {
        output("Current Balance: $", string);
        output(balance, float, 2);
    } else if (choice == 2) {
        float amount;
        output("Enter deposit amount: $", string);
        input(amount, float);
        balance = balance + amount;
        output("Deposited: $", string);
        output(amount, float, 2);
        output("New Balance: $", string);
        output(balance, float, 2);
    } else if (choice == 3) {
        float amount;
        output("Enter withdrawal amount: $", string);
        input(amount, float);
        if (amount > balance) {
            output("Insufficient funds!", string);
        } else {
            balance = balance - amount;
            output("Withdrawn: $", string);
            output(amount, float, 2);
            output("New Balance: $", string);
            output(balance, float, 2);
        }
    } else if (choice == 4) {
        output("Thank you for banking with us!", string);
        running = 0;
    } else {
        output("Invalid option!", string);
    }
}
```

---

### Text Statistics Analyzer

```pie
string text;
output("Enter a sentence: ", string);
input(text, string);

// Basic statistics
int length = strlen(text);
int words = string_count_char(text, ' ') + 1;

output("\n=== Text Statistics ===", string);
output("Characters: ", string);
output(length, int);
output("Words: ", string);
output(words, int);

// Count vowels
int vowels = 0;
vowels = vowels + string_count_char(text, 'a');
vowels = vowels + string_count_char(text, 'e');
vowels = vowels + string_count_char(text, 'i');
vowels = vowels + string_count_char(text, 'o');
vowels = vowels + string_count_char(text, 'u');
vowels = vowels + string_count_char(text, 'A');
vowels = vowels + string_count_char(text, 'E');
vowels = vowels + string_count_char(text, 'I');
vowels = vowels + string_count_char(text, 'O');
vowels = vowels + string_count_char(text, 'U');

output("Vowels: ", string);
output(vowels, int);

// Display transformations
output("\nUppercase: ", string);
output(string_to_upper(text), string);
output("Lowercase: ", string);
output(string_to_lower(text), string);
output("Reversed: ", string);
output(string_reverse(text), string);
```

---

### Contact Manager

```pie
// Store contacts using dictionaries
dict contact1 = {
    "name": "John Doe",
    "phone": "555-1234",
    "email": "john@example.com"
};

dict contact2 = {
    "name": "Jane Smith",
    "phone": "555-5678",
    "email": "jane@example.com"
};

// Display contacts
output("=== Contact List ===", string);

string name1 = dict_get(contact1, "name");
string phone1 = dict_get(contact1, "phone");
string email1 = dict_get(contact1, "email");

output("\nContact 1:", string);
output("Name: " + name1, string);
output("Phone: " + phone1, string);
output("Email: " + email1, string);

string name2 = dict_get(contact2, "name");
string phone2 = dict_get(contact2, "phone");
string email2 = dict_get(contact2, "email");

output("\nContact 2:", string);
output("Name: " + name2, string);
output("Phone: " + phone2, string);
output("Email: " + email2, string);

// Search for contact
string search;
output("\nEnter name to search: ", string);
input(search, string);

if (string_contains(name1, search) == 1) {
    output("Found: " + name1, string);
    output("Phone: " + phone1, string);
} else if (string_contains(name2, search) == 1) {
    output("Found: " + name2, string);
    output("Phone: " + phone2, string);
} else {
    output("Contact not found", string);
}
```

---

## Tips for Writing PIE Programs

1. **Always initialize variables before use**
   ```pie
   int count = 0;  // Good
   int value;      // Avoid unless you assign before use
   ```

2. **Use meaningful variable names**
   ```pie
   int studentCount;  // Good
   int sc;           // Avoid
   ```

3. **Comment your code**
   ```pie
   // Calculate average grade
   float avg = arr_avg(grades);
   ```

4. **Check array bounds**
   ```pie
   int size = arr_size(numbers);
   for (int i = 0; i < size; i++) {
       // Safe array access
   }
   ```

5. **Close files after use**
   ```pie
   file f = file_open("data.txt", "r");
   string content = file_read_all(f);
   file_close(f);  // Always close
   ```

6. **Use appropriate precision for floats**
   ```pie
   output(price, float, 2);  // Display money with 2 decimals
   ```

---

## See Also

- [Language Reference](language-reference.md) - Complete syntax guide
- [Standard Library](standard-library.md) - All built-in functions
- [Advanced Features](advanced-features.md) - In-depth feature guides
