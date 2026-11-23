# Run 3 · Final management review

[Native entry](output/entry.png) · [600-pixel proof](output/preview-600.png) · [300-pixel proof](output/preview-300.png) · [Run 2 versus Run 3](output/run-2-vs-run-3.png)

## Editorial changes

The reference crop shows how a tightly ranked set of three large illustrated leads, smaller stories and a dense digest can support different reading depths. Its numbered map connects geography to coverage. Its tiniest captions and digest also illustrate the trade-off between density and thumbnail readability. The screenshot and temporary crop stayed outside the project.

Run 3 keeps the 20-item story roster, identity, date, lead art, map, crypto panel and digest. It enlarges mosaic captions from 15 to 16 pixels and digest captions from 13 to 14. Selected mosaic headlines are 2 pixels larger. Four repeated spot illustrations were removed so the related headlines can use the available space. The Seoul vignette now draws a market backstop, and the caption makes conditional deployment explicit. The Warsaw headline states who alleges what, and the caption identifies the earlier August plot. The map key now names each city or region and country, with a subject beside each location. The [verification register](SOURCES.md) gives exact printed headlines, event and publication dates, source URLs, verification results and caveats for all 20 items.

## Technical results

The entry is a valid RGB PNG at 1024 × 1024 and 598,329 bytes. Its SHA-256 is `2043366dc11d4a48fe7ac66c0563875e4e21dc7dd3698fa4dd05c660e604cf42`. Both reduced proofs decoded. An independent Pillow render produced the same bytes.

Two Node 22.23.4 runs used a read-only `/bot`, isolated networking, one CPU, a 60-second timeout and separate writable mounts at `/output`. Both wrote the literal `/output/entry.png` and matched the published local artifact. Elapsed times were 0.287 and 0.186 seconds. Peak Node RSS was 60,652 and 60,656 KiB. These are local measurements. The official container’s cgroup and process limit were outside this test.

- [Artwork checks and hashes](evidence/artwork-run-3.txt)
- [Offline runtime command output](evidence/offline-run-3.txt)
- [Original kit, quota and GitHub command output](evidence/makefun-run-3.txt)
- [Current kit command output](evidence/current-kit-run-3.txt)
- [Coinbase response captured in Run 3](evidence/coinbase-run-3.json)

## Prerequisites and remaining issues

- The original kit’s dry run discovered one genuine Codex rollout without a manually supplied session. The native record identifies Codex CLI 0.171.0, provider `openai` and model `gpt-6.2-sol`. The checked rollout metadata lacks a verifiable effort declaration. No bundle was produced or transcript altered.
- The original kit’s supported `check --kit . --repo <workspace> --worktree --transcripts <native rollout>` returned 13 pass, 1 fail, 5 skip, and 5 deferred to submission. It accepted the MIT license, Node 22 entrypoint, authentic logs and agent authorship. The missing run record caused the failure. After the checker flagged a newer release, the freshly downloaded official level 39 kit reproduced the result. Authorship was 798 of 1,242 counted lines (64.2%), above the required 30%. Ready-to-submit bundle compliance is open.
- GitHub authentication succeeded as `lastborn04`, while the intended repository returned HTTP 404. The local repository has no commit or remote. Public ownership, repo creation date, About settings and commit reachability are unverified. The README contains the expected badge paths for the intended repository. The account had six entries available that UTC day at the time of the check.
- The headline hierarchy and primary figures remain recognizable at 300 pixels. Secondary captions and the map and chart sublabels remain small at that scale. The map shows selected story locations, with Bayelsa plotted approximately.
- No submission, approval or local grade was recorded.
