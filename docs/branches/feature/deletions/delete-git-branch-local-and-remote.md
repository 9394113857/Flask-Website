# Delete Git Branch (Local + Remote) using VS Code Git Bash

## Prerequisites
- Open **VS Code**.
- Open the integrated terminal (**Git Bash**).
- Navigate to your Git repository.

---

## Step 1: Switch to the `main` branch

```bash
# Switch to the main branch
git checkout main
```

---

## Step 2: Update the `main` branch (Recommended)

```bash
# Download the latest changes from GitHub
git pull origin main
```

---

## Step 3: Delete the local branch

```bash
# Delete the local branch
git branch -D feature/navbar-enhancement
```

> **Note:** `-D` force deletes the branch even if it has not been merged.

---

## Step 4: Delete the remote branch from GitHub

```bash
# Delete the branch from the GitHub repository
git push origin --delete feature/navbar-enhancement
```

---

## Step 5: Remove stale remote-tracking branches

```bash
# Clean up deleted remote branch references
git fetch --prune
```

---

## Step 6: Verify the branch has been deleted

### View local branches

```bash
git branch
```

### View remote branches

```bash
git branch -r
```

### View all branches

```bash
git branch -a
```

---

# All Commands in One Go

```bash
# Switch to main
git checkout main

# Pull the latest changes
git pull origin main

# Delete the local branch
git branch -D feature/navbar-enhancement

# Delete the remote GitHub branch
git push origin --delete feature/navbar-enhancement

# Remove stale remote references
git fetch --prune

# Verify all branches
git branch -a
```

---

# One-Line Command

```bash
git checkout main && git pull origin main && git branch -D feature/navbar-enhancement && git push origin --delete feature/navbar-enhancement && git fetch --prune && git branch -a
```

---

## Replace with Any Branch Name

You can replace:

```text
feature/navbar-enhancement
```

with any branch you want to delete, for example:

```text
feature/deletions
feature/tags
feature/main-enhancements
feature/math-toolkit
feature/raghu-changes
```

---

## Expected Result

- ✅ Branch deleted from your **local repository**.
- ✅ Branch deleted from **GitHub (remote)**.
- ✅ Stale remote references removed.
- ✅ Branch list updated and verified.