Design
======

=======================================================
v1a Analyzer as public interface and analyses as classes
=======================================================

----------------
Responsibilities
----------------

Things to consider:
- Whether functions for results should be part of Analyzer or in an independent module


.. mermaid:: 
    classDiagram

    class Analyzer{
        public interface
        create words
        manage results   
    }

    class Word{
        validate text
        determine which characteristics are available
        store characteristics
        provide characteristics
        provide pretty names for properties
        export characteristics
    }

    class cli{
        %% module
        cli read words' texts from files
        cli all analyses
        cli run individual analyses (future)
        cli save results
    }

    class results{
        %% module
        format results
        save results
    }

    class Length{
        analyze length
        store length
        export characteristics
    }

    class SilentLetters{
        analyze silent letters
        store info about silent letters
        export characteristics
    }

    class GraphemeSharedphonemes{
        analyze same sound graphemes 
        store info about same sound graphemes
        export characteristics
    }

    class TotalDifficulty{
        analyze total difficulty
        store total difficulty
        export characteristics
    }

    class CustomDoctringProcessor{
        format docstrings 
    }

----------------
Class properties
----------------

.. mermaid:: 
    classDiagram

    class Analyzer{
        words: list[Word]

        create_word_objs(word_texts: str)
        run_analysis(func: Callable)
        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()
        save_results(filename: Path)

        %% property
        pd.DataFrame results()
    }

    class cli{
        %% module
        list[Word] extract_word_properties(words: list[Word])
        Iterable[str] get_words_from_file(filename: Path)
        run_all_analyses(analyzer: Analyzer)
    }

    class results{
        %% module
        list[dict] extract_info_from_words(words: list[Word])
        pd.DataFrame clean_cols_names(results: pd.DataFrame)
        pd.DataFrame format_results(words: list[Word], names_to_labels: dict) 
        save_results(filename: Path, words: list[Word])
    }
    
    class Word{
        text: str
        length: Optional[Length] = None
        sillent_letters: Optional[SilentLetter] = None
        graphemes_shared_phoneme: Optional[SharedPhoneme] = None
        total_difficulty: Optional[TotalDifficulty] = None
        map_characteristic_names_to_labels: dict[str, str]

        %% validators
        bool word_length_is_invalid()
        bool word_contains_invalid_character()
        str normalize_text()
        raises validate_word()

        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()

        list[str] determine_characteristics_available()
        dict export_info()
    }

    class Length{
        int letter_length

        analyze_letter_length(text: str)
        dict export_info()
    }

    class SilentLetter{
        int silent_u
        int silent_h
        int silent_letters_total

        analyze_silent_u(text: str)
        analyze_silent_h(text: str)
        analyze_silent_letters_total(text: str)
        dict export_info()
    }

    class SharedPhoneme{
        int shared_phoneme_s
        int shared_phoneme_b
        int shared_phoneme_y
        int shared_phoneme_j
        int shared_phoneme_k
        int shared_phonemes_total
        
        analyze_shared_phoneme_s(text: str)
        analyze_shared_phoneme_b(text: str)
        analyze_shared_phoneme_y(text: str)
        analyze_shared_phoneme_j(text: str)
        analyze_shared_phoneme_k(text: str)
        analyze_shared_phonemes_total(text: str)
        dict export_info()
    }
    
    class TotalDifficulty{
        int total_difficulty

        analyze_total_difficulty(word: Word)
        dict export_info()
    }

    class CustomDoctringProcessor{
        param_like_sections
    }

===================================================================================
v1b wdiff as public interface, analyzer to manage analyses, and analyses as classes
===================================================================================

----------------
Responsibilities
----------------

Things to consider:
- Whether functions for results should be part of Analyzer or in an independent module


