---
name: empirical-prompt-tuning
description: Methodology for iteratively improving agent-facing instructions (skills / slash commands / CLAUDE.md / code-gen prompts) via bias-free executor + two-sided evaluation (self-report + instruction-side metrics). Meta-skill, invoke ONLY when the user explicitly asks for an "empirical" eval of a prompt or skill, or for the Iter-0 description / body consistency check. Do NOT auto-invoke after every skill edit; this loop is operator-triggered by name.
---

# Empirical Prompt Tuning

The author of a prompt cannot judge its quality. The clearer the writer thinks something is, the more likely another agent will stumble on it. The core of this skill is to **have a bias-free executor actually run the instruction, evaluate it two-sidedly, and iterate**. Do not stop until improvements plateau.

## When to use

- Right after creating or substantially revising a skill / slash command / task prompt
- When an agent does not behave as expected and you want to attribute the cause to ambiguity on the instruction side
- When hardening high-importance instructions (frequently used skills, automation-core prompts)

When not to use:
- One-off throwaway prompts (evaluation cost does not pay off)
- When the goal is not to improve success rate but merely to reflect the writer's subjective preferences

## Workflow

0. **Iteration 0 — description / body consistency check** (static, no dispatch needed)
   - Read the triggers / use cases claimed by the frontmatter `description`
   - Read the scope the body actually covers
   - If there is a gap, reconcile description or body before moving to iter 1
   - Example: description says "navigation / form filling / data extraction" but the body is only a CLI reference for `npx playwright test` — detect that kind of gap
   - If you skip this, the subagent will "reinterpret" the body to match the description, and accuracy will come out high even though the skill does not actually meet the requirements (false positive)

1. **Baseline preparation**: Fix the target prompt and prepare the following two things.
   - **Evaluation scenarios**, 2 to 3 kinds (1 median + 1 to 2 edge). Realistic tasks that assume actual situations where the target prompt would apply.
   - **Requirements checklist** (for computing accuracy). For each scenario, enumerate 3 to 7 items the deliverable must satisfy. Accuracy % = items satisfied / total items. Fix this in advance (do not move it afterward).
