# Iraq: law history in git

The Constitution of the Republic of Iraq of 2005 as a git repository: the preamble and Articles 1 to 144, one file each, one paragraph per line, so `git blame` and `git diff` work line by line.

**Language: Arabic**, the official text. The English translations of the Constitution are not used.

**What this repository is not, yet: a history.** It holds one version: the Constitution as published in the Official Gazette (Al-Waqa'i' Al-Iraqiya, no. 4012) on 28 December 2005, after the referendum of 15 October 2005. Later amendments and the corrections that the Gazette printed for a few articles are not applied. Iraq's statutes are not in this repository: the official Iraqi legal sites cannot be read by an ordinary program, so Iraq's laws, regulations and treaties are not covered.

**Where the text comes from.** It is a third-party copy: a page of the College of Law, Al-Muthanna University, that copies the Official Gazette text. It may be published because Iraq Copyright Law no. 3 of 1971, Article 6(3), excludes official documents such as the texts of laws from protection; the clause is quoted in [`LICENSE`](LICENSE). The copy was checked against a scan of the Gazette itself (hosted by WIPO Lex, read with OCR, which is used only as a check and is not published) and against a second retyped copy: where the copies differ, the host's wording follows the Gazette. The text carries vowel marks that the Gazette prints in part only. Part, chapter and section headings are not kept as files; each article keeps its number.

## What it holds

| Folder | Text | Versions |
| --- | --- | ---: |
| `constitution/` | Constitution of the Republic of Iraq 2005: preamble and Articles 1 to 144 | 1 |

## Dates

Each commit is dated at noon, Asia/Baghdad, on 28 December 2005, the day of publication in the Gazette (Article 144 makes the Constitution effective after the referendum, its publication and the seating of the government formed under it). The day is in the `In-force:` trailer.

## Source and licence

Source: College of Law, Al-Muthanna University, retrieved 2026-10-30. See [`LICENSE`](LICENSE).
