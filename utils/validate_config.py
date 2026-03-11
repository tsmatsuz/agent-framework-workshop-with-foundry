"""Configuration validation utilities for the Agent Framework workshop.

This module provides functions to validate environment configuration
before running notebooks, helping catch common setup mistakes early.
"""

import os
import re
from dotenv import load_dotenv


def validate_config(verbose: bool = True) -> bool:
    """Validate environment configuration before running notebooks.
    
    Checks that required environment variables are set and have the correct format.
    
    Args:
        verbose: If True, print detailed status messages.
        
    Returns:
        True if configuration is valid, False otherwise.
        
    Example:
        >>> from utils import validate_config
        >>> if not validate_config():
        ...     raise SystemExit("Please fix configuration before proceeding")
    """
    load_dotenv()
    
    errors = []
    warnings = []
    
    endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT", "")
    model = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "")
    
    # Check endpoint
    if not endpoint or endpoint == "your-project-endpoint":
        errors.append(
            "❌ AZURE_AI_PROJECT_ENDPOINT not configured.\n"
            "   Please set this in your .env file."
        )
    elif "openai.azure.com" in endpoint:
        errors.append(
            "❌ AZURE_AI_PROJECT_ENDPOINT appears to be an Azure OpenAI endpoint.\n"
            "   This is a common mistake - you need the Foundry PROJECT endpoint instead.\n"
            "\n"
            "   ❌ Wrong (Azure OpenAI):  https://xxx.openai.azure.com/...\n"
            "   ✅ Correct (Foundry):     https://xxx.services.ai.azure.com/api/projects/...\n"
            "\n"
            f"   You provided: {endpoint}\n"
            "\n"
            "   To find the correct endpoint:\n"
            "   1. Go to Azure Portal → your Foundry project resource\n"
            "   2. Or open the Microsoft Foundry Portal dashboard\n"
            "   3. Copy the project endpoint from the overview page"
        )
    elif not re.match(r"https://[\w-]+\.services\.ai\.azure\.com/api/projects/[\w-]+", endpoint):
        warnings.append(
            "⚠️  AZURE_AI_PROJECT_ENDPOINT format may be incorrect.\n"
            f"   Expected: https://[FOUNDRY-NAME].services.ai.azure.com/api/projects/[PROJECT-NAME]\n"
            f"   Got: {endpoint}"
        )
    
    # Check model deployment name
    if not model or model == "your-model-deployment-name":
        errors.append(
            "❌ AZURE_AI_MODEL_DEPLOYMENT_NAME not configured.\n"
            "   Please set this to your deployed model name (e.g., gpt-4o, gpt-4.1)"
        )
    
    # Print results
    if verbose:
        if errors:
            print("=" * 60)
            print("Configuration Errors Found")
            print("=" * 60)
            for e in errors:
                print(f"\n{e}")
            print("\n" + "=" * 60)
            
        if warnings:
            print("\nWarnings:")
            for w in warnings:
                print(f"\n{w}")
            print()
                
        if not errors:
            print("✅ Configuration looks valid!")
            print(f"   Endpoint: {endpoint}")
            print(f"   Model: {model}")
    
    return len(errors) == 0


def check_azure_cli_login() -> bool:
    """Check if the user is logged into Azure CLI.
    
    Returns:
        True if logged in, False otherwise.
    """
    import subprocess
    try:
        result = subprocess.run(
            ["az", "account", "show"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("✅ Azure CLI is logged in")
            return True
        else:
            print("❌ Not logged into Azure CLI. Run: az login")
            return False
    except FileNotFoundError:
        print("❌ Azure CLI not found. Please install it first.")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Azure CLI check timed out")
        return False


if __name__ == "__main__":
    # Allow running as a script for quick validation
    import sys
    if not validate_config():
        sys.exit(1)
    check_azure_cli_login()
