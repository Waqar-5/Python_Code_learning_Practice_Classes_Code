# GitHub: Key Points for Developers

# 1. What GitHub Is
# GitHub is a remote hosting platform for Git repositories.


# Allows collaboration, version tracking, and project management.


# Works with Git commands to sync local and remote repos.




# 2. Core Concepts
# Term	Meaning
# Repository (Repo)	A project folder containing code and history, stored on GitHub.
# Fork	Copy of someone else’s repo to your account to work independently.
# Clone	Copy a repo from GitHub to your local machine (git clone <url>).
# Pull Request (PR)	Propose changes from your branch/fork to be merged into the original repo.
# Issues	Track bugs, features, or tasks inside a repo.
# Actions / CI-CD	Automate testing, deployment, or workflows using GitHub’s built-in pipelines.
# Branches	Separate lines of development inside a repo (feature, bugfix).
# Stars / Watch / Fork	Star → bookmark repo, Watch → get notifications, Fork → copy repo.


# 3. Workflow with GitHub
# Create a repo on GitHub.

# Clone it locally: git clone <url>

# Make changes → stage: git add . → commit: git commit -m "message"

# Push changes to GitHub: git push origin main

# Collaborate using branches and pull requests.

# Pull updates from GitHub before making changes: git pull origin main



# 4. Collaboration Features

# Pull Requests (PRs) → review, discuss, and merge code.

# Code Reviews → comment on PRs to maintain code quality.

# Protected Branches → prevent direct pushes to important branches (like main).

# Teams & Permissions → control who can read, write, or admin repos.




# 5. Best Practices

# Keep main branch stable, use feature branches.

# Write clear PR titles and commit messages.

# Use issues to track bugs or features.

# Sync regularly: git pull before git push.

# Document repo with a README.md.

# ✅ Key takeaway: GitHub is the remote collaboration and hosting platform, while Git provides the commands and version control system to interact with it.