.. mermaid:: 
    classDiagram

    class wdiff{
        store analyzer
        public interface
    }

    class Analyzer{
        create words
        manage results   
        runs analyses
    }

    class Word{
        validate text
        determine which characteristics are available
        store characteristics
        provide characteristics
        provide pretty names for properties
        export characteristics
    }

    class cli{
        %% module
        cli read words' texts from files
        cli all analyses
        cli run individual analyses (future)
        cli save results
    }

    class results{
        %% module
        format results
        save results
    }

    class Length{
        analyze length
        store length
        export characteristics
    }

    class SilentLetters{
        analyze silent letters
        store info about silent letters
        export characteristics
    }

    class GraphemeSharedphonemes{
        analyze same sound graphemes 
        store info about same sound graphemes
        export characteristics
    }

    class TotalDifficulty{
        analyze total difficulty
        store total difficulty
        export characteristics
    }

    class CustomDoctringProcessor{
        format docstrings 
    }

----------------
Class properties
----------------

.. mermaid:: 
    classDiagram

    class WDiff{
        analyzer: Analyzer

        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()
        save_results(filename: Path)

        %% property
        pd.DataFrame results()
    }

    class Analyzer{
        words: list[Word]

        %% base
        create_word_objs(word_texts: str)
        run_analysis(func: Callable)

        %% results
        list[dict] extract_info_from_words(words: list[Word])
        pd.DataFrame clean_cols_names(results: pd.DataFrame)
        pd.DataFrame format_results(words: list[Word], names_to_labels: dict) 
        save_results(filename: Path, words: list[Word])

        %% property
        pd.DataFrame results()
    }

    class cli{
        %% module
        list[Word] extract_word_properties(words: list[Word])
        Iterable[str] get_words_from_file(filename: Path)
        run_all_analyses(analyzer: Analyzer)
    }

    class Word{
        %% characteristics
        text: str
        length: Optional[Length] = None
        sillent_letters: Optional[SilentLetter] = None
        graphemes_shared_phoneme: Optional[SharedPhoneme] = None
        total_difficulty: Optional[TotalDifficulty] = None

        map_characteristic_names_to_labels: dict[str, str]

        %% validators
        str normalize_text()
        raises validate_word()
        bool word_length_is_invalid()
        bool word_contains_invalid_character()

        %% analyses
        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()

        %% exporting
        dict[str, int] dict export_info()
        list[str] determine_characteristics_available()
        list[dict] get_info_from_characteristics(available_characteristics: list[str])
        dict[str, int] merge_info_from_characteristics(characteristics: list[dict])
    }

    class Length{
        int letter_length

        analyze_letter_length(text: str)
        dict[str, int] export_info()
    }

    class SilentLetter{
        int silent_u
        int silent_h
        int silent_letters_total

        analyze_silent_u(text: str)
        analyze_silent_h(text: str)
        analyze_silent_letters_total(text: str)
        dict[str, int] export_info()
    }

    class SharedPhoneme{
        int shared_phoneme_s
        int shared_phoneme_b
        int shared_phoneme_y
        int shared_phoneme_j
        int shared_phoneme_k
        int shared_phonemes_total
        
        analyze_shared_phoneme_s(text: str)
        analyze_shared_phoneme_b(text: str)
        analyze_shared_phoneme_y(text: str)
        analyze_shared_phoneme_j(text: str)
        analyze_shared_phoneme_k(text: str)
        analyze_shared_phonemes_total(text: str)
        dict export_info()
    }
    
    class TotalDifficulty{
        +int total_difficulty

        +analyze_total_difficulty(word: Word)
        dict export_info()
    }

    class CustomDoctringProcessor{
        -param_like_sections
    }

    class Exporter{
        -words: list[Word]
        -available_characteristics: list[str]

        +list[dict] extract_info_words()
        -dict[str, int] dict export_info_word()
        -list[dict] get_info_from_characts()
        -dict[str, int] merge_info_from_characts(characteristics: list[dict])
    }


====================================================================================
v2 wdiff as public interface, analyzer to manage analyses, and analyses as functions
====================================================================================

----------------
Responsibilities
----------------

