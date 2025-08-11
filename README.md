# Automated API Testing CLI Tool (at.exe / auttest.exe)

A simple command-line tool for automated API request testing, interactively controlled via terminal prompts.

---

## Features

- Interactive input for base URL, route, HTTP method, headers, JSON body, and request count  
- Repeat requests multiple times  
- Default base URL configurable  
- Outputs HTTP status and response body for each request  
- Works on Windows CMD and PowerShell  

---

## Installation & Usage

### From Python script

1. Clone this repository or download `at.py`.

2. Install dependencies:

```bash
pip install requests termcolor
```

3. Run the tool:

```bash
python at.py
```

---

### Using the executable (`.exe`)

- The repository includes a prebuilt `.exe` file (e.g., `at.exe`).

- **Important:** Windows has a built-in `at` command, so rename the `.exe` to something unique like `auttest.exe` to avoid conflicts. im to lazy for that

- Copy the renamed `.exe` (e.g., `auttest.exe`) to a folder included in your system `PATH` (e.g., `C:\tools`).

- Then you can run the tool from **any directory** by simply typing:

```powershell
auttest
```

---

## How it works

You will be prompted for:

- **Base URL** (default: `http://localhost:4000`)  
- **Route** (e.g., `/api/users`)  
- **HTTP method** (GET, POST, PUT, DELETE, etc.)  
- **Headers** in JSON format (e.g., `{"Authorization": "Bearer token"}`)  
- **Body** in JSON format (e.g., `{"name": "John"}`)  
- **Number of requests** to send  

Use `?` as input for examples or help on each prompt.

---

## Example

```
Base URL (default http://localhost:8000): 
Route: /api/login_check
Method (default POST): 
Headers (JSON): {"Content-Type": "application/json"}
Body (JSON): {"username": "user", "password": "pass"}
Number of requests (default 1): 3
```

This sends 3 POST requests to `http://localhost:8000/api/login_check` with the given headers and body.

---

## Notes

- Make sure your API server is running and reachable.  
- JSON inputs must be valid or left empty if not needed.  
- The executable is Windows-only.  
- If you want to rebuild the `.exe` yourself, run:

```bash
pip install pyinstaller
pyinstaller --onefile at.py
