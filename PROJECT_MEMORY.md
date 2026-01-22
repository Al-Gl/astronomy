1. Executive Summary
Project Name: TheAstronomy.space

Objective: Build a high-performance, SEO-first astronomy hobby website targeting beginners and intermediate amateur astronomers.

Monetization Strategy: Affiliate marketing (high-ticket telescopes/gear) and ad revenue (Mediavine/Raptive target).

Tech Stack: Astro (Framework), Tailwind CSS (Styling), Markdown/MDX (Content), Cloudflare Pages (Hosting).

2. Strategic Architecture & SEO
This project uses a Topic Cluster (Hub & Spoke) model to establish topical authority.

Core Hubs (Categories):
/planets/: Evergreen beginner content about the solar system.

/gear-reviews/: Transactional content for affiliate conversions (Telescopes, Binoculars, Cameras).

/blog/: Dynamic content, news, "What's in the sky tonight," and tutorials.

/tools/: Interactive engagement tools (Telescope Calculator, Light Pollution Map).

SEO Constraints:
Speed: 100/100 Lighthouse score is mandatory.

Schema: Every page must have specific JSON-LD (e.g., Product for reviews, Article for blogs, HowTo for guides).

Format: Use semantic HTML5. No div soup. Use <article>, <section>, and <aside> appropriately.

3. Technical Implementation Rules
The following rules apply to all code generation in Cursor/Claude Code:

Framework: Use Astro. Prefer .astro components for static UI and only use React/Vue "Islands" if complex client-side state is required.

Styling: Use Tailwind CSS. Theme: "Deep Space" (Dark Mode).

Primary Background: #050505

Accent Color: Nebula Purple (#6d28d9)

Images: Always use the <Image /> component from astro:assets for automatic WebP conversion and lazy loading.

Content: Store all long-form content in src/content/ using Content Collections for type-safety.

4. Feature Roadmap (Phased Build)
Phase 1 (Foundation): Responsive Layout, SEO-optimized Header/Footer, Dark Theme.

Phase 2 (Content Engine): Setup Content Collections for Blog and Gear Reviews.

Phase 3 (Monetization UI): Build "Affiliate Card" components with "Check Price" buttons and Disclosure tags.

Phase 4 (Interactive): Build a "Telescope Selection Quiz" using Astro + a small React component.