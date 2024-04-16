import subprocess
import sys

import requests


class DiscordIntegration:
    def __init__(self, discord_webhook: str):
        self.headers = {"Content-Type": "application/json"}
        self.webhook = discord_webhook

    def send_message_to_discord(self, temp: str):
        message = f"@here Raspberry is at {temp} degrees!!!"
        try:
            r = requests.post(self.webhook, headers=self.headers, json={"content": message})
            r.raise_for_status()
        except Exception:
            print("An error has occurred while calling Discord")


class CPUInfo:
    @staticmethod
    def get_cpu_temperature() -> float:
        """
        Temp is received as: temp=47.6'C
        :return: Given temp as float
        """
        cmd = "vcgencmd measure_temp"
        ret = subprocess.check_output(cmd.split()).decode("utf-8")
        r = ret.split("=")
        temp = float(r[1].split("'")[0])
        return temp


def main():
    print("starting")
    # We receive our input
    input_webhook = sys.argv[1]
    threshold_temp = float(sys.argv[2])

    # We start our classes
    discord_integration = DiscordIntegration(discord_webhook=input_webhook)
    cpu_info = CPUInfo()

    # Logic
    current_temp = cpu_info.get_cpu_temperature()
    if current_temp > threshold_temp:
        discord_integration.send_message_to_discord(str(current_temp))
    print("finished")
