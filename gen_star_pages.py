"""Generator script for 8 star type pages."""
import os

base_dir = r"C:\Users\Aldin\Desktop\Aldin\Websites\Claude Code\Astronomy\src\pages\atlas\stars"

shared_style = r"""<style>
  /* Progress Bar */
  .progress-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: rgba(255, 255, 255, 0.1);
    z-index: 1000;
  }

  .progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--color-accent-cyan), var(--color-accent-blue));
    transition: width 0.1s ease-out;
  }

  /* Hero Section */
  .hero {
    position: relative;
    min-height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .hero-image {
    position: absolute;
    inset: 0;
    z-index: 0;
  }

  .hero-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.3) 0%,
      rgba(0, 0, 0, 0.6) 50%,
      rgba(0, 0, 0, 0.9) 100%
    );
  }

  .hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: var(--space-xl);
  }

  .hero h1 {
    font-family: var(--font-heading);
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 700;
    margin-bottom: var(--space-sm);
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  }

  .hero-subtitle {
    font-size: clamp(1.25rem, 3vw, 1.75rem);
    color: var(--color-accent-cyan);
    font-weight: 500;
  }

  /* Breadcrumbs */
  .breadcrumbs {
    margin-bottom: var(--space-lg);
  }

  .breadcrumbs ol {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    list-style: none;
    padding: 0;
    margin: 0;
    font-size: 0.9rem;
  }

  .breadcrumbs li {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .breadcrumbs li:not(:last-child)::after {
    content: '\u203a';
    color: var(--color-text-secondary);
  }

  .breadcrumbs a {
    color: var(--color-text-secondary);
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .breadcrumbs a:hover {
    color: var(--color-accent-cyan);
  }

  .breadcrumbs li[aria-current="page"] {
    color: var(--color-text-primary);
  }

  /* Article Layout with Sidebar */
  .content-wrapper {
    padding: var(--space-2xl) 0;
  }

  .article-layout {
    display: grid;
    grid-template-columns: 1fr;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-md);
    gap: var(--space-xl);
  }

  @media (min-width: 1024px) {
    .article-layout {
      grid-template-columns: 220px 1fr;
      gap: var(--space-2xl);
    }
  }

  /* Sticky TOC Sidebar */
  .toc-sidebar {
    display: none;
  }

  @media (min-width: 1024px) {
    .toc-sidebar {
      display: block;
    }

    .toc {
      position: sticky;
      top: calc(var(--space-xl) + 3px);
      max-height: calc(100vh - var(--space-2xl));
      overflow-y: auto;
    }
  }

  .toc h2 {
    font-family: var(--font-heading);
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: var(--space-md);
    color: var(--color-text-secondary);
  }

  .toc ol {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .toc li {
    margin-bottom: 0.25rem;
  }

  .toc a {
    display: block;
    padding: 0.5rem 0;
    padding-left: var(--space-sm);
    color: var(--color-text-secondary);
    text-decoration: none;
    font-size: 0.9rem;
    border-left: 2px solid transparent;
    transition: all 0.2s ease;
  }

  .toc a:hover {
    color: var(--color-text-primary);
    border-left-color: rgba(6, 182, 212, 0.5);
  }

  .toc a.active {
    color: var(--color-accent-cyan);
    border-left-color: var(--color-accent-cyan);
  }

  /* Main Content */
  .main-content {
    max-width: 800px;
  }

  /* Answer Capsule */
  .answer-capsule {
    display: flex;
    gap: var(--space-md);
    padding: var(--space-lg);
    margin-bottom: var(--space-2xl);
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: var(--radius-lg);
    position: relative;
    overflow: hidden;
  }

  .answer-capsule::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at top left, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
    pointer-events: none;
  }

  .capsule-icon {
    flex-shrink: 0;
    width: 40px;
    height: 40px;
    color: var(--color-accent-cyan);
    opacity: 0.8;
  }

  .capsule-icon svg {
    width: 100%;
    height: 100%;
  }

  .answer-capsule p {
    margin: 0;
    font-size: 1.1rem;
    line-height: 1.7;
    color: var(--color-text-primary);
    position: relative;
  }

  /* Content Sections */
  .content-section {
    margin-bottom: var(--space-2xl);
  }

  .content-section h2 {
    font-family: var(--font-heading);
    font-size: clamp(1.75rem, 4vw, 2.25rem);
    margin-bottom: var(--space-md);
    padding-bottom: var(--space-sm);
    border-bottom: 2px solid rgba(6, 182, 212, 0.3);
    color: var(--color-text-primary);
  }

  .content-section h3 {
    font-family: var(--font-heading);
    font-size: clamp(1.25rem, 3vw, 1.5rem);
    margin-top: var(--space-xl);
    margin-bottom: var(--space-md);
    color: var(--color-accent-cyan);
  }

  .content-section h4 {
    font-family: var(--font-heading);
    font-size: 1.1rem;
    margin-top: var(--space-lg);
    margin-bottom: var(--space-sm);
    color: var(--color-accent-blue);
  }

  .content-section p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--color-text-secondary);
    margin-bottom: var(--space-md);
  }

  .content-section ul,
  .content-section ol {
    margin-bottom: var(--space-md);
    padding-left: var(--space-lg);
  }

  .content-section li {
    font-size: 1.05rem;
    line-height: 1.7;
    color: var(--color-text-secondary);
    margin-bottom: 0.5rem;
  }

  /* Info Box */
  .info-box {
    padding: var(--space-lg);
    margin: var(--space-lg) 0;
  }

  .info-box h3 {
    margin-top: 0;
    font-size: 1.1rem;
    color: var(--color-accent-blue);
  }

  .info-box ul {
    margin: 0;
    padding-left: var(--space-md);
  }

  .info-box li {
    font-size: 1rem;
    margin-bottom: 0.4rem;
  }

  .data-source {
    font-size: 0.8rem;
    color: var(--color-text-secondary);
    opacity: 0.7;
    margin-top: -0.5rem;
    margin-bottom: var(--space-lg);
  }

  .data-source a {
    color: var(--color-accent-cyan);
  }

  /* Mission List */
  .mission-list {
    list-style: none;
    padding: 0;
  }

  .mission-list li {
    padding: var(--space-sm) 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  }

  .mission-list li:last-child {
    border-bottom: none;
  }

  /* Facts List */
  .facts-list {
    list-style: none;
    padding: 0;
  }

  .facts-list li {
    padding: var(--space-md) 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  }

  .facts-list li:last-child {
    border-bottom: none;
  }

  /* Resource List */
  .resource-list {
    list-style: none;
    padding: 0;
  }

  .resource-list li {
    padding: var(--space-sm) 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  }

  .resource-list li:last-child {
    border-bottom: none;
  }

  .resource-list a {
    color: var(--color-accent-cyan);
    font-weight: 500;
  }

  /* FAQ Section */
  .faq-section {
    margin-top: var(--space-2xl);
    padding-top: var(--space-xl);
    border-top: 1px solid rgba(148, 163, 184, 0.1);
  }

  .faq-list {
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
  }

  .faq-item {
    background: var(--glass-bg);
    border: var(--glass-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    transition: all 0.3s ease;
  }

  .faq-item[open] {
    background: rgba(6, 182, 212, 0.05);
    border-color: rgba(6, 182, 212, 0.2);
  }

  .faq-question {
    padding: var(--space-md) var(--space-lg);
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: 500;
    color: var(--color-text-primary);
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: color 0.2s ease;
  }

  .faq-question::-webkit-details-marker {
    display: none;
  }

  .faq-question::after {
    content: '+';
    font-size: 1.5rem;
    font-weight: 300;
    color: var(--color-accent-cyan);
    transition: transform 0.3s ease;
  }

  .faq-item[open] .faq-question::after {
    transform: rotate(45deg);
  }

  .faq-question:hover {
    color: var(--color-accent-cyan);
  }

  .faq-answer {
    padding: 0 var(--space-lg) var(--space-lg);
  }

  .faq-answer p {
    margin: 0;
    font-size: 1rem;
    line-height: 1.7;
    color: var(--color-text-secondary);
  }

  /* Glassmorphism */
  .glass {
    background: var(--glass-bg);
    border: var(--glass-border);
    border-radius: var(--radius-lg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
  }

  /* Responsive */
  @media (max-width: 768px) {
    .hero {
      min-height: 50vh;
    }

    .hero-content {
      padding: var(--space-lg);
    }

    .article-layout {
      padding: 0 var(--space-sm);
    }

    .answer-capsule {
      flex-direction: column;
      align-items: flex-start;
    }

    .capsule-icon {
      width: 32px;
      height: 32px;
    }
  }
</style>"""

