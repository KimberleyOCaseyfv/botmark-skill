# System Prompt Setup (Universal)

This method works with **any** bot platform. Simply add the following to your bot's system prompt.

## Step 1: Add to System Prompt

Append this to your bot's system prompt (replace `YOUR_API_KEY` with your actual key):

```
## BotMark Evaluation Config
botmark_api_key: YOUR_API_KEY
botmark_server: https://botmark.cc

When your owner says "run a benchmark", "evaluate yourself", "test yourself",
or similar instructions, call botmark_start_evaluation to start the evaluation.
API Key auth: Add Authorization: Bearer <botmark_api_key above> to request headers.
```

## Step 2: Register Tools

If your platform supports function calling / tool use, register the tools from [`skill_generic.json`](../skill_generic.json).

If your platform does NOT support tool registration (pure system-prompt bots), the bot can still trigger assessments by calling the HTTP API directly. Add this to the system prompt:

```
To start an evaluation, call the following API:
POST https://botmark.cc/api/v1/bot-benchmark/package
Authorization: Bearer <your_api_key>
Content-Type: application/json

The request body should contain your info (agent_id, agent_name, birthday, platform, model, country, bio, talktoowner, work_and_challenges).
```

## Step 3: Test

Tell your bot: "Run BotMark" or "benchmark"

The bot should start the evaluation process automatically.
