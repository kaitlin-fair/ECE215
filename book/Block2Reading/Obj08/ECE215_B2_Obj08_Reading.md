# Objective 2.8

| LO# | Description |
|----------|----------|
| 2.8 | I can model Moore and Mealy Finite State Machines (FSMs) using tools such as state transition diagrams, transition tables, and combinational and sequential logic circuits.  |

---

## 1. Introduction to Finite State Machines (FSMs)

### 1.1 What is a Finite State Machine?
A **Finite State Machine (FSM)** is a computational model used to represent and control the execution flow of a system that can exist in a **finite number of states**. At any given time, an FSM is in one particular state. Based on the input it receives and the current state, it determines the next state and may produce an output. This behavior makes FSMs ideal for modeling systems where outcomes depend on both past and present events.

FSMs are defined by the following components:
- **States** – A finite set of distinct configurations that represent the system’s condition at any given moment.
- **Inputs** – A set of signals or conditions that affect the state transitions.
- **Transitions** – A set of rules that define how the FSM moves from one state to another based on inputs.
- **Outputs** – Signals or values that the FSM generates based on the current state and/or inputs.
- **Initial State** – The state where the FSM starts operating.

FSMs are widely used in various fields of engineering and computer science because they provide a structured and predictable way to model complex systems. They are especially useful in **control systems**, **digital circuits**, **communication protocols**, **robotics**, and **software development**.

---

### 1.2 Why Use FSMs?
FSMs are used because they offer:
✅ **Predictability** – FSMs follow a clear and deterministic pattern of state transitions based on inputs.  
✅ **Simplicity** – Complex problems are broken down into manageable states and transitions.  
✅ **Reusability** – FSM models can be reused and adapted across different applications.  
✅ **Debuggability** – FSMs offer clear, structured models that simplify troubleshooting.  
✅ **Automation** – FSMs enable the automation of complex sequences and decision-making processes.  

---

### 1.3 FSM Examples in Engineering
FSMs are used extensively in both hardware and software applications:

1. **Digital Circuits**  
   - Used in control logic for microprocessors, memory controllers, and communication interfaces.
   - Example: An FSM controlling an elevator's floor selection system.

2. **Networking and Protocols**  
   - FSMs define the state-based behavior of communication protocols (e.g., TCP/IP handshake).
   - Example: A protocol state machine for handling data transmission and reception.

3. **Embedded Systems**  
   - Used to control devices like washing machines, traffic lights, and vending machines.
   - Example: An FSM managing the washing cycles of a washing machine.

4. **Software Development**  
   - Used in artificial intelligence for decision-making models.
   - Example: Game AI where different NPC (Non-Player Character) states determine behavior.

5. **Automotive Systems**  
   - Used for managing state-dependent functions like anti-lock braking systems (ABS) and automatic transmission.  
   - Example: FSM controlling gear shifts based on speed and load.

---

### 1.4 Moore vs. Mealy Machines
FSMs are classified into two types based on how they generate outputs:

#### **Moore Machine**  
- The output depends **only on the current state**.  
- State transitions are determined by inputs, but outputs are defined solely by the state.  
- Moore machines typically have **more states** but **simpler transition logic**.  
- Outputs are generated after a state transition has occurred, which may introduce a delay.  

![](./ECE215_B2_Obj08_Reading_media/image2.png)

✅ **Advantages of Moore Machines:**  
- Simpler to design and understand.  
- Outputs are more stable since they depend only on the state.  

❌ **Disadvantages:**  
- More states may be required to implement the same functionality compared to Mealy machines.  

✅ **Example:**  
Traffic lights are typically modeled as Moore machines where the light state determines the output (red, green, yellow).  

---

#### **Mealy Machine**  
- The output depends on **both the current state and the input**.  
- State transitions and outputs can change simultaneously when the input changes.  
- Mealy machines can have **fewer states** than Moore machines for the same task but require **more complex transition logic**.  
- Outputs can change more quickly in response to inputs since they are not tied to state alone.  

![](./ECE215_B2_Obj08_Reading_media/image3.png)

✅ **Advantages of Mealy Machines:**  
- Fewer states are required for complex behavior.  
- Can respond faster to inputs since the output is computed directly from the input and state.  

❌ **Disadvantages:**  
- More complex to design and test.  
- Outputs can be less stable since they depend on real-time inputs.  

✅ **Example:**  
A vending machine is often modeled as a Mealy machine because the output (dispensing an item) depends on both the state (amount of money entered) and the input (coin type).  