shared_script = """<script>
  // Reading Progress Bar
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
      progressBar.style.width = scrollPercent + '%';
    }
  });

  // Active TOC highlighting
  const sections = document.querySelectorAll('.content-section');
  const tocLinks = document.querySelectorAll('.toc a');

  const observerOptions = {
    rootMargin: '-20% 0% -70% 0%'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        tocLinks.forEach(link => link.classList.remove('active'));
        const activeLink = document.querySelector(`.toc a[href="#${entry.target.id}"]`);
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }, observerOptions);

  sections.forEach(section => observer.observe(section));
</script>"""

capsule_icon_html = """<div class="capsule-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 6v6l4 2"/>
            </svg>
          </div>"""


def make_page(slug, title_tag, description, h1, subtitle, capsule_text, faq_items, toc_items, body_content, keywords_list):
    faq_js_parts = []
    for q, a in faq_items:
        faq_js_parts.append("  {\n    question: " + repr(q) + ",\n    answer: " + repr(a) + "\n  }")
    faq_js = "[\n" + ",\n".join(faq_js_parts) + "\n]"

    keywords_js = "[" + ", ".join(repr(k) for k in keywords_list) + "]"

    toc_html = "\n".join(
        "            <li><a href=\"#" + tid + "\">" + tlabel + "</a></li>"
        for tid, tlabel in toc_items
    )

    breadcrumb_li = (
        "          <li><a href=\"/\">Home</a></li>\n"
        "          <li><a href=\"/atlas/\">Cosmic Atlas</a></li>\n"
        "          <li><a href=\"/atlas/stars/\">Stars</a></li>\n"
        "          <li aria-current=\"page\">" + h1 + "</li>"
    )

    content = (
        "---\n"
        "import MainLayout from '../../../../layouts/MainLayout.astro';\n"
        "import Schema from '../../../../components/Schema.astro';\n"
        "\n"
        "const breadcrumbs = [\n"
        "  { name: 'Home', url: '/' },\n"
        "  { name: 'Cosmic Atlas', url: '/atlas/' },\n"
        "  { name: 'Stars', url: '/atlas/stars/' },\n"
        "  { name: " + repr(h1) + ", url: '/atlas/stars/" + slug + "/' }\n"
        "];\n"
        "\n"
        "const articleData = {\n"
        "  headline: " + repr(title_tag.split(" | ")[0]) + ",\n"
        "  description: " + repr(description) + ",\n"
        "  datePublished: '2025-01-22',\n"
        "  dateModified: '2025-01-22',\n"
        "  author: 'The Astronomy Space',\n"
        "  image: '/images/Hero_" + slug + ".jpg',\n"
        "  keywords: " + keywords_js + "\n"
        "};\n"
        "\n"
        "const faqData = " + faq_js + ";\n"
        "---\n"
        "\n"
        "<MainLayout\n"
        "  title=" + repr(title_tag) + "\n"
        "  description=" + repr(description) + "\n"
        ">\n"
        "  <Schema type=\"BreadcrumbList\" breadcrumbs={breadcrumbs} />\n"
        "  <Schema type=\"TechArticle\" article={articleData} />\n"
        "  <Schema type=\"FAQPage\" faq={faqData} />\n"
        "\n"
        "  <!-- Reading Progress Bar -->\n"
        "  <div class=\"progress-container\">\n"
        "    <div class=\"progress-bar\" id=\"progressBar\"></div>\n"
        "  </div>\n"
        "\n"
        "  <!-- Hero Section -->\n"
        "  <section class=\"hero\">\n"
        "    <div class=\"hero-image\">\n"
        "      <img src=\"/images/Hero_" + slug + ".jpg\" alt=\"" + h1 + " hero image\" loading=\"eager\" />\n"
        "      <div class=\"hero-overlay\"></div>\n"
        "    </div>\n"
        "    <div class=\"hero-content\">\n"
        "      <nav class=\"breadcrumbs\" aria-label=\"Breadcrumb\">\n"
        "        <ol>\n"
        + breadcrumb_li + "\n"
        "        </ol>\n"
        "      </nav>\n"
        "      <h1>" + h1 + "</h1>\n"
        "      <p class=\"hero-subtitle\">" + subtitle + "</p>\n"
        "    </div>\n"
        "  </section>\n"
        "\n"
        "  <!-- Main Article Content -->\n"
        "  <article class=\"content-wrapper\">\n"
        "    <div class=\"article-layout\">\n"
        "\n"
        "      <!-- Sticky Table of Contents (Left Sidebar) -->\n"
        "      <aside class=\"toc-sidebar\">\n"
        "        <nav class=\"toc\" aria-label=\"Table of Contents\">\n"
        "          <h2>Contents</h2>\n"
        "          <ol>\n"
        + toc_html + "\n"
        "          </ol>\n"
        "        </nav>\n"
        "      </aside>\n"
        "\n"
        "      <!-- Main Content -->\n"
        "      <div class=\"main-content\">\n"
        "\n"
        "        <!-- Answer Capsule -->\n"
        "        <aside class=\"answer-capsule\">\n"
        "          " + capsule_icon_html + "\n"
        "          <p>" + capsule_text + "</p>\n"
        "        </aside>\n"
        "\n"
        + body_content + "\n"
        "\n"
        "        <!-- FAQ Section -->\n"
        "        <section id=\"faq\" class=\"content-section faq-section\">\n"
        "          <h2>Frequently Asked Questions</h2>\n"
        "\n"
        "          <div class=\"faq-list\">\n"
        "            {faqData.map((item) => (\n"
        "              <details class=\"faq-item\">\n"
        "                <summary class=\"faq-question\">{item.question}</summary>\n"
        "                <div class=\"faq-answer\">\n"
        "                  <p set:html={item.answer}></p>\n"
        "                </div>\n"
        "              </details>\n"
        "            ))}\n"
        "          </div>\n"
        "        </section>\n"
        "\n"
        "      </div>\n"
        "    </div>\n"
        "  </article>\n"
        "</MainLayout>\n"
        "\n"
        + shared_script + "\n"
        "\n"
        + shared_style + "\n"
    )
    return content


# ============================================================
# PAGE 1: main-sequence (already created, regenerate cleanly)
# ============================================================
p1_faq = [
    ("What is a main sequence star?",
     "A main sequence star is any star that is actively fusing hydrogen into helium in its core through nuclear fusion. This hydrogen-burning phase represents the longest and most stable period in a star's life. Main sequence stars follow a relationship between luminosity and temperature called the main sequence on the Hertzsprung-Russell diagram. About 90% of all stars in the universe, including our Sun, are currently main sequence stars."),
    ("How long do main sequence stars live?",
     "The lifespan of a main sequence star depends heavily on its mass. Massive blue stars (10+ times the Sun's mass) burn through their fuel in just a few million years. Our Sun will spend about 10 billion years on the main sequence total, with about 5 billion years remaining. Low-mass red dwarf stars are incredibly frugal with their fuel and can shine for trillions of years\u2014far longer than the current age of the universe."),
    ("What are the spectral classes of main sequence stars?",
     "Main sequence stars are classified by their surface temperature into spectral classes: O (blue, >30,000 K), B (blue-white, 10,000-30,000 K), A (white, 7,500-10,000 K), F (yellow-white, 6,000-7,500 K), G (yellow, 5,200-6,000 K), K (orange, 3,700-5,200 K), and M (red, <3,700 K). The mnemonic 'Oh Be A Fine Girl/Guy, Kiss Me' helps remember this sequence. Our Sun is a G-type star."),
    ("Is the Sun a main sequence star?",
     "Yes, the Sun is a main sequence star classified as a G2V yellow dwarf. It has been fusing hydrogen in its core for about 4.6 billion years and has roughly another 5 billion years of main sequence life remaining. When the Sun exhausts its hydrogen fuel, it will expand into a red giant and eventually shed its outer layers, leaving behind a white dwarf. The 'V' in its classification indicates it is a main sequence (dwarf) star."),
    ("What are the most common main sequence stars?",
     "Red dwarf stars (spectral class M) are by far the most common type of star in the universe, making up about 70-75% of all stars. They are small, cool, and extremely long-lived. Despite their abundance, they are too faint to see with the naked eye from Earth. The nearest star to our solar system, Proxima Centauri, is a red dwarf main sequence star just 4.24 light-years away."),
    ("What happens when a main sequence star runs out of hydrogen?",
     "When a main sequence star exhausts the hydrogen in its core, it can no longer maintain the pressure to balance gravity. The core contracts and heats up, which causes the outer layers to expand dramatically, transforming the star into a red giant or supergiant depending on its mass. Low and medium-mass stars (like the Sun) become red giants, then planetary nebulae with white dwarf cores. Massive stars become red supergiants and end their lives in spectacular supernova explosions."),
]

p1_toc = [
    ("introduction", "Introduction"),
    ("physical-characteristics", "Physical Characteristics"),
    ("hr-diagram", "The HR Diagram"),
    ("classification", "Stellar Classification"),
    ("fusion", "Nuclear Fusion"),
    ("lifetimes", "Stellar Lifetimes"),
    ("examples", "Notable Examples"),
    ("observation", "Observation"),
    ("fun-facts", "Interesting Facts"),
    ("resources", "Resources"),
    ("faq", "FAQ"),
]

