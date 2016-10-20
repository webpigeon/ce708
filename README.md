# ce708
Computer security module examples

# Automated Auditing tools
Here are some examples of automated tools which can be used for auditing.

## For system configuration
* [Lynis](https://cisofy.com/lynis/)
* [OpenVAS](http://www.openvas.org/)
* [Nessus](https://www.tenable.com/products/nessus-vulnerability-scanner) (commercial)

## For source code
* [Sonarqube](http://www.sonarqube.org/) [My sonar server](https://sonar.fossgalaxy.com/)
* [findbugs](http://findbugs.sourceforge.net/)

# files in this repo
* linux_perimissions.md - (Example file in ```/home/alice``` inside the VM) - explains some basics about linux file permissions

# OVA image
An ova image is a virtual machine image that is designed to run inside a hypervisor (like virtualbox).
In order to use it on your home machine, you can download the OVA file from [here](http://stuff.webpigeon.me.uk/ce708).

If you are in the lab, you should **NOT** download this file directly, instead use the setup-ova.sh script which will download it
into temporary storage (/tmp/).

This will let you use linux commands in bash, change permissions and see the effects.

## Technical details
For those of you intrested in the machine setup:

* The virtual machine is a [Debian](https://www.debian.org/) Jessie image, initially setup with 1GB of ram.
* It has no desktop envrioment installed (is command line only).
* It has an ssh server running
* It has been configured with two network interfaces (eth0 and eth1)

## User accounts
The user accounts are:

| username | password   | groups           |
| -------- | ---------- | ---------------- |
| root     | password42 | root             |
| alice    | password42 | alice, csee      |
| bob      | password42 | bob, csee        |
| eve      | password42 | eve              |


