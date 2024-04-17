from macal.macal import Macal
import json
from dotenv import load_dotenv
import os
import sys

sys.path.append("./meraki_scripts")


def main() -> None:
    load_dotenv("./meraki_scripts/.env")
    macal = Macal("./meraki_scripts/meraki_v11.mcl")
    macal.add_path("./lib")
    macal.add_path("./meraki_scripts")

    with open("./meraki_scripts/meraki_api_agent_configuration.json") as f:
        config = json.load(f)

    macal.add_const("configuration", config)
    macal.add_variable("api_key", os.getenv("api_key"))
    macal.add_variable("org_name", os.getenv("org_name"))
    macal.add_variable("host_name", os.getenv("host_name"))
    macal.add_variable("agent_version", "Meraki API Agent v10.1.0")
    macal.add_variable("org_id", None)
    print()
    print("Running Meraki API Agent v10.1.0, please wait...")
    print()
    macal.Run()
    print()
    print("Meraki API Agent v10.1.0 has completed successfully.")
    print()


if __name__ == "__main__":
    main()
