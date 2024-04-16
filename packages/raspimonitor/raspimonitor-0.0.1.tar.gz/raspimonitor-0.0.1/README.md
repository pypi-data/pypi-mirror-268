# raspimonitor

Monitoring and alerting to your Discord server for your RaspberryPi

## Installation

You will need to set up a Discord server and webhook, see
how [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
After that, proceed to install the package in your raspberry:

```bash
pip3 install raspimonitor
```

## Usage

### Direct usage

```bash
# raspimonitor YOURHOOKHERE THRESHOLD_TEMP_IN_CELSIUS
# Example
raspimonitor http://your.web.hook.here 45
# Example temp as float:
raspimonitor http://your.web.hook.here 45.6
```

### As a cron job

Add your cron job as a script from above:

```bash
# 1. Open cron file
crontab -e
# 2. Add a cron
# Example - run every minute:
* * * * * raspimonitor http://your.web.hook.here 45
# Example - run every 5 minutes
*/5 * * * * raspimonitor http://your.web.hook.here 45
# 3. Reload cron service
sudo service cron reload
```

Ref. https://superuser.com/questions/232144/how-to-stop-a-currently-running-cron-job

## Contributing

Pull requests and issues are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/) - [License file](LICENSE)

## Obtained inspiration from

- https://github.com/git-ogawa/raspi-statmon/blob/main/src/rstatmon/statdata.py
- https://github.com/mityax/rpi-temperature-alert/tree/master
- https://www.howtogeek.com/discord-slack-alert-raspberry-pi-too-hot/
