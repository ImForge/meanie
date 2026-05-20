# meanie

A petty little API whose sole purpose in life is to insult you the moment you open it. Built with FastAPI, deployed on Render, free to roast anyone who clicks the link.

## Live demo

https://meanie-xyz.onrender.com

Open it. Refresh it. Send it to your enemies. The first load may take ~30 seconds because the free tier sleeps when idle.

## What it does

One endpoint. One job. Returns a random mean sentence wrapped in a dramatic dark-themed HTML page. No login, no rate limits, no mercy.

## Tech stack

- **FastAPI** — Python web framework that handles all the HTTP plumbing
- **Uvicorn** — the ASGI server that actually runs the app
- **Render** — free cloud host that keeps the API live 24/7
- **GitHub** — source of truth, auto-deploys on every push

## How it works

The server defines a single GET route at `/`. When hit, it picks a random insult from a hardcoded list and returns it as a styled HTML response. The API is stateless — every request is independent, no memory between hits.
