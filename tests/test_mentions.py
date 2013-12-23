#!/usr/bin/env python

import unittest
from httmock import urlmatch, HTTMock

from ronkyuu import findMentions, findEndpoint, discoverEndpoint


post_url  = "https://bear.im/bearlog/2013/325/indiewebify-and-the-new-site.html"
post_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">

    <link rel="alternate" type="application/atom+xml" href="https://bear.im/bearlog/atom.xml"/>

    <link href="/css/bootstrap.css" rel="stylesheet"/>
    <link href="/css/bootstrap-responsive.min.css" rel="stylesheet"/>
    <link href="/css/pygments.css" rel="stylesheet"/>
    <link href="/css/local.css" rel="stylesheet"/>

    <link href="https://bear.im/webmention" rel="webmention"/>
</head>
<body>
    <div id="content">
      <article class="h-entry">
        <div class="content-title">
             <h1 class="p-name">IndieWebify&#8217;ing the&nbsp;Site</h1>
        </div>
        <p>
        <a href="https://bear.im/bearlog/2013/325/indiewebify-and-the-new-site.html" class="u-url">
          <time class="dt-published" datetime="2013-11-21">
          Thu 21 November 2013
          </time>
        </a> 
        by <a href="https://bear.im" class="p-author h-card">bear</a>
        </p>
        <div class="e-content">
          <p>
I&#8217;ve been following, heck even participated in the earlier scene, the <a href="http://indiewebcamp.com/">IndieWeb</a> movement by trying to always use <a href="http://microformats.org/wiki/microformats2">microformats</a>, open standards and the like.
The earlier work sometimes was rather tedious in ways that just didn&#8217;t make&nbsp;sense.
</p>
<p>
  Cue a couple years of iteration&nbsp;&#8230;
</p>
<p>
  Now the IndieWeb is going even stronger, what with the <span class="caps">NSA</span> Snowden stuff and people realizing that even friendly and nice looking silos are still just that, silos &#8212; looking at you Google! One site that makes it <em>very</em> easy to implement is <a href="http://indiewebify.me/">IndieWebify.Me</a> and it&#8217;s series of guides and&nbsp;examples.
</p>
<p>
Currently I&#8217;m at Level 2.1 - <a href="http://microformats.org/wiki/microformats2#h-card">h-card</a> and
<a href="http://microformats.org/wiki/microformats2#h-entry">h-entry</a> items are all in place, just need to figure out
how to do <a href="https://github.com/converspace/webmention/blob/master/README.md">WebMentions</a> with a purely static&nbsp;site.
</p>
<p>
  <a href="http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration" rel="in-reply-to">test post link</a>
</p>
        </div>
        <hr />
      </div>
    </article>
