---
date: 2025-04-01 15:01:50
layout: post
title: "Matrix those Ads - Part 1"
subtitle: How to protect yourself from ads and trackers
description: "First steps to protect yourself from ads and trackers: uBlock Origin"
image:
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743540259/dmbuil-github-pages/ads-1-crop.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1743540259/dmbuil-github-pages/ads-1-crop.jpg
category: tutorial
tags:
  - ads
  - uBO
  - privacy
  - security
author: dmbuil
paginate: false
---

When surfing the web, we are constantly stormed with ads and eavesdropped by
trackers. They are _annoyingly_ everywhere, and more often than not, even dangerous.

This will be, I hope, the first of a post series about how to protect yourself
from ads & trackers on your workstation by using several tools.  
They can be used together or separately, depending on your needs, knowledge and,
mostly, time.

## Going down the rabbit hole

![ABT](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743540487/dmbuil-github-pages/abt-1.png){: w="400" .right .shadow}

The reason for this post is this tool I stumbled[^1] upon: [adblock-tester.com](https://adblock-tester.com/).

It tells you in a very visual fashion how _protected_ you are against a bunch of
trackers: you will score up to 100 points depending on how well you perform when
trying to dodge all these ads coming right at you. It is quite interesting to
see how many of them are blocked by default, and how many are left to be blocked
by an ad-blocker.

As cybersecurity itself, privacy is a matter of layers. Should any of them fail,
the next one should firmly be there to protect you.
The more layers involved, the more failures you can withstand.

## The objective

Let's begin with the first layer: the browser itself.

> For the sake of this and future posts, I will be using both **Firefox** and
> **Edge**, since they are my personal choices, but the tools I will be talking
> about are available for Firefox and Opera.
> Besides, I will be using Incognito mode for the tests, so that no previous cache
> nor cookies are involved.
{: .prompt-info }

When accessing the Tester Website with any non-default extension disabled, Firefox
perfoms... well, it achieved a **38/100** protection score. So did Edge: **38/100**.

![Firefox](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743539137/dmbuil-github-pages/ads-ff-1.png){: w="400" .shadow }
_Firefox Score: 38/100_

![Edge](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743539208/dmbuil-github-pages/ads-ms-1.png){: w="400" .shadow }
_Edge Score: 38/100_

Now that we know the baseline, let's see how we can improve it.

## First stop: uBlock'em all

The first and foremost tool is [uBlock Origin](https://ublockorigin.com/es).
This is a browser extension that blocks ads, trackers and malware sites. It is
available for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/),
[Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm),
[Edge](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak)
(or any other Chromium-based browser).
And [Opera](https://addons.opera.com/en/extensions/details/ublock/).

Some time ago, it was even available for Safari (back in Safari 13), but it is
no longer maintained, due to the restrictions Apple imposes on its extensions
_(do not worry, we will get to that)_.

It is quite easy to install and use. Just install the extension and have a look
at the available filters.

> **Beware of the imitations**  
> There are many clones of uBlock Origin, but the original
> is the one that is maintained by [Raymond Hill](https://github.com/gorhill).
> You can find the source code [here](https://github.com/gorhill/uBlock).
{: .prompt-warning }

Seriously. You would be [amazed](https://x.com/SwiftOnSecurity/status/1696547799167291471)
at how many threats are blocked by this extension.  
And how much faster the pages load.

So, after installing uBlock Origin, I went back to the Tester Website and reloaded.
The result was a **100/100** protection score on Firefox and a close **96/100**
on Edge[^2].  
Impressive, right?

![Firefox](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743539247/dmbuil-github-pages/ads-ff-2.png){: w="400" .shadow .rounded-10 }
_Firefox Score: 100/100. Yay!_

![Edge](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743539262/dmbuil-github-pages/ads-ms-2.png){: w="400" .shadow .rounded-10 }
_Edge Score: 98/100. Not bad..._

If your uBO is not working this smoothly, you may want to check the blocking settings of the extension.
The default settings are quite good, but you may want to enable the language settings
or just select a bunch of filters to block more ads and trackers.
Some of them are worth giving a try, such as the custom Cookie Annoyance Blockers.

![uBO](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743539279/dmbuil-github-pages/ads-ubo-1.png){: w="400" .shadow .rounded-10 }
_List of uBO filters I personally use._

Just don't go overboard with the filters, as it may break some websites.

### Wait! I heard something about uBO being deprecated

Chrome is _upgrading_ their extensions' support up from
[Manifest v2 to v3](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=es-419).  
Some of these changes are aimed to improve security, but also imply that _many_
extensions that rely on these specific features will be left behind, such as uBO.

This affects uBO in Chrome, but at least for now, other Chromium-based browsers
such as Edge are not following their path.

Regarding uBO, they didn't back down and released **uBlock Origin Lite**
(**uBOL**), which is a paired-down version of uBO. You may read more about this
[here](https://github.com/uBlockOrigin/uBlock-issues/wiki/About-Google-Chrome's-%22This-extension-may-soon-no-longer-be-supported%22).
Or maybe you should just [ditch Chrome](https://chromeisbad.com).

## Apple eater? _Gotcha_

If you are an Apple's Safari user, there are other alternatives. My personal
best is [**Ghostery**](https://www.ghostery.com),
as it can be installed in Safari with no hassle[^3], and has proven itself to
be the most consistent across versions.

But we will get to that in a future post.
Stay tuned.

_Hope it helps!_

---
[^1]: There are some other websites that will test your ad-blocker, but this
      one is quite visual, and illustrative enough.

[^2]: The difference is due to the fact that site was not able to check the
      ad presence in Edge, so it just assumed it was not blocking some ads.
      Sometimes, Firefox even reported "just" a 90/100 score, due to the same
      reason.

[^3]: It's been some noise around Ghostery doing some blocking trackers and allowing
      You know, _who watches the watcher_