---

### 1.5 FSM Implementation in Hardware
FSMs are commonly implemented in digital hardware using:
- **Flip-Flops** – To store the current state.  
- **Combinational Logic** – To compute the next state and outputs based on current state and inputs.  

Modern FSM designs are often implemented using **Field Programmable Gate Arrays (FPGAs)** and **hardware description languages** like **VHDL** and **Verilog**.  

#### **Basic FSM Structure in Hardware:**
1. **Inputs** – Binary signals that control the state transitions.  
2. **Next State Logic** – Determines the next state based on the present state and inputs using combinational logic.  
3. **Flip-Flops** – Hold the current state and update it on each clock cycle.  
4. **Output Logic** – Generates the output signals based on the state and inputs (Mealy) or state alone (Moore).  

FSM Hardware Block Diagram:

```
         +-------------+               +--------------+
 Inputs →| Next State  |→ Next State → | Flip-Flops    |
         | Logic       |               | (State Memory)|
         +-------------+               +--------------+
                |                             |
                ↓                             ↓
         +-------------+               +--------------+
         | Output Logic |→ Outputs →   | Output Signals|
         +-------------+               +--------------+
```

**Example:**  
A traffic light FSM in hardware would:  
- Use a D flip-flop to store the current state.  
- Combinational logic to determine the next state and outputs.  
- Outputs would control the traffic lights based on the current state.  

---

### 1.6 FSM Implementation in Software
FSMs are also widely used in software design for state-based control and behavior modeling.  
- A state can be represented using **constants** or **enumerations**.  
- A state transition table can be implemented using **arrays** or **switch-case** statements.  
- Transitions can be triggered by user input, timeouts, or external events.  

**Example:**  
A video game AI might use an FSM to control the behavior of a character:  
- **State 1** – Idle →  
- **State 2** – Patrol →  
- **State 3** – Attack →  
- **State 4** – Flee  

Transitions would be based on game events like proximity to an enemy or health level.  

---

### 1.7 Advantages and Limitations of FSMs
**✅ Advantages:**  
✔️ Simple to design and understand.  
✔️ Predictable behavior.  
✔️ Efficient in hardware and software implementations.  
✔️ Good for sequential control problems.  

**❌ Limitations:**  
✖️ Limited scalability – FSMs become difficult to manage when the number of states becomes large.  
✖️ Not well suited for complex, parallel operations.  
✖️ State explosion – As the complexity increases, the number of states can grow exponentially.  

---

### 1.8 Summary
Finite State Machines provide a structured approach to modeling complex state-based behavior. Moore and Mealy machines each offer unique advantages depending on the application. FSMs are central to digital design, embedded systems, and software development due to their simplicity and predictability. When properly designed, FSMs can lead to efficient, reliable, and scalable systems.  

---

## 2. State Transition Diagrams
FSMs are often modeled using **state transition diagrams**, which provide a graphical representation of states and transitions.

### Components of a State Transition Diagram:
1. **States** – Represented as circles, showing all possible configurations of the system.  
2. **Transitions** – Represented as arrows connecting states, indicating how the system moves from one state to another.  
3. **Events/Inputs** – Labels on the arrows that describe the condition that causes the transition.  
4. **Outputs** – The values produced based on the state (Moore) or state and inputs (Mealy).  

### Moore Machine Example:
A Moore FSM that recognizes the binary sequence `10` would have states:
- S0 → Start state  
- S1 → After seeing `1`  
- S2 → After seeing `10`  

Transition Example:
- Start in S0  
- If input = `1`, transition to S1  
- If next input = `0`, transition to S2 and generate an output  

![](./ECE215_B2_Obj08_Reading_media/image4.png)

### Mealy Machine Example:
In a Mealy FSM, the output can change based on the input while in a given state. This can reduce the number of required states but increases the complexity of the transition logic.

---

## 3. FSM Design Process
### Step 1: Define/Encode the States
- Assign a binary value to each state.  
- Example: 3 states require 2 bits ($2² = 4$ states).  
- S0 = 00, S1 = 01, S2 = 10  

### Step 2: Define/Encode the Inputs
- Inputs are typically binary (0 or 1), but multi-bit inputs are possible.  
- Example: An input `x` could represent `0` or `1`, or more complex values.  

### Step 3: Define/Encode the Outputs
- In a Moore machine, output depends on state only.  
- In a Mealy machine, output depends on state and input.  

### Step 4: Create a State Transition Diagram
- Draw the states as circles.  
- Connect them with arrows showing the transitions based on input.  