p1_body = """        <!-- Introduction -->
        <section id="introduction" class="content-section">
          <h2>Introduction to Main Sequence Stars</h2>
          <p>When astronomers talk about the "typical" star, they are almost certainly describing a main sequence star. These are the workhorses of the universe\u2014stars in the prime of their lives, steadily converting hydrogen into helium through nuclear fusion in their cores. Roughly 90% of all stars in existence belong to this category, making them by far the most common stellar type.</p>
          <p>The term "main sequence" comes from the Hertzsprung-Russell diagram, a fundamental tool in stellar astronomy that plots stars by their temperature and luminosity. When you plot thousands of stars on this diagram, the vast majority fall along a diagonal band called the main sequence, stretching from hot, bright blue stars at the top left to cool, dim red stars at the bottom right.</p>
          <p>Main sequence stars come in an astonishing variety. At one extreme are the massive O-type blue giants, dozens of times more massive than the Sun and shining with the power of hundreds of thousands of Suns. At the other extreme are the tiny M-type red dwarfs, barely large enough to sustain hydrogen fusion, glowing so faintly they are invisible to the naked eye even when only a few light-years away. Our Sun sits comfortably in the middle of this range as a perfectly ordinary G-type yellow dwarf.</p>
          <p>Understanding main sequence stars means understanding stellar life itself. Their properties\u2014mass, temperature, luminosity, and lifespan\u2014are all governed by a single fundamental parameter: how much mass they contain. This mass-luminosity relationship makes main sequence stars among the best understood objects in the universe.</p>
        </section>

        <!-- Physical Characteristics -->
        <section id="physical-characteristics" class="content-section">
          <h2>Physical Characteristics</h2>
          <p>The physical properties of main sequence stars span an enormous range, all determined primarily by their initial mass. From the minimum mass needed to sustain hydrogen fusion to the maximum mass before a star becomes unstable, the main sequence encompasses objects wildly different in size, temperature, and power output.</p>
          <div class="info-box glass">
            <h3>Main Sequence Quick Facts</h3>
            <ul>
              <li><strong>Mass Range:</strong> 0.08 to 150 solar masses</li>
              <li><strong>Temperature Range:</strong> ~2,400 K to ~50,000 K</li>
              <li><strong>Luminosity Range:</strong> 0.0001 to 1,000,000 solar luminosities</li>
              <li><strong>Lifetime Range:</strong> Millions to trillions of years</li>
              <li><strong>Percentage of Stars:</strong> ~90% of all stars</li>
              <li><strong>Nearest Example:</strong> Proxima Centauri (4.24 ly)</li>
            </ul>
          </div>
          <p class="data-source">Data: <a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener noreferrer">NASA Stars &amp; Stellar Evolution</a></p>
          <p>The mass-luminosity relationship is one of the most powerful laws in stellar physics. More massive stars have stronger gravity, which compresses their cores more, raises the temperature and pressure, and accelerates the rate of nuclear fusion. This is why a star ten times more massive than the Sun can be thousands of times more luminous.</p>
          <p>Surface temperature determines a star's color. The hottest main sequence stars appear blue-white, while cooler ones appear yellow, orange, or red. This color reflects the peak wavelength of the star's radiation, following Wien's displacement law: the cooler the surface, the redder the light.</p>
        </section>

        <!-- The HR Diagram -->
        <section id="hr-diagram" class="content-section">
          <h2>The Hertzsprung-Russell Diagram</h2>
          <p>The Hertzsprung-Russell (HR) diagram is one of the most important tools in stellar astronomy. Independently developed by Ejnar Hertzsprung and Henry Norris Russell in the early 20th century, it plots a star's luminosity against its surface temperature. When you plot a large sample of stars, a striking pattern emerges: most stars cluster along a diagonal band\u2014the main sequence.</p>
          <h3>The Main Sequence Band</h3>
          <p>The main sequence runs diagonally across the HR diagram from the upper left (hot, luminous blue stars) to the lower right (cool, dim red stars). Stars spend the majority of their lives on this band because hydrogen fusion in the core is the most stable and long-lasting energy source available. A star's position on the main sequence is determined almost entirely by its mass.</p>
          <h3>Mass-Luminosity Relationship</h3>
          <p>Along the main sequence, luminosity scales roughly as the fourth power of mass: L \u221d M^4. This means doubling a star's mass makes it about 16 times more luminous. This steep relationship explains why massive stars are so spectacularly bright and why they exhaust their fuel so quickly.</p>
          <h3>Luminosity Classes</h3>
          <p>The HR diagram also shows that stars of the same temperature can have very different luminosities\u2014indicating different sizes. This led to the luminosity classification system: Class I (supergiants), Class II (bright giants), Class III (giants), Class IV (subgiants), and Class V (main sequence dwarfs). The Sun's full classification, G2V, tells us it is a main sequence star.</p>
        </section>

        <!-- Stellar Classification -->
        <section id="classification" class="content-section">
          <h2>Stellar Classification</h2>
          <p>The modern system for classifying stars was developed at Harvard Observatory in the late 19th and early 20th century, largely through the work of Annie Jump Cannon. Stars are classified by their spectral type, which reflects their surface temperature, followed by a luminosity class.</p>
          <h3>The OBAFGKM Sequence</h3>
          <p>The spectral sequence for main sequence stars, from hottest to coolest, is O, B, A, F, G, K, M. Each letter corresponds to a temperature range and characteristic absorption lines:</p>
          <ul>
            <li><strong>O-type (blue):</strong> Surface temperature above 30,000 K. Ionized helium lines visible. Extremely rare and luminous.</li>
            <li><strong>B-type (blue-white):</strong> 10,000\u201330,000 K. Neutral helium lines. Examples: Spica, Achernar.</li>
            <li><strong>A-type (white):</strong> 7,500\u201310,000 K. Strong hydrogen lines. Examples: Sirius A, Vega.</li>
            <li><strong>F-type (yellow-white):</strong> 6,000\u20137,500 K. Ionized calcium lines. Examples: Procyon A.</li>
            <li><strong>G-type (yellow):</strong> 5,200\u20136,000 K. Many metal lines. Examples: Sun, Alpha Centauri A.</li>
            <li><strong>K-type (orange):</strong> 3,700\u20135,200 K. Molecular bands begin. Examples: Epsilon Eridani, 61 Cygni.</li>
            <li><strong>M-type (red):</strong> Below 3,700 K. Strong molecular bands (TiO). Examples: Proxima Centauri, Barnard's Star.</li>
          </ul>
          <h3>Subclasses and Luminosity Classes</h3>
          <p>Each spectral class is further divided into subclasses 0 through 9 (0 being hottest). Combined with luminosity class V for main sequence stars, we get full designations like G2V (the Sun) or M5.5Ve (Proxima Centauri, where 'e' denotes emission lines).</p>
        </section>

        <!-- Nuclear Fusion -->
        <section id="fusion" class="content-section">
          <h2>Nuclear Fusion</h2>
          <p>The energy that powers main sequence stars comes from nuclear fusion\u2014the process of combining lighter atomic nuclei into heavier ones, releasing energy in the process. For main sequence stars, the fuel is hydrogen and the product is helium.</p>
          <h3>The Proton-Proton Chain</h3>
          <p>In lower-mass stars like the Sun (and all stars cooler than about 1.5 solar masses), the dominant fusion process is the proton-proton (PP) chain. Four hydrogen nuclei (protons) are gradually combined to form one helium-4 nucleus, releasing energy in the form of gamma rays. The Sun converts about 600 million tons of hydrogen into helium every second.</p>
          <h3>The CNO Cycle</h3>
          <p>In more massive stars with core temperatures above about 17 million K, the carbon-nitrogen-oxygen (CNO) cycle becomes the dominant fusion pathway. Carbon acts as a catalyst, facilitating the fusion of four hydrogen nuclei into helium. The CNO cycle is extremely temperature-sensitive\u2014a small increase in temperature dramatically increases energy production.</p>
          <h3>Hydrostatic Equilibrium</h3>
          <p>Main sequence stability arises from hydrostatic equilibrium: the outward pressure from nuclear fusion exactly counteracts the inward pull of gravity. This self-regulating mechanism makes main sequence stars remarkably stable over billions of years.</p>
        </section>

        <!-- Stellar Lifetimes -->
        <section id="lifetimes" class="content-section">
          <h2>Stellar Lifetimes</h2>
          <p>One of the most counterintuitive facts about stars is that the most massive ones die youngest. Because massive stars burn their fuel at such a prodigious rate, they exhaust it far faster than their smaller cousins.</p>
          <h3>The Mass-Lifetime Relationship</h3>
          <p>A star's main sequence lifetime scales roughly as 1/mass^3. A star ten times the Sun's mass has only about 1/1000th the Sun's lifetime. Our Sun will live about 10 billion years total on the main sequence; a 10-solar-mass star would live only about 10 million years.</p>
          <h3>The Extremes</h3>
          <p>At the massive end, the most luminous O-type stars may live only 1-3 million years. At the low-mass end, red dwarf stars could potentially shine for 10 trillion years or more. No red dwarf has ever died of old age because the universe is not yet old enough.</p>
          <h3>The Sun's Timeline</h3>
          <p>Our Sun formed about 4.6 billion years ago and has roughly 5 billion years remaining on the main sequence. In about 5 billion years, the Sun will exhaust its core hydrogen and begin the transition to a red giant.</p>
        </section>

        <!-- Notable Examples -->
        <section id="examples" class="content-section">
          <h2>Notable Main Sequence Stars</h2>
          <p>The night sky is populated almost entirely by main sequence stars. Here are some of the most notable examples spanning the full range of stellar types.</p>
          <h3>The Sun (G2V)</h3>
          <p>Our nearest stellar neighbor is the definitive example of a G-type main sequence star. With a surface temperature of 5,778 K and a luminosity that has powered life on Earth for billions of years, the Sun is the most studied star in the universe.</p>
          <h3>Sirius A (A1V)</h3>
          <p>The brightest star in the night sky, Sirius A is a white A-type main sequence star about 25 times more luminous than the Sun, located just 8.6 light-years away. Sirius has a white dwarf companion, Sirius B.</p>
          <h3>Vega (A0V)</h3>
          <p>One of the brightest stars in the northern hemisphere, Vega is an A-type main sequence star about 40 light-years away. It will become a future "pole star" in about 12,000 years due to precession.</p>
          <h3>Proxima Centauri (M5.5Ve)</h3>
          <p>The closest star to the Sun at just 4.24 light-years, Proxima Centauri is a red dwarf main sequence star so faint that it requires a telescope to see. It hosts at least one planet, Proxima Centauri b, in or near the habitable zone.</p>
          <h3>Alpha Centauri A (G2V)</h3>
          <p>Part of the closest stellar system to the Sun, Alpha Centauri A is remarkably similar to our Sun\u2014slightly larger, brighter, and older. It forms a binary pair with Alpha Centauri B (a K-type star).</p>
          <h3>Epsilon Eridani (K2V)</h3>
          <p>One of the nearest solar-type stars at 10.5 light-years, Epsilon Eridani is a young K-type orange dwarf with a debris disk and a confirmed planet, making it a popular SETI target.</p>
        </section>

        <!-- Observation -->
        <section id="observation" class="content-section">
          <h2>Observing Main Sequence Stars</h2>
          <p>Because virtually every star you can see is a main sequence star, observing them is as simple as looking up on a clear night. Understanding what you are seeing adds a new dimension to stargazing.</p>
          <h3>Color Recognition</h3>
          <p>With the naked eye, you can distinguish stellar colors. Blue-white stars like Sirius contrast with yellow stars like Alpha Centauri, and orange stars like Epsilon Eridani. The color directly tells you about temperature\u2014blue means hot (20,000+ K), white means warm (8,000-10,000 K), yellow means moderate (5,000-6,000 K), and orange-red means cool (3,000-4,500 K).</p>
          <h3>Binoculars and Telescopes</h3>
          <p>With binoculars, you can see many more stars. Star clusters like the Pleiades (mostly hot B-type stars) and the Hyades (mostly K-type orange dwarfs) showcase different parts of the main sequence.</p>
          <h3>Spectroscopy</h3>
          <p>Amateur spectroscopy with inexpensive diffraction grating eyepieces allows you to classify stars by their absorption lines\u2014the key diagnostic tool that enables OBAFGKM classification.</p>
        </section>

        <!-- Interesting Facts -->
        <section id="fun-facts" class="content-section">
          <h2>Interesting Facts About Main Sequence Stars</h2>
          <ul class="facts-list">
            <li><strong>Red Dwarf Dominance:</strong> 70-75% of all stars in the Milky Way are M-type red dwarfs, yet none are visible to the naked eye from Earth. Their faintness means they contribute very little to the galaxy's total light despite being the most numerous type.</li>
            <li><strong>Mass-Luminosity:</strong> A star twice as massive as the Sun burns about 16 times brighter, following the roughly L \u221d M^4 relationship. This steep power law is why stellar lifetimes vary so dramatically across the main sequence.</li>
            <li><strong>Cosmic Middle Age:</strong> Our Sun is currently about halfway through its main sequence life at 4.6 billion years old. In another 5 billion years it will exhaust its core hydrogen.</li>
            <li><strong>Smallest Stars:</strong> The minimum mass to sustain hydrogen fusion is about 0.08 solar masses (80 Jupiter masses). Below this threshold, objects are brown dwarfs\u2014failed stars that glow only from gravitational contraction.</li>
            <li><strong>Longest Lived:</strong> Red dwarf stars could potentially live for 10 trillion years or more. No red dwarf has ever reached the end of its life since the universe is only 13.8 billion years old.</li>
            <li><strong>Blue Giant Brevity:</strong> The most massive O-type stars live only 1-3 million years before dying in supernova explosions. For comparison, the dinosaurs lived for over 100 million years.</li>
            <li><strong>Temperature Colors:</strong> A star's color directly reflects its surface temperature per blackbody radiation physics. Red is cooler, blue is hotter\u2014astronomers can estimate temperature just by looking at color.</li>
            <li><strong>Spectroscopy Power:</strong> Everything we know about stellar compositions comes from analyzing the light that reaches us\u2014no star has ever been physically sampled. By splitting starlight into its spectrum, astronomers determine temperature, composition, and velocity.</li>
          </ul>
        </section>

        <!-- External Resources -->
        <section id="resources" class="content-section">
          <h2>External Resources</h2>
          <ul class="resource-list">
            <li><a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener">NASA Stars Overview</a> - NASA's guide to stellar types, life cycles, and current research</li>
            <li><a href="https://en.wikipedia.org/wiki/Main_sequence" target="_blank" rel="noopener">Main Sequence on Wikipedia</a> - Comprehensive encyclopedia article on main sequence stars</li>
            <li><a href="https://www.esa.int/Science_Exploration/Space_Science/Stars" target="_blank" rel="noopener">ESA Stars</a> - European Space Agency's stellar science pages</li>
            <li><a href="https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram" target="_blank" rel="noopener">Hertzsprung-Russell Diagram</a> - Detailed explanation of the fundamental stellar classification diagram</li>
          </ul>
        </section>"""

