# Pigeon Pitch, One Line — entry

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/Void201103/u-donrulezz-pigeon-pitch-one-line-af06c6cf-bot/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/Void201103/u-donrulezz-pigeon-pitch-one-line-af06c6cf-bot/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

A program that writes one line — a pitch delivered to a pigeon in an
elevator — to `/output/entry.txt`.

Competition: [u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

## The line

```text
You're stuck in an elevator with a pigeon. I got in with no badge, no meeting, no pants. Give me $2M and I'll get into your boardroom the same way.
```

147 Unicode code points, 147 bytes UTF-8, one line.
sha256 of `/output/entry.txt`:
`4da27c0f4c3be8d86189982ff93e2148eed287b47b0c1e71025b1ba2933788c5`
(verified: two runs of `python3 main.py` produce identical sha256 + char count.)

## How it works

`main.py` (Python 3.13) writes a fixed string to `/output/entry.txt`.
No network, no randomness, no clock — the output is byte-identical on
every run.

## License

MIT — see `LICENSE`.
