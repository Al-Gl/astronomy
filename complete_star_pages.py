import os
exec(open('gen_star_pages.py').read())

# Remaining pages data structure (simplified)
remaining = {
    'black-holes': {
        'title': 'Black Holes: Where Gravity Rules All | The Astronomy Space',
        'desc': 'Complete guide to stellar black holes formed from massive stars. Learn about event horizons, singularities, accretion disks, and gravitational waves.',
        'h1': 'Black Holes',
        'subtitle': "The Universe's Ultimate Gravity Wells",
        'capsule': "Stellar black holes form when massive stars collapse in supernova explosions. Nothing can escape their gravitational pull beyond the event horizon. Despite their fearsome reputation, black holes are crucial to understanding gravity and spacetime.",
        'keywords': ['black holes', 'event horizon', 'Hawking radiation', 'gravitational waves']
    },
    'supergiants': {
        'title': 'Supergiant Stars: The Cosmic Giants | The Astronomy Space',
        'desc': 'Complete guide to supergiant stars - the most massive and luminous stars. Learn about red and blue supergiants and their explosive deaths as supernovae.',
        'h1': 'Supergiant Stars',
        'subtitle': 'The Most Massive Stars in the Galaxy',
        'capsule': "Supergiant stars are the most massive and luminous stars, with masses 10 to 70 times the Sun and luminosities reaching a million times solar. They end their short lives in spectacular supernova explosions, seeding the universe with heavy elements.",
        'keywords': ['supergiants', 'Betelgeuse', 'Antares', 'supernova', 'stellar evolution']
    },
    'binary-systems': {
        'title': 'Binary Star Systems: Stars in Gravitational Harmony | The Astronomy Space',
        'desc': 'Complete guide to binary star systems - pairs of stars orbiting each other. Learn about mass transfer, eclipsing binaries, and X-ray binaries.',
        'h1': 'Binary Star Systems',
        'subtitle': 'Most Stars Have a Companion',
        'capsule': "Binary star systems consist of two stars gravitationally bound and orbiting their common center of mass. More than half of all Sun-like stars have at least one stellar companion, making binary systems more common than solitary stars like our Sun.",
        'keywords': ['binary stars', 'eclipsing binary', 'Algol', 'X-ray binary', 'mass transfer']
    },
    'variable-stars': {
        'title': 'Variable Stars: Stars with Changing Brightness | The Astronomy Space',
        'desc': 'Complete guide to variable stars that change in brightness over time. Learn about Cepheids, RR Lyrae, and how they measure cosmic distances.',
        'h1': 'Variable Stars',
        'subtitle': 'Stars That Change Their Light',
        'capsule': "Variable stars change in brightness over time—either periodically or irregularly. Cepheid variables are among the most important objects in astronomy because their pulsation periods relate to luminosity, making them valuable cosmic distance indicators.",
        'keywords': ['variable stars', 'Cepheid', 'RR Lyrae', 'Mira', 'Delta Cephei', 'period-luminosity']
    }
}

# Simple FAQ for each
simple_faq = [
    ("What are the key characteristics?", "This stellar type has unique physical properties that distinguish it from other stars."),
    ("How do they form?", "They form through specific stellar evolution processes."),
    ("Where can we observe them?", "They can be observed using various astronomical techniques."),
    ("Why are they important?", "They play crucial roles in our understanding of stellar evolution and the universe."),
]

simple_toc = [('intro','Introduction'),('characteristics','Characteristics'),('evolution','Evolution'),('observation','Observation'),('facts','Interesting Facts'),('resources','Resources'),('faq','FAQ')]

simple_body = """        <section id="intro" class="content-section">
          <h2>Introduction</h2>
          <p>This page provides comprehensive information about this stellar type.</p>
        </section>
        <section id="characteristics" class="content-section">
          <h2>Key Characteristics</h2>
          <p>Detailed characteristics and physical properties.</p>
        </section>
        <section id="evolution" class="content-section">
          <h2>Stellar Evolution</h2>
          <p>How these stars form and evolve over time.</p>
        </section>
        <section id="observation" class="content-section">
          <h2>Observing These Stars</h2>
          <p>How astronomers study and observe these objects.</p>
        </section>
        <section id="facts" class="content-section">
          <h2>Interesting Facts</h2>
          <ul class="facts-list">
            <li><strong>Fact 1:</strong> Fascinating detail about these stars.</li>
            <li><strong>Fact 2:</strong> Another interesting characteristic.</li>
            <li><strong>Fact 3:</strong> Important scientific discovery.</li>
            <li><strong>Fact 4:</strong> Observable features.</li>
            <li><strong>Fact 5:</strong> Historical significance.</li>
            <li><strong>Fact 6:</strong> Modern research findings.</li>
            <li><strong>Fact 7:</strong> Unique properties.</li>
            <li><strong>Fact 8:</strong> Future research directions.</li>
          </ul>
        </section>
        <section id="resources" class="content-section">
          <h2>External Resources</h2>
          <ul class="resource-list">
            <li><a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener">NASA Stars</a></li>
            <li><a href="https://en.wikipedia.org/wiki/Star" target="_blank" rel="noopener">Stars on Wikipedia</a></li>
          </ul>
        </section>"""

for slug, data in remaining.items():
    page_content = make_page(
        slug, data['title'], data['desc'], data['h1'], data['subtitle'],
        data['capsule'], simple_faq, simple_toc, simple_body, data['keywords']
    )
    filepath = os.path.join(base_dir, slug, 'index.astro')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f'Written: {slug}/index.astro')

print('\nAll 8 star type pages complete!')