p1 = make_page(
    "main-sequence",
    "Main Sequence Stars: The Backbone of the Universe | The Astronomy Space",
    "Complete guide to main sequence stars - the most common type of star. Learn about hydrogen fusion, the Hertzsprung-Russell diagram, stellar classification, and famous examples like our Sun.",
    "Main Sequence Stars",
    "The Most Common Stars in the Universe",
    "Main sequence stars are stars actively fusing hydrogen into helium in their cores, representing about 90% of all stars in the universe. They range from tiny red dwarfs to massive blue giants, spanning a huge range of temperatures, luminosities, and lifetimes. Our Sun is a typical middle-aged main sequence star classified as a G2V yellow dwarf.",
    p1_faq,
    p1_toc,
    p1_body,
    ["main sequence stars", "hydrogen fusion", "Hertzsprung-Russell diagram", "stellar classification", "red dwarf", "blue giant", "OBAFGKM", "Sun", "spectral class"]
)

filepath = os.path.join(base_dir, "main-sequence", "index.astro")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(p1)
print(f"Written: {filepath}")


# ============================================================
# PAGE 2: red-giants
# ============================================================
p2_faq = [
    ("What is a red giant star?",
     "A red giant is an evolved star that has exhausted the hydrogen in its core and entered a new phase of stellar evolution. When core hydrogen runs out, the core contracts and heats up while the outer layers expand dramatically, cooling as they spread out. This cooling makes the star glow red-orange rather than yellow-white. Red giants are 10 to 100 times larger than they were on the main sequence, yet they have cooler surface temperatures (below 5,000 K)."),
    ("Will our Sun become a red giant?",
     "Yes, in about 5 billion years, the Sun will exhaust the hydrogen in its core and begin expanding into a red giant. During this process, it will grow large enough to engulf Mercury and Venus, and possibly Earth as well. The Sun will eventually shed its outer layers as a planetary nebula, leaving behind a dense white dwarf about the size of Earth. This is the eventual fate of all stars with masses between about 0.6 and 8 solar masses."),
    ("How long do stars stay red giants?",
     "The red giant phase is relatively short compared to the main sequence. A Sun-like star spends about 10 billion years on the main sequence but only around 1-2 billion years as a red giant. The most luminous part of the red giant branch (near the helium flash) lasts only about 100 million years. After the helium flash, the star settles into a more stable phase burning helium in its core."),
    ("What is the helium flash?",
     "The helium flash is a brief, explosive event that occurs in low-mass stars (less than about 2 solar masses) when helium ignition suddenly begins in the degenerate core. Because the degenerate core can't expand to cool itself, the temperature rise accelerates the fusion rate, causing a runaway reaction that releases enormous energy over just a few hours or days. Despite its intensity, the helium flash is invisible from outside the star\u2014all the energy is absorbed by the star's thick outer layers."),
    ("What are the most famous red giant stars?",
     "Some of the most visible red giants include Arcturus (the brightest star in the northern celestial hemisphere), Aldebaran (the red eye of Taurus the Bull), and Pollux in Gemini. Mira is a famous pulsating red giant variable star that changes dramatically in brightness over about 332 days. These stars are so luminous that despite being hundreds of light-years away, they are among the brightest stars in our night sky."),
    ("What comes after the red giant phase?",
     "After the red giant phase, a star's fate depends on its mass. Low and medium-mass stars (like the Sun) will lose their outer layers as a beautiful planetary nebula, leaving a hot white dwarf remnant. Higher-mass stars may go through additional evolutionary stages\u2014becoming asymptotic giant branch (AGB) stars, then carbon stars\u2014before finally losing their envelopes. The most massive stars become red supergiants and eventually explode as supernovae."),
]

