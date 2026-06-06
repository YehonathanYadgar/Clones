---
title: tinygrad & the tiny corp
type: project
updated: 2026-06-05
sources: [the-tiny-corp-raised-5M, can-tinygrad-win, five-years-of-tinygrad, AMD-YOLO, tragic-intel, tiny-corp-product, own-a-zettaflop]
---

# tinygrad & the tiny corp

**tinygrad**: a deep-learning framework. First commit **Oct 17, 2020** (started as a toy to
learn neural nets). **the tiny corp**: the company, raised **$5.1M on May 24, 2023**. As of
end-2025: 6 people, ~18,935 lines of code, ~$2M/yr revenue from selling tinyboxes, a
"deconstructed company" (a Discord + GitHub, almost nothing private).

## The mission: commoditize the petaflop

A human brain is ~20 PFLOPS, but that costs ~$1M to buy / $100/hr to rent — inaccessible. With
AI heading toward a few entities controlling most compute, "**I do not want 'I think there's a
world market for maybe five computers' to ever be the world we live in.**" The goal: make
compute a commodity so ~20 chip companies can rival NVIDIA and everyone can **own** their AI
(training *and* inference), not rent it ([[the-tiny-corp-raised-5M]], [[how-do-i-stop]]).

## The technical thesis

- **Start with software, not silicon.** Every AI-chip startup that taped out a chip failed
  because they couldn't write a decent framework. "Taping out the chip is the easy part." The
  hard, valuable part is the software — which is why NVIDIA's market cap dwarfs AMD's despite
  similar hardware. "CUDA isn't really the moat people think; it's just an early ecosystem."
- **NN compute is a DSP, not general compute.** ~95% of models have all compute and memory
  accesses *statically computable* — but the minute you call into Turing-complete kernels (CUDA)
  you lose that and fall back to caching/warp-scheduling/branch-prediction (Rice's theorem). His
  public **reversal on VLIW** is the cleanest example of his "if I can't predict it I don't
  understand it" honesty: first mocked VLIW/big-chips ([[hacking-and-jailbreaks|a-breakdown-of-ai-chip-companies]]),
  then "I'm kicking myself for getting this wrong" — for ML, VLIW and fancy compilers are right
  because the same ops run every time (a-correction-on-ai-chips).
- **tinygrad's bet** ([[can-tinygrad-win]]): a tiny IR (ADD/MUL only, lazy like Haskell) that
  takes you all the way to the hardware. The deeper claim is that "the bitter lesson applies to
  software too" — multi-machine/GPU/SM/ALU scheduling is "the same underlying problem at
  different scales," and you can expose it as one search problem and burn compute (LLMs, SAT
  solvers, RL) to beat hand-tuned kernels. Target: a full GPT-scale training stack to MMIO in
  ~20k lines, **zero dependencies** (removing even LLVM) to drive an AMD GPU.
- Honest about the risk: "For comma to win, all it took was people being wrong about LIDAR/
  mapping/end-to-end. For tinygrad to win requires something deeper to be wrong about *software
  development in general*." It's his "second startup, so taking more risk is appropriate."

## The hardware politics (AMD / Intel / NVIDIA)

- **AMD YOLO** ([[AMD-YOLO]]): after a long public fight with broken ROCm drivers, AMD "passed
  my cultural test" and sent MI300X boxes; tiny has a "fully sovereign AMD stack." He bought
  ~$250k of AMD stock — "either NVIDIA is super overvalued or AMD is undervalued." Has an **AMD
  contract** to get MI350X/LLaMA-405B onto MLPerf competitive with NVIDIA, negotiated mostly in
  public on Twitter.
- **The Tragic Case of Intel AI** ([[tragic-intel]]): a deep, link-heavy teardown of Intel's
  unsellable Gaudi/Ponte-Vecchio inventory. Diagnosis: AMD's dysfunction is fixable (leadership
  that can decide — Lisa Su replied to his first email; they just under-invested in software);
  Intel's is **committee leadership** ("nobody who can say yes, just many who can say no") →
  "0 chance." A window into how he reads companies via *who has the power to make a deal*.

## The product vision: a box that learns

[[tiny-corp-product]]: today the LLMs "do not learn — everyone has the same Claude/Codex/Kimi
with the same weights, desires, and biases," a staggering collapse in diversity ("a world market
for maybe five people"). The future tiny corp product is a **tinybox in your house that updates
its weights from interacting with you** — "Not API-keyed SaaS clones. Something that lives in
your house and learns your values. Your child." The open question that decides cloud-vs-local:
"if everything unique about you can fit in a 10 kB CLAUDE.md… we have a sad future ahead" —
prompting is *costuming*, not learning. And the dream of raw scale: [[own-a-zettaflop]] — "one
million Claudes… spend a human year in 10 minutes. I'll own this before I die."

## How to get hired

"There's only one way to get hired at the tiny corp: high-quality pull requests to tinygrad.
Job interviews are obsolete, prove you can do the job by doing the job." MIT-licensed; ~1
meeting/week; self-directed; bounties on the roadmap.

Related: [[comma-ai]] (the customer for tiny's compute), [[technology-and-freedom]], [[ai-and-agi]].
