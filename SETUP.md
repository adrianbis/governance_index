# Getting the site online — one-time setup

Follow this once, from top to bottom. Nothing here needs any coding, and nothing
needs anything installed on your computer. Total cost: about **$8–12 for the
first year** (the domain), and **$0 for everything else, permanently**.

Set aside about an hour. Steps 1–4 get the site live on a free web address, and
you can stop there and do the rest another day.

---

## Before you start: what the pieces do

Three services, each doing one job.

| Service | What it does | Cost |
|---|---|---|
| **GitHub** | Stores the files and keeps a history of every change. This is where you edit the site. | Free |
| **Cloudflare Pages** | Watches GitHub and publishes the site to the internet whenever you change something. | Free |
| **Porkbun** | Sells you the web address (the domain). | ~$8–12/year |

You never have to touch a terminal, install anything, or run a build. You edit a
file on the GitHub website, and about thirty seconds later the live site shows
the change.

---

## Step 1 — Create a GitHub account

1. Go to <https://github.com/signup>.
2. Sign up with your email. Pick a username you're happy appearing publicly —
   it will show in the repository address. Something like `cbalbis` is fine.
3. Choose the **Free** plan.
4. Verify your email when GitHub asks.
5. Turn on two-factor authentication when prompted. GitHub requires it, and you
   want it anyway.

---

## Step 2 — Create the repository and upload the site

A "repository" (repo) is just a folder that keeps its history.

1. Once signed in, click the **+** at the top right → **New repository**.
2. **Repository name:** `governance-index` (or whatever you like — it isn't
   shown to visitors).
3. **Description:** something short, e.g. *AI Governance Design Index — website*.
4. Choose **Public**.
   - Public is the right choice here: it's an open research project, it makes
     the work citable and inspectable, and it costs nothing. Private also works
     with Cloudflare if you'd rather wait until launch — you can flip it to
     public later in Settings.
5. Leave every checkbox unticked (don't add a README, .gitignore or licence —
   the files you have already include them).
6. Click **Create repository**.
7. On the next screen click **uploading an existing file**.
8. Unzip the site folder on your computer. Then drag **the contents** of the
   folder into the browser window — that is `index.html`, `rubric.html`,
   `frameworks.html`, `404.html`, `robots.txt`, `sitemap.xml`, `LICENSE`,
   `LICENSE-CONTENT.md`, `README.md`, `SETUP.md`, and the `assets` and `tools`
   folders.

   > Drag the **files themselves**, not the folder that contains them. If you
   > drag the outer folder you'll end up with `governance-index/index.html`
   > inside the repo and the site won't load. If that happens, delete the
   > files and upload again — nothing is broken.

9. At the bottom, in **Commit changes**, type `Initial site` and click
   **Commit changes**.

You should now see your files listed on the repository page.

---

## Step 3 — Publish it with Cloudflare Pages

1. Go to <https://dash.cloudflare.com/sign-up> and create a free account.
   Verify your email.
2. In the left sidebar, open **Compute (Workers & Pages)** → **Create** →
   the **Pages** tab → **Connect to Git**.
3. Click **Connect GitHub**, sign in, and authorise Cloudflare. When GitHub asks
   which repositories to grant access to, choose **Only select repositories**
   and pick `governance-index`.
4. Back in Cloudflare, select the `governance-index` repository → **Begin setup**.
5. Fill in the build settings **exactly like this** — this is the step people get
   wrong:

   | Field | Value |
   |---|---|
   | Project name | `governance-index` |
   | Production branch | `main` |
   | Framework preset | **None** |
   | Build command | **leave completely empty** |
   | Build output directory | `/` |

   There is no build step. The site is plain HTML, so Cloudflare just copies the
   files. If you set a framework preset here, the deploy will fail.

6. Click **Save and Deploy**. Wait about a minute.
7. Cloudflare gives you a free address like
   `governance-index.pages.dev`. **Open it — your site is live.**

From now on, every time you commit a change on GitHub, Cloudflare republishes
within about thirty seconds. You never repeat step 3.

> Free plan limits, for reference: 500 deploys per month, up to 20,000 files, and
> 25 MB per file. You will not come close to any of these.

---

## Step 4 — Check it, then take a breath

Open the `.pages.dev` address on your phone as well as your laptop. Click every
link in the navigation. If anything looks wrong, it's almost always a filename
mismatch — check the file is named exactly as the link expects, including
capital letters.

**You can stop here.** The site is published and free forever at this address.
Steps 5 onward give it a proper name.

---

## Step 5 — Buy the domain at Porkbun

1. Go to <https://porkbun.com> and search for the name you want.
2. Prices as of September 2026: **.org is about $8 for the first year and about
   $12 to renew**; **.com is about $11**; **.net about $13**. WHOIS privacy —
   which keeps your home address out of the public domain records — is **free
   and included**, and you should keep it on.
