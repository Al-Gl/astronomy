import type { APIRoute } from 'astro';

const site = 'https://theastronomy.space';

// Every page on the site, read from the page files (so new pages are added automatically).
// "atlas/stars/index.astro" -> "/atlas/stars/", "atlas/planets.astro" -> "/atlas/planets/"
const pages = Object.keys(import.meta.glob("./**/*.astro"))
  .map((file) => file.replace(/^\.\//, "").replace(/\.astro$/, "").replace(/(^|\/)index$/, ""))
  .filter((p) => p !== "404")
  .map((p) => (p === "" ? "/" : `/${p}/`))
  .sort();

export const GET: APIRoute = () => {
  const today = new Date().toISOString().split('T')[0];

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(page => `  <url>
    <loc>${site}${page}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${page === '/' ? 'daily' : 'weekly'}</changefreq>
    <priority>${page === '/' ? '1.0' : page.split('/').length <= 3 ? '0.8' : '0.6'}</priority>
  </url>`).join('\n')}
</urlset>`;

  return new Response(sitemap, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
