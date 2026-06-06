---
title: comma.ai
type: project
updated: 2026-06-05
sources: [an-architecture-for-life, imitation-learning, on-device-learning, a-machine-ecology, anticloud-hopecore, can-tinygrad-win, the-opinion]
---

# comma.ai

Founded **2015**. Sells openpilot hardware (the comma device, now **comma four**) that adds
L2 driver assistance to existing cars. As of 2026: ~10 years old, profitable, growing, ~30k
cars running openpilot for driving, with a thriving ecosystem of forks and third-party hardware.

## Why it exists (the real goal)

Self-driving is just **step one** toward *machine life* — AI that can fight entropy without
humans ([[a-machine-ecology]], [[to-fight-against-entropy]]). "After comma solves self driving,
we'll turn our attention to [the Coffee Test]." The roadmap in his head: self-driving → home
robots (cook/clean) → general-purpose robots → robots that fix robots. "openpilot is the next
generation of ROS" — universal robotics software. "Let's at least get to human."

He also started comma for the [[power-centralization|centralization]] reason, not because
self-driving is good for the world: "the technology is inevitable, but whether it's centrally
owned and controlled is not." A Waymo network can revoke your "right" to transport; openpilot
is individually owned and open source ([[the-problem-of-the-state]]). "Who has root?"

## Technical approach (the AI bet)

- **Learn everything end-to-end; hard-code only what's in human DNA.** "There's nothing about
  traffic cones in your DNA, so don't hire a guy to write cone-handling software"
  ([[where-the-bitter-lesson-ends]]). The famous "cone guy" / "bishop guy" critique.
- **The three functions** ([[an-architecture-for-life]]): representation (the "vision model,"
  an EfficientNet outputting a 1024-d gaussian), dynamics (the "temporal model," a GRU),
  prediction (dense layers) — the MuZero h/g/f decomposition applied to driving.
- **Imitation learning & behavioral cloning** ([[imitation-learning]]): naive `f(state)->action`
  drifts because errors accumulate and alter the next input. comma's history: steering-angle
  model → lane-position model as an unbiased correction → e2e. "Lanes" were "the original sin"
  they keep trying to remove. The billion-dollar open question: how do you end-to-end ground-truth
  the error-correction function?
- **Three model paradigms:** (1) hand-coded lanes/cars (openpilot ≤0.6), (2) supervised learning
  in simulation (current), (3) **RL on the world** (temperature 0 — "nobody wants their car to
  explore"). You can't jump 1→3 ([[on-device-learning]]).
- **On-device learning** is the only way forward for general robots — you can't put gravel,
  snow, and banana peels in a simulator. "What is the human reward function?" (the meta reward
  in DNA: autoregression, curiosity, behavioral cloning, doing-what-others-want).

## comma vs. the field

His four-labs framing ([[happy-brithday-to-me]]): DeepMind (games/sim), OpenAI (scale/scrape),
Tesla (shippability/grit), **comma (real world, real data, end-to-end, RL, on-device)**.

## On Tesla / "the opinion that pisses everyone off"

[[the-opinion]] / [[can-tinygrad-win]]: he expects **Tesla to solve self-driving first** (and
it's "real AI you can evaluate, unlike remote-control cars that break when the power goes out")
but says it's "**8 years away** from being *finished*" (even money) — meaning matching a skilled
attentive human everywhere, not just useful (comma is already useful). It's iOS vs Android, not
winner-take-all. Most self-driving competition "wasn't even playing the right game" and is now
out of business with billions lost. Robotaxis make economic sense in 3-5 years in limited scopes
([[war-on-car-ownership]]).

Related: [[tinygrad-and-tiny-corp]] (the compute layer for comma's robots), [[ai-and-agi]].
