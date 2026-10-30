# How this repository was made (Iraq)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| College of Law, Al-Muthanna University: Constitution of the Republic of Iraq 2005 | <https://law.mu.edu.iq/%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D8%AC%D9%85%D9%87%D9%88%D8%B1%D9%8A%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A7%D9%82-%D9%84%D8%B3%D9%86%D8%A9-2005/> | 2026-10-30 | Official legislative text; Iraq Copyright Law no. 3 of 1971, Article 6(3). The page states no reuse terms. |
| WIPO Lex: Constitution of Iraq (scan of Al-Waqa'i' Al-Iraqiya no. 4012, 28 December 2005) | <https://www.wipo.int/wipolex/ar/legislation/details/10027> | 2026-10-30 | Scan of the Official Gazette; used only to check the text |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | دستور جمهورية العراق لعام 2005 | 1 | 2005-12-28 to 2005-12-28 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 2 tags.

## Dates

Each commit is dated at noon (Asia/Baghdad) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Constitution of 2005 was approved by referendum on 15 October 2005 and published in Al-Waqa'i' Al-Iraqiya no. 4012 on 28 December 2005. Article 144 makes it effective after the referendum, its publication in the Official Gazette and the seating of the government formed under it; the version is dated by its publication. https://www.wipo.int/wipolex/ar/legislation/details/10027

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `2704ec668721d254b10105fb8d50824ca418b21cc5842c84bab78c22054f0c50` (117458 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Arabic is built: it is the official text. The English translation hosted by WIPO and the UN is not used.
- The Iraqi official sites (Council of Representatives, Higher Judicial Council, the laws database) could not be read without passing a bot check, so they were not used. The text comes from a university law faculty page that copies the Official Gazette.
- Iraq Copyright Law no. 3 of 1971, Article 6(3), excludes collections of official documents such as the texts of laws, regulations and judicial decisions from protection; that is why the copy may be published.
- The copy was compared with two other sources: a retyped copy on Arabic Wikisource, and the Gazette scan (WIPO Lex PDF) read with OCR (tesseract, Arabic). The two copies agree on 115 of 144 articles after ignoring vowel marks and hamza forms. On the 29 that differ, the Muthanna text matched the scan better in 24 and the Wikisource text in 5 (each a one-letter difference). Articles 35, 49, 65 and 122 were read against the OCR of the scan: the Muthanna wording follows the Gazette there, and the Wikisource retyping adds or changes words (for example it adds a second "regulated by law" to Article 49 and "authentic" becomes "real" in Article 35).
- The OCR is a check only: no OCR text is published.
- The text carries vowel marks that the Gazette prints in part only; they are kept as the host prints them. Part, chapter and section headings are not kept as files; each article keeps its number.
- Only the Gazette text of 28 December 2005 is in this record. Amendments and the corrections later published in the Gazette are not applied.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parser and chose the sources; it did not write or alter any legal text. OCR (tesseract) was used only to compare candidate copies with the Gazette scan.
