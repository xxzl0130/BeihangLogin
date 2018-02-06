# BeihangLogin

```上网不涉密，涉密不上网！```

## The Original Project: ```login.sh```

Hey mate, are you from BUAA? Me<sub>2</sub> , and maybe this script will help.

This script requires ```bash```, ```base64``` and ```curl``` installed.

If you want to login automatically when the openwrt/lede router boots, add the command to ```/overlay/upper/etc/rc.local```:

```bash

<some_dir>/login.sh login
exit 0

```

### Usage

#### login：

```./login.sh login```

#### logout：

```./login.sh logout```

## Python 3 Transcription

Requirements: ```requests```
