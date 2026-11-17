# Open problems for Anthropic: batch 2

A template for writing up open problems for the second batch of questions that Iliad researchers and fellows send to Anthropic (November 2026). Coordinated by Marcus Wilhelm in Zulip #AskAnthropic.

**Deadline: Thursday 19 November 2026, 09:00 UK time** (Wednesday 01:00 in California).

This repository only holds the template and a packing script. **Submissions are collected privately**, so please don't open pull requests or push your problem here: this repository is public.

## Contributing a problem

1. Clone the repository (or download it as a zip from GitHub):
   `git clone https://github.com/marcwil/anthropic-batch-2.git`
2. Copy [`template/question-template.tex`](template/question-template.tex) to `problems/<topic>-<short-name>/<short-name>.tex`, e.g. `problems/relu-max-units/relu-max-units.tex`. Put any figures in the same folder. One folder per problem; a problem may contain several related questions.
3. Fill it in. Define every symbol: the problem must make sense to someone who has never seen our Zulip. Fill in the metadata block, including any related unpublished work by group members.
4. Check that it compiles: `latexmk -pdf <short-name>.tex`.
5. Pack it: run `python3 make_archive.py` in the repository root. This writes `batch2-<folder>-<date>.zip` with the problem folders you added or changed, without build files or PDFs. To choose folders yourself: `python3 make_archive.py <folder> [<folder> ...]`.
6. Send the zip to Marcus Wilhelm by Zulip DM, or post it in the batch-2 topic in #AskAnthropic.

A rough description posted in Zulip is also fine; we will format it and ask you to check the result.

If you use an agent to write it up, the prompt at the bottom of the template is a good start. Please read and check its output before sending it.

## Layout

| Path | Contents |
| --- | --- |
| `template/` | The problem template |
| `problems/` | Where you put your problem folder (empty here) |
| `make_archive.py` | Packs your problem folder(s) into a zip to send in |

## Credit

Each problem names its contributors. Where a question overlaps with unpublished work by a group member, the problem says so.
