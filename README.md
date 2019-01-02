# HeadUnit Desktop

[![Gitter chat](https://badges.gitter.im/viktorgino/headunit-desktop.png)](https://gitter.im/headunit-desktop)


HeadUnit Desktop is a Qt based free and open source software that is intended to be run on computers built into cars. This software is currently under active development and lot of the features are experimental. As of now there are two main features: 

 - Media player with a media library and media scanner
 - Android Auto™ client
 - DAB radio

Proposed features:

 - FM Radio
 - CAN bus sniffer (depending on how much control different modules of the car allow and how much information, such as A/C steering wheel controls, different gauges and sensor data) with a customizable profile for each car.

The GUI for some of the proposed features is already there. For screenshots of the current state of the GUI [go to the screenshots page.](http://headunit.viktorgino.me/SCREENSHOTS)

Getting started
-------------------
Download the Raspberry Pi image which is based on Raspbian Stretch Lite from here: http://files.headunit.viktorgino.me/index.html
The Pi image has all the prerequesit libraries included and a fully built headunit-desktop with wellei.io included.
The login details are the Raspbian defaults:

> Username: pi

> Password: raspberry

You can run it with the following command:

    sudo xinit /opt/headunit-desktop/headunit-app
    
If you'd like to run it without X11 using OpenGL change the content of /etc/environment to:

    QT_QPA_PLATFORM=eglfs
    
And run it without sudo:

    /opt/headunit-desktop/headunit-app

-------------------

For building your own Raspbian images see: [viktorgino/pi-gen](https://github.com/viktorgino/pi-gen)

There aren't any packages available for other platforms, but it is in the making.

For more details and install instructions see: [headunit.viktorgino.me/](http://headunit.viktorgino.me/)

-------------------

If you like this project and would like to support me, then buy me a beer or something [here](http://amzn.eu/3FbYXDC)



qtconnectivity-dev
libcanberra
libgconf2-dev
