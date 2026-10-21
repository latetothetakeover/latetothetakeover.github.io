# Late to the Takeover: Jekyll site (GitHub Pages)

Unofficial Bitcoin Takeover fan blog. Target URL: https://latetothetakeover.github.io

## Deploy (not done yet)
1. Create the GitHub repo **latetothetakeover/latetothetakeover.github.io**, owned by the `latetothetakeover` account.
2. Push the contents of this folder to `main`.
3. In repo Settings → Pages → Build and deployment, set **Source: GitHub Actions**. The workflow in `.github/workflows/pages.yml` builds with Jekyll 4 and deploys.
   (Classic "Deploy from a branch" also works, because jekyll-seo-tag, jekyll-sitemap and jekyll-feed are all on GitHub Pages' allowed list. It builds with Jekyll 3.10, though, so Actions is preferred.)
4. Add the site to Google Search Console and Bing Webmaster Tools, then submit `/sitemap.xml`.

## Local build
    bundle config set --local path vendor/bundle
    bundle install
    JEKYLL_ENV=production bundle exec jekyll build   # output in _site/
    bundle exec jekyll serve                          # preview at http://localhost:4000

## Writing a post
Create `_posts/YYYY-MM-DD-slug.md` with this front matter: title, seo_title (the `<title>` tag), description (meta, under 155 chars),
tags (the post's labels), episode, episode_title, episode_url, episode_aired, rating (e.g. 4.5).
Links written in Markdown render as plain `<a href>` with no rel attribute, so they are dofollow.

## Top 10
`top-10.md` has `published: false`. Once there are 20 or more posts, fill in the list and delete that line. The nav link appears automatically
once `site.posts.size >= top10_threshold` (20, set in `_config.yml`).
