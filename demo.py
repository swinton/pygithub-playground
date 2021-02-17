import os
import base64

from github import GithubIntegration

# Get the App
id = int(os.getenv("GITHUB_APP_ID"))
private_key = base64.b64decode(os.getenv("GITHUB_APP_PRIVATE_KEY"))
app = GithubIntegration(id, private_key)

# Get the installation
owner = os.getenv("GITHUB_OWNER")
repo = os.getenv("GITHUB_REPO")
installation = app.get_installation(owner, repo)

# Get an installation access token
tok = app.get_access_token(installation.id)

# Print the token to STDOUT
print(tok.token)