### Step 5: Create a State Transition Table
A state transition table maps the present state and input to the next state and output. In the example below, there are two states represented by two bits, $q_1$ and $q_0$, and one input, $x$. All possible combinations of the states and input a listed. The third column shows the next state (represented by the $^+$) for each present state and input combination, while the fourth column shows the output, $z$.

| Present State, $q_1 q_0$ | Input, $x$ | Next State, $q_1^+ q_0^+$ | Output, $z$ |
|:-------------:|:-----:|:----------:|:------:|
| 00 | 0 | 00 | 0 |
| 00 | 1 | 01 | 0 |
| 01 | 0 | 10 | 1 |
| 01 | 1 | 00 | 0 |

### Step 6: Express Logic Equations
Use Boolean algebra to express the next state and output logic. From the state transition table above, we use the Sum of Products (SOP) form to find $q_1^+$, $q_0^+$, and $z$:
- Next state equation:  

$$q_1^+ = \overline{q_1} q_0 \overline{x}$$
$$q_0^+ = \overline{q_1} \overline{q_0} x$$


- Output equation:  

$$z = q_1^+ = \overline{q_1} q_0 \overline{x}$$


### Step 7: Implement with Flip-Flops and Logic Gates
Use flip-flops to store the state and combinational logic to calculate the next state and outputs:
- Flip-flop holds the current state.  
- Combinational logic calculates the next state and output.  

---

## 4. Example FSM Designs

The following examples will be worked out in class. 

### Example 1: Sequence Recognizer
**Design Goal:** Recognize the sequence `10`  
- States: S0 → S1 → S2  
- Inputs: Binary input  
- Outputs: Output `1` when sequence `10` is detected  

### Example 2: 2-Bit Counter
**Design Goal:** Count from 0 to 3 and wrap around  
- States: 00, 01, 10, 11  
- Inputs: Increment signal (1 = increment, 0 = hold)  
- Outputs: Current state (Moore machine)  

| Present State | Input | Next State | Output |
|---------------|-------|------------|--------|
| 00 | 0 | 00 | 00 |
| 00 | 1 | 01 | 01 |
| 01 | 0 | 01 | 01 |
| 01 | 1 | 10 | 10 |

### Example 3: Vending Machine
**Design Goal:** Dispense product after receiving 20¢  
- States represent total amount inserted (0¢, 5¢, 10¢, 15¢, 20¢)  
- Inputs: N = nickel, D = dime, Q = quarter  
- Outputs: Dispense product and return change  

| Present State | Input | Next State | Output |
|---------------|-------|------------|--------|
| 00 | N | 01 | 0 |
| 01 | D | 11 | 0 |
| 11 | N | 00 | 1 (Dispense) |

### Example 4: Traffic Light Control
**Design Goal:** Control traffic light based on sensor inputs  
- States:  
  - S0 = NS green, EW red  
  - S1 = NS yellow, EW red  
  - S2 = NS red, EW green  
  - S3 = NS red, EW yellow  
- Inputs: Sensor data  
- Outputs: Light configuration  

| Present State | Input | Next State | Output |
|---------------|-------|------------|--------|
| S0 | 00 | S0 | NS green, EW red |
| S0 | 01 | S1 | NS yellow, EW red |
| S1 | - | S2 | NS red, EW green |
| S2 | 10 | S2 | NS red, EW green |

---

## 5. Summary
 
Finite State Machines (FSMs) provide a structured and systematic way to design and analyze state-based systems. They are widely used in both hardware and software applications due to their ability to represent complex sequences of operations in a clear and predictable manner. FSMs consist of a finite number of states, and the system transitions between these states based on inputs and defined transition rules.  

FSMs are classified into two main types: **Moore machines** and **Mealy machines**. Moore machines generate outputs based only on the current state, making them more stable and easier to test. Mealy machines generate outputs based on both the current state and the inputs, allowing them to respond more quickly to changes but adding complexity to the design.  

The design process for FSMs includes defining the states, encoding inputs and outputs, creating state transition diagrams and tables, deriving logic equations, and implementing the system using flip-flops and combinational logic. Modern FSMs are frequently implemented using **FPGAs** and programmed with hardware description languages like **VHDL** and **Verilog**.  

FSMs offer significant advantages, such as predictability, simplicity, and reusability, but they can become challenging to manage when the number of states grows too large. Despite this, FSMs remain one of the most effective methods for modeling and controlling state-dependent behavior in modern engineering and computer science.  

