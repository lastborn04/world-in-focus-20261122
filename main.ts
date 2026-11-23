import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

// The offline runner publishes the locally rendered edition byte for byte.
const destination = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(destination, { recursive: true });
copyFileSync(new URL('./edition.png', import.meta.url), join(destination, 'entry.png'));
