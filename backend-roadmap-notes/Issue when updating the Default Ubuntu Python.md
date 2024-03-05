I had experienced recently an issue updating my alternatives for Python3 on my Pop OS! 

I ideally wanted to use python3.12.x as my default python, so I followed a tutorial on which they suggested to do the following

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
```

While this in theory makes things easy as the latest python will now be the default Python. It can cause APT to fail.

After doing that I then in the next day logged into my computer and tried to do the regular `sudo apt update` and then faced the error:

```bash
Hit:10 http://apt.pop-os.org/ubuntu jammy-backports InRelease
Traceback (most recent call last):
  File "/usr/lib/cnf-update-db", line 3, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
Reading package lists... Done
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code
```

Doing some search on the internet I found [this response](https://askubuntu.com/a/1374345) in one Ubuntu forum:

"APT (and many other components of Ubuntu) requires a certain version of python to function properly."

