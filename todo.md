# Todo — The Astronomy Space

---

## Atlas Leaf Pages — Design Consistency Audit (DONE 2026-09-24)

Audited all 44 leaf pages under `/atlas/{planets,stars,galaxies,nebulae,constellations,small-bodies}/*`.
**Good news:** HTML structure is identical on every page (same hero → breadcrumbs → TOC sidebar → answer capsule → sections → FAQ), no inline styles, and the CSS rules are the same everywhere (stars + small-bodies just have them written out long-form, which renders identically).

**What actually differs:**
1. **Stars (8 pages) — broken breadcrumb separator.** CSS uses `'›'` (invalid in CSS) → renders literal text "u203a" between crumbs instead of `›`. All other categories use `'\203a'`.
2. **Constellations (8 pages) — no hero image.** All 8 `Hero_*.jpg` files were never generated → empty black hero. (Already listed as pending below.)
3. **Small bodies (4 pages) — generic hero.** Asteroids, comets, dwarf-planets, meteors all reuse the wide `Hero_solar.jpg` planet-lineup banner instead of their own subject image.
4. **Nebulae (8 pages) — different hero style.** Full-bleed colourful scenes (some letterboxed with black bars) instead of the "single subject on pure black" look used by planets/stars/galaxies. Emission + HII-regions heroes are near-duplicates.
5. **Planets only** have `object-position: right center` on the hero (matches their subject-right images; only affects mobile crop).

### Todo items
- [x] 1. Fix stars breadcrumb separator `'›'` → `'\203a'` (8 files, one-line change each)
- [x] 2. Generate 8 constellation hero images (subject on black template)
- [x] 3. Generate 4 small-bodies hero images (asteroids, comets, dwarf-planets, meteors) and point each page at its own image
- [x] 4. Regenerate 8 nebula heroes to the "subject on black" template (approved)
- [x] 4b. Regenerate the 2 remaining full-frame outliers: stars/supergiants, galaxies/clusters
- [x] 5. Build + visually spot-check (contact sheet of all 44 heroes)
- [x] 6. Add review section to review.md
- [ ] Later: Observatory section consistency pass (deferred by owner)

---

## Constellation Family Sub-Pages (PAGES DONE 2026-07-24)

The `atlas/constellations.astro` hub linked to 8 family pages that didn't exist yet (dead links). Built all 8 following the `galaxies/spiral/index.astro` leaf template. Build verified — all 8 emit to `dist/atlas/constellations/`.

- [x] `zodiac/index.astro` — the 12 ecliptic constellations
- [x] `circumpolar/index.astro` — never-setting N & S patterns
- [x] `orion-family/index.astro` — Orion, Canis Major/Minor, Monoceros, Lepus
- [x] `ursa-major-family/index.astro` — the Great Bear group (10 constellations)
- [x] `perseus-family/index.astro` — Perseus myth cycle (9 constellations)
- [x] `hercules-family/index.astro` — largest family (19 constellations)
- [x] `heavenly-waters/index.astro` — aquatic-themed group (9 constellations)
- [x] `la-caille-family/index.astro` — southern scientific-instrument set (13)
- [x] Added hub + 8 sub-page URLs to sitemap.xml.ts and llms.txt

### Follow-up (images — still pending; pages reference these paths)
- [x] 8 hero images (done 2026-09-24) `Hero_{slug}.jpg` (subject right, pure black left template) — slugs: zodiac, circumpolar, orion-family, ursa-major, perseus, hercules, heavenly-waters, la-caille
- [ ] 8 hub card images `card_*.jpg` (hub still shows broken card thumbnails)

---

## Hero Images — 8 Star Sub-Pages (COMPLETE 2026-02-19)

- [x] `public/images/Hero_main-sequence.jpg` — G-type yellow dwarf, photosphere granulation, limb darkening
- [x] `public/images/Hero_red-giants.jpg` — Enormous bloated red-orange sphere, diffuse outer atmosphere
- [x] `public/images/Hero_white-dwarfs.jpg` — Small dense brilliant blue-white sphere, hard crisp edge
- [x] `public/images/Hero_neutron-stars.jpg` — Tiny glowing blue-white sphere with twin polar jet beams
- [x] `public/images/Hero_black-holes.jpg` — Black Schwarzschild sphere with glowing accretion disk
- [x] `public/images/Hero_supergiants.jpg` — Massive brilliant blue supergiant with stellar wind glow
- [x] `public/images/Hero_binary-systems.jpg` — Red giant + hot blue companion with gas transfer stream
- [x] `public/images/Hero_variable-stars.jpg` — Pulsating Cepheid yellow supergiant with expanding shell halo

---

## Binoculars Pages — Bug Fix + Hero Images (PENDING)

### Bug Fix: Answer Capsule stretched full width
Affects 6 pages where `<aside class="answer-capsule">` is outside any `.container`.
Fix: wrap each in `<div class="container">...</div>`.

- [x] Fix `accessories-maintenance/index.astro`
- [x] Fix `beginners-guide/index.astro`
- [x] Fix `deep-sky-targets/index.astro`
- [x] Fix `image-stabilized/index.astro`
- [x] Fix `moon-observing/index.astro`
- [x] Fix `planetary-observing/index.astro`

