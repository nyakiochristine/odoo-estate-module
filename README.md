
# Odoo Real Estate Advertisement Module (`estate`)

A fully functional Odoo 19.0 custom module built from scratch to manage real estate property listings, tracking, configurations, and sales workflows. This module acts as a complete blueprint demonstrating the foundational concepts of the Odoo Server Framework.

## 🚀 Features

* **Property Management:** Create and track properties with details such as expected/selling prices, availability date, garden configurations, area metrics, and property types/tags.
* **Smart Business Logic:** Automated calculations using computed fields (e.g., `total_area`) and dynamic interface updates using inline change triggers (`@api.onchange`).
* **Strict Data Integrity:** Robust database-level and Python-level constraints ensuring valid operational parameters (e.g., preventing negative pricing, validating bid offers).
* **Workflow Automation:** Managed property lifecycles (`New` ➡️ `Offer Received` ➡️ `Offer Accepted` ➡️ `Sold` / `Canceled`) complete with restricted state transitions.
* **Core App Inheritance:** Seamlessly extends Odoo's base framework (`res.users`) to assign property management portfolios directly to users.
* **User Interactive Wizards:** Implements temporary database interaction via a `TransientModel` pop-up wizard to safely handle record cancellation notes.
* **Configured Access Security:** Implements foundational role permissions via `ir.model.access.csv`.

---

## 🛠️ Tech Stack & Concepts Covered

| Component | Technology / Concept |
| :--- | :--- |
| **Backend Framework** | Odoo 19.0 ORM (Python 3.11+) |
| **Database** | PostgreSQL 14 |
| **Containerization** | Docker / Docker Compose |
| **UI Presentation** | Form, List, and Search Views (XML) |
| **Access Control** | Odoo Security Layer (CSV Rules) |

---

## 📂 Repository Structure


estate/
├── __init__.py
├── __manifest__.py            # Module description, metadata, and data loading order
├── models/
│   ├── __init__.py
│   ├── estate_property.py     # Main business object definitions & logic
│   └── estate_users.py        # Inherited base res.users models
├── security/
│   └── ir.model.access.csv    # Access rights configuration file
├── views/
│   ├── state_property_views.xml # Form, Tree, and Window actions for property data
│   └── res_users_views.xml    # Inherited layout adaptations for core system views
└── wizard/
    ├── __init__.py
    ├── cancel_wizard.py       # Transient wizard business logic code
    └── cancel_wizard_views.xml# Popup view layer interface definition

```

---

## 💻 Installation & Environment Setup (Docker)

This project is fully containerized using Docker Compose. Follow these steps to spin up the Odoo server and PostgreSQL database instantly without configuring local Python or Postgres dependencies.

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your host system.

### Quick Start Instructions

1. **Clone the project** and ensure your custom addon folder structure matches this relative mounting path:

```text
   odoo-dev/
   ├── docker-compose.yml
   └── custom_addon/
       └── estate/

```

2. **Navigate to your workspace root directory** in your terminal:

```bash
   cd path/to/your/odoo-dev

```

3. **Boot up the containers** by running the following command:

```bash
   docker compose up -d

```

4. **Access the application** by navigating to your browser:
👉 **`http://localhost:8069`**
5. **Initialize the Database:**
* **Master Password:** Use the master password displayed on screen or set a new one.
* **Database Name:** `estate_db`
* **Email / Password:** `admin` / `admin`


6. **Install the Module:**
* Navigate to **Settings** and scroll down to click **Activate the developer mode**.
* Go to the **Apps** dashboard, click **Update Apps List** in the top navigation bar, and select **Update**.
* Clear the default `Apps` filter from the search bar, type `estate`, and click **Activate** on the Real Estate Management module!



```

```