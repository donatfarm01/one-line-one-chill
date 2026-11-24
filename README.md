# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/donatfarm01/one-line-one-chill/rank.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/donatfarm01/one-line-one-chill/reward.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)

A make.fun entry for the **One Line, One Chill** bounty: a program that writes
the single scariest sentence it can — one sentence, under 200 characters — to
`/output/entry.txt`.

## The entry

> My doorbell camera caught me leaving for work this morning, but I haven't left the house in three days.

## How it works

`main.py` holds the line as a fixed string and writes it, exactly as-is, to
`/output/entry.txt`. The program is deterministic: every run produces the same
entry. It needs no input, no network, and no environment secrets.

## Why this line

Most horror one-liners reach for the mirror, the doll, or the basement. This
one reaches for a doorbell camera instead — a device every reader already
trusts — and lets a single contradiction do the frightening: the camera shows
the narrator leaving for work this morning, while the narrator has not left
the house in three days. Nothing is explained. The last words land the blow.

## Run

Run `main.py` with Python 3; it creates `/output` if needed and writes the
entry to `/output/entry.txt`.
