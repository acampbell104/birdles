# birdbath-ai

A Raspberry Pi-based bird feeder camera with motion capture, local AI classification, labelling, and Telegram alerts.

## Features
- Motion-triggered photo capture
- Local classification (MobileNet)
- Web UI for manual labelling
- Auto-retraining every 4 days
- Telegram notifications + reply-to-label

## Setup
Run:
```bash
chmod +x install.sh
./install.sh
source venv/bin/activate
python bird_server.py
```

## Autostart
Add to crontab:
```
@reboot /home/pi/birdbath-ai/venv/bin/python /home/pi/birdbath-ai/bird_server.py &
```
