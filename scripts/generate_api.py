# /// script
# dependencies = ["openapi-python-client>=0.28.0"]
# ///
#
# run script with: `uv run scripts/generate_api.py`
#
import subprocess
import shutil
import os
import pathlib

# Define the target library directory inside your workspace
SURE_VERSION = "0.7.2"
WORKSPACE_ROOT = pathlib.Path(__file__).parent.parent
LIB_PATH = WORKSPACE_ROOT / "libs" / "sure-api-client"
CONFIG_PATH = WORKSPACE_ROOT / "scripts" / "generate_api_config.yaml"


print("🚀 Generating OpenAPI client with native uv metadata...")
# generate YAML config for openapi-python-client
config_yaml_content = f"""
# project_name_override: "sure_api_client"
# package_name_override: "sure_api_client"
package_version_override: "{SURE_VERSION}"
# literal_enums: true
"""
with open(CONFIG_PATH, "w") as config_file:
    config_file.write(config_yaml_content)


# Clean the old directory entirely to prevent stale file conflicts
if os.path.exists(LIB_PATH):
    shutil.rmtree(LIB_PATH)


# Run openapi-python-client generator with the specified configuration
subprocess.run(
    [
        "openapi-python-client",
        "generate",
        "--url",
        f"https://raw.githubusercontent.com/we-promise/sure/refs/tags/v{SURE_VERSION}/docs/api/openapi.yaml",
        "--meta",
        "uv",
        "--config",
        str(CONFIG_PATH),
        "--output-path",
        str(LIB_PATH),
        "--overwrite",
    ],
    check=True,
)


print("🔄 Syncing workspace environments...")
subprocess.run(["uv", "sync"], check=True)


print("✅ Generation and workspace sync complete!")
