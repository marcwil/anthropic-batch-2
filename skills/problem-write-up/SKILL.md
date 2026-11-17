---
name: problem-write-up
description: Turn notes, agent output or a discussion thread about an open problem into a self-contained LaTeX problem write-up (template/question-template.tex) that a mathematician who was not there can follow. Separates the facts from the writing, writes the prose in a fresh context, and tests it on cold readers and fact checkers. Use for "write up this problem", "make this readable", "polish this", or "deslop this".
---

# Write up an open problem

Adapted from the Iliad SRI skill `sri-write-up`, whose method comes from Zach Furman with additions by Arturs Berzins. This version is for the open-problem template in this repository: short LaTeX documents that state questions precisely and say what is known.

The agent (or person) that worked on a problem should not write it up alone. By then it carries a lot of context: names it coined, results it assumes are established, threads the reader never saw. It writes for itself and gives every detail equal weight. This skill splits the job into roles so that the writer and the reviewers cannot inherit that context.

## Roles

| Role | Sees | Does |
|---|---|---|
| **Lead** (you) | Everything | Runs the process, checks the key claims, decides when to stop |
| **Curator** | The sources | Chooses what goes in and writes the fact sheet |
| **Writer** | The fact sheet, [style.md](style.md), a voice sample | Writes the prose |
| **Cold reader** | The problem as a reader would see it | Reports what confused it |
| **Fact checker** | The problem, the fact sheet and the sources | Finds errors in mathematics, quantifiers, status and credit |

Start each writer, cold-reader and checker call in a fresh session with no other context (a new agent session, or a subagent that is not a fork of your conversation), from an empty directory. Put the files it needs in the prompt. Do not tell a reader or checker who wrote the text. If you can, use a different model for writing than for checking; isolation matters more than the choice of model. The prompts are in [prompts.md](prompts.md).

## Pick the mode

- **Light pass** (a problem of up to about three pages, or a short revision): you curate (step 2) and rewrite the prose yourself following [style.md](style.md), then run one cold read (step 5) and one fact check (step 6). Repeat the fact check after every rewrite.
- **Full pipeline** (a long problem with several questions, or one built from long, messy sources): all steps.

## What the author owns

The statements are the author's. Do not reword a `question`, `conjecture` or `theorem` environment beyond fixing notation and defining undefined symbols. Never strengthen, weaken or add a variant without the author's agreement; mark any such suggestion `[CHECK]`. Polishing covers the prose around the statements: Background, What is known, What would count as an answer, Why it matters.

## Process

**1. Settle the brief.** The reader is a strong mathematician (and a strong model) who has never seen our discussions. Afterwards they should know exactly what is being asked, what is known, and what would count as an answer. Ask the author for a paragraph of their own writing to use as the voice sample, or use one of their papers.

**2. Curate.** List every claim the write-up makes: definitions, known results, partial progress, heuristics, motivation. For each, note its source (paper, theorem number, message, unpublished draft and its author) and its status, using distinct labels:

- **Proved**: with a citation precise enough to find the theorem.
- **Unpublished**: proved in a draft or note; name the author.
- **Computed**: say over which sizes or samples. This is evidence, not a theorem.
- **Informal**: an argument someone checked by reading.
- **Conjectured** or **heuristic**.

Cut claims you cannot source. Check the key claims yourself against the sources: a citation in an agent's notes can be wrong, and a "proved" result can turn out to be conditional. Rank what remains into **main** (the reader needs it to understand the question) and **detail** (context a reader can skip; it goes in a remark or footnote).

**3. Write the fact sheet.** Bullets, no prose, one block per template section: the question(s) exactly as the author states them, every symbol that needs defining, the known results with status and source, what counts as an answer, why it matters, the caveats. Mark exactly one MAIN point per section. Mark any judgement of significance as opinion. The sheet must stand alone: replace coined names with descriptions and remove references to threads, earlier drafts and other files.

**4. Write the prose.** Give the writer the sheet, [style.md](style.md) and the voice sample, and ask for the LaTeX body of the template sections. In the full pipeline, write each section in a separate call. The writer decides wording and order; it does not add facts.

**5. Read it cold.** Give a cold reader only the compiled text of the problem. Send its report back to the writer verbatim as notes.

**6. Check the facts after every writing round.** A fact checker compares the draft with the sheet and the sources, claim by claim: wrong statements, dropped quantifiers ("for all sufficiently large n"), reversed implications, sufficient conditions described as equivalent, conditional results stated unconditionally, informal results presented as proved, results credited to the wrong person. Writers reintroduce overstatements in every round, and curators make errors too. When the error is in the sheet, correct the sheet against the sources first. Send corrections to the writer as notes rather than editing the prose yourself.

**7. Decide when to stop.** Repeat steps 4 to 6 while each round produces fewer complaints. Stop when a round finds nothing that would change what a reader understands, but keep fact-checking until a round comes back clean. If serious complaints remain and stop falling, the problem is the curation: go back to step 2 or ask the author. When a section is hard because the mathematics is hard, keep one idea in the main text and move the machinery into remarks.

**8. Hand it to the author.** A human has to read the result before it is sent. Report the status of each claim and what you cut. Ask the author to name anything that feels off, and pass their words to the writer unchanged.

## Output

The output is the filled-in template, `problems/<topic>-<short-name>/<short-name>.tex`, compiling with `latexmk -pdf`. Keep the fact sheet next to it while you work (for example `notes/fact-sheet.md`, outside the archive you send) so that a claim can be traced to its source. Do not post the write-up anywhere unless the author asks.
