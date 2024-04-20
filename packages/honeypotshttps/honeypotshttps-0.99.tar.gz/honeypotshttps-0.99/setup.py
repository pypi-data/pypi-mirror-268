
from setuptools import setup, find_packages

setup(
    name="honeypotss",
    version="0.99",
    author="John",
    author_email="john12@gmail.com",
    description="30 different honeypots in one package! (dhcp, dns, elastic, ftp, http proxy, https proxy, http, https, imap, ipp, irc, ldap, memcache, mssql, mysql, ntp, oracle, pjl, pop3, postgres, rdp, redis, sip, smb, smtp, snmp, socks5, ssh, telnet, vnc)",
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/john10909/honeypots",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "twisted==21.7.0",
        "psutil==5.9.0",
        "psycopg2-binary==2.9.3",
        "pycryptodome==3.19.0",
        "requests==2.28.2",
        "requests[socks]==2.28.2",
        "impacket==0.9.24",
        "paramiko==3.1.0",
        "scapy==2.4.5",
        "service_identity==21.1.0",
        "netifaces==0.11.0",
        "dnspython==2.4.2",  # This could be moved to dev dependencies if not required for basic installation
        "elasticsearch",
        "ldap3",
        "mysql-connector",
        "pymssql",
        "pysnmplib",
        "redis",
        "vncdotool"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pre-commit"
        ]
    }
)