### Hero Images (6 missing)
- [x] `Hero_binocular_accessories.jpg` — binoculars with cleaning kit, tripod adapter on dark table
- [x] `Hero_beginners_guide.jpg` — person holding binoculars pointing at starry night sky
- [x] `Hero_deep_sky_targets.jpg` — wide-field binocular view of Milky Way / star cluster
- [x] `Hero_image_stabilized_binoculars.jpg` — IS binoculars mid-air, cityscape/sky background
- [x] `Hero_moon_observing.jpg` — close-up Moon surface (craters) seen through binocular eyepiece
- [x] `Hero_planetary_observing.jpg` — Jupiter or Saturn through binoculars, dark sky

---

## Saturn Ring Material Zoom — Interactive Component (PENDING)

Canvas-based interactive embedded in the `#ring-system` section of `saturn.astro`. Three zoom levels reveal what the rings look like up close.

### Three visual levels

| Level | Label | What's drawn |
|-------|-------|--------------|
| 0 | 1× | Saturn planet + smooth glowing rings (ellipses, wide view) |
| 1 | 1,000× | B-Ring interior — horizontal brightness bands with density wave stripes |
| 2 | 1,000,000× | Animated swarm of ice-crystal particles (varying sizes, slow drift) |

### Todo items
- [ ] 1. Add TOC entry in `saturn.astro`
- [ ] 2. Add Ring Zoom HTML inside `#ring-system` section
- [ ] 3. Add Ring Zoom JS before `</script>`
- [ ] 4. Add Ring Zoom CSS before `</style>`

---

## Completed

- [x] **8 Planet type infographics** — Info_terrestrial-planets, Info_gas-giants, Info_ice-giants, Info_dwarf-planets, Info_exoplanets, Info_super-earths, Info_hot-jupiters, Info_rogue-planets — dark space sci-fi style matching moon_info_basic2.jpg template (2026-02-20)
- [x] **8 Galaxy hero images** — Hero_spiral, Hero_elliptical, Hero_irregular, Hero_lenticular, Hero_dwarf, Hero_milky-way, Hero_active, Hero_clusters — subject right, pure black left template (2026-02-19)
- [x] **8 Galaxy sub-pages** — spiral, elliptical, irregular, lenticular, dwarf, milky-way, active, clusters — full content, Schema markup, hero images, sitemap + llms.txt updated (2026-02-19)
- [x] **sitemap.xml & llms.txt** — Fully rebuilt to include all pages: solar system, small bodies, stars, galaxies, constellations, nebulae (8 sub-pages), planets (8 sub-pages), telescopes (9 sub-pages), binoculars (9 sub-pages), stargazing guides (2026-02-19)
- [x] **8 Nebula sub-pages** — emission, reflection, dark, planetary, supernova-remnants, hii-regions, molecular-clouds, protoplanetary — all created with full content, Schema markup, hero images (2026-02-17)
- [x] **8 Planet sub-pages** — terrestrial-planets, gas-giants, ice-giants, dwarf-planets, exoplanets, super-earths, hot-jupiters, rogue-planets — all created with full content, Schema markup, hero images (2026-02-17/19)
- [x] **Planet hero images regenerated** — 8 images replaced to match Mars reference style (subject right, pure black left) (2026-02-19)
- [x] **Stargazing in India** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero + hanle + spiti + rann), Schema markup, sitemap + llms.txt updated (2026-02-19)
- [x] **Stargazing in China** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero + qinghai + xinjiang + yunnan), Schema markup, sitemap + llms.txt updated (2026-02-19)
- [x] **Stargazing in Germany** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero + eifel + westhavelland + rhoen), Schema markup, sitemap + llms.txt updated (2026-02-19)
- [x] **Stargazing in Poland** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero + bieszczady + tatra + bialowieza), Schema markup, sitemap + llms.txt updated (2026-02-19)
- [x] **Stargazing index.astro** — 6 guide cards total (Scandinavia, England, India, China, Germany, Poland) (2026-02-19)
- [x] **Hero centering fix** — India, China, Germany, Poland hero headings centred to match Scandinavia/England (2026-02-19)
- [x] **Inline images for England & Scandinavia** — 3 inline images per page added using `.inline-image` CSS class, generated with nano-banana (2026-03-26)
- [x] **Stargazing in France** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero_france + cevennes + provence + pyrenees), Schema markup, llms.txt updated (2026-03-26)
- [x] **Stargazing in Spain** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero_spain + teide + extremadura + sierra_nevada), Schema markup, llms.txt updated (2026-03-26)
- [x] **Stargazing in Sweden** — Full SEO guide, 12 sections, 3 info-boxes, 6 FAQs, 4 images (Hero_sweden + abisko + lapland + southern), Schema markup, llms.txt updated (2026-03-26)
- [x] **Stargazing index.astro** — 9 guide cards total (added France, Spain, Sweden) (2026-03-26)
- [x] **Sweden link from Scandinavia** — Added inline link to /chronicles/stargazing/sweden/ in the Sweden section of scandinavia.astro (2026-03-26)