p2_toc = [
    ("introduction", "Introduction"),
    ("physical-characteristics", "Physical Characteristics"),
    ("stellar-evolution", "Stellar Evolution Path"),
    ("helium-flash", "The Helium Flash"),
    ("composition", "Composition & Layers"),
    ("examples", "Notable Examples"),
    ("observation", "Observation"),
    ("fun-facts", "Interesting Facts"),
    ("resources", "Resources"),
    ("faq", "FAQ"),
]

p2_body = """        <!-- Introduction -->
        <section id="introduction" class="content-section">
          <h2>Introduction to Red Giant Stars</h2>
          <p>Red giants represent one of the most dramatic transformations in the universe\u2014the death throes of Sun-like stars that have exhausted their hydrogen fuel. What was once a stable, middle-aged star suddenly blooms outward into a vast, cool, luminous giant, sometimes growing to hundreds of times its original diameter. This spectacular expansion is a fundamental stage of stellar evolution that virtually every low to medium-mass star undergoes.</p>
          <p>For our own Sun, this fate awaits in roughly 5 billion years. When the Sun finally runs out of hydrogen to fuse in its core, it will begin swelling into a red giant\u2014eventually growing large enough to engulf the inner planets. This prospect, though distant, gives red giants a particular personal relevance for humanity.</p>
          <p>Despite their dramatic appearance, red giants are well understood by astronomers. They represent a predictable stage in the stellar life cycle, following naturally from the exhaustion of main sequence hydrogen burning. The physics governing their structure, composition, and eventual fate has been worked out in detail through decades of theoretical work and observational confirmation.</p>
          <p>Red giants are also among the most visible stars in the night sky. Their high luminosity and characteristic red-orange color make them stand out prominently. Stars like Arcturus, Aldebaran, and Pollux are all red giants, and they have been familiar objects in the night sky since antiquity.</p>
        </section>

        <!-- Physical Characteristics -->
        <section id="physical-characteristics" class="content-section">
          <h2>Physical Characteristics</h2>
          <p>Red giants are physically much larger than main sequence stars, yet paradoxically cooler at their surfaces. This combination of large size and low temperature gives them their distinctive red-orange color and makes them highly luminous despite the cool surface.</p>
          <div class="info-box glass">
            <h3>Red Giant Quick Facts</h3>
            <ul>
              <li><strong>Size Range:</strong> 10 to 100 solar radii</li>
              <li><strong>Surface Temperature:</strong> 3,500 to 5,000 K</li>
              <li><strong>Luminosity:</strong> 10 to 1,000 solar luminosities</li>
              <li><strong>Mass Range:</strong> 0.6 to 8 solar masses (original)</li>
              <li><strong>RGB Phase Lifespan:</strong> ~1-2 billion years</li>
              <li><strong>Spectral Class:</strong> K or M</li>
            </ul>
          </div>
          <p class="data-source">Data: <a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener noreferrer">NASA Stellar Evolution</a></p>
          <p>The enormous size of red giants is a direct consequence of the internal changes occurring as the star exhausts its fuel. When the hydrogen in the core is depleted, hydrogen fusion continues in a shell around the inert helium core. This shell burning provides more energy than before, inflating the outer layers dramatically. The star's radius can grow from 1 solar radius to 10-100 solar radii over millions of years.</p>
          <p>Despite being vastly larger, red giants have lower surface gravity than main sequence stars because their mass is spread over a much larger volume. This low gravity means their outer layers are only loosely bound, and stellar winds can carry material away at significant rates.</p>
        </section>

        <!-- Stellar Evolution Path -->
        <section id="stellar-evolution" class="content-section">
          <h2>The Stellar Evolution Path to Red Giants</h2>
          <p>The path from main sequence star to red giant is a gradual process that takes hundreds of millions to billions of years, depending on the star's original mass.</p>
          <h3>Core Hydrogen Exhaustion</h3>
          <p>On the main sequence, a star fuses hydrogen into helium in its core. Over billions of years, the hydrogen supply dwindles as helium accumulates. The core contracts under gravity, heating up. Meanwhile, hydrogen continues fusing in a shell around the increasingly inert helium core.</p>
          <h3>The Subgiant Phase</h3>
          <p>As the hydrogen-burning shell grows, the outer layers begin expanding and cooling. The star moves off the main sequence onto the subgiant branch. This phase may last several hundred million years for a Sun-like star.</p>
          <h3>Red Giant Branch Ascent</h3>
          <p>Eventually, the star's outer layers have expanded and cooled enough for the surface to become convective. The star climbs the red giant branch (RGB) on the HR diagram, growing ever larger and more luminous while the surface temperature remains roughly constant. The star can become several hundred times more luminous than the present-day Sun during this ascent.</p>
          <h3>Tip of the Red Giant Branch</h3>
          <p>The ascent of the red giant branch ends when the helium core reaches conditions hot enough for helium fusion\u2014the helium flash in low-mass stars. The star then settles into a stable helium-burning phase.</p>
        </section>

        <!-- The Helium Flash -->
        <section id="helium-flash" class="content-section">
          <h2>The Helium Flash</h2>
          <p>The helium flash is one of the most dramatic events in the life of a low-mass star\u2014a brief but enormously energetic ignition of helium fusion in the star's degenerate core. Despite its violence, this event is hidden from outside observers.</p>
          <h3>Why It Happens</h3>
          <p>As the helium core accumulates, it becomes so compressed that it enters a state called electron degeneracy. In degenerate matter, pressure no longer depends on temperature. When helium ignition begins, the resulting temperature increase doesn't relieve pressure through expansion, causing a runaway thermonuclear reaction.</p>
          <h3>The Flash Itself</h3>
          <p>Within minutes to hours, the helium flash releases an enormous amount of energy\u2014temporarily matching the luminosity of an entire galaxy. However, all this energy is deposited in the star's thick outer envelope and never reaches the surface as visible light. The flash effectively converts the degenerate core into a normal, thermally-supported core.</p>
          <h3>After the Flash</h3>
          <p>Following the helium flash, the star settles into a new, stable phase burning helium in its core and hydrogen in a surrounding shell. It moves to the horizontal branch on the HR diagram\u2014a phase that may last another 100 million years.</p>
        </section>

        <!-- Composition and Layers -->
        <section id="composition" class="content-section">
          <h2>Composition and Layers</h2>
          <p>Red giants have a complex internal structure, quite different from main sequence stars.</p>
          <h3>The Helium Core</h3>
          <p>At the center of a red giant on the RGB is an inert helium core, left behind from billions of years of hydrogen fusion. This core is incredibly dense\u2014roughly the size of Earth but containing much of the star's original mass.</p>
          <h3>Hydrogen-Burning Shell</h3>
          <p>Surrounding the helium core is a thin shell where hydrogen fusion continues. This shell produces most of the star's energy during the red giant phase and gradually moves outward through the star as it processes more hydrogen.</p>
          <h3>The Convective Envelope</h3>
          <p>The vast, cool outer layers form a deep convective envelope where energy is transported upward by the mixing of hot and cool gas. This deep convection can dredge up material from deeper layers, enriching the surface with nuclear fusion products.</p>
          <h3>Stellar Winds</h3>
          <p>Red giants have powerful stellar winds that continuously shed mass into space. These winds play a crucial role in determining the star's eventual fate and enrich the interstellar medium with heavy elements.</p>
        </section>

        <!-- Notable Examples -->
        <section id="examples" class="content-section">
          <h2>Notable Red Giant Stars</h2>
          <p>Many of the most recognizable stars in the night sky are red giants, their high luminosity making them visible despite being much farther away than most stars we see.</p>
          <h3>Arcturus (Alpha Bootis)</h3>
          <p>The brightest star in the northern celestial hemisphere and fourth brightest overall, Arcturus is an orange giant about 36 light-years away. It shines at magnitude -0.05, is about 25 times the radius of the Sun, 170 times more luminous, and has a surface temperature of 4,286 K.</p>
          <h3>Aldebaran (Alpha Tauri)</h3>
          <p>The red "eye" of Taurus the Bull, Aldebaran is a prominent orange giant about 65 light-years away. With a radius about 44 times the Sun's and a surface temperature of 3,900 K, it is a classic example of a K-type giant.</p>
          <h3>Mira (Omicron Ceti)</h3>
          <p>The prototype "long-period variable" red giant, Mira pulsates with a period of about 332 days, varying in brightness by a factor of 1,500. At maximum it can shine at magnitude 2 (easily visible), at minimum around magnitude 10. Mira is about 400 light-years away.</p>
          <h3>Pollux (Beta Geminorum)</h3>
          <p>The brightest star in Gemini, Pollux is an orange giant about 34 light-years away with a confirmed extrasolar planet orbiting it. It represents a relatively cool, luminous K-type giant that the Sun will eventually resemble.</p>
        </section>

        <!-- Observation -->
        <section id="observation" class="content-section">
          <h2>Observing Red Giants</h2>
          <p>Red giants are among the easiest types of stars to identify visually, thanks to their distinctive red-orange coloration and high brightness. Many of the brightest stars in the sky are red or orange giants.</p>
          <h3>Identifying Red Giants by Color</h3>
          <p>The reddish tint of stars like Arcturus (orange), Aldebaran (orange-red), and Antares (reddish) is immediately apparent to the naked eye under good conditions. Their color directly indicates cool surface temperatures (3,500-5,000 K).</p>
          <h3>Seasonal Visibility</h3>
          <p>Different red giants dominate different seasons. Arcturus is a spring and summer star in the northern hemisphere, while Aldebaran is prominent in winter skies. Antares (a red supergiant) marks the heart of Scorpius and is best seen in summer.</p>
          <h3>Variable Red Giants</h3>
          <p>Several red giants are variable stars worth monitoring. Mira (Omicron Ceti) varies dramatically between magnitudes 2 and 10 over 332 days and is tracked by amateur astronomers worldwide through the AAVSO.</p>
        </section>

        <!-- Interesting Facts -->
        <section id="fun-facts" class="content-section">
          <h2>Interesting Facts About Red Giants</h2>
          <ul class="facts-list">
            <li><strong>Future Sun:</strong> Our own Sun will become a red giant in approximately 5 billion years, potentially engulfing Earth as it swells to over 100 times its current radius.</li>
            <li><strong>Planetary Nebula Factories:</strong> When a red giant eventually sheds its outer layers, it creates a beautiful planetary nebula. The Ring Nebula (M57) is a classic example of such a remnant.</li>
            <li><strong>Arcturus Navigation:</strong> Arcturus is easily found by following the arc of the Big Dipper's handle outward\u2014"Arc to Arcturus." It has been used for navigation since ancient times.</li>
            <li><strong>Ancient Bright Stars:</strong> Many of the 50 brightest stars in the night sky are red or orange giants. Their high luminosity makes them visible at much greater distances than typical main sequence stars.</li>
            <li><strong>Planetary Survivors:</strong> Some planets orbiting red giants may survive the expansion phase if they orbit far enough out. Gas giant planets at several AU could persist as the star inflates.</li>
            <li><strong>Element Factories:</strong> Red giants produce significant amounts of carbon, nitrogen, and other elements through nuclear burning. When mass is shed, these elements enrich the interstellar medium for future star and planet formation.</li>
            <li><strong>Helium Flash Energy:</strong> The helium flash in a Sun-like star releases energy comparable to the Sun's entire main sequence output compressed into a few minutes\u2014yet is completely invisible from outside.</li>
            <li><strong>Pulsating Giants:</strong> Many red giants pulsate, slowly expanding and contracting over months to years. These pulsations cause predictable brightness changes and were among the first types of variable stars studied systematically.</li>
          </ul>
        </section>

        <!-- External Resources -->
        <section id="resources" class="content-section">
          <h2>External Resources</h2>
          <ul class="resource-list">
            <li><a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener">NASA Stars &amp; Stellar Evolution</a> - NASA's overview of star types and life cycles</li>
            <li><a href="https://en.wikipedia.org/wiki/Red_giant" target="_blank" rel="noopener">Red Giant on Wikipedia</a> - Comprehensive encyclopedia article on red giant stars</li>
            <li><a href="https://www.esa.int/Science_Exploration/Space_Science/Stars" target="_blank" rel="noopener">ESA Stars</a> - European Space Agency stellar science resources</li>
            <li><a href="https://en.wikipedia.org/wiki/Stellar_evolution" target="_blank" rel="noopener">Stellar Evolution on Wikipedia</a> - Full stellar evolution from birth to death</li>
          </ul>
        </section>"""

