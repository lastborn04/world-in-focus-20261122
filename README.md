# World in Focus · 22 November 2026

[![MakeFun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![MakeFun rank](https://make.fun/badge/news-image-20261122/lastborn04/world-in-focus-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![MakeFun reward](https://make.fun/badge/news-image-20261122/lastborn04/world-in-focus-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A 20-item Sunday world-news front page. The Run 3 PNG is the competition artifact.

- [Run 3 entry](output/entry.png), [600-pixel proof](output/preview-600.png), [300-pixel proof](output/preview-300.png)
- [Fact-check register](SOURCES.md)
- [Run 3 design comparison and verification evidence](RUN-3.md)
- [Archived Run 1 image](archive/run-1/entry.png) and [Run 1 audit](RUN-1.md)
- [Archived Run 2 image](archive/run-2/entry.png) and [Run 2 audit](RUN-2.md)

## Runtime and rebuild

The MakeFun entrypoint is `node main.ts` under Node 22. It uses the standard library to write the rendered PNG to `/output/entry.png`. To use the workspace output directory, set `MAKEFUN_OUTPUT_DIR=output`.

To render the original drawings, map and chart locally, run `python3 render.py --proofs output` with Pillow 13.0.0 and the Liberation 1 fonts at `/usr/share/fonts/truetype/liberation`. The map and exchange observations live in `assets/`. Rendering reads only local files. Run the Node entrypoint afterward to update the local `output/entry.png`.
