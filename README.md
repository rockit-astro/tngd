## TNG weather proxy daemon

`tngd` is a Pyro frontend that proxies queries seeing, brightness, and dust concentration from the TNG weather API.

### Software setup
After installing the package, the systemd service should be enabled:
```
sudo systemctl enable --now tngd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9011/tcp --permanent
sudo firewall-cmd --reload
```
