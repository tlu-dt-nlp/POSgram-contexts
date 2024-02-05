# POS-gram Context Finder

The tool can be applied to analyse the usage contexts of part-of-speech (POS) n-grams, or POS-grams, in Estonian language. It converts each sentence of a text to a POS string and finds different POS-grams of a given length, then detects the probabilities of their preceding and/or subsequent contexts. A context is defined as a certain POS or the beginning/end of a sentence.

Usage examples can be found in the Python script `example.py` and the Colab file `context_finder_demo_et.ipynb` (in Estonian).

The [Stanza NLP package](https://stanfordnlp.github.io/stanza/) is employed for POS tagging. Language-specific ('XPOS') tags are used to group words into POS n-grams, or POS-grams. Custom tags denote sentence onset and ending, which are not considered a part of POS-grams but count as a possible pre- and postcontext, respectively. The tagset is explained in the following table.
| Tag | Meaning |
|:--------------:|:-------------:|
| ^ | Sentence onset |
| A | Adjective |
| D | Adverb |
| G | Genitive attribute |
| I | Interjection |
| J | Conjunction |
| K | Adposition |
| N | Numeral |
| P | Pronoun |
| S | Substantive/Noun |
| V | Verb |
| X | Auxiliary adverb |
| Y | Abbreviation |
| $ | Sentence ending |


By default, the application searches for contexts of POS trigrams, i.e., three-word sequences. This can be changed using the `nlength` argument. For example, setting the argument value to 2 instead of 3 would allow to determine the usage contexts of POS bigrams.
```
PosgramContexts("Juku tuli kooli. Juku tuli kooli ruttu. Unine Juku tuli kooli.", nlength=2)
```

In the current version, punctuation is skipped when analysing word sequences. It means that words in a POS-gram or their context may not be adjacent. For example, 'SZSZS' is considered an instance of the trigram 'SSS', i.e., three consecutive nouns.

If applied on a large general corpus, the tool can be used to build a statistical language model. A related tool, the [POS-gram Error Finder](https://github.com/tlu-dt-nlp/POSgram-errors), utilizes such a model to detect unlikely POS sequences. The model is based on the Estonian Reference Corpus. In this repository, you can find a smaller corpus for testing the POS-gram Context Finder. It is the L1 reference subcorpus of the [Estonian Interlanguage Corpus](https://elle.tlu.ee/tools), including opinion articles published in 2014 on the websites of the two biggest Estonian daily newspapers Postimees and Õhtuleht (with a volume of 107,179 words).
