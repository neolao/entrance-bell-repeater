Entrance bell repeater
======================

![Sketch](./sketch.png)

Installation
------------

```bash
sudo ln -s $(pwd)/buzzer.service /etc/systemd/system/buzzer.service
sudo systemctl enable buzzer.service
```
