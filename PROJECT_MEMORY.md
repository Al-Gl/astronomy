1. Executive Summary
Project Name: TheAstronomy.space Objective: Build a high-performance, SEO-first astronomy hobby website targeting beginners and intermediate amateur astronomers. Monetization Strategy: Affiliate marketing (high-ticket telescopes/gear) and ad revenue (Mediavine/Raptive target). Tech Stack: Astro (Framework), Tailwind CSS (Styling), Markdown/MDX (Content), Cloudflare Pages (Hosting).

2. Strategic Architecture & SEO
This project uses a Topic Cluster (Hub & Spoke) model to establish topical authority.

Core Hubs (Categories):

/atlas/: The definitive Knowledge Database. Evergreen guides on planets, stars, and galaxies. (Primary SEO driver).

/gear-reviews/: Transactional content for affiliate conversions (Telescopes, Binoculars, Cameras).

/blog/: Dynamic content, news, "What's in the sky tonight," and tutorials.

/tools/: Interactive engagement tools (Telescope Calculator, Light Pollution Map).

SEO & Content Rules:

Speed: 100/100 Lighthouse score is mandatory.

Semantic HTML: No "div soup." Use <article>, <section>, and <nav> appropriately.

Slug Structure: Use logical hierarchies, e.g., /atlas/solar-system/mars/.

3. Knowledge Database (The Atlas) Standards
Every entry in the Atlas hub must follow these structural requirements:

Page Architecture:

Hero Section: H1 Header + High-res Hero Image + "Fast Facts" Data Bar (Physical Stats).

The Abstract: 2–3 sentence high-level summary for the Meta Description.

Core Content: Structured H2 sections (Composition, Orbit, History, Observation).

Media: Use <Image /> for all infographics and celestial photography.

Observation Guide: Specific section for hobbyist viewing tips (naked eye vs. telescope).

Schema Markup (JSON-LD):

BreadcrumbList: Mandatory for all /atlas/ sub-pages to show hierarchy in SERPs.

Article/TechArticle: Use for planetary and deep-sky object guides.

4. Technical Implementation Rules
Framework: Astro. Prefer .astro components for static UI. Use "Islands" only for interactive tools.

Styling: Tailwind CSS. Theme: "Deep Space" (Dark Mode).

Primary Background: #050505

Accent Color: Nebula Purple (#6d28d9)

Images: Always use astro:assets. Mandatory alt text for SEO.

Content: Use Astro Content Collections for type-safety in the /atlas/ and /blog/ directories.

5. Feature Roadmap (Phased Build)
Phase 1 (Foundation): Responsive Layout, Dark Theme, SEO-optimized Header/Footer.

Phase 2 (The Atlas): Build the Solar System hub and individual planet templates.

Phase 3 (Content Engine): Setup Content Collections for Blog and Gear Reviews.

Phase 4 (Monetization UI): Build "Affiliate Card" components and Disclosure tags.

Phase 5 (Interactive): Build "Telescope Selection Quiz" or "Live Observatory" data tools.