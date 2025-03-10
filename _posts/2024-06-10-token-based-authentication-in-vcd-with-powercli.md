---
date: 2024-06-10 23:00:51
layout: post
title: "Token-based Authentication in VCD with PowerCLI"
subtitle: Authenticate with an Access Token in VMware Cloud Director
description: When username and password are not an option.
image: 
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1739229957/dmbuil-github-pages/connectv2.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1739229957/dmbuil-github-pages/connectv2.jpg
category: snippets
tags:
 - powershell
 - vmware
 - scripting
author: dmbuil
paginate: false
---

For all of those who use PowerCLI to automate tasks in VMware Cloud Director (VCD), you may have noticed that the `Connect-CIServer` cmdlet does not support token-based authentication. Even in most recent versions ([PowerCLI 13.3](https://developer.broadcom.com/tools/vmware-powercli/latest/)), the only way to authenticate is by providing a username and password[^1].

This ~~can be~~ **is** a bit of a nuisance, especially when you want to do some sripting or automate tasks in a CI/CD pipeline.

To overcome this limitation, I created a simple function that allows you to authenticate using a token. It is a mere _wrapper_ of the original `Connect-CIServer` cmdlet, but adds the ability to hydrate a session with an Access Token.

## The Token

In order to use it, first you need to have a valid Access Token.

1. Log in to your VCD instance.
2. Go to your profile settings.
3. Under the **API Tokens** section, click on <kbd>Generate Token</kbd>.
4. Copy the token and save it in a secure place.

Keep it safe and warm. It is your key to the kingdom.

## The Function

Then, copy the following function to your script or PowerShell profile:

<script src="https://gist.github.com/dmbuil/397a2dd7b429b93d74151a2ff687a219.js"></script>

## The Miracle

Now _we can set Cerberus free_ and use the `Connect-CIServerV2` function to authenticate with the Access Token, like this:

```powershell
Connect-CIServerV2 -Server "vcd.example.com" -Org "MyOrg" -AccessToken "your_access_token"
```

This function will create a session with the VCD instance and store it in the `$global:DefaultCIServers` variable, so you can use it in subsequent cmdlets.

I could have added the typical `begin{}`, `process{}`, and `end{}` PowerShell blocks to the function, but I wanted to keep it as simple as possible. Feel free to enhance it as you see fit.

_Hope this helps!_

---

[^1]: You may check the official documentation for the `Connect-CIServer` cmdlet [here](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.cloud/commands/connect-ciserver).
