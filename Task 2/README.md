# Task 2 – Binary Heap and Heap Sort
This repository contains the Python code of Min-Heap, Max-Heap, Priority Queue and Heap Sort.
The chosen data structure is the Binary Heap and the chosen algorithm is Heap Sort.

Below is a **User Guide** for running the **OOP versions** of:

- **Min‑Heap**
- **Max‑Heap**
- **Priority Queue (Max‑Heap)**
- **Heap Sort**

---

# **User Guide: Running the Heap Data Structure & Algorithm Programs**

This project contains four Python programs demonstrating the implementation and usage of:

- **Min‑Heap (OOP)**
- **Max‑Heap (OOP)**
- **Priority Queue using Max‑Heap (OOP)**
- **Heap Sort using Max‑Heap (OOP)**

Each program is structured using **multiple Python files** (modules) and follows the design principles taught in COMP8090SEF.

---

# **1. Prerequisites**

Before running any program, ensure that:

- You have **Python 3.8+** installed  
- All files for each program are placed in the **same folder**  
- You run the program using the **main.py** file in each module

To check your Python version:

```
python --version
```

or

```
python3 --version
```

---

# **2. Project Structure**

Each program follows a similar multi‑file structure:

```
program_name/
│
├── max_heap.py         # or min_heap.py depending on program
├── priority_queue.py   # only for PQ program
├── heap_sort.py        # only for heap sort program
├── app.py              # user interface
└── main.py             # entry point
```

You should always run:

```
python main.py
```

---

# **3. Running the Min‑Heap Program**

### **Folder Structure**
```
min_heap/
│
├── min_heap.py
├── min_heap_app.py
└── min_heap_main.py
```

### **Run the program**
```
python min_heap_main.py
```

### **What the program does**
- Prompts the user to enter a list of integers  
- Builds a **Min‑Heap**  
- Displays the internal heap array  
- Extracts the minimum element  
- Shows the heap after extraction  

### **Example Input**
```
12 3 25 7 18 2
```

---

# **4. Running the Max‑Heap Program**

### **Folder Structure**
```
max_heap/
│
├── max_heap.py
├── max_heap_app.py
└── max_heap_main.py
```

### **Run the program**
```
python max_heap_main.py
```

### **What the program does**
- Prompts the user for integers  
- Builds a **Max‑Heap**  
- Displays the heap  
- Extracts the maximum element  
- Shows the heap after extraction  

### **Example Input**
```
12 3 25 7 18 2
```

---

# **5. Running the Priority Queue (Max‑Heap) Program**

### **Folder Structure**
```
priority_queue/
│
├── max_heap.py
├── priority_queue.py
├── priority_queue_app.py
└── priority_queue_main.py
```

### **Run the program**
```
python priority_queue_main.py
```

### **What the program does**
- Accepts user input values  
- Inserts them into a **Priority Queue implemented using a Max‑Heap**  
- Displays:
  - The internal heap array  
  - The maximum element  
  - The result of extracting the maximum  

### **Example Input**
```
10 4 15 7 20 3
```

---

# **6. Running the Heap Sort Program**

### **Folder Structure**
```
heapsort/
│
├── max_heap.py
├── heap_sort.py
├── heap_sort_app.py
└── heap_sort_main.py
```

### **Run the program**
```
python main.py
```

### **What the program does**
- Prompts the user for a list of integers  
- Builds a Max‑Heap  
- Performs **Heap Sort**  
- Outputs the sorted array in ascending order  

### **Example Input**
```
12 3 25 7 18 2
```

---

# **7. Expected Output Examples**

### **Heap Sort Example**
```
Original array: [12, 3, 25, 7, 18, 2]
Sorted array:   [2, 3, 7, 12, 18, 25]
```

### **Priority Queue Example**
```
Internal heap array: [20, 15, 10, 7, 4, 3]
Maximum element: 20
Extracted: 20
Heap after extraction: [15, 7, 10, 3, 4]
```

---

# **8. Troubleshooting**

### **“ModuleNotFoundError: No module named 'maxheap'”**
Ensure all files are in the **same folder** and you run `main.py` from inside that folder.

### **“ValueError: invalid literal for int()”**
Ensure your input contains **only integers separated by spaces**.

---

# **9. Summary**

This project demonstrates:

- Custom implementation of **heap data structures**
- A **Priority Queue ADT** built on a Max‑Heap
- The **Heap Sort algorithm**
- Modular **OOP design**
- User‑interactive programs for demonstration

---

# **10. Link to a 5-minute introduction video**
https://www.dropbox.com/scl/fi/c6uzjjzrq1vkzk2vwrkmv/20260417_104144.mp4?rlkey=qnj17t7qredrcgkvu3i3krohs&st=nxyy2l9a&dl=0

