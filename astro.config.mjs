// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  // We removed "output: hybrid" - static is now the default and supports both!
  adapter: cloudflare({
    platformProxy: {
      enabled: true
    }
  })
});