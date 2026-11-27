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
| `الأحكام/<المحكمة>/<السنة>/<الشهر>/<اليوم>/` | Court decisions (محكمة-التمييز-الاتحادية, المحكمة-الاتحادية-العليا, محكمة-تمييز-إقليم-كوردستان, محكمة-استئناف-<المنطقة> sitting in cassation), one per decision, dated by the decision day | one decision (`قرار-<الرقم>.md`; the Federal Supreme Court's own English translations `قرار-<الرقم>-اتحادية-<السنة>.en.md`) |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per instrument or version, in the order they took effect.
- The author date is 12:00 Baghdad time on the in-force day the instrument's own clause gives (its publication in
  al-Waqa'i al-Iraqiya or Waqai'i Kurdistan, its issue day, or a stated day). Before 1970 the date is 1970-01-01 and
  the real day starts the subject.
- Trailers on every commit: `Kind:`, `In-force:`, `In-force-basis:` and `Source:`.
- An instrument whose in-force day cannot be read is held, not committed.

## Court decisions

- `الأحكام/` holds Iraqi court decisions, one file per decision, committed at 12:00 Baghdad time on the
  decision day the decision or its record gives.
- Sources so far are copies: the Higher Judicial Council's decision pages (hjc.iq) and the Federal Supreme
  Court's PDFs (iraqfsc.iq) as captured by the Internet Archive, and mohamah.net; every commit says
  `Source-copy-status: secondary copy; verification against the official text pending`.
- Personal-status, juvenile, sexual-offence, honour and family decisions are not published here.

## Sources

- Secondary copies (`التشريعات/`): the Iraqi Local Governance Law Library (iraq-lg-law.org, now offline; read from Internet Archive copies); an instrument already in the repo from al-Waqa'i or legislation.krd is not taken again.

- al-Waqa'i al-Iraqiya issue PDFs published by the Ministry of Justice (moj.gov.iq), 2012 onwards.
- The Kurdistan Parliament's legislation base (legislation.krd): Kurdistan laws, law-decisions, instructions,
  regulations, and the federal laws in force in the Region.

`constitution/` was renamed `الدستور/` on 2026-11-26 (a rename only; no text changed).
