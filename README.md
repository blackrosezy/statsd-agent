statsd-agent
============

Statsd client to monitor CPU, Memory, Disk and Network

Quickstart
============

## Installation (Ubuntu)
First, download both *statsd-agent.py* and *statsd-agent.conf*. Create a directory `/opt/statsd-agent` and place *statsd-agent.py* in it. Place the Upstart configuration file *statsd-agent.conf* in `/etc/init/`. The statsd-agent.py will automatically start as service on system startup or you can manually start it using the following command:
```
service statsd-agent start
```

## Installation (Other Linux/Windows/Mac)
stasd-agent.py is really just a single python file. You can run it directly using python command:
```
python statsd-agent.py
```
You can use any daemon tools to make it run as service/background. One of an example is [Supervisor](http://supervisord.org/).

## Running/Stopping (Ubuntu)
Use upstart command to run/stop statsd-agent:
```
service statsd-agent start
service statsd-agent stop
service statsd-agent restart
service statsd-agent status
```
More info about Ubuntu Upstart can be found at http://askubuntu.com/questions/19320/how-to-enable-or-disable-services

License
============

    The MIT License (MIT)
    
    Copyright (c) 2013 Mohd Rozi
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
