# Run 1 audit evidence

## Artifact and runtime

| Check | Result |
| --- | --- |
| Official kit integrity | All 11 files matched the size and SHA-256 in `kit.json`. Manifest bundle digest `00314c2cb5a445fd508bab7f92ae6a1a15dec902d84b7c9dcaa326beafe638bb`. |
| Entry artifact | RGB PNG, 1024 × 1024, 475,500 bytes. Pillow verified the file and fully decoded its pixel data. |
| SHA-256 | `d5bd8bfcb3208556a629eb25450fd602e19a0de505bab5cffc4fb593b5e205c0` |
| Runtime and determinism | Node 22.23.4. Two fresh output directories produced byte-identical copies with a read-only copy of the input, one CPU, a 60-second timeout and seccomp blocking socket creation. Elapsed wall times were 0.119 s and 0.110 s, including the launcher. A third run measured 60,676 KiB peak child RSS. |
| Literal output path | A separate Bubblewrap run exited 0 with an unshared network namespace, a read-only `/bot`, and the workspace’s `output` directory bound to writable `/output`. |
| Artwork rebuild | A separate Pillow render compared byte for byte with `edition.png`. |
| Thumbnail | Inspected the 300 × 300 proof. Headlines remain readable. Supporting captions and some section labels are small at that size. |
| Official grader | No local grade exists for this bounty. The facility-specific container and full MakeFun submission checks remain unverified. |

## Transcript discovery

The first successful official discovery dry run followed creation of the entrypoint. The final dry run again found exactly one genuine Codex rollout by repository match, with zero explicitly supplied sessions, zero ancestor-directory sessions and zero family sessions. It found the system prompt in-session and collected one settings file. Excerpt from the second dry run:

```text
1 session file(s): 0 named with --session, 1 matched to the repository, 0 started above it and working on it, 0 the parent or a subagent of another
  sessions/codex/rollout-2026-11-23T16-54-25-01a20954-8a7c-7f20-ac1c-06203b1ff187.jsonl  codex  31 turns  199 lines
  system prompt: in-session
  missing: the agent facts: one is neither declared nor recorded by every root session, so the site would reject the entry: the effort (--effort <level>, or --effort default for the harness's own)
dry run: nothing written
```

The native rollout started at 16:54:25 UTC on 23 November, inside the competition window. Codex preserved the original rollout in its native session directory. No recording command, synthetic transcript, edit to the source logs, or upload was performed. The official dry run exercised discovery only. An admissible bundle needs a verified effort declaration and the full official checks against the eventual commit.

## Account and repository

- MakeFun identified the authenticated account as `@adeodu-yinka`. The official quota response on 23 November showed 0 entries made, 6 of 6 daily entries left, 50 of 50 submission attempts left, and 40 of 40 under the hard limit. It reported that submission was currently allowed and withheld the reputation-adjusted total. The deadline and daily reset were both 00:00 UTC on 24 November.
- The GitHub token check failed. A public repositories query for `lastborn04` returned no match for `world-in-focus-20261122`. The workspace is an unborn local `main` with no remote. The three README badges assume the workspace name becomes the public repository name.
- GitHub eligibility remains unverified. It requires a public repo created after the competition opens, a commit reachable on a branch, verified ownership or a linked-wallet claim, and the required GitHub About settings. The work uses the kit starter’s license. Previous bounty projects were left untouched. No submission was made.

## Editorial limitations

The page covers Nigeria, Türkiye, Iran, the United States, Portugal, China through the chip story, and Japan and Europe through BepiColombo. One African story carries the continent’s coverage. Latin America and Oceania have no standalone items. Bitcoin and U.S. futures carry the markets section, and the Bitcoin price relies on a published Coinbase observation rather than a direct exchange extract. At thumbnail size the footer and detailed captions require closer viewing.