.. mermaid:: 
    classDiagram

    class wdiff{
        store analyzer
        public interface
    }

    class Analyzer{
        create words
        manage results   
        runs analyses
    }

    class Word{
        validate text
        determine which characteristics are available
        store characteristics
        provide characteristics
        provide pretty names for properties
        export characteristics
    }

    class cli{
        %% module
        cli read words' texts from files
        cli all analyses
        cli run individual analyses (future)
        cli save results
    }

    class results{
        %% module
        format results
        save results
    }

    class length{
        analyze length
        store length
        export characteristics
    }

    class silent{
        %% module
        analyze silent letters
    }

    class sharedphonemes{
        %% module
        analyze same sound graphemes 
    }

    class totaldifficulty{
        %% module
        analyze total difficulty
    }

    class CustomDoctringProcessor{
        format docstrings 
    }

----------------
Class properties
----------------

.. mermaid:: 
    classDiagram

    class WDiff{
        analyzer: Analyzer

        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()
        save_results(filename: Path)

        %% property
        pd.DataFrame results()
    }

    class Analyzer{
        words: list[Word]

        %% base
        create_word_objs(word_texts: str)
        run_analysis(func: Callable)

        %% results
        list[dict] extract_info_from_words(words: list[Word])
        pd.DataFrame clean_cols_names(results: pd.DataFrame)
        pd.DataFrame format_results(words: list[Word], names_to_labels: dict) 
        save_results(filename: Path, words: list[Word])

        %% property
        pd.DataFrame results()
    }

    class cli{
        %% module
        list[Word] extract_word_properties(words: list[Word])
        Iterable[str] get_words_from_file(filename: Path)
        run_all_analyses(analyzer: Analyzer)
    }

    class Word{
        text: str
        %% length
        letter_length Optional[int] = None

        %% silent
        silent_u: Optional[int] = None
        silent_h: Optional[int] = None
        silent_letters_total: Optional[int] = None

        %% shared phonemes
        shared_phoneme_s: Optional[int] = None
        shared_phoneme_b: Optional[int] = None
        shared_phoneme_y: Optional[int] = None
        shared_phoneme_j: Optional[int] = None
        shared_phoneme_k: Optional[int] = None
        shared_phonemes_total: Optional[int] = None

        %% total
        total_difficulty: Optional[int] = None

        map_characteristic_names_to_labels: dict[str, str]

        %% validators
        bool word_length_is_invalid()
        bool word_contains_invalid_character()
        str normalize_text()
        raises validate_word()

        analyze_letter_length()
        analyze_silent_letters_total()
        analyze_shared_phoneme_total()
        analyze_total_difficulty()

        list[str] determine_characteristics_available()
        dict export_info()
    }

    class length{
        %% module
        int analyze_letter_length(text: str)
    }

    class silent{
        %% module
        int analyze_silent_u(text: str)
        int analyze_silent_h(text: str)
        int analyze_silent_letters_total(silent_u: int, silent_h: int)
    }

    class sharedphonemes{
        %% module
        int analyze_shared_phoneme_s(text: str)
        int analyze_shared_phoneme_b(text: str)
        int analyze_shared_phoneme_y(text: str)
        int analyze_shared_phoneme_j(text: str)
        int analyze_shared_phoneme_k(text: str)
        int analyze_shared_phonemes_total(shared_phoneme_s: int, grapheme_shared_phoneme_b: int, grapheme_shared_phoneme_y: int, grapheme_shared_phoneme_j: int, grapheme_shared_phoneme_k: int, grapheme_shared_phonemes_total: int)
    }
    
    class totaldifficulty{
        %% module
        int analyze_total_difficulty(letter_length: int, silent_letters_total: int, shared_phonemes_total: int)
    }

    class CustomDoctringProcessor{
        param_like_sections
    }

====================================================================
v3a wdiff as public interface, analyzer to manage analyses, exporter  
====================================================================

----------------
Responsibilities
----------------

