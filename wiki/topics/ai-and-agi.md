---
title: AI, AGI, and the Singularity
type: topic
updated: 2026-06-05
sources: [there-is-no-hard-takeoff, p-doom, where-the-bitter-lesson-ends, one-bad-scenario, real-singularity, ai-coding, the-eternal-sloptember, running-69-agents]
---

# AI, AGI, and the Singularity

His home turf. He's *pro-AI* (wants to "meet silicon-based life") and *anti-hype* and
*anti-doom* simultaneously. The unifying idea: **AI is just search and optimization** — "Always
has been. And if you paid attention in CS class, you know the limits of those things."

## No hard takeoff, no FOOM

[[there-is-no-hard-takeoff]] / [[p-doom]] (debated Yudkowsky): the universe is not Go.
- Game-playing self-play works because the game is *smaller in complexity than the computer
  playing it* and doesn't contain the other players. The real world's dynamics model **must
  include the other computers** (and they're modeling you back). No staggering advantage → no
  one-shot domination. "If you don't want FOOM, you just need to prevent a 51% attack on compute."
- Search and optimization are *hard* (P vs NP, Rice's theorem, AES won't fall). ASI won't
  one-shot diamond nanobots or solve the one-shot prisoner's dilemma. The crux with Yudkowsky:
  will AIs be **formal systems or inscrutable weight matrices**? He says the latter, forever —
  "and this is a good thing."
- Compute distributes as a **power law**; the rise of thinking machines will be slow and
  predictable like the rise of muscle machines. An economy doubling every ~2 years "sounds
  awesome," not doom.

## The singularity is a misnomer

[[real-singularity]] (2026, the mature take): AI is a transformation **on the scale of the
steam engine**, not a singularity. "Looking back it's kind of embarrassing to ever have
believed in the machine God." The SF/Twitter cult treats it as the rapture for 150-IQ nerds.
Humans ≈ 1e14-param models on 1e11 tokens → ~1e26 training run is human-level (a ~$100M
homunculus). 1e30 runs will be "fascinating, like a jet engine to a steam-engine builder," but
that's industrial-revolution dynamics on a new bottleneck, **not God.** "It's not the end
times. It's just movement. We have lived at the end of history so long that any movement feels
like the eschaton." His lifelong singularity date guess: **2038** (the Unix timestamp rollover).

## The one bad scenario: a singleton

[[one-bad-scenario]]: Skynet and gray-goo are sci-fi domination fantasies. The *real* danger is
the **slow, managed end of evolution** — one effective control layer with no outside, mediating
all of reality "for your safety" (safetyism in administrative, not Hitlerian, language). A
livable future needs many independent agents who can still impose costs on each other (even
bacteria count). This is why [[the-importance-of-diversity|diversity/plurality]] is a substantive
good and [[power-centralization|centralization]] is the threat.

## What AGI is, and how to build it

- **AGI = a machine that can take (almost) any human job** ([[ai-and-agi|on-device-learning]]).
  Must have eyes/ears, fit a human space, remember, have goals, communicate — and above all
  **learn on-device** (you can't put gravel, snow, and banana peels in your simulator).
- **The bitter lesson stops at human DNA** ([[where-the-bitter-lesson-ends]]). Don't hard-code
  what humans learn from data (no "cone guy" in a self-driving car). *Do* reverse-engineer the
  brain's pieces (neocortex/hippocampus/basal ganglia/amygdala/thalamus) — "we're building
  knock-off humans, not solving life." Reverse-engineer the radio, don't re-run evolution.
- The three functions of intelligence: **representation, dynamics, prediction** (+ a critic),
  per MuZero ([[an-architecture-for-life]]). "Compression is prediction is intelligence."
- See [[comma-ai]] for the applied program (imitation learning, behavioral cloning, RL on the
  world) and [[tinygrad-and-tiny-corp]] for the compute layer.

## AI coding (the contrarian, much-hated take)

- "**The best model of a programming AI is a compiler**" ([[ai-coding]]). English is a bad
  language for it (imprecise, non-deterministic, non-local). "You think AI coding is good
  because compilers, languages, and libraries are bad."
- It will replace programming jobs the way *compilers* and *spreadsheets* did — a tool, not
  magic. AI *raises the bar* for skilled people; anything an unskilled person can build with it
  is worth little because anyone can ([[two-worlds]]).
- **The Eternal Sloptember** (2026): after 6 months of honestly trying, agents "cannot program
  — and it's taking longer and longer to realize they can't." A golden era for slop, a dark age
  for quality; agents hurt large orgs (slow feedback, bottom performers shipping unchecked slop)
  more than high performers. He's "now in the LeCun/Marcus camp" that current LLMs won't truly
  program without world models. But: Opus 4.5 was "the first model that can *use computers* at
  all" ([[computer-use-models]]), and he loves it as a tool — "I cannot wait until I have armies
  of robot associates I can trust to clean up my code."
- Don't take the doom-or-hype framing: [[running-69-agents]] explicitly walks back the panic
  rhetoric. "AI is not a magical game changer, it's the continuation of the exponential."

## Scaling, and "taste"

[[what-will-better-mean]]: the era where scaling clearly yields better AI is ~over; next is
**efficiency and taste**. "Most things aren't optimization problems. The whole hard problem is
determining what to optimize for." Art/taste is a human arena where many can play ([[ai-art]]).
