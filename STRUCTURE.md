# Structure of iraq-law

Folder names are in Arabic, the language people search Iraqi federal law in, and in Kurdish (Sorani) for the law of
the Kurdistan Region. Years and numbers use Western digits. No folder holds more than 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `الدستور/` | The Constitution of 2005 | one article (`art-001.md`) |
| `الوقائع-العراقية/<السنة>/<العدد>/` | Issues of al-Waqa'i al-Iraqiya, split into the instruments they publish | one instrument (`<NN>-<النوع>-<الرقم>.md`, NN = its order in the issue) |
| `التشريعات/<السنة>/` | Federal and local laws, regulations, instructions, orders and decisions from free public secondary sources (first: the Iraqi Local Governance Law Library, iraq-lg-law.org, via Internet Archive copies); every commit says `Source-copy-status: secondary copy; verification against the official text pending` | one text (`<النوع>-<الرقم>-<الاسم>.md`) |
| `القوانين-الاتحادية/<السنة>/` | Federal laws in force in the Kurdistan Region, as the Kurdistan Parliament's legislation base gives them | one law (`<الرقم>-<الاسم>.md`) |
| `هەرێمی-کوردستان/یاساکان/<ساڵ>/` | Laws of the Kurdistan Parliament | one law (`<ژمارە>.md`) |
| `هەرێمی-کوردستان/بڕیارە-یاساکان/<ساڵ>/` | Law-decisions | one decision |
| `هەرێمی-کوردستان/ڕێنماییەکان/<ساڵ>/` | Instructions | one instruction |
| `هەرێمی-کوردستان/پەیڕەوەکان/<ساڵ>/` | Regulations | one regulation |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per instrument or version, in the order they took effect.
- The author date is 12:00 Baghdad time on the in-force day the instrument's own clause gives (its publication in
  al-Waqa'i al-Iraqiya or Waqai'i Kurdistan, its issue day, or a stated day). Before 1970 the date is 1970-01-01 and
  the real day starts the subject.
- Trailers on every commit: `Kind:`, `In-force:`, `In-force-basis:` and `Source:`.
- An instrument whose in-force day cannot be read is held, not committed.

## Sources

- Secondary copies (`التشريعات/`): the Iraqi Local Governance Law Library (iraq-lg-law.org, now offline; read from Internet Archive copies); an instrument already in the repo from al-Waqa'i or legislation.krd is not taken again.

- al-Waqa'i al-Iraqiya issue PDFs published by the Ministry of Justice (moj.gov.iq), 2012 onwards.
- The Kurdistan Parliament's legislation base (legislation.krd): Kurdistan laws, law-decisions, instructions,
  regulations, and the federal laws in force in the Region.

`constitution/` was renamed `الدستور/` on 2026-11-26 (a rename only; no text changed).
