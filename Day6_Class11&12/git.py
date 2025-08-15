# Git: Most Important Points (with Commands)
# Core Concepts

# Git → Tracks changes in your code (version control).

# Local repo → On your computer.

# Remote repo → Hosted online (GitHub, GitLab).

# Commit → Snapshot of changes; creates commit ID.

# Head → Pointer to latest commit.

# Branch → Parallel version of project (feature/dev branch).

# Stage / Index → Area to prepare changes before committing.

# Essential Commands

# Repository Setup & Cloning

# git init                   # Initialize a local repository
# git clone <url>            # Copy remote repo to local


# Tracking & Saving Changes

# git status                 # See changed/untracked files
# git add <file>             # Stage file for commit
# git add .                  # Stage all files
# git commit -m "message"    # Commit staged changes


# Viewing History & Changes

# git log                    # Show all commits
# git show HEAD              # Show latest commit details
# git diff                    # Show unstaged changes
# git diff --staged           # Show staged changes


# Branching & Merging

# git branch                 # List local branches
# git branch <name>          # Create new branch
# git checkout <branch>      # Switch branch
# git merge <branch>         # Merge branch into current
# git branch -d <branch>     # Delete branch


# Remote Repo Commands

# git remote add origin <url>   # Link local repo to GitHub
# git push -u origin main       # Push commits to remote
# git pull origin main          # Pull remote changes


# Navigating Commits

# git checkout <commit_id>      # Go to specific commit

# Key Best Practices

# Commit often with clear messages.

# Work in branches for new features or fixes.

# Always pull before pushing.

# Keep main branch stable.

# Stage only what you want to commit.