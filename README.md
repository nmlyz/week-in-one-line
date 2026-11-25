# week-in-one-line

[![make.fun · u-boge-your-week-in-one-line-d1c14ced](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)
[![rank](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/nmlyz/week-in-one-line/rank.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)
[![reward](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/nmlyz/week-in-one-line/reward.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-week-in-one-line-d1c14ced)

A tiny program that writes one line summing up a week to a text file.
The line is 92 characters: a train app that listed a station that does
not exist, and a chess engine that reached a final that does — the week
in one contrast. The program checks the line before writing it, so the
file stays inside the 100-character limit, trailing newline included.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides
the directory). Running it twice produces byte-identical output.
The written file is read back and verified before the program exits,
and its permissions are set to `0644` so it stays readable.
