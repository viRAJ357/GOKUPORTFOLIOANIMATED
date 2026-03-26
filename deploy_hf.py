import os
from huggingface_hub import HfApi

token = os.environ.get("HF_TOKEN", "")
api = HfApi(token=token)
repo_id = "viraj-421/PortfolioGoku"

print(f"Creating or checking space {repo_id}...")
api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="static", exist_ok=True)

print("Uploading dist folder...")
api.upload_folder(
    folder_path="app/dist",
    repo_id=repo_id,
    repo_type="space"
)
print(f"Deployed successfully to https://huggingface.co/spaces/{repo_id}")
