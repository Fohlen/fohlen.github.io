---
title: "Apple may be the last stronghold for privacy"
description: "In an interesting turn of events Apple will inadvertently become the leading company to protect consumer privacy"
author: "Lennard Berger"
date: "2023-12-28"
toc: true
categories: [apple,privacy]
---

![A painting on a wall warning visitors about video surveillance by Tobias Tullius](./tobias-tullius-4dKy7d3lkKM-unsplash-2.jpg)

When Microsoft first gave the news that it would [ditch their homegrown browser engine for Chromium in 2018](https://www.windowscentral.com/microsoft-building-chromium-powered-web-browser-windows-10), users where ecstatic. Internet Explorer was a slow, buggy and cumbersome piece of technology that many, including Microsoft, saw as nothing else but legacy.

On the flip side, it meant that Chromium (and by extension Google) would increase their leverage in the web browser market. Suddenly, the independant browser engines (Quantum, WebKit, Chromium, Internet Explorer) would be reduced by one.

Already back then, privacy advocates were warning that we [may be headed to a Chrome-only web](https://arstechnica.com/gadgets/2019/03/microsofts-new-skype-for-web-client-an-early-taste-of-the-browser-monoculture/). If a monopoloy doesn't immediately sound alarm bells, it will eventually come around to get you.

In November this year, Google decided to use the leverage they have on the browser market. They've had enough of Ad Blockers, and [Manifest V3](https://developer.chrome.com/blog/resuming-the-transition-to-mv3) will make sure they'll get to eat their cake too.

The V3 manifest version has a few profound implications on the way ad-blockers can interact with Chromium-based browsers, most notably in two ways:

1. ["Improving" content filtering in Manifest V3](https://developer.chrome.com/blog/improvements-to-content-filtering-in-manifest-v3), this directly restricts and cuts back the ability to filter content (which is the main functionality of AdBlock extensions)
2. [Google added a new and mandatory Safety check](https://developer.chrome.com/blog/extension-safety-hub) to extensions in the Chrome Store. While it provides better security to users, it will significantly slow down the update time of extensions, which effectively gives Google more time to counteract updates in Adblock extensions (such as filter rules)

## Defying Manifest v3

Mozilla has announced that they will support [both V3 and V2 extensions](https://blog.mozilla.org/en/products/firefox/extensions-addons/heres-whats-going-on-in-the-world-of-extensions/), which means existing extensions *may* support the V2 manifest. I'll note *may* here, as supporting an outdated version of an extension places a heavy burden, both on the browser vendor and the extension developers. Maintenance is an uphill battle, and supporting the V2 extension protocol might not be enough. 

It suffices to take a look at the browser market share provided by [StatCounter](https://gs.statcounter.com/browser-market-share):

![Browser Market Share Worldwide](./StatCounter-browser-ww-monthly-202211-202311.png)

At a market share of 3.23% many extension developers may opt to discontinue V2 extensions, even if Mozilla keeps the old standard alive indefinitely.

While Apple has also introduced support for [V3 extensions](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/#safari-web-extensions), existing support for [content filter providers](https://developer.apple.com/documentation/networkextension/content_filter_providers) will **not** be impacted.

This means extension developers such as [Magic Lasso](https://www.magiclasso.co) are not impacted by this extension update.

Unlike Firefox (who needs V3 to bring in more extensions for their users), Apple has no incentive to remove this capability in the long term. Ad blockers are likely to stay at the same level of quality in Safari indefinitely.

## Rolling out a two-hop encrypted privacy network

One of two features rolled out by Apple in September 2023 is private relay. Quoting the [technical details here](https://support.apple.com/en-gb/102602):

> - When Private Relay is enabled, your requests are sent through two separate, secure internet relays.
Your IP address is visible to your network provider and to the first relay, which is operated by Apple. Your DNS records are encrypted, so neither party can see the address of the website you’re trying to visit.
> - The second relay, which is operated by a third-party content provider, will generate a temporary IP address, decrypt the name of the website you’ve requested and connect you to the site.

This works very similarly to TOR, obscuring your identity in an end-to-end encrypted way. Unlike TOR however, [Apple is obnoxious enough to simply push their network onto service providers](https://developer.apple.com/support/prepare-your-network-for-icloud-private-relay/). Whereas you may run into constant issues with TOR or VPNs, you can now enjoy a similarly secure service, and run high likelyhood to be serviced.

## Disposable emails made by Apple

The second feature released by Apple is ["hide my email"](https://support.apple.com/en-gb/guide/mac-help/mchle62f7f45/mac). While there are a myriad of disposeable email services, they are usually blacklisted by major vendors (say Amazon). Hide my email will give you a permanent redirect email alias from `icloud.com`. Are you tired of newsletters that don't respect your unsubscribe preference? Simply remove the email alias, begone!

## Apple is on a quest for user privacy

Apple's commitment to withstand the V3 manifesto changes pushed by Google, together with their iCloud+ offering (that comes as cheap as $1 a month), makes me believe that they are taking user privacy seriously.
It is refreshing to see a major tech company pushing technology that benefits their users once in a while. 2023 was an exciting year of changes in terms of security and privacy, and I'm looking forward to what 2024 will bring. Who knows, maybe we'll see disposable credit cards and phone numbers next (if I'm allowed to dream).
