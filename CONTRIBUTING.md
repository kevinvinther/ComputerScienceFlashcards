# Contributing

Before adding a new card, be sure to read the [20 Rules of Formatted Knowledge](http://super-memory.com/articles/20rules.htm).

## Adding a new card
To add a new card, simply add a new line in the file corresponding to the card type, filling out the required information except the GUID.

`brainbrew run recipes/source_to_anki.yaml` to compile the crowdanki json file.

## Tags

All cards must have relevant tags, and all tags must begin with CS::. There are two required tags on each card: CS::Course and CS::`CC`Chapter, with the first two C's meaning Course Code.

The chapter must be the chapter relevant chapter for the flashcard. If a chapter is uninmportant, mark it as CS::CCMisc, where CC, again, is course code. 

These are the current course names in tags:

* CS::software-engineering
* CS::formal-languages
* CS::algorithms-and-probability

The course codes are:

* DM571, Software Engineering
* DM565, Formal Languages 
* DM551, Algorithms and Probability

