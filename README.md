# VIDHI – Legal AI Platform

VIDHI is a desktop legal-practice management application built with
[Flet](https://flet.dev) (Python UI framework, powered by Flutter). It gives
advocates (lawyers) and their clients a shared platform to manage cases,
hearings, documents, billing, and client communication — with a built-in
English ⇄ Telugu translation toggle and a simple AI assistant for quick
case/hearing lookups.

## Features

- **Dual dashboards** — separate advocate and client-facing views tailored to each role's needs
- **Case management** — track active cases, pending service requests, and upcoming hearings
- **Document management** — upload, organize, and retrieve case documents by folder/category, with collision-safe file naming
- **Billing & payments** — track fees, payments, and deadlines per case
- **Multi-language support** — full Telugu translation alongside English (180+ translated strings across the app)
- **Light/dark theme support** with theme-aware styling throughout
- **Local calendar view** for hearings and deadlines

## Tech Stack

| Layer          | Technology                     |
|----------------|---------------------------------|
| UI Framework   | [Flet](https://flet.dev) (Flutter for Python) |
| Language       | Python 3.10                        |
| Database       | SQLite (`vidhi_users.db`)        |
| Assets         | Local images (`assets/logo.png`, `assets/background.png`) |

## Project Structure

```
vidhi_fixed/
├── main.py                     # App entry point, routing, sidebar/navbar wiring
├── i18n.py                     # English ⇄ Telugu translation layer
├── assets/
│   ├── logo.png
│   └── background.png
├── components/                 # Reusable UI building blocks
│   ├── cards.py
│   ├── navbar.py
│   ├── sidebar.py
│   ├── tables.py
│   └── trend_chart.py
├── services/                   # Data & business logic
│   ├── db.py                   # SQLite schema, init, CRUD helpers
│   └── case_data.py            # Case-related data helpers
├── views/                      # Screens (one file per page)
│   ├── home.py                 # Landing page (choose Advocate/Client)
│   ├── login.py                # Login/signup screen
│   ├── dashboard.py             # Advocate dashboard
│   ├── client_dashboard.py      # Client dashboard
│   ├── new_case.py              # Create new case form
│   ├── active_cases.py          # All active cases (legacy/sidebar route)
│   ├── active_cases_only.py     # Dashboard "Active Cases" widget
│   ├── service_requests.py      # Dashboard "Pending Requests" widget
│   ├── hearings_this_week.py    # Dashboard "Hearings This Week" widget
│   ├── case_detail.py           # Single case detail view
│   ├── matters.py               # Active matters listing
│   ├── documents.py             # Advocate document management
│   ├── client_documents.py      # Client document view
│   ├── calendar.py              # Hearings calendar
│   ├── billing.py               # Advocate billing/payments
│   ├── client_billing.py        # Client billing/payments
│   ├── assistant.py             # AI assistant chat screen
│   ├── settings.py              # App settings
│   ├── contacts.py
│   └── about.py
└── vidhi_users.db               # SQLite database (auto-created/migrated on run)
```

## Screenshots

> Add your screenshots to a `screenshots/` folder in the project root, then
> update the image paths below to match your filenames.

### Home Screen
![Home Screen](screenshots/home.png)

### Login
![Login](screenshots/login.png)

### Advocate Dashboard
![Advocate Dashboard](screenshots/dashboard.png)

### Client Dashboard
![Client Dashboard](screenshots/client_dashboard.png)

### Active Cases
![Active Cases](screenshots/active_cases.png)

## Getting Started

### Prerequisites

- Python 3.9+
- `flet` package

### Installation

```bash
# (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install flet
```

### Running the App

From inside the `vidhi_fixed/` directory:

```bash
python main.py
```

This launches a desktop window (1600×900) titled **"VIDHI Legal AI"**. On
first run, `init_db()` will create/migrate all required tables in
`vidhi_users.db` automatically — no manual database setup is needed.

### Usage

1. From the home screen, choose **Client Login** or **Advocate Login**.
2. Log in / sign up with a username, contact, and password.
3. Use the sidebar to navigate between Dashboard, Cases, Documents,
   AI Assistant, Calendar, Billing, and Settings (menu items differ based on
   role).
4. Use the **Translate** control (available on most screens) to switch the
   entire UI between English and Telugu.

## Database Schema (SQLite)

| Table       | Purpose                                              |
|-------------|-------------------------------------------------------|
| `users`     | User accounts (contact, username, password)           |
| `cases`     | Case records (client, advocate, court, status, type)  |
| `hearings`  | Hearing dates, court, judge, advocate per case         |
| `documents` | Uploaded document metadata per case                    |
| `doc_files` | Document folder structure                              |
| `payments`  | Fee amount, status, method, deadline per case           |
| `case_notes`| Free-form notes attached to a case                     |

Schema migrations (adding new columns to existing tables) are handled
automatically inside `init_db()`.

## Notes

- This is a **local desktop app** — data is stored in a local SQLite file
  and is not synced to any external server.
- The AI Assistant currently uses simple keyword matching (e.g. "hearing",
  "case", "document") rather than a full LLM integration — a good area for
  future enhancement.
- `dashboard_old.py` and `client_dashboard.py.bak` are legacy/backup files
  retained for reference and are not used by `main.py`.

## Future Improvements

- Integrate a real LLM-based backend for the AI Assistant.
- Add authentication hardening (password hashing, session management).
- Add automated tests for `services/db.py` and view logic.
- Package as a standalone executable (`flet build`) for distribution.
