# **Reflection: Challenges in Translating Requirements to Use Cases and Tests**

This system **Risk Management System** required translating system requirements into **use cases** and **test cases**. This process had several challenges, which are addressed systematically.

## **1. Understanding Ambiguous Requirements**
Many requirements were unclear, making it difficult to define specific actions. For example, "The system should allow risk assessment" did not specify who performs the assessment or how the system responds.

**Solution:** Refined the requirements by engaging stakeholders and using user stories to break them into clear use cases.

---

## **2. Selecting Critical Use Cases**
With many possible system interactions, prioritizing the most important use cases was challenging. Initially, considering use cases like "Logout," but they were not central to risk management.

**Solution:** Used a Use Case Diagram to identify key use cases, such as **"Identify Risk," "Assess Risk Impact," and "Approve Mitigation Plans."**

---

## **3. Defining Preconditions and Postconditions**
Ensuring each use case had clear **preconditions (required system state before execution)** and **postconditions (system state after completion)** was essential.

**Example:** In "Submit Mitigation Plan," a risk must exist before submission (precondition). After execution, the plan is saved and a notification is sent (postcondition).

**Solution:**Carefully reviewed each step to ensure logical flow and system integrity.

---

## **4. Handling Alternative Flows and Errors**
Not all actions follow a smooth path. Users may enter incorrect data or lack the necessary permissions.

**Example Challenge:** What if a Risk Manager tries to approve a mitigation plan instead of a Compliance Officer?

**Solution:** Documented error scenarios in alternative flows, ensuring the system prevents unauthorized actions and provides meaningful error messages.

---

## **5. Creating Meaningful Test Cases**
Writing effective test cases was difficult because they needed to cover all possible situations.

**Key challenges:**
- Ensuring all functional requirements were tested.
- Simulating real-world use.
- Addressing performance and security concerns.

**Example:**
- A test case for "Identify Risk" checks if valid risks are saved, missing fields trigger errors, and the system handles bulk risk entries.

**Solution:** Developed a structured test case table, covering normal scenarios, edge cases, and failures. Also included **performance and security tests**, such as handling **1,000 concurrent users** and preventing **unauthorized modifications**.

---

## **Conclusion**
Translating requirements into **use cases and test cases** is challenging but crucial. By refining requirements, selecting key use cases, defining clear flows, handling errors, and designing comprehensive tests, ensured the **Risk Management System** is functional, efficient, and meets stakeholder expectations.




