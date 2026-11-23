# Run 2 · Management audit

## Design comparison

[Side-by-side comparison at 600 pixels per edition](output/design-comparison.png) · [Run 1 baseline](archive/run-1/entry.png) · [Run 2 entry](archive/run-2/entry.png)

| Element | Run 1 | Run 2 |
| --- | --- | --- |
| Density | Eight items with one dominant story, six cards and a technology ticker | 20 distinct items across three leads, nine mosaic stories, two digital-assets items and six digest stories. The dashboard and locator repeat context without adding to the count. |
| Page hierarchy | Near-full-width masthead and a single large COP31 panel | Name and date share the masthead. COP31 occupies the left 406 pixels of a three-lead row. Separate editorial scales organize the leads, mosaic and digest. |
| Visual reporting | Symbolic COP31 globe and isolated spot illustrations | A split negotiating table, collapsed apartment block and Bayelsa riverboat explain the lead subjects. The mosaic adds nine subject-specific drawings. The market chart and map encode verified values and locations. |
| Global coverage | One African story and no standalone Canadian, South American or Oceanian items | Canada, Mexico, Colombia, two additional African locations, Poland, South Korea, New Zealand and further Middle East developments appear alongside retained coverage. |
| Data | A rounded Bitcoin threshold and a brief futures mention | Four sourced numerical callouts, a seven-location Natural Earth map, and a Coinbase UTC-day chart with a low, high, open and close. The U.S. futures line has been dropped. |
| Editorial verification | Mercury caption was geographically ambiguous. The Bitcoin timestamp relied on press reporting. | Mercury insertion is dated 21 Nov and AP coverage 22 Nov. Direct Coinbase candle data resolves the prior price timestamp and supplies the new close and range. The digest attributes unconfirmed reports in the text. |

## Technical verification

| Check | Result |
| --- | --- |
| Official kit | Read the governing rules and checked all 11 files against the official kit manifest. All matched. |
| Native entry | 1024 × 1024 RGB PNG, 575,665 bytes. Passed Pillow integrity verification and full decode. SHA-256 `853d0dac81b059ea94dae6603e94ed515a5ced168b18bd3917459e627f14702a`. |
| Proofs | 600 × 600, 338,354 bytes. 300 × 300, 113,746 bytes. Both passed PNG integrity verification and full decode. |
| Offline execution | Two Node 22.23.4 runs with Bubblewrap in an isolated network namespace, read-only `/bot`, freshly mounted writable `/output`, affinity to one CPU and a 60-second timeout. Both wrote the literal `/output/entry.png`. |
| Runtime measurements | 0.785 and 0.120 s elapsed, including sandbox launch. Both runs measured 60,528 KiB peak Node RSS. This is a local runtime probe. The official container’s process count and memory enforcement were not reproduced. |
| Determinism | Both isolated outputs matched each other and the workspace entry. An independent renderer invocation reproduced the same bytes. |
| Visual checks | Inspected native, 600 and 300 proofs. The masthead, date, leads and main figures survive the thumbnail. The digest, map legend and market sublabels work best at larger sizes. |

## Transcript and repository evidence

The official `bundle --dry-run` discovered exactly one matching native Codex session by repository, with zero manually supplied and zero family sessions. The same genuine session contains the Run 1 and Run 2 work. The dry run found an in-session system prompt and reported the missing reasoning-effort declaration. It wrote no archive. The native rollout was neither manufactured nor modified.

```text
sessions/codex/rollout-2026-11-23T16-54-25-01a20954-8a7c-7f20-ac1c-06203b1ff187.jsonl  codex  59 turns  379 lines
system prompt: in-session
missing: ... the effort (--effort <level>, or --effort default for the harness's own)
dry run: nothing written
```

MakeFun reported 0 entries used, 6 of 6 available that UTC day, 50 of 50 submission attempts remaining and 40 of 40 remaining under the hard ceiling. The account-adjusted total was withheld. GitHub authentication still failed for `lastborn04`, and `GET /repos/lastborn04/world-in-focus-20261122` returned 404. The local repository is on unborn `main` with no remote. Public ownership and the complete commit-and-transcript gate remain unverified. The badge URLs assume the workspace name will be the GitHub repository name.

## Remaining weaknesses

- Thumbnail density is high. The masthead, date, lead headlines and main figures carry the reduced proof, while most secondary captions need the 600-pixel or native version.
- Three featured illustrations provide the richest storytelling. Mosaic drawings are necessarily compact. The Poland file illustration is less distinctive than the event-specific artwork.
- Seven markers provide locators for a selection of stories. The map uses a land-only base with an approximate Bayelsa placement and no country boundaries.
- The science item clearly gives the 21 November UTC insertion and the 22 November AP report. ESA’s public confirmation predated AP’s report, and the event itself fell on 22 November in Japan time. This day-boundary distinction is documented in the register.
- Financial coverage centers on Coinbase and Seoul’s stabilization preparations. The edition has no dedicated South American lead.
- The official bounty has no local grade. No score, approval, publication or submission was recorded.

## Deliverables

| File | Purpose |
| --- | --- |
| `output/entry.png` | 1024-pixel competition image |
| `output/preview-600.png`, `output/preview-300.png` | Reduced proofs |
| `output/design-comparison.png` | Run 1 and Run 2 visual comparison |
| `SOURCES.md` | Claim-by-claim register, dates and links |
| `render.py`, `assets/`, `edition.png`, `main.ts` | Editable renderer, data, canonical image and competition entrypoint |
| `verify_runtime.py` | Local isolation and resource measurement probe |
| `archive/run-1/` | Preserved Run 1 image, thumbnail, renderer and source register |