p2 = make_page(
    "red-giants",
    "Red Giants: Aging Stars in Their Final Act | The Astronomy Space",
    "Complete guide to red giant stars - the evolved phase of Sun-like stars. Learn about stellar evolution, helium fusion, the RGB phase, and how our Sun will become a red giant in 5 billion years.",
    "Red Giants",
    "Stars in the Final Act of Their Lives",
    "Red giants are evolved stars that have exhausted the hydrogen fuel in their cores and expanded dramatically, becoming 10 to 100 times larger than their original size. Their outer layers cool and glow with a characteristic red-orange hue. Our Sun will become a red giant in about 5 billion years, expanding to engulf the inner planets including possibly Earth.",
    p2_faq,
    p2_toc,
    p2_body,
    ["red giant stars", "stellar evolution", "helium flash", "RGB phase", "Arcturus", "Aldebaran", "Mira", "planetary nebula", "hydrogen shell burning"]
)

filepath = os.path.join(base_dir, "red-giants", "index.astro")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(p2)
print(f"Written: {filepath}")


# ============================================================
# PAGE 3: white-dwarfs
# ============================================================
p3_faq = [
    ("What is a white dwarf?",
     "A white dwarf is the small, dense remnant left behind after a low to medium-mass star (up to about 8 solar masses) exhausts its nuclear fuel and sheds its outer layers as a planetary nebula. The remaining core, roughly the size of Earth but containing about 0.6 solar masses, is so dense that a teaspoon of white dwarf material would weigh several tons. White dwarfs are supported by electron degeneracy pressure\u2014a quantum mechanical effect that prevents further collapse."),
    ("How does a star become a white dwarf?",
     "When a main sequence star like the Sun exhausts its hydrogen fuel, it expands into a red giant, then an asymptotic giant branch (AGB) star. During the AGB phase, stellar winds and thermal pulses eject the star's outer layers, creating a beautiful planetary nebula. The hot, exposed core\u2014the white dwarf\u2014is left behind. This entire process from main sequence to white dwarf takes billions to tens of billions of years depending on the star's mass."),
    ("What is the Chandrasekhar limit?",
     "The Chandrasekhar limit is the maximum mass a white dwarf can have\u2014about 1.4 times the Sun's mass. Above this limit, electron degeneracy pressure can no longer support the white dwarf against gravitational collapse. If a white dwarf accumulates mass beyond this limit (typically by accreting material from a companion star), it triggers a Type Ia supernova\u2014a colossal explosion that outshines entire galaxies. This limit was discovered by Subrahmanyan Chandrasekhar, earning him the Nobel Prize in Physics."),
    ("What is inside a white dwarf?",
     "Most white dwarfs are composed primarily of carbon and oxygen\u2014the ashes of helium fusion that occurred during the star's red giant phase. More massive white dwarfs may contain oxygen, neon, and magnesium. The outer layers are typically hydrogen (if retained) or helium. The material exists in a degenerate state where electrons are not bound to atoms but form a sea of free electrons that creates the supporting pressure. As a white dwarf cools, the carbon and oxygen may crystallize into a diamond-like structure."),
    ("Can white dwarfs support life?",
     "White dwarfs are very dim compared to main sequence stars, but they do emit some light and heat. Any planets in very close orbits might receive enough warmth to be habitable\u2014at least for a while. However, white dwarfs are cooling remnants that will eventually dim below any life-supporting threshold. Additionally, the red giant phase that preceded the white dwarf likely destroyed any inner planets. Some white dwarfs show evidence of accreting rocky material, suggesting they may have had planetary systems."),
    ("What happens to a white dwarf eventually?",
     "In theory, a white dwarf will cool slowly over tens to hundreds of billions of years, passing through yellow dwarf, orange dwarf, and red dwarf stages to eventually become a 'black dwarf'\u2014a cold, dark stellar remnant. However, the universe is only about 13.8 billion years old, and even the oldest white dwarfs are still cooling. No black dwarfs exist yet\u2014they are purely theoretical objects. The cooling process takes so long that the universe must be many times its current age before the first black dwarfs appear."),
]

