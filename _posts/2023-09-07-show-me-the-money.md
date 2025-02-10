---
date: 2023-09-07 20:46:40
layout: post
title: "Show me the money"
subtitle: Copy files between Windows servers with no hassle
description: Learn how to copy files between Windows servers with no hassle using a simple trick.
image: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1739215034/dmbuil-github-pages/money-1.jpg
optimized_image: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1739215034/dmbuil-github-pages/money-1.jpg
category: tricks
tags: 
 - windows
author: dmbuil
paginate: false
---

Today I will bring a short but handy post that many people may find useful.

Sysadmin that have to deal with a _somewhat big_ environments, must know all the neats and tricks to make their lives better. Transferring files in such environments is one of those.

# The easiest

Whenever you connect to a Windows server with RDP (_Remote Desktop Protocol_), you can safely transfer files between the client (source) machine and server (destination). The file transfer is encrypted the same way that the RDP session itself, through TCP Port 3389. 

But this method will only allow you to copy a [2GB file](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/copying-2-gb-file-by-clipboard-redirection-fails). _Ups._ 

Funny thing, last time I tried this, my RDP client did not warn me about the size limitation. It will leave you suffer, while the agonising bitrate vanishes slowly, until the transfer is no more.

# The most complete

There are several alternatives that I can think of right now:

 - `xcopy` files.
 - Drive Redirection through RDP.
 - Share and mount any destination machine's folder.

But all of those require additional steps (ad-hoc permissions), have complex syntax (never been able to recall whether `xcopy` paths' order is `src dst` or `dst src`) or may leave _rubbish_ behind.

And here comes the _magic_.

# Show me the _money_

Or at least, use the `$`.

Follow with me:

 - Open a **File Explorer** window.
 - Go to the navigation bar.
 - Type the following, replacing `{destination-ip}` with destination server IP and `{destination-drive}` with the Drive letter you want to access to:  

```
\\{destination-ip}\{destination-drive}$\some\path
```
 - Enter some local or domain credentials.
 - Voilà.

> **Example**  
> To access `C:\` drive on a destination server with IP `192.168.1.23`, you would do:  
> `\\192.168.1.23\c$\my\cool\destination`
{: .prompt-info }

You are accessing a remote drive path with no need of previous mount. 
And the best part, once you close the File Explorer Window, it will be gone.

For this to work, you will need TCP Port 445, as this is a network copy through SMB.
But other than that, it's done.

Hope it helps.