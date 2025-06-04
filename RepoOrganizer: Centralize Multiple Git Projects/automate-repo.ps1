# Variables
$NewRepo = ""   #name of new repo. Change to your own specialized name
$GitHubUser = ""  #add your github username
$Repos = @(
    "Repo1",
    "Repo2",
    "Repo3",
    "Repo4",
)      #add your repositories names
$BaseUrl = "https://github.com/$GitHubUser"

# Create new GitHub repo
Write-Host "Creating new GitHub repository: $NewRepo"
gh repo create "$GitHubUser/$NewRepo" --public --confirm

# Clone new repo locally
Write-Host "Cloning new repo locally..."
git clone "$BaseUrl/$NewRepo.git"
Set-Location $NewRepo

# Loop through each repo and import files
foreach ($repo in $Repos) {
    Write-Host "Processing $repo ..."
    # Clone repo into temp folder
    git clone "$BaseUrl/$repo.git" temp_repo

    # Create subfolder for repo
    New-Item -ItemType Directory -Name $repo -Force | Out-Null

    # Move all files and hidden files except .git to subfolder
    Get-ChildItem -Path temp_repo -Force | Where-Object { $_.Name -ne ".git" } | ForEach-Object {
        Move-Item -Path $_.FullName -Destination $repo
    }

    # Remove temp folder
    Remove-Item -Recurse -Force temp_repo
}

# Commit and push
git add .
git commit -m "Import repos into subfolders"
git push origin main

Write-Host "All done! Repository '$NewRepo' is ready."
