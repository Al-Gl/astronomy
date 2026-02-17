# Ring Material Zoom — Saturn Page

## Plan

### What we're building
A canvas-based "Ring Material Zoom" interactive component embedded inside the `#ring-system` section of `saturn.astro`. Three zoom levels reveal what the rings really look like up close.

### Three visual levels

| Level | Label | What's drawn |
|-------|-------|--------------|
| 0 | 1× | Saturn planet + smooth glowing rings (ellipses, wide view) |
| 1 | 1,000× | B-Ring interior — horizontal brightness bands with density wave stripes |
| 2 | 1,000,000× | Animated swarm of ice-crystal particles (varying sizes, slow drift) |

### Interaction
- Three toggle buttons at bottom of canvas: **1×** | **1,000×** | **1,000,000×**
- Clicking a button fades the canvas out → redraws new level → fades back in (CSS `transition: opacity 0.2s`)
- Particle view runs a `requestAnimationFrame` loop; other levels are static
- Description text below buttons changes per level

### Canvas (560 × 300px)

**1× — Wide View:**
- Star-field bg (30 tiny white dots)
- Saturn body: circle at center, tan/beige radial gradient
- Ring bands drawn as rotated ellipses (canvas `save/scale/restore` trick):
  - D ring (faint gray), C ring (medium gray), B ring (bright white, widest), Cassini Division (black gap), A ring (pale gray)
- Soft radial glow behind rings

**1,000× — Band View (zoomed into B-Ring):**
- Dark space background
- ~12 horizontal stripes of varying white/gray brightness simulating the B-Ring's density variations
- 2 thin dark "density wave" stripes cutting across
- Corner label: "B-Ring — 25,500 km wide"

**1,000,000× — Particle View (animated):**
- 55 particles initialised with random position, size (2–12px), color (mostly icy-white/light-blue, ~20% gray-rock), and very slow drift velocity
- `requestAnimationFrame` loop moves particles; they wrap at canvas edges
- Larger particles get a subtle shimmer (opacity oscillation)
- Corner label: "Particles range from sand grains to mountain-sized chunks"

### Files to change
1. **`saturn.astro`** — 4 additions:
   - TOC `<li>` entry "Ring Material Zoom" linking to `#ring-zoom`
   - New `<div id="ring-zoom">` block embedded at the end of the `#ring-system` section (before closing `</section>`)
   - `<script>` block appended before `</script>` (self-contained, no globals conflict)
   - CSS appended before `</style>`

---

## Todo Items
- [ ] 1. Add TOC entry in saturn.astro
- [ ] 2. Add Ring Zoom HTML inside `#ring-system` section
- [ ] 3. Add Ring Zoom JS before `</script>`
- [ ] 4. Add Ring Zoom CSS before `</style>`
