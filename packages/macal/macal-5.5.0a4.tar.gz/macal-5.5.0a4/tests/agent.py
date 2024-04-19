from macal.macal import Macal  # type: ignore
import json
from dotenv import load_dotenv
import os
import sys

sys.path.append("./meraki_scripts")


def main() -> None:
    load_dotenv("./meraki_scripts/.env")
    search_paths = ["./lib", "./meraki_scripts"]
    macal = Macal(search_paths=search_paths)

    with open("./meraki_scripts/meraki_api_agent_configuration.json") as f:
        config = json.load(f)

    macal.RegisterConstant("configuration", config)
    macal.RegisterVariable("api_key", os.getenv("api_key"))
    macal.RegisterVariable("org_name", os.getenv("org_name"))
    macal.RegisterVariable("host_name", os.getenv("host_name"))
    macal.RegisterVariable("agent_version", "Meraki API Agent v10.1.0")
    macal.RegisterVariable("org_id", None)
    print()
    print("Running Meraki API Agent v10.1.0, please wait...")
    print()
    macal.Run("./meraki_scripts/meraki_v11.mcl")
    print()
    print("Meraki API Agent v10.1.0 has completed successfully.")
    print()


if __name__ == "__main__":
    main()
