 🔁 RepoFusion: Merge Multiple GitHub Repos into One Super Repo

Automate the consolidation of multiple GitHub repositories into a single, organized monorepo using PowerShell and GitHub CLI. Ideal for grouping related projects — like coding utilities, cheat sheets, or microtools — into one place.

 🚀 Features

 ✅ Automatically creates a new GitHub repository
 ✅ Clones and organizes multiple existing repos into subfolders
 ✅ Cleans up temp files and handles all file movements
 ✅ Commits and pushes the final structure — all automated

 📦 Use Case Example

You have two utility projects:

├── Windows-Privilege-Escalation/
├── Linux-privilege-escalation/
├── RedTeamSQLServerCheatSheet/
├── VOIP-Red-Team/
└── Complete-AD-Red-Team-Cheatsheet/

This script combines them under a new repository called "red-team-cheat-sheets", each in its own folder.

 🧰 Prerequisites

 [Git](https://git-scm.com/)
 [GitHub CLI ("gh")](https://cli.github.com/)
  Authenticate with "gh auth login"
 PowerShell 5.1+ (or PowerShell Core)



 📝 How to Use

1. Clone this repo or copy the script file locally.
2. Open PowerShell and run:

"""powershell
.\import-cheat-sheets.ps1
"""

> ✏️ Modify the "$NewRepo", "$GitHubUser", and "$Repos" variables in the script to fit your case.



 🧪 Sample Script Configuration

"""powershell
$NewRepo = "random-coding"
$GitHubUser = "deep1792"
$Repos = @(
    "youtube-playlist-download",
    "python-give-away"
)
"""

 ✅ Output

A new GitHub repo like this:

"""
red-team-cheat-sheets/
├── Windows-Privilege-Escalation/
├── Linux-privilege-escalation/
├── RedTeamSQLServerCheatSheet/
├── VOIP-Red-Team/
└── Complete-AD-Red-Team-Cheatsheet/

"""

Everything committed and pushed to GitHub automatically.

 🤝 License

MIT — feel free to use and modify.