</body>
</html>
"""
tantek_url  = "http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration"
tantek_html = "<!DOCTYPE html><html><head><meta charset=\"utf-8\" />\n<title>The Homebrew Computer Club 38th Reunion: Inspiration To Try A Variant - Tantek</title>\n<base href=\"http://tantek.com/2013/\" />\n<link rel=\"hub\" href=\"http://pubsubhubbub.appspot.com/\" />\n<link rel=\"home alternate\" type=\"application/atom+xml\" href=\"../updates.atom\" />\n<link rel=\"webmention\" href=\"http://webmention.io/tantek.com/webmention\" />\n<style type=\"text/css\">/*<![CDATA[*/ \n@import \"simple.css\";\n.header {\n border-bottom:solid 1px #666;\n padding-bottom:3em;\n}\nform.search { width:34%; float:right; white-space:nowrap; font-size:1.3em; text-align:right }\ninput,button { font-size:1em }\nbutton { margin: 0 0.5em 0 0; padding:0 0.5em }\nform.search input[type=search] { width:62% }\n/*]]>*/</style>\n<script type=\"text/javascript\" src=\"cassis.js\"></script>\n</head>\n<body class=\"post\">\n<header><div class=\"header\">\n<h1><a href=\"../\" rel=\"author home\">tantek.com</a></h1>\n\n<form class=\"search\" action=\"http://www.google.com/search\" method=\"get\">\n<input type=\"hidden\" name=\"as_sitesearch\" value=\"tantek.com\"/>\n<input type=\"hidden\" name=\"tbs\" value=\"sbd:1,cdr:1,cd_min:1/1/1970\"/>\n<input type=\"search\" name=\"q\"/>\n<button type=\"submit\">Search</button>\n</form>\n\n</div></header>\n<ol>\n\n<li class=\"h-entry hentry h-as-article\" id=\"d322b1\">\n<a href=\"../\" class=\"p-author h-card author-icon\" rel=\"author\" title=\"Tantek \u00c7elik\"><img src=\"../logo.jpg\" alt=\"Tantek \u00c7elik\" /></a>\n<div class=\"sidestuff\">\n\n<ul class=\"snav\">\n<li><a href=\"322/t1/post-note-thoughts-sooner-without-expectations-article\" id=\"previtem\" title=\"View the previous (older) item in the stream.\" rel=\"prev\"><abbr title=\"Previous\">&#x2190;</abbr></a></li><li><a href=\"323/t1/rain-san-francisco-feels-amazing\" id=\"nextitem\" title=\"View the next (newer) item in the stream\" rel=\"next\"><abbr title=\"Next\">&#x2192;</abbr></a></li>\n</ul>\n</div>\n<article>\n<div class=\"article\">\n<header><div class=\"header\"><h1 class=\"p-name entry-title\">\nThe Homebrew Computer Club 38th Reunion: Inspiration To Try A Variant\n</h1><span class=\"info\"><span class=\"dt-published published dt-updated updated\"><time class=\"value\">21:36</time> on <time class=\"value\">2013-11-18</time></span> <span class=\"lt\">(ttk.me b/4T71)</span></span></div></header><div class=\"e-content entry-content\">\n<p class=\"h-event\">\n<time class=\"dt-start\" datetime=\"2013-11-11T18:00\">Last Monday night</time> \n<abbr class=\"p-attendee h-card\" title=\"Tantek &#xC7;elik\">I</abbr> \nattended the <a class=\"u-url p-name\" href=\"http://tantek.com/2013/315/t1/watching-stevewoz-speak-homebrew-computer-club\">Homebrew Computer Club 38th Reunion</a> and got to hear <a class=\"p-attendee h-card\" href=\"http://woz.org/\">Steve Wozniak</a> give an impromptu speech from the heart. It was both inspiring and reminded me of many of the reasons I developed a passion for computers in the first place.\n</p>\n<p>\nIn reflecting on <a href=\"http://tantek.com/2013/315/t1/watching-stevewoz-speak-homebrew-computer-club\">my notes from his speech</a>, I realized that everything that Woz said about how the Homebrew Computer Club from the start about your \"own machine\" or your \"own computer\" applies today nearly 40 years later to your own online identity and your own website.\n</p>\n<p>However, like the early 1970s, the dominant computing paradigm is once again stuck in a <a href=\"http://en.wikipedia.org/wiki/timesharing\">timesharing</a> mindset, updated with new terms and prettier interfaces.\n</p>\n<p>\nYou may \"own\" your own handheld machine and computer, but your software and data are more and more updated, controlled, and stored in  one or more proprietary centralized \"clouds\" (whether Google's Gmail/Calendar/Documents, or Apple's iCloud, or Facebook, or others vying to replace them).\n</p>\n<p>\nYou used to be able to buy two Apple devices, e.g. an iPad/iPod/iPhone and a Mac, and sync them directly with each other. However, as of the latest version of Apple's operating system, ironically named \"Mavericks\", you can no longer do so, and <a href=\"http://support.apple.com/kb/PH12117\">must sync them both with iCloud</a>, which they treat as the \"true\" copy of your data:\n</p>\n<blockquote cite=\"http://support.apple.com/kb/PH12117\"><p>\n[...] If you use OS X Mavericks v.10.9 or later, your contacts, calendars, and other info are updated on your computers and iOS devices via iCloud. [...]\n</p></blockquote>\n<p>\nStuck somewhere without an internet connection, or a connection that is <a href=\"http://tantek.com/2011/239/t4/network-slowest-unreliable-untrusted-insecure-computer\">slow or unreliable</a>?</p>\n<p>\nToo bad, you can no longer sync between the devices that you hold in your hand, despite physically connecting them to each other with a cable. You are blocked from syncing the data between the devices in your very hands.\n</p>\n<p>\nLast week Woz said: \n</p>\n<blockquote><p>\nWe all wanted to be close to our own machine.\n</p></blockquote>\n<p>\nIf our machines are where we store (and share) our data, we are getting further from our machines, not closer.\n</p>\n<p>\nThe timesharing systems of the 1970s were not disrupted overnight. Nor were they disrupted by large corporations no matter how innovative they thought they were. Nor were they disrupted by first <a href=\"http://indiewebcamp.com/antipatterns#mass_adoption\">designing for every user</a>.\n</p>\n<p>\nThey were disrupted by the emergence of innovations from a small group of dedicated enthusiasts who were first looking to empower each other, and second empower others. Woz continued:\n</p>\n<blockquote>\n<p>\nWe wanted to own our own computer.\n</p>\n<p>\nYou were going to go into your company, and take your own machine. \n</p>\n<p>\nEverybody was going to be empowered and a master of their own life.\n</p>\n</blockquote>\n<p>\nSo what was it about the Homebrew Computer Club that <a href=\"http://www.atariarchives.org/deli/homebrew_and_how_the_apple.php\">made so much possible</a>? Was it the timing - <time>1975-03-05</time>? The Silicon Valley location(s)? The people? The frequency of meetings? The structure - how <a class=\"h-card\" href=\"http://www.leefelsenstein.com/\">Lee Felsenstein</a> ran the meetings?\n</p>\n<p>\n<a href=\"http://techland.time.com/2013/11/12/for-one-night-only-silicon-valleys-homebrew-computer-club-reconvenes/\"><img style=\"float:right\" src=\"http://timenerdworld.files.wordpress.com/2013/11/image9.jpg\" alt=\"Homebrew member Chris Espinosa with an original club newsletter.\"/></a> At the 38th reunion I had the chance to catch up with <a class=\"h-card\" href=\"http://cdespinosa.tumblr.com/\">Chris Espinosa</a>, a frequent attendee of Homebrew Computer Club meetings, and asked him about some of the details.\n</p>\n<dl>\n<dt>What time was the meeting?</dt>\n<dd>Right after work [7pm according to <a href=\"http://www.computerhistory.org/revolution/personal-computers/17/312/1138\">first issue of <abbr title=\"Homebrew Computer Club\">HCC</abbr> newsletter</a>]</dd>\n<dt>How often did they meet?</dt>\n<dd>Every two weeks. Often enough for a growing sense of continuity, yet infrequent enough to encourage going rather than skipping to go \"next week\".</dd>\n<dt>What was the general structure?</dt>\n<dd>Lee would start the meeting with a microphone, and then given the microphone to anyone who raised their hand with a point to make, or a question to ask. After that there was the \"random access\" period where people would break off and have smaller discussions, and eventually leave and go get something to eat, like at The Oasis in Palo Alto, or Bob's Big Boy in Cupertino (especially if you were under 21 [which Chris was at the time]).</dd>\n</dl>\n<p>\nFor a few years now we've had another <a href=\"http://indiewebcamp.com/\">growing community, focused on owning your own online identity and data</a>. Primarily online with a wiki and <a href=\"http://indiewebcamp.com/IRC\">IRC channel</a>, we've also had a strong in-person component, meeting annually in various cities on weekends, and sometimes for evening dinners.\n</p>\n<p>\nHearing the speeches at the Homebrew reunion and speaking with Chris made me wonder: what if we cloned some aspects of the Homebrew Computer Club and created an equivalent for personal websites?\n</p>\n<ul>\n<li>\nWe want to own our own web identity and data.\n</li>\n<li>\nWe all want to be close to our machines, content, identities.\n</li>\n<li>\nImagine going into a company, not only with your own machine(s), but your own online identity, document storage, etc.\n</li>\n<li>\nWe want to make tools that make us and eventually everyone a master of their own life.\n</li>\n</ul>\n<p>\nI mentioned these parallels to <a class=\"h-card\" href=\"http://werd.io/\">Ben Werdmuller</a> and he said it made complete sense to him as well.\n</p>\n<p>\nSo we're doing this. Started with inspiration, re-using much of the HCC structure, yet without asking permission:\n</p>\n<dl class=\"h-event\" style=\"font-weight:bold\">\n<dt>What</dt>\n<dd class=\"p-name\">The Homebrew Website Club</dd>\n<dt>Who</dt>\n<dd class=\"p-description\"><p style=\"margin-top:0\">Are you building your own website? Indie reader? Personal publishing web app? Or some other digital magic-cloud proxy?</p>\n<p style=\"margin-bottom:0\">If so, you might like to come to a gathering of people with likeminded interests. Exchange information, swap ideas, talk shop, help work on a project, whatever... (copied and modified from <a href=\"http://www.computerhistory.org/revolution/personal-computers/17/312/1138\">issue 1</a>).</p>\n</dd>\n<dt>When</dt>\n<dd class=\"dt-start\"><time class=\"value\">18:30</time>-<time class=\"dt-end\" datetime=\"2013-11-20T19:30-0800\">19:30</time> every other Wednesday night, starting <time class=\"value\">2013-11-20</time></dd>\n<dt>Where <ins datetime=\"2013-11-19\">(Updated!)</ins></dt> \n<dd class=\"p-location\"><ins datetime=\"2013-11-19\"><a href=\"https://wiki.mozilla.org/SF\">MozillaSF</a> 7th floor</ins> in San Francisco (transit BART:Embarcadero, MUNI:Embarcadero&amp;Folsom).</dd>\n</dl>\n<p>\nI really liked the \"mapping\" and \"random access\" meeting phases that Lee Felsenstein came up with. Perhaps we'll adopt similar phases like 30 minutes of \"broadcasting\" (for anyone to show what they've got working, or ask an open question for help with something) and 30 minutes of \"peer to peer\".\n</p>\n<p>I also remember someone at the reunion relating how when someone with the microphone went too long, Lee would cut them off and pass the mic to another person. We'll have to see how much such explicit \"blowhard\" management is needed. Maybe we just timebox \"broadcasting\" to 30 min total, and 2 minutes per person? Or maybe we'll figure it out as we go.\n</p>\n<p>\nChris Espinosa's description about how the Homebrew meetings were \"right after work\" stuck with me. This meant the meetings were something you could go to <em>before</em> other plans, leaving the rest of the evening free to fork off in smaller groups for food, or seeing other friends, or going to home to spend time with the family. Such timing provides greater flexibility for a broader set of people who may have other evening obligations. Ben and I have decided to try starting at 18:30 and see how that goes. We figure you should all be leaving work by 18:00 anyway (regardless of what you do), leaving 30 minutes for transit.\n</p>\n<p>\nOnce we've confirmed a venue (<ins datetime=\"2013-11-19\">we have</ins>), I'll update this post (<ins datetime=\"2013-11-19\">updated</ins>) and post an update. Until then, put it in your calendar:</p>\n<ul>\n<li>18:30 on Wednesday 2013-11-20 <ins datetime=\"2013-11-19\"><a href=\"https://wiki.mozilla.org/SF\">@MozSF</a></ins>: Homebrew Website Club</li>\n</ul>\n<p>\nBe seeing you.\n</p>\n<p>\nThanks to <a class=\"h-card\" href=\"http://joel.franusic.com\">Jo\u00ebl Franusic</a> and <a class=\"h-card\" href=\"http://werd.io/\">Ben Werdmuller</a> for reviewing drafts of this post.\n</p>\n</div></div>\n<footer>\n<div class=\"info footer\">\n<form action=\"http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration\"><div>\n<label><span class=\"lt\">URL:</span>\n<input class=\"u-url url u-uid uid bookmark\" type=\"url\" size=\"70\" value=\"http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration\" />\n</label>\n<label><span class=\"lt\">HTML:</span>\n<input class=\"code\" type=\"text\" size=\"70\" value='&lt;cite class=\"h-cite\"&gt;&lt;a class=\"u-url p-name\" href=\"http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration\"&gt;The Homebrew Computer Club 38th Reunion: Inspiration To Try A Variant&lt;/a&gt; (&lt;abbr class=\"p-author h-card\" title=\"Tantek \u00c7elik\"&gt;\u00c7elik&lt;/abbr&gt; &lt;time class=\"dt-published\"&gt;2013-11-18&lt;/time&gt;)&lt;/cite&gt;' />\n</label>\n\n<action do=\"post\" with=\"http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration\">\n<span class=\"tweet-button\">\n<a href=\"http://twitter.com/share\" class=\"twitter-share-button\" data-url=\"http://tantek.com/2013/322/b1/homebrew-computer-club-reunion-inspiration\" data-text=\"The Homebrew Computer Club 38th Reunion: Inspiration To Try A Variant:\" data-count=\"horizontal\" data-via=\"t\" data-related=\"html5now:microformats\">Tweet</a><script type=\"text/javascript\" src=\"http://platform.twitter.com/widgets.js\"></script>\n</span>\n</action>\n</div></form>\n</div>\n</footer>\n</article>\n</li>\n</ol>\n<script type=\"text/javascript\">/*<![CDATA[*/\nfunction select_all(e) {\n e = e ? e : window.event;\n var el = targetelement(e);\n el.focus();\n /* el.select(); // fails in Mobile Safari */\n el.selectionStart=0;\n el.selectionEnd=el.value.length;\n}\n\nvar fs = document.forms, i = 0, j = 0, es;\nfor (i = 0; i<fs.length; i++) {\n  es = document.forms[i].elements;\n  if (es) {\n    for (j=0;j<es.length;j++) {\n      switch (es[j].type) {\n      case \"text\":\n      case \"url\":\n        es[j].onclick = select_all;\n      }\n    }\n  }\n}\n\ndocument.onkeyup = keyup;\n\nfunction clearactive() {\n  var e = document.getElementById(\"previtem\");\n  if (e) { e.className = \"\"; }\n  e = document.getElementById(\"nextitem\");\n  if (e) { e.className = \"\"; }\n}\n\nfunction keyup(e)\n{\n   var kid = (window.event) ? event.keyCode : e.keyCode;\n   var nid = \"\";\n   if (document.activeElement !== document.body) {\n     return;\n   }\n   switch(kid) {\n    case 37:\n    case 74:\n      nid = \"previtem\";\n      break;\n    case 39:\n    case 75:\n      nid = \"nextitem\";\n      break;\n   }\n   if (nid!=\"\") {\n      ne = document.getElementById(nid);\n      if (ne) {\n        ne.className = \"active\";\n        doevent(ne,\"click\");\n        window.onunload = clearactive;\n      }\n   }\n}\n\n/*]]>*/</script>\n</body>\n</html>\n"

event_config = { "handler_path": "./tests/test_event_handlers",
                    
               }

@urlmatch(netloc=r'(.*\.)?bear\.im$')
def bear_im_mock(url, request):
    return post_html

class TestParsing(unittest.TestCase):
    # test the core mention and replies link finding
    def runTest(self):
        with HTTMock(bear_im_mock):
            mentions = findMentions(post_url, ['bear.im'])

            assert len(mentions) > 0
            assert 'http://indiewebify.me/' in mentions.keys()
            assert tantek_url in mentions.keys()

class TestEndpoint(unittest.TestCase):
    # run the html parsing for a discoverWebmentions result using a stored
    # GET from one of Tantek's posts
    def runTest(self):
        assert findEndpoint(tantek_html) == 'http://webmention.io/tantek.com/webmention'

@urlmatch(netloc=r'(.*\.)?tantek\.com$')
def tantek_mock(url, request):
    return tantek_html

class TestDiscovery(unittest.TestCase):
    def runTest(self):
        with HTTMock(tantek_mock):
            result = discoverEndpoint(tantek_url)

            assert result[1] == 'http://webmention.io/tantek.com/webmention'
