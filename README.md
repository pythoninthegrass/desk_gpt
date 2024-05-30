# desk_gpt

Silly project to mimic the fantastic [QuickGPT](https://sindresorhus.gumroad.com/l/quickgpt) app but using the Python SDK instead of the web interface.

## Minimum requirements

* [Python 3.11](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/)
* [Node.js](https://nodejs.org/en/download/)
* [Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html)

## Installation

* Clone the repo
    ```bash
    git clone https://github.com/pythoninthegrass/desk_gpt.git
    cd desk_gpt
    ```
* Install the backend
    ```bash
    poetry install
    ```
* Install the frontend
    ```bash
    cd app
    npm install         # bun install
    ```

## Quickstart

### Run server

```bash
cd backend
./run_django.py
```

### Run frontend

Either run the vite dev server

```bash
cd app
npm run dev             # vite dev
```

or start the tauri app (recommended)

```bash
cd app/src-tauri
npm run tauri dev       # bunx tauri dev
```

## TODO

* [devbox services](https://www.jetify.com/devbox/docs/guides/services/)
  * Automates the setup of the backend and frontend services
* Tauri integration
  * ~~Add tray icon~~
  * Add global shortcut
  * Add notifications
* Package the app
  * Create a distributable package
  * Setup CI
* Create sidebar
  * `+ New chat` button
  * Chat history with title truncated
  * `Clear conversations` button
  * `Log out` button
* UI/UX design tweaks
  * Better code snippet formatting
  * Add loading spinner
  * Fixed width for chat form
  * Change font
* Auth (Login / Logout)
  * Save token to disk
  * Load token from disk
