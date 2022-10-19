---
date: 2022-10-18 18:59:16
layout: post
title: "Auto-Profiles with iTerm2"
subtitle: Using Profile triggers to switch when SSH'ing
description:
image:
optimized_image:
category: tutorial
tags:
 - iTerm2
 - ssh
 - automatization
author: dmbuil
paginate: false
---

My favourite terminal is, without heasitation, [iTerm2](https://iterm2.com/index.html).
Everytime I've switched to a new macOS, one of the first steps is always installing it. Right away.

Not only that the personalisation it offers is a delight, but also, the automatisation features to make your terminal experience a lot smoother.

I could jump in with all of those, but today I'd like to talk about one of the latest I've playing with: **Profile Triggers.**

But first, you must understand the meaning of the word **Profile**.

## iTerm2 Profiles: a dress for every ocasion

A **profile** on iTerm2 is a set of features that are packed up altogether, so you can easily switch to another one easily.

![image](https://res.cloudinary.com/dguibifnv/image/upload/v1666128098/dmbuil-github-pages/iterm2-profiles_hmnmey.png)
<figcaption id="fig1"> Figure 1. Profile section </figcaption>

You always begin with the _Default_ profile (seems legit), and as you can see on [Figure 1](#fig1), which contains pre-configured features such as the terminal's colours and fonts, cursor types, bells, etc.

Let's say you want to display a big red warning when going `su -`. You can do that: a nice 

You can set up a shortcut to switch to a specific profile. Alright. But what if the change 
Moreover, what if you could open a specific SSH session to a Server when switching to a profile?

## Make iTerm2 work for you

