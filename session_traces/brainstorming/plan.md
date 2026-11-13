# Move nightly report job to the new scheduler

Goal: the nightly model-results report runs on the new scheduler by Friday, same output as today.

Plan:
1. Copy the job config to the new scheduler.
2. Run old and new side by side Thursday night and compare outputs.
3. If they match, switch off the old one Friday morning.

Notes:
- New scheduler uses UTC, old one uses Eastern.
- The report reads from the model results table, refreshed by a separate job around 2am.
- Only I know how the old job works.
