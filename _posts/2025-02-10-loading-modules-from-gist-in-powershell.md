---
date: 2025-02-11 01:00:27
layout: post
title: "Loading Modules from Gist in PowerShell"
subtitle: Load a module from a Gist in PowerShell
description: Learn how to load a module from a Gist (or URLs) in PowerShell.
image:
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1739526405/dmbuil-github-pages/robot-1.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1739526405/dmbuil-github-pages/robot-1.jpg
category: tricks
tags: powershell
author: dmbuil
paginate: false
---

In this post, I'll show you how to load a module from a Gist in PowerShell. This technique is particularly useful when you want to test a module or function quickly or just let someone else test your module without having to publish it to the PowerShell Gallery.

## Preparation

PowerShell does not have a built-in cmdlet to download and import modules from external URLs. 
However, you can achieve this by using the Module **importfromURL**, which is available in the [PowerShell Gallery](https://www.powershellgallery.com/packages/importfromURL/1.1.5).

The installation is pretty straightforward, as long as you have the PowerShell Gallery as a valid source of modules[^1]. You can install the module by running the following command:

```powershell
Install-Module -Name importfromURL
```

## Loading a Module from a Gist

Once you have the **importfromURL** module installed, you can load a module from a Gist by running the following command:

```powershell
Import-FromURL -URL "https://gist.github.com/path/to/your/gist"
```

For instance, if you want to load this nice function that I've created:

```powershell
Import-FromURL -URL "https://gist.github.com/dmbuil/" -Ps1
```

The switch `-Ps1` is used to specify that the module is a PowerShell script file. If you are loading a full module, you would use the `-Psm1` switch instead. Or even `-DLL`, if you are loading a DLL.

## But wait, is it safe?

You might be wondering if it's safe to load modules from external URLs, or even if the **Import-FromURL** module is safe.  
The latter is easy: the module is open-source, so you can check the code yourself[^2]. As for loading modules from external URLs, well, the answer is: it depends.

Obviously, you should only load modules from sources you **actually** trust. If you are loading a module from a Gist or any other source, not only you must trust the author, but the content itself. There was a [_nice debate_ on Reddit](https://www.reddit.com/r/pihole/comments/7n8nm8/our_code_is_completely_open_but_piping_to_bash/) on that subject about this convenient way to install software, this case about PiHole's single-line installer.

_Hope this helps!_

---

[^1]: If you don't have the PowerShell Gallery as a valid source of modules... Brace yourselve! (tbd)
[^2]: Most of the modules published in the PowerShell Gallery open-source, and you can check them before running them. You would only extend the **File List** section and click on the file. For instance [Import-FromURL Source Code](https://www.powershellgallery.com/packages/importfromURL/1.1.5/Content/importfromURL.psm1).
