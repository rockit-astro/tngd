## W1m Vaisala TNG weather proxy daemon

`tngd` is a Pyro frontend that proxies queries seeing, brightness, and dust concentration from the TNG weather API.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-tng-server`, the `tngd` must be enabled using:
```
sudo systemctl enable tngd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start tngd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9011/tcp --permanent
sudo firewall-cmd --reload
```
