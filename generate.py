# Generator for my website hanprogramer.github.io
import os
import glob
import sys
import markdown2

# Reads the template files
f = open("index.template.html", "r")
INDEX_TEMPLATE = f.readlines()
f.close()

f = open("posts.template.html", "r")
POSTS_TEMPLATE = f.read()
f.close()
f = open("wikiposts.template.html", "r")
WIKI_TEMPLATE = f.read()
f.close()
# posts formatted using string formatting with %s
# format (title, bodyHTML)

# List all available posts
POSTS = {}
for i in os.listdir("posts"):
    POSTS[i] = os.listdir("posts/%s" % i)

# Load in the wiki JSON
f = open("images/ef-wiki.json")
wiki_raw = f.read()
f.close()
import json
wiki = json.loads(wiki_raw)
# Template header for all files
header = """<!DOCTYPE html>
<html>
    <head>
        <meta property="og:title" content="Hanprogramer's Website" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="http://hanprogramer.github.io" />
        <meta property="og:image" content="https://hanprogramer.github.io/banner.png" />
        <meta property="og:description" content="Come check out my stuffs :3" />
        <meta name="theme-color" content="#FF0000">

        <!-- Include this to make the og:image larger -->
        <meta name="twitter:card" content="summary_large_image">
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="../../../index.css">
        <!-- <link rel="stylesheet" href="../../../nav.css"> -->
        <link rel="icon" type="image/png" href="../../../logo.png">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        <script data-ad-client="ca-pub-9638544368327690" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <title>Hanprogramer</title>
    </head>
    <body>
        <script>
            CSS.paintWorklet.addModule('../../../bubblePaint.js')
        </script>
        
        <div class="navbar">
            <img class="round-icon" src="../../../favicon.ico">
            <div class="titletext">
                <a href="../../../index.html">HANPROGRAMER</a>
                <!-- <a href="https://youtube.com/Hanprogramer" target="_blank" class="subtitle">youtube.com/Hanprogramer</a> -->
            </div>
            <div style="flex-grow: 1"></div>
            <button class="button" onclick="window.location = '../../../tools.html'">Tools</a>
            <button class="button" onclick="window.location = '../../../addons.html'">Addons</a>
        </div>

        <div style="margin-bottom: 56px"></div>
        <div class="maindivider" style="position: relative">
        <div class="content">"""
header_root = """<!DOCTYPE html>
<html>
    <head>
        <meta property="og:title" content="Hanprogramer's Website" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="http://hanprogramer.github.io" />
        <meta property="og:image" content="https://hanprogramer.github.io/banner.png" />
        <meta property="og:description" content="Come check out my stuffs :3" />
        <meta name="theme-color" content="#FF0000">

        <!-- Include this to make the og:image larger -->
        <meta name="twitter:card" content="summary_large_image">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="index.css">
        <!-- <link rel="stylesheet" href="nav.css"> -->
        <link rel="icon" type="image/png" href="logo.png">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        <script data-ad-client="ca-pub-9638544368327690" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <title>Hanprogramer</title>
    </head>
    <body>
        <script>
            CSS.paintWorklet.addModule('bubblePaint.js')
        </script>
        
        <div class="navbar">
            <img class="round-icon" src="favicon.ico">
            <div class="titletext">
                <a href="index.html">HANPROGRAMER</a>
                <!-- <a href="https://youtube.com/Hanprogramer" target="_blank" class="subtitle">youtube.com/Hanprogramer</a> -->
            </div>
            <div style="flex-grow: 1"></div>
            <button class="button" onclick="window.location = './tools.html'">Tools</a>
            <button class="button" onclick="window.location = './addons.html'">Addons</a>
        </div>
        <div style="margin-bottom: 56px"></div>
        
        <div class="maindivider" style="position: relative">
        <div class="content">
        %s
        <div class="post-container">"""
footer = """<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <!-- github.io -->
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-9638544368327690"
             data-ad-slot="9490828740"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
        
                <div class="tweets">
                        <a class="twitter-timeline" data-height="512" data-dnt="true" data-theme="dark" href="https://twitter.com/Hanprogramer123?ref_src=twsrc%5Etfw">Tweets by Hanprogramer123</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                </div></div></div>
    </body>
</html>"""
f = open("index.html", "w")

