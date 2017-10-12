## W1m Vaisala TNG weather proxy daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/tngd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/tngd)

Part of the observatory software for the Warwick one-meter telescope.

`tngd` is a Pyro frontend that proxies queries to the TNG weather API.

`tng` is a commandline utility that shows the current weather status.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-tng-server`, the `tngd` must be enabled using:
```
sudo systemctl enable tngd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start tngd.service
```