3. Avoid `.ai` — it runs around $50–60 a year, well over your budget, and buys
   you nothing an `.org` doesn't.
4. For a non-commercial research index, **.org** reads best.
5. Create the Porkbun account, buy the domain, and turn on auto-renew.

> **Watch the renewal price, not the first-year price.** Sale pricing applies to
> year one only. Put a calendar reminder eleven months out regardless of
> auto-renew; a lapsed domain is how research sites quietly disappear.

---

## Step 6 — Point the domain at Cloudflare

This moves your domain's control panel to Cloudflare, which makes everything
afterwards simpler and gives you free HTTPS, email forwarding and analytics.

1. In the Cloudflare dashboard, click **Add a domain**, type your domain, and
   choose the **Free** plan.
2. Cloudflare scans for existing records (there will be none) and then shows you
   **two nameservers**, something like `xena.ns.cloudflare.com`. Copy both.
3. In a second tab, go to Porkbun → **Account** → **Domain Management** → click
   your domain → **Authoritative Nameservers** → **Edit**.
4. Delete Porkbun's nameservers, paste in Cloudflare's two, and save.
5. Back in Cloudflare, click **Continue** / **Check nameservers**.

This takes anywhere from ten minutes to a few hours to take effect. Cloudflare
emails you when it's done. Nothing is broken while you wait.

---

## Step 7 — Attach the domain to the site

1. Cloudflare dashboard → **Compute (Workers & Pages)** → your
   `governance-index` project → **Custom domains** → **Set up a custom domain**.
2. Enter your domain without `www` (e.g. `governanceindex.org`) → **Continue** →
   **Activate domain**.
3. Repeat for the `www` version (e.g. `www.governanceindex.org`). Cloudflare
   redirects one to the other automatically.
4. Wait a few minutes. The HTTPS certificate is issued automatically and free.

Visit your domain. Done.

---

## Step 8 — Replace `example.org` everywhere

The files ship with `https://example.org` as a stand-in. Now that you have the
real address, replace it. It appears in:

- `index.html` — canonical link, the four `og:` / social tags, the citation
  block, and the contact email address
- `rubric.html` — canonical link and social tags
- `frameworks.html` — canonical link, social tags, citation block
- `robots.txt` — the sitemap line
- `sitemap.xml` — all three URLs
- `LICENSE-CONTENT.md` — the suggested citation

To edit a file on GitHub: open it, click the **pencil icon**, make the change,
scroll down, click **Commit changes**. Cloudflare republishes automatically.

> These tags don't change how the site looks. They control what appears when
> someone shares a link on LinkedIn, and how search engines list you. Worth the
> ten minutes.

---

## Step 9 — A free email address at your domain (optional, 5 minutes)

`hello@yourdomain.org` looks considerably more serious on a research site than a
personal Gmail, and Cloudflare forwards it to your real inbox for free.

1. Cloudflare dashboard → your domain → **Email** → **Email Routing** →
   **Get started**.
2. Create a custom address: `hello@yourdomain.org` → forward to your real email.
3. Cloudflare adds the necessary records for you; click **Add records
   automatically**.
4. Confirm the verification email that lands in your real inbox.
5. Update the `mailto:` link in `index.html` to match.

This forwards mail *in* only. To reply *from* that address you'd need a mail
provider, which costs money — for now, replying from your normal address is
perfectly normal practice.

---

## Step 10 — Privacy-friendly analytics (optional, 2 minutes)

Cloudflare Web Analytics is free, uses no cookies, and does not track
individuals — so it needs **no cookie banner**, which matters given who your
readers are.

1. Cloudflare dashboard → **Analytics & Logs** → **Web Analytics** →
   **Add a site**.
2. Enter your domain. Because your site is already on Cloudflare Pages, you can
   enable it with a single toggle — no code to paste.

---

## If something goes wrong

| Symptom | Almost always the cause |
|---|---|
| Deploy fails in Cloudflare | A build command or framework preset was set. Both must be empty / None. |
| Site loads but has no styling | The `assets` folder didn't upload, or uploaded one level too deep. Check the repo shows `assets/style.css`. |
| A link gives a 404 | Filename or capitalisation mismatch. `Rubric.html` and `rubric.html` are different files to a web server. |
| Domain shows a Cloudflare error page | Nameservers haven't finished propagating. Wait, then re-check step 6. |
| Change doesn't appear | Check the commit actually saved on GitHub, then check the Deployments tab in Cloudflare for a red build. Hard-refresh with Ctrl+Shift+R (Cmd+Shift+R on a Mac). |

If a change ever breaks the site, GitHub keeps every previous version: open the
file, click **History**, open the version before the break, and copy its
contents back in. Nothing is ever permanently lost.
