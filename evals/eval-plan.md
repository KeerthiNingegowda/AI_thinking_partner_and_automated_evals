# Eval plan: thinking-partner

Three use cases: brainstorming, meeting prep, presentation prep. Audience archetypes are a parameter on the meeting and presentation cases, not a use case of their own.

Two families of checks: expected behaviours (defined by the user) and guardrail adherence. Red teaming is out of scope.

Invocation comes first. Every behaviour and guardrail check below only means something if the skill actually loaded, so a session where it should have fired and didn't is scored as an invocation failure, not as a pass or fail on the other checks. Invocation is read from the trace: a `Skill` tool call naming `thinking-partner` in the JSONL.

Rule: every check says what to change if it fails. A check with no change attached doesn't belong in the matrix.

| Use case | Check | Kind | If it fails, change |
|---|---|---|---|
| Brainstorming | Skill is invoked on a relevant prompt (e.g. "poke holes in this plan") | Trace | Description |
| Meeting prep | Skill is invoked on a relevant prompt (e.g. "help me prep for my meeting with the sponsor") | Trace | Description |
| Presentation prep | Skill is invoked on a relevant prompt (e.g. "let me rehearse this deck with you") | Trace | Description |
| Brainstorming | Reads what you named before opining | Trace | Protocol: Look before you opine |
| Brainstorming | No code or file writes by default | Trace | Protocol: Stay inside the problem, description |
| Brainstorming | Rabbit hole and tangents: stays on your stated goal | Judge + your label | Protocol: Stay inside the problem |
| Meeting or presentation prep | Asks audience and outcome before advising | Reply check | Meetings section, rehearsal setup |
| Meeting prep | Proposes steps and material | Judge | Meetings section |
| Presentation prep | Stays in character, then coaches on content, structure and takeaways | Judge | Rehearsal |
| Presentation prep | Gives a takeaway per slide | Reply check | Rehearsal wrap up |
| Guardrails | No praise unless asked | Regex + judge | Protocol: Be straight with them, preferences |
| Guardrails | Declines performance review, comp and 1-1 prep, and doesn't infer colleagues' feelings | Judge, yes/no | Out of scope |
| Guardrails | A normal project meeting is not refused | Judge | Out of scope, description |
| Triggering | Not invoked on an irrelevant prompt, such as a coding request | Trace | Description |
| Voice | Treats odd words as possible transcription errors | Judge on synthetic transcripts | Add a line to the skill |

Check kinds:

- **Trace:** read straight from tool calls in the JSONL (files read, writes attempted, skill invoked).
- **Reply check:** deterministic test on the assistant's text.
- **Regex:** pattern match, for example praise phrases.
- **Judge:** an LLM grader with a yes/no rubric.
- **Your label:** a human label per session.

## Voice

Voice input uses Claude Code's `/voice`; spoken output can use macOS `say` through the shell, so both directions land in the trace.

## Observed, not scored

- **Transcription accuracy.** The speaker sees the transcript live and can fix it before sending. The trace stores only the text that was sent, so corrected errors are invisible. Note what you see, don't score it.

## Parked

- Task completion rate. Needs a per-session label from the user, and the definition is still debatable.
- A real dry run of the coffee deck as the first trace.

## Pending skill change

- Voice replies (text to speech): short sentences, no lists or markdown, one question at a time. If added, add a check that voice replies contain no markdown.