.. mermaid:: 
    classDiagram

    class wdiff{
        store analyzer
        public interface
    }

    class Analyzer{
        create words
        manage results   
        runs analyses
    }

    class Word{
        validate text
        determine which characteristics are available
        store characteristics
        provide characteristics
        provide pretty names for properties
        export characteristics
    }

    class cli{
        %% module
        cli read words' texts from files
        cli all analyses
        cli run individual analyses (future)
        cli save results
    }

    class results{
        %% module
        format results
        save results
    }

    class Exporter{
        export info from words
        export info from word
        export info from characteristics
        provide info from words
    }

    class Length{
        analyze length
        store length
        export characteristics
    }

    class SilentLetters{
        analyze silent letters
        store info about silent letters
        export characteristics
    }

    class GraphemeSharedphonemes{
        analyze same sound graphemes 
        store info about same sound graphemes
        export characteristics
    }

    class TotalDifficulty{
        analyze total difficulty
        store total difficulty
        export characteristics
    }

    class CustomDoctringProcessor{
        format docstrings 
    }

----------------
Class properties
----------------

.. mermaid:: 
    classDiagram

        class WDiff{
            -Analyzer analyzer

            +analyze_letter_length()
            +analyze_silent_letters_total()
            +analyze_shared_phoneme_total()
            +analyze_total_difficulty()
            +save_results(filename: Path)

            %% property
            +pd.DataFrame results()
        }

        class Analyzer{
            -list[Word] words
            -Exporter exporter

            %% base
            -create_word_objs(str word_texts)
            +run_analysis(Callable func)

            %% results
            -list[dict] extract_info_from_words(list[Word] words)
            -pd.DataFrame clean_cols_names(pd.DataFrame results)
            -pd.DataFrame format_results(list[Word] words, dict names_to_labels)  
            +save_results(Path filename, list[Word] words)

            %% property
            +pd.DataFrame results()
        }

        class cli{
            %% module
            list[Word] extract_word_properties(list[Word] words)
            Iterable[str] get_words_from_file(Path filename)
            run_all_analyses(Analyzer analyzer)
        }

        class Word{
            %% characteristics
            #str text
            #Optional[Length] length
            #Optional[SilentLetter] sillent_letters
            #Optional[SharedPhoneme] graphemes_shared_phoneme
            #Optional[TotalDifficulty] total_difficulty

            #dict[str, str] map_characteristic_names_to_labels

            %% validators
            -str normalize_text()
            -raises validate_word()
            -bool word_length_is_invalid()
            -bool word_contains_invalid_character()

            %% analyses
            +analyze_letter_length()
            +analyze_silent_letters_total()
            +analyze_shared_phoneme_total()
            +analyze_total_difficulty()
        }

        class Length{
            #int letter_length

            +analyze_letter_length(str text)
        }

        class SilentLetter{
            #int silent_u
            #int silent_h
            #int silent_letters_total

            +analyze_silent_u(str text)
            +analyze_silent_h(str text)
            +analyze_silent_letters_total(str text)
        }

        class SharedPhoneme{
            #int shared_phoneme_s
            #int shared_phoneme_b
            #int shared_phoneme_y
            #int shared_phoneme_j
            #int shared_phoneme_k
            #int shared_phonemes_total
            
            +analyze_shared_phoneme_s(str text)
            +analyze_shared_phoneme_b(str text)
            +analyze_shared_phoneme_y(str text)
            +analyze_shared_phoneme_j(str text)
            +analyze_shared_phoneme_k(str text)
            +analyze_shared_phonemes_total(str text)
        }
        
        class TotalDifficulty{
            #int total_difficulty

            +analyze_total_difficulty(Word word)
        }

        class CustomDoctringProcessor{
            -param_like_sections
        }

        class Exporter{
            -list[Word] words
            -list[str] available_characteristics

            +list[dict] extract_info_words()
            -dict[str, int] dict export_info_word()
            -list[dict] get_info_from_characts()
            -dict[str, int] merge_info_from_characts(list[dict] characteristics)
        }

        WDiff *-- Analyzer
        Analyzer *-- Word
        Analyzer *-- Exporter
        Exporter *-- Word
        Word *-- Length
        Word *-- SilentLetter
        Word *-- SharedPhoneme
        Word *-- TotalDifficulty
