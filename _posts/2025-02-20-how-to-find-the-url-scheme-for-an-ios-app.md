---
date: 2025-03-10 17:00:00
layout: post
title: "How to find the URL Scheme for an iOS App"
subtitle: "Quick guide to find the URL Scheme for an iOS App"
description: |
  A quick guide to find the URL Scheme for an iOS App and other reverse 
  engineering tricks
image:
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741624762/dmbuil-github-pages/url-scheme.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1741624762/dmbuil-github-pages/url-scheme.jpg
category: 
tags:
- ios
- reverse-engineering
- home-assistant
author: dmbuil
paginate: false
---

I recently purchased a [Home Assistant Green](https://www.home-assistant.io/green/)
and I am migrating many old automations and workflows into it. And also playing
around with the new features of HA. It had been a while since the last time.

One of the things I wanted to do was not to cause any friction in my daily routines.
For instance, minimising the number of taps to get to the information I need.
Lazy me, I know.

So, when I found out that the HA app had added [Actionable Notifications](https://companion.home-assistant.io/docs/notifications/actionable-notifications/), I was excited. But _all that glitters is not gold_.
And this is where my adventure began.

## X marks the spot

In order for **Actionable Notifications** to work, you need to know _what you_
_actually are going to do_. As obvious as it sounds, it is not always clear.

For the sake of my mental health, I decided to keep things simple: when a HA
notification pops up, I want to be able to tap on an action and be taken
directly to somewhere else, the Ajax app in this case.

And for the HA notification to be actionable, I need to know the notification's
[target URI](https://companion.home-assistant.io/docs/notifications/actionable-notifications/#building-actionable-notifications)
to open the Ajax app. Its **URL Scheme**. This is where the fun begins.

## What is a URL Scheme?

A **URL scheme**[^1] is a way to communicate with an app by using a URL. You can
use a URL scheme to open an app, pass data to an app, or perform other actions
within an app.

This comes in handy when you want to create a shortcut on your phone to open an
app straight away. The mythical _Open in ..._.

An App's URL Scheme is defined by the developer. Not all apps have a URL Scheme
and **not all URL Schemes are public**.

An app's URL Scheme is usually in the format `appname://` (small caps).
For example:

- **Twitter/X**: `twitter://`
- **Home Assistant**: `homeassistant://`

## But why the fuss?

Some apps have a public URL Scheme that you can find in the app's documentation,
such as the OS Official Apps. But **not all apps** have a public URL Scheme.

You may reach the developer to ask for it. Or maybe start guessing. Or maybe pay
for some reverse engineering tools.
But if you are a member of the _Clenched-Fist Guild_[^2] as I am, this will not
sound any good.

So, let's do it the hard way.

Well, not that hard. After some _googling_ I found these post
([1](https://stackoverflow.com/questions/52318063/find-the-url-scheme-of-an-app-on-my-iphone),
[2](https://stackoverflow.com/questions/37950962/url-schemes-to-personal-apps))
in **StackOverflow**.
Which states an alternative way, yet not so... _elegant_. But will work:

 1. Download and Install [Apple Configurator 2](https://apps.apple.com/us/app/apple-configurator-2/id1037126344).
 2. Connect your iPhone to your computer. Make sure that the App you want to get
    its URL Scheme for is installed.
 3. Open Apple Configurator 2. Your iPhone should appear in the list of devices.
    Front page.
 4. Then, right-click on it and press <kbd>Add</kbd>. A new window will appear.

    ![Download App 1](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741625240/dmbuil-github-pages/download-ajax-1.png)

 5. Select the App you want to get the URL Scheme for, and click again on
    <kbd>Add</kbd> (You can use the search bar to find it).

    ![Download App 2](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741625309/dmbuil-github-pages/download-ajax-2.png)

 6. A download will start. Once it finishes, I will most probably state that the
    App is already installed on your device. Do not worry, but **do not close**
    the window.

    ![Do not Replace](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741625345/dmbuil-github-pages/do-not-replace.png){: w="300" h="400" }

 7. Open a terminal and type:

    ```bash
    cd ~/Library/Group Containers/K36BKF7T3D.group.com.apple.configurator/Library/Caches/Assets/TemporaryItems/MobileApps/
    open .
    ```

    > The path is where the `.ipa` file is downloaded. The `open .` command will
    > open a Finder window with the content of the folder.
    {: .prompt-tip }

 8. You will see a new `.ipa`[^3] file.
 9.  Copy the `.ipa` file anywhere you want. Now you can close the popup window
    from step 6.
 10. Now you must access the content of the `.ipa` container. You can:
     1. Change the `.ipa` extension to `.zip` and unzip it.
     2. Just right-click on the `.ipa` file and select <kbd>Show Package Contents</kbd>.

     ![Show package contents](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741625880/dmbuil-github-pages/show-package-content.png){: w="300" h="400" }
     _Show package contents_

 11. Inside the `.ipa` container, you will find a `Info.plist` file. Open it.
 12. Search for `CFBundleURLSchemes`. You will find the URL Scheme for the App
     you were looking for.  

     ![CFBundle](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1741625644/dmbuil-github-pages/bundle-url-name.png){: w="300" .center }
     _The `CFBundleURLSchemes` key._

In my case, the URL Scheme for the Ajax app is `ajax://`. Now I can create a
shortcut in Home Assistant to open the Ajax app on an actionable notification.
But that will be another post.

> In case of Windows, you would have to find yourself a way
> to download the `.ipa` file for your App, but other than that, it's basically
> the same procedure (check
> [this comment](https://www.reddit.com/r/widgy/comments/1c8402h/comment/l0cjxkq/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
> on Reddit)
{: .prompt-info }

_Hope it helps!_

---
[^1]: As per [Apple Documentation](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app),
      or if you prefer Wikipedia, [URL Scheme](https://en.wikipedia.org/wiki/List_of_URI_schemes).

[^2]: This is a literal translation from Spanish: _Cofradía del Puño cerrado_,
      which means that you are very careful with your money. You don't like to
      spend it lightly.

[^3]: An `.ipa` file is an iOS application archive file which stores an iOS app.
      Each `.ipa` file includes a binary for the ARM architecture and ~~can~~
      _should_ only be installed on an iOS-device.
