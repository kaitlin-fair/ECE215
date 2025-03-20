# **ECE215 Project #2 Spring 2025**

## **Finite State Machine for Automated Sorting System**

### **Practical Application: Automated Sorting System in a Factory**
Consider an **automated conveyor belt system** used in a packaging factory to **sort products based on their sizes**. Your finite state machine (FSM) will classify and track items as they move along the conveyor belt.

#### **How It Works:**
1. **Distance Sensor for Object Classification**  
   The sensor measures the height of objects passing through. Based on the measured height, the system assigns an input value (A = 0, 1, or 2):
   - **Small items (0-5 cm)** → A = 0
   - **Medium items (5-10 cm)** → A = 1
   - **Large items (10-15 cm)** → A = 2

2. **Control Input (B) for Sorting Direction**
   - **B = 1 (Forward Sorting Mode)** → The system increments the current state to cycle through the sorting bins.
   - **B = 0 (Reverse Sorting Mode)** → The system decrements the state to track the previous item category.

3. **Moore Machine Output for Actuation**  
   The state output voltage controls an actuator that directs items to different bins:
   - **State 0 -> output 0.8V** → Directs small items to **Bin 1**
   - **State 1 -> output 1.6V** → Directs medium items to **Bin 2**
   - **State 2 -> output 2.4V** → Directs large items to **Bin 3**

Now that you have the practical application in mind, you get to build a version of this using your Arduino Due, distance sensor, and jumper cables!

---

### **Project Overview:**
You are tasked with designing an Arduino Due-based FSM. Since we are using software instead of logic gates, we do not have to encode states, inputs, and outputs in binary (hurray!). The system will have two distinct inputs:

1. **ADC Input A**: The Sharp GP2Y0A51SK0F distance sensor will measure obstacles 2cm to 15cm away. The measurement system should produce the following values for input A:

    | Distance Measured | Logical Input A |
    |-------------------|----------------|
    | 2 - 5 cm         | 0              |
    | 5 - 10 cm        | 1              |
    | 10 - 15 cm       | 2              |

    **Error should be no more than ±0.5 cm.**

2. **Digital input B**: For this input you will use a jumper wire to connect one of the digital input/output (I/O) pins on the Arduino to either +3.3V (B = 1 or HIGH) or GND (B = 0 or LOW). B = 1 indicates "count up" and B = 0 indicates "count down".

The FSM will have three states numbered **0, 1, and 2**. This should be a **Moore Machine**, and the output should be:

| State | Output Voltage Z |
|-------|-----------------|
| 0     | 0.8V           |
| 1     | 1.6V           |
| 2     | 2.4V           |

The present state should be sent to the **Serial Monitor** (clearly labeled as the integer state value). The output voltage should be sent to **DAC1** (measured by a Digital Multimeter connected to a jumper wire at DAC1). The update rate should be **2 seconds**.

The FSM should respond to combinations of inputs as outlined in the following Transition Table. *Note the expected sequence is for starting at 0 and maintaining the same input combination.* 
#### **Transition Table:**

| B | A | Next State | Expected Sequence if Start at 0 |
|---|---|-----------|---------------------------------|
| 1 | 0 | Add 0     | 0, 0, 0, ...                   |
| 1 | 1 | Add 1     | 0, 1, 2, 0, 1, 2, ...          |
| 1 | 2 | Add 2     | 0, 2, 1, 0, 2, 1, ...          |
| 0 | 0 | Subtract 0| 0, 0, 0, ...                   |
| 0 | 1 | Subtract 1| 0, 2, 1, 0, 2, 1, ...          |
| 0 | 2 | Subtract 2| 0, 1, 2, 0, 1, 2, ...          |

*Hint*: Note similarities between the sequences for different combinations of inputs. Can you use this to simplify your FSM?

---

### **Steps:**
1. Make sure you understand the definitions of the states, inputs, and outputs.
2. Draw the state transition diagram.
3. Write the state transition table.
4. Implement your FSM design in Arduino code and with the correct physical connections to the distance sensor, jumper wires, and DMM.
5. Demonstrate your FSM to your instructor.

---

### **Discussion Points:**
- Investigate your choice of **bit-resolution for both the ADC and the DAC** to ensure precise voltage outputs.
    - What are the pros and cons of using a higher number of bits for your ADC? For your DAC?
    - Are you able to achieve the project objectives with fewer than the default 10 bits? Why or why not?
---

### **Submission Requirements:**
- **Demonstrate your FSM** to your instructor.
- Submit a **PDF to Gradescope** containing:
  - **State transition diagram** and **corresponding state transition table**
  - A copy of your **final code**
  - Answers to the discussion questions

*(Just submit a PDF with these three sections and a doc statement. Don’t worry about a specific format!)*

