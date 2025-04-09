## Reflection

### 1. Challenges in Designing the Domain Model and Class Diagram

One of the main challenges was deciding the level of abstraction for entities. For example, deciding whether an `Alert` should be an entity or just an event was tricky. Eventually, it was modeled as a class because it contains timestamped, actionable data. Additionally, balancing between **composition** and **aggregation** for relationships like `MitigationPlan` and `Task` took multiple iterations.

Another challenge was identifying **methods** for each class. While it was easy to map system-level functionality, converting that to object methods required a shift in thinking towards **encapsulation** and **object behavior**.

---

### 2. Alignment with Previous Assignments

This class diagram builds directly upon the **functional requirements and user stories** from Assignments **4 to 8**. For example:

- **FR-001** (Identify and Assess Risks) maps to the `Risk` class.
- **FR-002** (Approve Mitigation Plans) is modeled using `MitigationPlan` and `Task`.
- The `Backup` class models **FR-011** (Automated Backups).

The **states** defined in Assignment 8 (like the `Risk` lifecycle) were useful in deciding which methods to add per class. This diagram is the natural continuation of the **state/activity workflows** from Assignment 8, giving a more static, structural perspective.

---

### 3. Trade-offs Made

To maintain simplicity:

- **Inheritance** was limited to user roles only (e.g., `Analyst`, `Admin`).
- **Composition** was favored over inheritance for complex entities (e.g., `MitigationPlan` contains `Tasks`).
- Some system-level processes (like **authentication**) were abstracted away to avoid clutter.

---

### 4. Lessons Learned

Through this assignment, I deepened my understanding of **object-oriented design**. I learned the importance of aligning **domain logic** with **system requirements**, and the value of **visual modeling** in communicating software structure. 

**Mermaid.js**, in particular, made it easier to visualize complex relationships. I also realized how much clarity comes from linking models back to **user stories** and **Agile artifacts** it makes each class purposeful and grounded in real-world scenarios.
