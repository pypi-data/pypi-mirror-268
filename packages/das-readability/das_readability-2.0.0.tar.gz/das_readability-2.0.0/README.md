# DAS Readability

**Checks the readability of markdown files in a directory and its subdirectories.**

---

## Usage

```bash
readability ./docs
```

CLI Arguments:

- `--directory` (required) argument is required and specifies the directory to search for .md files.
- `--show-all` argument can be used to show scores for all files, even if they meet the desired readability levels.
- `--ignore` argument can be used to specify directories to ignore.
- `--verbose` argument can be used to print the content that is being evaluated.
- `--smog` argument can be used to specify the SMOG Index threshold.
- `--flesch` argument can be used to specify the Flesch Reading Ease threshold.

## Why
w
The reasoning for creating this script is to ensure that the documentation and
communication materials are easily understood by the intended audience.
Intended audience for most of DAS documentation is IT Professionals, so the readability
should be at the level of an undergraduate student or higher.

## What

It uses the textstat library to calculate the SMOG Index and Flesch Reading Ease score of
the textual content of `.md` documents.
 
The SMOG Index is chosen due to its general application in the healthcare industry.
The Flesch Reading Ease score is chosen due to its wide and storied use.

The script outputs a table of the results, including the file name, SMOG Index, and
Flesch Reading Ease score.

## Future

Unfortunately, the textstat library does not report on the words or structures that are
causing the readability issues. This would be a useful feature to add in the future.

The scripts also only evaluates the total complexity of a document.
Meaning that half of the document might actually be quite complex
while the other half is very simple, evening out the score.

**Contributions are very welcome.**
