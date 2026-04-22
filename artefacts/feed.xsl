<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:media="http://search.yahoo.com/mrss/">
  <xsl:output method="html" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>

  <xsl:template match="/rss">
    <html lang="fr">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title><xsl:value-of select="channel/title"/></title>
        <style>
          :root {
            --bg: #fafafa;
            --fg: #1a1a1a;
            --muted: #666;
            --accent: #ff6600;
            --card-bg: #fff;
            --border: #e5e5e5;
          }
          @media (prefers-color-scheme: dark) {
            :root {
              --bg: #0f0f0f;
              --fg: #e8e8e8;
              --muted: #999;
              --card-bg: #1a1a1a;
              --border: #2a2a2a;
            }
          }
          * { box-sizing: border-box; }
          body {
            margin: 0;
            padding: 2rem 1rem;
            font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--fg);
            background: var(--bg);
          }
          .wrap { max-width: 720px; margin: 0 auto; }
          header.feed {
            padding-bottom: 1.5rem;
            border-bottom: 2px solid var(--accent);
            margin-bottom: 2rem;
          }
          header.feed h1 {
            margin: 0 0 .4rem;
            font-size: 1.7rem;
            color: var(--accent);
          }
          header.feed p { margin: .25rem 0; color: var(--muted); font-size: .95rem; }
          header.feed .meta a { color: var(--muted); text-decoration: none; border-bottom: 1px dotted var(--muted); }
          article {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
          }
          article h2 {
            margin: 0 0 .35rem;
            font-size: 1.15rem;
            line-height: 1.35;
          }
          article h2 a { color: var(--fg); text-decoration: none; }
          article h2 a:hover { color: var(--accent); }
          article time { color: var(--muted); font-size: .85rem; }
          article .thumb {
            float: right;
            margin: 0 0 .5rem 1rem;
            max-width: 140px;
            max-height: 140px;
            border-radius: 4px;
            object-fit: cover;
          }
          article .desc { margin-top: .75rem; font-size: .96rem; }
          article .desc h2 { font-size: 1rem; margin-top: 1.25rem; color: var(--muted); }
          article .desc p { margin: .5rem 0; }
          article .desc ul { padding-left: 1.25rem; }
          article .desc li { margin: .15rem 0; }
          article .desc hr { border: none; border-top: 1px solid var(--border); margin: 1rem 0; }
          article footer { margin-top: .75rem; font-size: .85rem; color: var(--muted); }
          article footer a { color: var(--muted); }
          a { color: var(--accent); }
        </style>
      </head>
      <body>
        <div class="wrap">
          <header class="feed">
            <h1><xsl:value-of select="channel/title"/></h1>
            <p><xsl:value-of select="channel/description"/></p>
            <p class="meta">
              RSS feed:
              <a href="{channel/atom:link/@href}">
                <xsl:value-of select="channel/atom:link/@href"/>
              </a>
            </p>
          </header>
          <main>
            <xsl:for-each select="channel/item">
              <article>
                <xsl:if test="media:group/media:thumbnail/@url">
                  <img class="thumb" src="{media:group/media:thumbnail/@url}" alt=""/>
                </xsl:if>
                <h2>
                  <a href="{link}">
                    <xsl:value-of select="title"/>
                  </a>
                </h2>
                <time><xsl:value-of select="pubDate"/></time>
                <div class="desc">
                  <xsl:value-of select="description" disable-output-escaping="yes"/>
                </div>
                <footer>
                  <a href="{comments}">Discussion Hacker News →</a>
                </footer>
              </article>
            </xsl:for-each>
          </main>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
