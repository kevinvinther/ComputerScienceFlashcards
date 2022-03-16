# Contributing
---

## Setup
Want to add new cards or fix an issue? First you have to install some dependencies. 

1. Fork and clone this repository to your machine
2. Install Python 3.7^
 - Make sure to install `pip`
3. Download and install [Brain Brew](https://github.com/ohare93/brain-brew/)

## Adding new cards from the CSV file
Add a new line in the correct CSV file. Ignore the GUID, it'll be added by brainbrew. Example:
```csv
O*8.f!-ud:,<p>What is the difference between deep binding and shallow binding?</p>,"<p>Deep binding binds the environment at the time a procedure is passed as an argument. Shallow binding binds the environment at the time a procedure is actually called. See more: <a href=""https://stackoverflow.com/questions/15550648/shallow-deep-binding-what-would-this-program-print"">https://stackoverflow.com/questions/15550648/shallow-deep-binding-what-would-this-program-print</a></p>","CS::programming-languages, CS::PLChapter7"
Af#xq$deBq,<p>What is an exception?</p>,"<p>An event which occurs during the execution of the program, that disrupts the normal flow of the programs instructions.</p>","CS::programming-languages, CS::PLChapter7"
,<p> This is a new card question </p>,"<p>This is a new card answer</p>","CS::These_are_tags"
```
However, the recommended way is to add them via anki.

## Adding new cards from Anki
To add new cards from anki, you'll have to add news cards as you would in a new anki deck. When you have done this, then export the deck as a CrowdAnki deck (File->Export->Export Format->CrowdAnki->Computer Science). 

When you have done this, make a new directory in your forked repository called `build` as well as another director in `build` called `Computer_Science`. Inside of `build/Computer_Science/` copy the contents from the CrowdAnki. 

After you have done this, go to the root folder of the forked repository and run the `anki_to_source.yaml` recipe: `brainbrew run recipes/anki_to_source.yaml`.

Then, make a merge request, and you're done!

## Tags
All cards must have relevant tags, and all tags must begin with `CS::`. There are two required tags on each card, `CS::Course` and `CS::CCChapter`, with the first two C's meaning Course Code. 

The chapter must be the chapter relevant chapter for the flashcard. If a chapter is uninmportant, mark it as `CS::CCMisc`. with CC meaning Course Code.

These are the current course names in tags: 
* `CS::programming-languages`
* `CS::operating-systems`

The course codes are: 
* PL, Programming Languages
* OS, Operating Systems