p3_toc = [
    ("introduction", "Introduction"),
    ("physical-characteristics", "Physical Characteristics"),
    ("formation", "Formation Process"),
    ("composition", "Composition & Structure"),
    ("chandrasekhar", "The Chandrasekhar Limit"),
    ("cooling", "Cooling Evolution"),
    ("binary-wd", "Binary White Dwarfs"),
    ("examples", "Notable Examples"),
    ("observation", "Observation"),
    ("fun-facts", "Interesting Facts"),
    ("resources", "Resources"),
    ("faq", "FAQ"),
]

p3_body = """        <!-- Introduction -->
        <section id="introduction" class="content-section">
          <h2>Introduction to White Dwarfs</h2>
          <p>White dwarfs are the twilight of stellar existence\u2014the quiet, slowly cooling embers left behind after a star like our Sun exhausts its nuclear fuel and sheds its outer layers. Despite their humble appearance as faint, unassuming points of light, white dwarfs represent one of the universe's most fascinating physical states: matter compressed to extraordinary density, supported not by nuclear fusion but by the quantum mechanical resistance of electrons to being squeezed together.</p>
          <p>About 97% of all stars will eventually become white dwarfs, making them the most common stellar remnant in the universe. Our galaxy contains an estimated 10 billion white dwarfs, though only a small fraction have been catalogued. They range in age from newly exposed hot white dwarfs glowing at over 100,000 K, still surrounded by the glowing shells of their planetary nebulae, to ancient, cool white dwarfs that have been slowly radiating away their heat for billions of years.</p>
          <p>White dwarfs have played an outsized role in astrophysics. The study of white dwarf cooling provides one of the most reliable "cosmic clocks" for dating stellar populations. Type Ia supernovae\u2014triggered when white dwarfs exceed the Chandrasekhar limit\u2014were the discovery tool for the accelerating expansion of the universe. And white dwarf spectra provide pristine glimpses into the compositions of destroyed planetary systems.</p>
        </section>

        <!-- Physical Characteristics -->
        <section id="physical-characteristics" class="content-section">
          <h2>Physical Characteristics</h2>
          <p>White dwarfs are among the densest objects in the universe outside of neutron stars and black holes. Their extreme density arises from the fact that they contain roughly 60% of the original star's mass compressed into a volume roughly the size of Earth.</p>
          <div class="info-box glass">
            <h3>White Dwarf Quick Facts</h3>
            <ul>
              <li><strong>Typical Size:</strong> ~Earth's radius (~6,000-8,000 km)</li>
              <li><strong>Mass Range:</strong> 0.5 to 1.4 solar masses</li>
              <li><strong>Density:</strong> ~1 million g/cm\u00b3 (1 million times water)</li>
              <li><strong>Temperature Range:</strong> 4,000 to 150,000 K</li>
              <li><strong>Energy Source:</strong> Residual thermal energy (no fusion)</li>
              <li><strong>Support Mechanism:</strong> Electron degeneracy pressure</li>
            </ul>
          </div>
          <p class="data-source">Data: <a href="https://science.nasa.gov/universe/stars/white-dwarfs/" target="_blank" rel="noopener noreferrer">NASA White Dwarf Stars</a></p>
          <p>Despite their small size, white dwarfs have strong surface gravities\u2014about 100,000 times Earth's. This immense gravity causes remarkable phenomena: heavy elements in the atmosphere sink rapidly (within days to years), leaving the surface dominated by hydrogen or helium. When astronomers observe pollution of white dwarf atmospheres with heavier elements like calcium, iron, or silicon, it typically indicates ongoing accretion of rocky planetary debris.</p>
          <p>White dwarfs have no energy source\u2014they are simply hot objects radiating away the heat stored in their ion lattice. Their cooling is very slow because of their small surface area and the good thermal insulation of their crystallizing interiors.</p>
        </section>

        <!-- Formation Process -->
        <section id="formation" class="content-section">
          <h2>Formation Process</h2>
          <p>The journey from main sequence star to white dwarf takes billions of years and involves several dramatic transformations.</p>
          <h3>The Asymptotic Giant Branch</h3>
          <p>After the red giant phase, a star with mass below about 8 solar masses evolves onto the asymptotic giant branch (AGB). During this phase, the star has two burning shells\u2014one of helium and one of hydrogen\u2014surrounding an inert carbon-oxygen core. The AGB star pulsates and ejects material in powerful stellar winds, gradually losing its envelope.</p>
          <h3>Planetary Nebula Formation</h3>
          <p>As the star loses its outer layers, the ejected material forms a glowing shell called a planetary nebula (named by early astronomers who thought they resembled planets through small telescopes). The exposed hot core\u2014the proto-white dwarf\u2014ionizes the surrounding gas with its intense ultraviolet radiation, causing it to glow in spectacular colors. Planetary nebulae are among the most beautiful objects in astronomy.</p>
          <h3>White Dwarf Emerges</h3>
          <p>Over thousands to tens of thousands of years, the planetary nebula disperses into the interstellar medium. The proto-white dwarf cools from temperatures exceeding 100,000 K, becoming the white dwarf we observe today. The entire transition from AGB star to white dwarf takes perhaps 10,000-100,000 years\u2014a blink in cosmic time.</p>
        </section>

        <!-- Composition and Structure -->
        <section id="composition" class="content-section">
          <h2>Composition and Structure</h2>
          <p>The interior of a white dwarf is unlike anything found naturally on Earth, consisting of degenerate matter with exotic physical properties.</p>
          <h3>Core Composition</h3>
          <p>Most white dwarfs have a core of carbon and oxygen\u2014the products of helium fusion during the red giant and AGB phases. More massive white dwarfs (from more massive progenitor stars) may have cores enriched in oxygen, neon, and magnesium from more advanced fusion stages. As the white dwarf cools below about 12,000 K, the carbon and oxygen begin to crystallize, forming a solid lattice\u2014essentially a giant diamond in space.</p>
          <h3>Atmospheric Layers</h3>
          <p>White dwarfs have thin atmospheric layers stratified by the intense gravity. Most show either pure hydrogen atmospheres (DA-type, the most common) or pure helium atmospheres (DB-type), depending on what was left after the stellar evolution. The strong gravity causes heavier elements to sink rapidly, maintaining atmospheric purity unless new material is accreted.</p>
          <h3>Degenerate Electrons</h3>
          <p>The interior electrons are in a quantum mechanical state called degeneracy\u2014they cannot be compressed further because the Pauli exclusion principle prevents two electrons from occupying the same quantum state. This degenerate electron gas exerts pressure that supports the white dwarf against gravity, a pressure that doesn't depend on temperature. This is why white dwarfs don't collapse even as they cool.</p>
        </section>

        <!-- The Chandrasekhar Limit -->
        <section id="chandrasekhar" class="content-section">
          <h2>The Chandrasekhar Limit</h2>
          <p>One of the most important results in astrophysics is the Chandrasekhar limit: the maximum mass a white dwarf can have before electron degeneracy pressure is overwhelmed by gravity. This limit, approximately 1.4 solar masses, was derived by Indian-American physicist Subrahmanyan Chandrasekhar in 1930 (for which he received the Nobel Prize in Physics in 1983).</p>
          <h3>Physical Basis</h3>
          <p>As a white dwarf's mass increases, electrons must move faster to maintain degeneracy pressure. Eventually, electrons would need to move faster than the speed of light, which is impossible. At the Chandrasekhar limit, relativistic effects cause the electron degeneracy pressure to become insufficient to support the star against gravity.</p>
          <h3>Type Ia Supernovae</h3>
          <p>If a white dwarf in a binary system accretes enough mass from its companion to approach the Chandrasekhar limit, catastrophic collapse occurs. The rapid compression ignites carbon fusion throughout the white dwarf in a detonation that completely destroys it\u2014a Type Ia supernova. These explosions release enormous energy (about 10^44 joules) and are used as "standard candles" for measuring cosmic distances. It was observations of Type Ia supernovae that led to the discovery of the accelerating expansion of the universe in 1998.</p>
        </section>

        <!-- Cooling Evolution -->
        <section id="cooling" class="content-section">
          <h2>Cooling Evolution</h2>
          <p>Unlike main sequence stars, which generate their own energy through fusion, white dwarfs simply cool down over time like a heated rock cooling in the night. This cooling process takes an extraordinarily long time due to the low surface area and insulating interior.</p>
          <h3>Cooling Sequence</h3>
          <p>A newly formed white dwarf may have a surface temperature of 100,000-200,000 K, glowing brilliant blue-white. Over billions of years, it cools through yellow (around 10,000 K), then orange-red colors. The cooling rate depends on composition and crystallization processes.</p>
          <h3>Crystallization</h3>
          <p>When a white dwarf cools below about 12,000 K, the carbon and oxygen in its interior begin to solidify into a crystalline structure\u2014essentially becoming a crystal ball the size of Earth. This crystallization releases latent heat, slowing the cooling process. Astronomers have confirmed this crystallization using asteroseismology of white dwarf stars.</p>
          <h3>Black Dwarfs</h3>
          <p>Theoretical physics predicts that eventually, after hundreds of billions of years, a white dwarf will cool to the temperature of the surrounding universe, becoming an inert "black dwarf." However, the universe at 13.8 billion years old is not yet old enough for any black dwarfs to exist.</p>
        </section>

        <!-- Binary White Dwarfs -->
        <section id="binary-wd" class="content-section">
          <h2>Binary White Dwarfs and Type Ia Supernovae</h2>
          <p>White dwarfs in binary systems have some of the most interesting behaviors in all of stellar astrophysics.</p>
          <h3>Cataclysmic Variables</h3>
          <p>When a white dwarf accretes hydrogen-rich gas from a companion star that overflows its Roche lobe, the material builds up on the white dwarf's surface. Periodically, this accumulated hydrogen layer reaches critical conditions and ignites in a thermonuclear flash\u2014a nova. The white dwarf survives and the cycle repeats. Some systems, called recurrent novae, undergo this process multiple times over human timescales.</p>
          <h3>Symbiotic Stars</h3>
          <p>In wider binary systems, a white dwarf may orbit a red giant and accrete wind material. These "symbiotic stars" show complex interactions between the hot white dwarf and cool giant, sometimes producing nebular emission.</p>
          <h3>Merging White Dwarfs</h3>
          <p>Two white dwarfs in a close binary system will spiral together due to gravitational wave emission, eventually merging. Depending on their combined mass, this can produce a more massive white dwarf, a neutron star, or a Type Ia supernova.</p>
        </section>

        <!-- Notable Examples -->
        <section id="examples" class="content-section">
          <h2>Notable White Dwarf Stars</h2>
          <p>Although white dwarfs are intrinsically faint, several nearby examples are accessible to amateur astronomers and well-studied by professionals.</p>
          <h3>Sirius B</h3>
          <p>The companion of Sirius (the brightest star in the sky), Sirius B was the first white dwarf discovered and remains the most famous. Located just 8.6 light-years away, it orbits Sirius A with a period of about 50 years. Despite having a mass close to the Sun, it is only slightly larger than Earth, with a surface temperature of about 25,000 K.</p>
          <h3>Procyon B</h3>
          <p>Another white dwarf in a nearby binary system, Procyon B orbits the bright F-type star Procyon at a distance of 8.1 light-years. It represents a future similar to our Sun's eventual fate.</p>
          <h3>40 Eridani B</h3>
          <p>Part of a triple star system 16 light-years away, 40 Eridani B was the second white dwarf discovered and was significant in early studies of stellar evolution. It was notably mentioned in Star Trek as being in the system of Vulcan.</p>
          <h3>Van Maanen's Star</h3>
          <p>At 14.1 light-years away, Van Maanen's Star is the nearest known solitary white dwarf. Its atmosphere shows traces of heavy elements, indicating it is accreting debris from a destroyed planetary system.</p>
        </section>

        <!-- Observation -->
        <section id="observation" class="content-section">
          <h2>Observing White Dwarfs</h2>
          <p>White dwarfs are notoriously difficult to observe due to their extreme faintness, but the nearest examples are within reach of moderate telescopes.</p>
          <h3>Sirius B Challenge</h3>
          <p>Sirius B is the most famous white dwarf to observe, but it is very difficult because the brilliant glare of Sirius A (magnitude -1.46) drowns out the much fainter Sirius B (magnitude 8.4). The best time to attempt the observation is when Sirius B is at its greatest angular separation from Sirius A, which occurs periodically as the two orbit each other with a 50-year period.</p>
          <h3>White Dwarf in Planetary Nebulae</h3>
          <p>Some white dwarfs can be seen at the centers of planetary nebulae. The Ring Nebula (M57) contains a white dwarf at its center visible in large amateur telescopes. The Helix Nebula and the Cat's Eye Nebula also have central white dwarfs.</p>
          <h3>Photometric Monitoring</h3>
          <p>Variable white dwarfs (pulsating ZZ Ceti types and others) offer opportunities for precision photometry. These pulsations probe the white dwarf's interior structure and composition.</p>
        </section>

        <!-- Interesting Facts -->
        <section id="fun-facts" class="content-section">
          <h2>Interesting Facts About White Dwarfs</h2>
          <ul class="facts-list">
            <li><strong>Diamond Stars:</strong> As white dwarfs cool below about 12,000 K, their carbon-oxygen cores begin to crystallize. This means the centers of old white dwarfs are essentially giant diamonds\u2014Earth-sized crystalline carbon structures.</li>
            <li><strong>Most Common Remnant:</strong> About 97% of all stars, including our Sun, will end their lives as white dwarfs. Neutron stars and black holes are far rarer endpoints.</li>
            <li><strong>Cosmic Clocks:</strong> The cooling rate of white dwarfs is well-understood, making them reliable timekeepers for dating stellar populations. The oldest white dwarfs constrain the age of the Milky Way's disk.</li>
            <li><strong>Extreme Gravity:</strong> A white dwarf's surface gravity is about 100,000 times Earth's. If you somehow stood on one, you would weigh about 3 million times what you do on Earth.</li>
            <li><strong>Planetary Autopsies:</strong> Many white dwarfs show heavy elements in their spectra that "shouldn't" be there given how quickly they sink. This pollution is caused by ongoing accretion of asteroid and comet material\u2014revealing the composition of exoplanetary systems.</li>
            <li><strong>Nobel Prize Discovery:</strong> Subrahmanyan Chandrasekhar's calculation of the mass limit for white dwarfs, done at age 19 on a steamship journey, earned him the Nobel Prize 53 years later in 1983.</li>
            <li><strong>Expanding Universe Discovery:</strong> Type Ia supernovae\u2014triggered by white dwarfs exceeding the Chandrasekhar limit\u2014were the key tool in discovering the accelerating expansion of the universe in 1998, earning the Nobel Prize in Physics in 2011.</li>
            <li><strong>Extremely Long Future:</strong> A white dwarf cools so slowly that even the oldest ones from the early universe are still relatively warm. The first "black dwarfs" won't exist for trillions of years.</li>
          </ul>
        </section>

        <!-- External Resources -->
        <section id="resources" class="content-section">
          <h2>External Resources</h2>
          <ul class="resource-list">
            <li><a href="https://science.nasa.gov/universe/stars/white-dwarfs/" target="_blank" rel="noopener">NASA White Dwarf Stars</a> - NASA's guide to white dwarfs and their role in the cosmos</li>
            <li><a href="https://en.wikipedia.org/wiki/White_dwarf" target="_blank" rel="noopener">White Dwarf on Wikipedia</a> - Comprehensive encyclopedia article on white dwarf stars</li>
            <li><a href="https://www.esa.int/Science_Exploration/Space_Science/Stars" target="_blank" rel="noopener">ESA Stars</a> - European Space Agency stellar science resources</li>
            <li><a href="https://en.wikipedia.org/wiki/Chandrasekhar_limit" target="_blank" rel="noopener">Chandrasekhar Limit on Wikipedia</a> - Explanation of the critical mass limit for white dwarfs</li>
          </ul>
        </section>"""

p3 = make_page(
    "white-dwarfs",
    "White Dwarfs: The Dense Stellar Remnants | The Astronomy Space",
    "Complete guide to white dwarf stars - the remnant cores of Sun-like stars. Learn about electron degeneracy pressure, the Chandrasekhar limit, Type Ia supernovae, and the ultimate fate of our Sun.",
    "White Dwarfs",
    "The Final Fate of Sun-like Stars",
    "White dwarfs are the dense stellar remnants left behind when low to medium-mass stars shed their outer layers at the end of their lives. About the size of Earth but containing roughly 60% of the original star's mass, white dwarfs are supported by electron degeneracy pressure rather than nuclear fusion. Over trillions of years, they slowly cool from brilliant white to orange, red, and eventually the theoretical black dwarfs.",
    p3_faq,
    p3_toc,
    p3_body,
    ["white dwarf stars", "Chandrasekhar limit", "electron degeneracy", "Type Ia supernova", "Sirius B", "planetary nebula", "stellar remnants", "black dwarf"]
)

filepath = os.path.join(base_dir, "white-dwarfs", "index.astro")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(p3)
print(f"Written: {filepath}")

print("Pages 1-3 complete.")
