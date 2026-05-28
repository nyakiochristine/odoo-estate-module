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
| **Database** | PostgreSQL |
| **UI Presentation** | Form, List, and Search Views (XML) |
| **Access Control** | Odoo Security Layer (CSV Rules) |
| **Data Architecture** | `Many2one`, `One2many`, `Many2many`, `TransientModel` |

---

## 📂 Repository Structure

```text
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

## 💻 Installation & Local Setup

### Prerequisites
* A running instance of Odoo 19.0
* Local Python 3.11 environment configured (`odoo-env`)
* PostgreSQL service active

### Installation Steps

1. Navigate to your main Odoo development directory:
   ```bash
 2. Ensure this custom_addon repository folder exists parallel to your core odoo directory.

 