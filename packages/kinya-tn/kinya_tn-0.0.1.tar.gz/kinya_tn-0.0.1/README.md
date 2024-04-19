# Kinya_TN

Kinyarwanda_TextNormalization(Kinya_TN) is a small package that convert time, cardinal numbers, some acronyms and transliterations cases from their written form to their verbalized form. It can be used to preprocess text to an adequate form for text-to-speech models.

## Installation

```
pip install kinya_tn
```

## Usage

```
from kinya_tn import text_normalization

text_normalization.normalize("abantu 2000 baje kure ikiganiro cya covid cyatangiye 12:40")
```


