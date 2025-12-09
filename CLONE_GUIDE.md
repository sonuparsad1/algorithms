# How to Clone and Setup This Project

## Quick Clone & Setup Guide

### Step 1: Clone the Repository
Open PowerShell or Command Prompt and run:

```powershell
git clone https://github.com/sonuparsad1/algorithms.git
cd algorithms
```

### Step 2: Verify the Structure
After cloning, you'll have the exact same folder structure as the original:

```
algorithms/
├── Algorithms-and-Data-Structures-Python/
├── Python_Theory/
├── python/
├── nunpy/
├── public/
├── README.md
└── .gitignore
```

### Step 3: (Optional) Setup Python Environment

If you want to run Python code:

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install NumPy if needed
pip install numpy
```

### Step 4: Start Learning/Developing

- **For Python Theory**: Open any markdown file in `Python_Theory/`
- **For NumPy**: Navigate to `nunpy/` and run Python files
- **For Algorithms**: Explore `Algorithms-and-Data-Structures-Python/`
- **For Web Viewer**: Open `Algorithms-and-Data-Structures-Python/web_viewer/index.html` in browser

---

## Directory Structure Explained

| Folder | Purpose |
|--------|---------|
| `Algorithms-and-Data-Structures-Python/` | Core algorithms, data structures, and mathematical concepts |
| `Python_Theory/` | Complete Python learning curriculum with 17 topics |
| `python/PythonMasteryRepo/` | Python code implementations (Algorithms, OOPs) |
| `nunpy/` | NumPy array operations and tutorials |
| `public/` | Public assets and resources |

---

## Keeping Your Local Copy in Sync

To pull latest updates from GitHub:

```powershell
cd algorithms
git pull origin main
```

To contribute changes back:

```powershell
# Stage changes
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub
git push origin main
```

---

## Notes

- The `.gitignore` file prevents unnecessary files (venv, __pycache__, etc.) from being uploaded
- All file permissions and structure are preserved during cloning
- The repository is organized hierarchically for easy navigation
- Each Python_Theory section includes definitions, theory, properties, syntax, examples, and practice questions

---

Created: December 2025  
Repository: https://github.com/sonuparsad1/algorithms
