# 🔐 Access Control System

This project implements **Role-Based Access Control (RBAC)** to ensure a secure and organized environment for managing library resources. Access is controlled through specific permissions assigned to different user roles.

---

## 📚 Permissions Defined on Book Model
Individual permissions are defined within the `Book` model to control specific database actions. These allow for granular security checks:

* **`can_view`**: Allows users to see the list of books and view detailed information for each entry.
* **`can_create`**: Allows users to add new book records to the database.
* **`can_edit`**: Allows users to modify existing information (title, author, etc.) for a specific book.
* **`can_delete`**: Allows users to permanently remove a book record from the system.

---

## 👥 Group Roles & Hierarchy
To simplify management, permissions are bundled into three primary roles. This structure follows the **Principle of Least Privilege**, ensuring users only have the access necessary for their tasks.

| Role | Permissions Granted | Typical User |
| :--- | :--- | :--- |
| **Viewers** | `can_view` | Standard students, guests, or members. |
| **Editors** | `can_view`, `can_create`, `can_edit` | Library staff and content moderators. |
| **Admins** | Full Access (`can_view`, `can_create`, `can_edit`, `can_delete`) | Senior librarians and IT managers. |

---

## 🛠 Enforcement and Security
* **Backend:** Access is enforced in `views.py` using the `@permission_required` decorator, which blocks unauthorized requests at the server level.
* **Frontend:** The user interface dynamically hides action buttons (like **Edit** or **Delete**) based on the logged-in user's permissions using Django template tags.