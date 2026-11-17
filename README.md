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

## Writing it up with an agent

If you use an agent, the prompt at the bottom of the template is a good start. Please read and check its output before sending it.

To turn notes, agent logs or a long thread into a problem a reader can follow, use the write-up skill in [`skills/problem-write-up/`](skills/problem-write-up/SKILL.md), adapted from the Iliad SRI skill `sri-write-up`. It separates the facts from the prose, has the prose written in a fresh context, and tests it on cold readers and fact checkers. In Claude Code, started in this repository, it is available as `/problem-write-up`; other agents can be told to read and follow `skills/problem-write-up/SKILL.md`. For a problem of a few pages, a light pass is enough:

1. **Curate.** List the claims and known results the write-up makes, with a source and a status for each (proved, unpublished, computed, conjectured). Cut what you can't back up.
2. **Rewrite the prose** (Background, What is known, Why it matters) following the skill's `style.md`. Leave the statements of your questions and conjectures as you wrote them.
3. **Cold read.** Give a fresh agent session, with no other context, only the problem text and ask: What is the question? Quote anything that confused you. Which symbols were undefined? Could you tell what counts as an answer? Fix what it reports.
4. **Fact check.** Give another fresh session the problem and your sources and ask it to compare them claim by claim: dropped quantifiers, reversed implications, conjectures stated as theorems, results credited to the wrong person.

For a long problem built from messy sources, follow the skill's full pipeline. The prompts for each role are in [`skills/problem-write-up/prompts.md`](skills/problem-write-up/prompts.md).

## Layout

| Path | Contents |
| --- | --- |
| `template/` | The problem template |
| `problems/` | Where you put your problem folder (empty here) |
| `make_archive.py` | Packs your problem folder(s) into a zip to send in |
| `skills/problem-write-up/` | Agent skill for writing up and polishing a problem (linked into `.claude/skills/`) |

## Credit

Each problem names its contributors. Where a question overlaps with unpublished work by a group member, the problem says so.