# Wiki generator
# generates markdown files 
for category in wiki.keys():
    if(category == "version"): continue
    if(not os.path.exists("posts/wiki/" + category)):
        os.makedirs("posts/wiki/" + category)

    # Generate sub posts for each category
    for item in wiki[category].keys():
        if(not os.path.exists("posts/wiki/" + category + "/" + item)):
            os.makedirs("posts/wiki/" + category + "/" + item)
        item_obj = wiki[category][item]

        item_file = open("posts/wiki/" + category + "/" + item + "/post.md", "w")
        item_file.write("#" + item + "\n")
        item_file.write('<a href="/wiki.html">Wiki</a> > <a href="/posts/wiki/%s">%s</a> > <a>%s</a>' % (category,category,item) + "\n")

        item_file.write('<div class="iteminfo">\n')
        item_file.write('<h3>%s</h3>' % item.replace("_", " ") + "\n")
        item_file.write('<img class="pixelimage" src="%s">' % (item_obj["image"]) + "\n\n")
        if("damage" in item_obj):
            item_file.write('<a class="iteminfoitem">Damage: %s</a>' % str(item_obj["damage"]))
        item_file.write('<a class="iteminfoitem">ID: %s</a>' % item)
        item_file.write('</div>\n')
        item_file.write(item_obj["description"])

        item_file.close()

# Generator
for line in INDEX_TEMPLATE:
    raw = line.strip()
    if(raw == "<div class=\"GENERATED\"></div>"):
        f.write('<div class="post-wrapper">')
        for key in POSTS.keys():
            if(key == "wiki"):  # exception for the wiki
                # Create wiki subcategories
                for wiki_category in os.listdir("posts/wiki/"):
                    if(not os.path.isdir("posts/wiki/%s/" % wiki_category)): continue
                    f_category_html = '<div class="wikilist">'
                    for post in os.listdir("posts/wiki/%s/" % wiki_category):
                        if(not os.path.exists("posts/wiki/%s/%s/post.md" % (wiki_category,post))):
                            continue
                        # Genereate the posts
                        template = """
                                    <a class="wikilistitem" href="/posts/wiki/%s/%s/post.html">
                                        <img src="%s">
                                        <h3>%s</h3>
                                    </a>\n""" % (wiki_category, post, wiki[wiki_category][post]["image"], post)
                        # <img src="/posts/wiki/%s/%s/thumb.png" style="width:512px; height: 256px">
                        f_category_html += template

                        # Generate the individual post html
                        html = WIKI_TEMPLATE % ("Post",markdown2.markdown_path("posts/wiki/%s/%s/post.md" %(wiki_category, post)))

                        f_post = open("posts/wiki/%s/%s/post.html" % (wiki_category,post), "w")
                        f_post.write(html)
                        f_post.close()
                    f_category_html += "</div>"
                    f_category = open("posts/wiki/%s/index.html" % wiki_category, "w")
                    f_category.write(WIKI_TEMPLATE % (wiki_category, f_category_html))
                    f_category.close()
                continue
            #########################################
            #      POSTS CONTENT GENERATOR
            #########################################
            f.write("<h1>%s</h1>" % key.title())
            f.write('<div class="post-container">')
            f_category = open("%s.html" % key, "w")
            f_category_html = ""
            for post in POSTS[key]:
                if(not os.path.exists("posts/%s/%s/post.md" % (key,post))):
                    continue
                # Genereate the posts
                template = """
                            <a class="post" href="posts/%s/%s/post.html">
                                <img src="posts/%s/%s/thumb.png">
                            </a>\n""" % (key, post, key, post)
                f.write(template)
                f_category_html += template

                # Generate the individual post html
                html = POSTS_TEMPLATE % ("Post",markdown2.markdown_path("posts/%s/%s/post.md" %(key, post)))

                f_post = open("posts/%s/%s/post.html" % (key,post), "w")
                f_post.write(html)
                f_post.close()
            f.write('</div>')
            f_category.write(POSTS_TEMPLATE % ("Post",f_category_html))
            f_category.close()
        
        f.write('</div>')
        continue
    else:
        f.write(line)
f.close()