2. **Bias-free read**: Have a "blank-slate" executor read the instruction. **Dispatch a new subagent** via the Task tool. Do not substitute with a self-reread (it is structurally impossible to view text you just wrote objectively). When running multiple scenarios in parallel, place multiple Agent invocations within a single message. For how to handle environments where dispatch is unavailable, see the "Environment constraints" section.
3. **Execution**: Hand the subagent a prompt that follows the **subagent invocation contract** described below, and have it execute the scenario. The executor produces an implementation or output and returns a self-report at the end.
4. **Two-sided evaluation**: Record the following from the returned results.
   - **Executor self-report** (extracted from the body of the subagent's report): unclear points / discretionary fill-ins / places where template application got stuck
   - **Trace interpretation**: each unclear point is tagged with the phase it originated in (Understanding / Planning / Execution / Formatting — see "Subagent invocation contract"). Phase-local fixes land better than global "the prompt was unclear" fixes; a single Understanding-phase ambiguity often looks like a chain of Execution-phase failures.
   - **Structured reflection**: each unclear point must be returned as `Issue / Cause / General Fix Rule`. The `General Fix Rule` is the class-level abstraction that feeds the "Failure pattern ledger" — without it, fixes stay as one-off patches that rediscover the same mistake later.
   - **Instruction-side measurements** (the judgment rules are defined canonically in this section; refer to it from elsewhere):
     - Success/failure: counts as success (○) only when **all** requirements tagged `[critical]` are ○. If even one is × or partial, it is failure (×). The label is the binary ○ / × only.
     - Accuracy (achievement rate of the requirements checklist, %. ○ = full score, × = 0, partial = 0.5; sum and divide by total items)
     - Step count (use the `tool_uses` field in the usage meta attached to the Task tool return value as-is. Include Read / Grep, do not exclude them)
     - Duration (`duration_ms` from the Task tool usage meta)
     - Retry count (how many times the subagent redid the same decision. Extract from the subagent's self-report; not measurable from the instruction side)
     - **On failure, add a one-line note to the "unclear points" section of the presentation format stating "which [critical] item dropped"** (for root cause tracing)
   - The requirements checklist must include **at least one** `[critical]`-tagged item (if there are zero, the success judgment becomes vacuous). Do not add or remove [critical] tags after the fact.
5. **Apply the diff**: Put the minimum fix into the prompt to eliminate the unclear points. One theme per iteration (multiple related fixes are OK, unrelated fixes go to next time).
   - **Before applying the fix, explicitly state "which item in the requirements checklist / judgment wording this fix satisfies"** (fixes inferred from axis names often do not land. See the "Fix propagation patterns" section below.)
   - **If the unclear point is a "missing / incorrect fact" type, run the attribution triage before writing anything** (see "Attributing factual errors"): verify the fact against a primary source, then decide whether the defect belongs to the platform (report it, don't encode a workaround) or to your instruction (write it assertively).
   - **Consult the failure pattern ledger first**. If the structured reflection's `General Fix Rule` already matches a known pattern, the first question is "why didn't the existing fix prevent it?" — the fix may need to move closer to the top of the prompt, or be re-worded, before a new ledger entry is added.
6. **Re-evaluate**: Run 2 → 5 again with a new subagent (do not reuse the same agent: it has learned the previous improvements). Increase parallelism if iterating further does not plateau improvements.
7. **Convergence check**: The rough rule is "stop when 2 consecutive iterations have zero new unclear points AND metric improvements fall below the thresholds (below)". Make it 3 consecutive for high-importance prompts.

## Evaluation axes

| Axis | How to capture | Meaning |
|---|---|---|
| Success/failure | Did the executor produce the intended deliverable (binary) | Minimum bar |
| Accuracy | What % of requirements the deliverable satisfies | Degree of partial success |
| Step count | Tool-call / decision-step count used by the executor | Indicator of instruction waste |
| Duration | Executor's duration_ms | Proxy indicator of cognitive load |
| Retry count | How many times the same decision was redone | Signal of instruction ambiguity |
| Unclear points (self-report) | Executor enumerates as bullets | Qualitative improvement material |
| Discretionary fill-ins (self-report) | Decisions not fixed by the instruction | Surfaces implicit specification |

**Weighting**: Qualitative (unclear points / discretionary fill-ins) is primary, quantitative (time / step count) is auxiliary. Chasing only time reduction makes the prompt too thin.

### Qualitative interpretation of `tool_uses`

Looking only at accuracy hides skill problems. Using `tool_uses` as a **relative value across scenarios** reveals structural defects:

- If one scenario is **3-5x or more** vs the others, that skill is a sign of being **decision-tree-index-leaning with low self-containment**. The executor is being forced into references descent.
- Typical example: all scenarios have `tool_uses` of 1-3 but one scenario alone has 15+ → there is no recipe for that scenario in the skill itself, so it is cross-searching references/
- Countermeasure: adding an "inline minimum complete example" or "guidance on when to read references" at the top of SKILL.md in iter 2 significantly drops `tool_uses`

Even at 100% accuracy, a skew in `tool_uses` is grounds for triggering iter 2. "Cut off based on accuracy alone" tends to miss structural defects.

### Fix propagation patterns (conservative / overshoot / zero-shoot)

Fix → effect is not linear. Pre-estimation can play out in the following 3 patterns:

- **Conservative swing** (estimate > actual): one fix aimed at multiple axes but only moved one. "Aiming at multiple axes tends to miss."
- **Overshoot** (estimate < actual): one structural piece of information (e.g., a combination of command + config + expected output) satisfied judgment wording across multiple axes at once. "Combinations of information structurally hit multiple axes."
- **Zero-shoot** (estimate > 0, actual = 0): a fix inferred from the axis name did not reach any of the judgment wording. "Axis names and judgment wording are different things."

To stabilize this, **before applying the diff, have the subagent verbalize "which judgment wording this fix satisfies"**. Estimation accuracy does not come out unless you tie things at the threshold-wording level. When adding a new evaluation axis, also concretize the judgment criteria for each point down to the threshold-wording level (at a granularity the subagent can judge, such as "all explicit" or "full text of a minimum working configuration" — so it knows what constitutes 2 points).

## Attributing factual errors (platform side vs instruction side)

When an unclear point is a **missing or incorrect fact** — not an ambiguity in your own wording — do not patch the prompt reflexively.

**First, verify the fact against a primary source** (official documentation, the implementation, or the live API / MCP server). **Do not treat executor reports as a primary source**: executors read the same upstream text you did, so several of them can share the same misreading, and a unanimous-looking claim can still be wrong.

**Then decide which side owns the defect.** A platform with a feedback channel (for Kuroco: `kuroco_feedback-send`) can fix confusing specs, thin tool `description`s, and missing reference docs — those fixes are permanent. A workaround written into the instruction becomes the misinformation source the moment the platform improves.

**Judgment rule: "if the platform side were fixed, would this sentence become wrong?"** YES → the platform owns it, report it and don't encode the workaround. NO → you own it, write the fact assertively.

| Symptom | Owner | What to do |
|---|---|---|
| Implementation bug (a declared field isn't saved; a documented parameter is ignored) | Platform | Report only. **Never encode the workaround** — once it is fixed, your instruction is the wrong one |
| A tool `description` / API reference / admin-screen label is ambiguous or incomplete, and **two or more independent executors misread it the same way** | **Both** | Report the wording fix (quote the current text, propose a replacement) **and** state the correct fact assertively in the instruction. Describing a spec is not a workaround — it stays true after the wording improves |
| Naming asymmetry (the same concept exposed under different parameter names across operations) | **Both** | Same as above: report the confusion, and write the correct names with the distinction spelled out |
| Behaviour no official document covers | **Both** | Ask for the doc addition. In the instruction, mark **exactly that one point** as "verify against the live system" — not the whole surrounding area |
| A feature gap (the operation you want simply does not exist) | Platform (feature request) + instruction | Write how to model the requirement **under the current spec**, marked as current-spec ("there is no X operation in the current spec"), and list it as a report candidate. This differs from a bug: the executor still needs to know what to do today |
| Your own typo / stale statement / mis-copied name | Instruction only | Fix the prompt. Nothing to report |

**Two independent executors making the same misreading is evidence about the source, not only about your prompt.** Both read the same upstream text and both got it wrong — that text's wording is a fix candidate. Record it as one.

**Reporting is an external transmission, so get approval first.** Show the user the exact fields that will be sent and obtain explicit approval before calling the feedback tool. When approval is not given, or no channel exists, **leave the report candidates as a list in the deliverable** (symptom / the exact wording at fault / proposed replacement / who reports it) so the finding is not lost.

### Separate the provisional notes from the durable instruction

Content that exists **because the upstream is currently confusing or incomplete** is a different kind of content from the durable instruction, and it should be removable later. The `Both` rows of the table above are what produce it: an ambiguous description or a feature gap forces you to write today's workaround, and that passage has a shelf life. Keep the two kinds physically distinguishable:

- **Keep the fact itself where it is used.** Moving a fact the executor needs into a separate "notes" file means executors don't read it and produce wrong output. What you separate is the *metadata*: why the passage exists and when it can be deleted.
- Mark each provisional passage in place with a grep-able marker (an HTML comment such as `<!-- spec-note: SN-3 -->` works: invisible when rendered, findable with one grep), and keep one **maintainer-facing** file listing: where the passage is / why it was written / the condition for deleting or shrinking it / the report status (receipt id).
- State in the instruction that this file is maintainer-facing and **not to be read while performing the task**, so it adds nothing to the executor's reading load.
- **Delete the passage and its ledger entry together.** Removing only one leaves either a stale note in the instruction or an untracked passage.
- What does **not** belong there: statements about stable specs (a model's response shape, an evaluation order, a documented parameter, a setting's semantics). Those stay true after the platform improves, so they have no deletion condition and belong in the instruction unmarked.

## Subagent invocation contract

The prompt given to the executor takes the following structure. This is the input contract for "two-sided evaluation".

```
You are an executor reading <target prompt name> with a blank slate.

## Target prompt
<Paste the full body of the target prompt, or specify a path for Read>

## Scenario
<One paragraph setting the scenario context>

## Requirements checklist (items the deliverable must satisfy)
1. [critical] <item that belongs to the minimum bar>
2. <normal item>
3. <normal item>
...
(Judgment rules are canonically defined in "Workflow 4. Two-sided evaluation / Instruction-side measurements". At least one [critical] is required.)

## Task
1. Follow the target prompt to execute the scenario and produce the deliverable.
2. On completion, respond with the report structure below.

## Report structure
- Deliverable: <artifact or execution summary>
- Requirement achievement: ○ / × / partial (with reason) for each item
- **Trace** (tag OK / stuck / skipped for each phase, one-line reason when not OK):
  - Understanding (reading the instruction and building a mental model)
  - Planning (deciding the approach / ordering)
  - Execution (actually doing the work)
  - Formatting (shaping the deliverable to the expected form)
  - *Collapsed form allowed*: when all four phases are OK, a single line `Trace: all OK` is sufficient. Emit phase-by-phase only when any phase is stuck or skipped. (This avoids happy-path boilerplate; the trace structure only earns its cost when something actually goes wrong.)
- **Unclear points (structured)**: for each issue, three lines:
  - Issue: <what observably happened>
  - Cause: <why, diagnosed at the instruction level>
  - General Fix Rule: <a class-level rule, not a spot fix, that would prevent this class of mistake>
- Discretionary fill-ins: places not fixed by the instruction and filled in by your own judgment (bullets)
- Retries: number of times you redid the same decision and why
```

The caller extracts the self-report portion from the report and fills the evaluation-axis table by obtaining `tool_uses` / `duration_ms` from the Agent tool's usage meta.

## Environment constraints

In environments where dispatching a new subagent is not possible (already running as a subagent, Task tool is disabled, etc.), **do not apply** this skill.
- Alternative 1: ask the parent session's user to start a separate Claude Code session and delegate the evaluation there
- Alternative 2: give up on evaluation and explicitly report to the user "empirical evaluation skipped: dispatch unavailable"
- **NG**: substitute with a self-reread (bias enters, so you must not trust the evaluation result)

**Structural review mode**: when you want to check only the **consistency and clarity of the description** of the skill / prompt rather than run empirical evaluation, carve it out explicitly as structural review mode. Note clearly in the request prompt to the subagent "this round is structural review mode: text consistency check, not execution". That way the subagent will not trip on the skip behavior in the environment-constraints section and can return a static review. Structural review is an aid to empirical, not a replacement (it cannot be used for consecutive-clear judgment).

## Iteration stopping criteria

- **Convergence (stop)**: 2 consecutive rounds satisfying **all** of the following:
  - New unclear points: 0
  - Accuracy improvement vs previous: +3 points or less (saturation such as 5% → 8%)
  - Step count variation vs previous: within ±10%
  - Duration variation vs previous: within ±15%
  - **Overfitting check**: at convergence judgment, add 1 hold-out scenario not used so far and evaluate. If accuracy drops 15 points or more from the recent average, overfitting. Go back to baseline scenario design and add edges.
- **Divergence (suspect the design)**: if new unclear points do not decrease across 3+ iterations → the design direction of the prompt itself may be wrong. Stop fixing by patches and rewrite the structure
- **Resource cutoff**: stop when importance and improvement cost no longer balance (the "ship at 80 points" call)

## Failure pattern ledger

Maintain a cumulative list of failure modes across iterations. Without it, each iteration re-discovers the same class of mistake, and accuracy improvements stall without the operator noticing that the same `General Fix Rule` keeps surfacing under different surface wording.

Entry format:

```
- **Pattern name**: short descriptive handle (not "ambiguous X"; prefer "over-eager template application when skip clause is absent")
  - Example: <representative Issue wording from some iter>
  - General Fix Rule: <the class-level rule from that iter's structured reflection>
  - Seen in: iter N, iter M, ...
```

Rules:
- Before generating a fix in Workflow step 5, scan the ledger. If the current `General Fix Rule` matches an existing entry, update `Seen in` and investigate why the existing fix did not prevent recurrence (wording ambiguity? position too late in the prompt? missing example?) before creating a new entry.
- A pattern that recurs 3+ times despite targeted fixes is a structural signal — escalate to the "Divergence" criterion above rather than continuing to patch.
- The ledger is per-target-prompt, not global across all empirical-prompt-tuning runs.

## Variant exploration (optional, plateau-breaking)

When iterations approach a plateau but convergence criteria (2 consecutive clears) are not met, suspect local optimum and run a 2-variant round:

- **Conservative variant**: current prompt + next-best minor fix
- **Exploratory variant**: current prompt with one structural change — reorder sections, split a dense paragraph, drop a redundant section, or add a missing scaffolding (e.g., a worked example)

Dispatch fresh subagents on the same scenarios in parallel (one message with multiple Agent tool calls). Keep the variant with higher accuracy; on tie, prefer fewer unclear points; on further tie, prefer lower `tool_uses`.

Pairwise-comparison caveats:
- Do **not** ask a subagent to rate "A vs B" directly. LLM position bias and self-preference bias make such judgments noisy at small n.
- Compare on the objective axes only (accuracy, step count, unclear-points count, phase-weakness counts). Those are reproducible; "which prompt felt better" is not.
- If qualitative comparison is genuinely needed, counterbalance: run both orderings (A,B) and (B,A) and accept a verdict only if both orderings agree.

Cost: variant exploration doubles dispatch count per iteration. Use when plateau is suspected, not by default.

## Presentation format

Record and present to the user with the following form at each iteration:

```
## Iteration N

### Changes (diff from previous)
- <one-line fix content>
- Pattern applied: <pattern name from ledger, or "(new)">

### Execution results (per scenario)
| Scenario | Success/Failure | Accuracy | steps | duration | retries | Weak phase |
|---|---|---|---|---|---|---|
| A | ○ | 90% | 4 | 20s | 0 | — |
| B | × | 60% | 9 | 41s | 2 | Execution |

### Structured reflection (newly surfaced this time)
- <Scenario B>: [critical] item N is × — <one-line reason for drop>
  - Issue: <what observably happened>
  - Cause: <why, at the instruction level>
  - General Fix Rule: <class-level abstraction>
- <Scenario A>: (nothing new)

### Discretionary fill-ins (newly surfaced this time)
- <Scenario B>: <fill-in content>

### Ledger updates
- Added: <pattern name> (from Scenario B)
- Re-seen: <pattern name> (originally iter K) — existing fix did not prevent recurrence because <reason>

### Next fix proposal
- <one-line minimum fix>

(Convergence check: X consecutive clears / Y rounds remaining to stop condition)
```

## Red flags (beware of rationalization)

| Rationalization that surfaces | Reality |
|---|---|
| "Rereading it myself has the same effect" | You cannot view text you just wrote "objectively". Always dispatch a new subagent. |
| "One scenario is enough" | One scenario overfits. Minimum 2, ideally 3. |
| "Zero unclear points once, so we're done" | Could be coincidence. Finalize with 2 consecutive rounds. |
| "Let's knock out multiple unclear points at once" | You lose track of what worked. One theme per iteration. |
| "Split each related micro-fix strictly into its own iter" | Trap in the opposite direction. "One theme" is a semantic unit. 2-3 related micro-fixes can be bundled into 1 iter. Splitting too far explodes the iter count. |
| "Metrics are good, so ignore qualitative feedback" | Time reduction can also be a sign of being too thin. Keep qualitative primary. |
| "Rewriting from scratch is faster" | Correct if unclear points do not decrease across 3+ iterations. Before that stage, it is escape. |
| "Let's reuse the same subagent" | It has learned the previous improvements. Always dispatch a new one. |

## Common failures

- **Scenario too easy / too hard**: neither produces signal. One at the median of real use, one edge
- **Only looking at metrics**: chasing only time reduction strips important explanations and makes it fragile
- **Too many changes per iteration**: you can no longer trace "which fix back then worked". One fix per iteration
- **Tuning scenarios to match the fix**: making the scenario side easier just to make unclear points look eliminated → putting the cart before the horse

## Related

- `superpowers:writing-skills` — the TDD approach for skill creation. Essentially the same as this skill's "baseline → fix → rerun with a subagent"
- `retrospective-codify` — fixating learnings after a task. This skill is during prompt development, retrospective-codify is after a task ends; use them differently
- `superpowers:dispatching-parallel-agents` — conventions for running multiple scenarios in parallel
- `waxa-eval` — operating manual for the `waxa` CLI, which automates the eval / iterate loop into an external process with a YAML scenario format and persistent ledger. This skill (empirical-prompt-tuning) covers the **methodology and the in-session Task-tool subagent flow**; `waxa-eval` covers the **CLI operation and YAML authoring**. They are complementary — use empirical for the Iter 0 static check, the `[critical]`-tagged checklist, and `tool_uses`-based skill diagnosis (none of which are accessible to a CLI process); use waxa-eval when persistence, CI repeatability, or external adoption gates are needed.
