# lazyvpn
https://zillowgroup.atlassian.net/wiki/spaces/AT/pages/181960338/LazyVPN

## Prerequisites
Python 3.6+

Follow this [wiki](https://zillowgroup.atlassian.net/wiki/spaces/ZillowOps/pages/175444125/Instructions+for+using+Okta+verify+to+connect+to+AnyConnect+VPN) to install **AnyConnect VPN** and 
this [wiki](https://zillowgroup.atlassian.net/wiki/spaces/ZillowOps/pages/329875529/Service+Desk+-+MFA+-+Setting+up+Okta+Verify+SOP) to set up **Okta Verify Push**

## Installation
This is a Python 3 project.

Install/Upgrade from PyPi:
```
pip3 install --upgrade lazyvpn/lazyvpn2
```

## Configuration
To set up or update the configuration for a password change run:
```
lazyvpn -c
```
OR
```
lazyvpn --configure
```

## Connect to VPN
```
lazyvpn -u
```
OR
```
lazyvpn --up
```
## Disconnect from VPN
```
lazyvpn -d
```
OR
```
lazyvpn --down
```
## Reconnect to VPN
```
lazyvpn -ud
```