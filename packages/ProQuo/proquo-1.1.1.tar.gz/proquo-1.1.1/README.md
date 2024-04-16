# Readme
This repository contains two tools, `ProQuo` and `ProQuoLM`. Both are tools for the detection of short quotations
(<= 4 words) between two texts, a source text and a target text. The target text is the text quoting the source text.
Quotations in the target text need to be marked with quotations marks. For more information, see below.

The main purpose of this tool is to use the pretrained models for the detection of short quotations. While we found both
approaches (`ProQuo` and `ProQuoLM`) to perform at the same level (for details, see our [publication](https://jcls.io/article/id/3590/)),
`ProQuoLm` is easier to use, better maintained and the **recommended approach**.

## Quotation Marks
By default, the "best", that is, most common, combination of opening and closing quotation mark in the specific text is used.
The following combinations are automatically tried:

1. " and "
2. „ and “
3. „ and "
4. “ and “
5. » and «
6. « and »
7. ‘ and ’

If this is not the desired behaviour, quotations marks can be manually defined using the command line options
`--open-quote` and `--close-quote`.

## Approaches Overview
`ProQuo` is a specialized pipeline which uses a [model for reference classification](proquo/model/reference/ReferenceModelTrainer.py)
and a [model for relation extraction](proquo/model/relation/RelationModelBertTrainer.py) between quotations and (page)
references to distinguish between relevant quotations (that is, quotations from the source text) and quotations
from other sources. In a third step, a rule-based algorithm is used to link the identified quotations to their source.

`ProQuoLM` uses a [fine-tuned BERT model](https://huggingface.co/Fredr0id/proquolm) in two ways: to distinguish between
relevant quotations and quotations from other sources and to link the quotations to their source.

## Pretrained Models and Training Data
The pretrained models and training data are made available and can be downloaded from [here](https://scm.cms.hu-berlin.de/schluesselstellen/proquodata).
For `ProQuoLm`, we also provide a model on [Hugging Face](https://huggingface.co/Fredr0id/proquolm). This is used by default.

## Installation

### From PyPi
**Note**: Both tools are part of the same PyPi package. So the following command installs both.

~~~
pip install ProQuo
~~~

### From Source
Checkout this repository and then run:

~~~
python -m pip install .
~~~

### Dependencies
Both installation methods install all dependencies except `tensorflow` which needs to be installed manually depending on
the individual needs, see [Tensorflow installation](https://www.tensorflow.org/install). The latest version that was tested is 2.14.1.

For `RelationModelLstmTrainer`, `tensorflow-text` is needed. `RelationModelLstmTrainer` should normally not be needed as
`RelationModelBertTrainer` performs better and is the default in the pipeline.

## Usage
The following sections describe how to use ProQuo on the command line.

### Quotation detection
To run `ProQuoLM` with the default model, use the following command:

~~~
proquolm compare path_to_source_text path_to_target_text --text --output-type text
~~~

<details>
<summary>All ProQuoLM command line options</summary>

~~~
usage: proquolm compare [-h] [--tokenizer TOKENIZER] [--model MODEL]
                        [--lower-case | --no-lower-case]
                        [--output-folder-path OUTPUT_FOLDER_PATH]
                        [--create-dated-subfolder | --no-create-dated-subfolder]
                        [--text | --no-text] [--output-type {json,text,csv}]
                        [--csv-sep CSV_SEP] [--open-quote OPEN_QUOTE]
                        [--close-quote CLOSE_QUOTE]
                        [--include-long-matches-in-result]
                        [--max-num-processes MAX_NUM_PROCESSES]
                        source-file-path target-path

ProQuoLm compare allows the user to find short quotations (<= 4 words) in two
texts, a source text and a target text. The target text is the text quoting
the source text. Quotations in the target text need to be clearly marked with
quotations marks.

positional arguments:
  source-file-path      Path to the source text file
  target-path           Path to the target text file or folder

options:
  -h, --help            show this help message and exit
  --tokenizer TOKENIZER
                        Name of the tokenizer to load from Hugging Face or
                        path to the tokenizer folder
  --model MODEL         Name of the model to load from Hugging Face or path to
                        the model folder
  --lower-case, --no-lower-case
                        Run model inference on lower case text (default: True)
  --output-folder-path OUTPUT_FOLDER_PATH
                        The output folder path. If this option is set the
                        output will be saved to a file created in the
                        specified folder
  --create-dated-subfolder, --no-create-dated-subfolder
                        Create a subfolder named with the current date to
                        store the results (default: False)
  --text, --no-text     Include matched text in the returned data structure
                        (default: True)
  --output-type {json,text,csv}
                        The output type
  --csv-sep CSV_SEP     output separator for csv (default: '\t')
  --open-quote OPEN_QUOTE
                        The quotation open character. If this option is not
                        set, then the type of quotation marks used in a target
                        text is auto automatically identified.
  --close-quote CLOSE_QUOTE
                        The quotation close character. If this option is not
                        set, then the type of quotation marks used in a target
                        text is auto automatically identified.
  --include-long-matches-in-result
                        Include matches longer than 4 words in the output
  --max-num-processes MAX_NUM_PROCESSES
                        Maximum number of processes to use for parallel
                        processing. This can significantly speed up the
                        process.
~~~

</details>

To run `ProQuo`, use the following command:

~~~
proquo compare path_to_source_text path_to_target_text
path_to_the_reference_vocab_file
path_to_the_reference_model_file
path_to_the_relation_tokenizer_folder
path_to_the_relation_model_folder
--text
--output-type text
~~~

`--output-type text` prints the results to the command line. To save the results to a file, use `--output-type csv` or
`--output-type json`. `--text` includes the quotation text in the output.

The output will look something like this:

~~~
10      15	    500	505	quote	quote
1000	1016	20	36	some other quote	some other quote
~~~

The first two numbers are the character start and end positions in the source text and the other two numbers are the
character start and end positions in the target text.

<details>
<summary>All ProQuo command line options</summary>

~~~
usage: proquo compare [-h] [--quid-match-path QUID_MATCH_PATH]
                      [--output-folder-path OUTPUT_FOLDER_PATH]
                      [--create-dated-subfolder] [--no-create-dated-subfolder]
                      [--parallel-print-files [PARALLEL_PRINT_FILES ...]]
                      [--parallel-print-first-page PARALLEL_PRINT_FIRST_PAGE]
                      [--parallel-print-last-page PARALLEL_PRINT_LAST_PAGE]
                      [--text] [--no-text] [--ref] [--no-ref]
                      [--output-type {json,text,csv}] [--csv-sep CSV_SEP]
                      [--open-quote OPEN_QUOTE] [--close-quote CLOSE_QUOTE]
                      [--include-long-matches-in-result]
                      [--max-num-processes MAX_NUM_PROCESSES]
                      source-file-path target-path ref-vocab-file-path
                      ref-model-file-path rel-tokenizer-folder-path
                      rel-model-folder-path

ProQuo compare allows the user to find short quotations (<= 4 words) in two
texts, a source text and a target text. The target text is the text quoting
the source text. Quotations in the target text need to be clearly marked with
quotations marks.

positional arguments:
  source-file-path      Path to the source text file
  target-path           Path to the target text file or folder
  ref-vocab-file-path   Path to the reference vocab text file
  ref-model-file-path   Path to the reference model file
  rel-tokenizer-folder-path
                        Path to the relation tokenizer folder
  rel-model-folder-path
                        Path to the relation model folder

options:
  -h, --help            show this help message and exit
  --quid-match-path QUID_MATCH_PATH
                        Path to the file or folder with quid matches. If this
                        option is not set, then Quid is used to find long
                        matches.
  --output-folder-path OUTPUT_FOLDER_PATH
                        The output folder path. If this option is set the
                        output will be saved to a file created in the
                        specified folder
  --create-dated-subfolder
                        Create a subfolder named with the current date to
                        store the results
  --no-create-dated-subfolder
                        Do not create a subfolder named with the current date
                        to store the results
  --parallel-print-files [PARALLEL_PRINT_FILES ...]
                        Filenames of files which quote a parallel print
                        edition
  --parallel-print-first-page PARALLEL_PRINT_FIRST_PAGE
                        Number of the first page with parallel print
  --parallel-print-last-page PARALLEL_PRINT_LAST_PAGE
                        Number of the last page with parallel print
  --text                Include matched text in the returned data structure
  --no-text             Do not include matched text in the returned data
                        structure
  --ref                 Include matched reference in the returned data
                        structure
  --no-ref              Do not include matched reference in the returned data
                        structure
  --output-type {json,text,csv}
                        The output type
  --csv-sep CSV_SEP     output separator for csv (default: '\t')
  --open-quote OPEN_QUOTE
                        The quotation open character. If this option is not
                        set, then the type of quotation marks used in a target
                        text is auto automatically identified.
  --close-quote CLOSE_QUOTE
                        The quotation close character. If this option is not
                        set, then the type of quotation marks used in a target
                        text is auto automatically identified.
  --include-long-matches-in-result
                        Include matches longer than 4 words in the output
  --max-num-processes MAX_NUM_PROCESSES
                        Maximum number of processes to use for parallel
                        processing.This can significantly speed up the
                        process.
~~~

</details>

## Parallel processing
`ProQuo` and `ProQuoLM` use [Quid](https://scm.cms.hu-berlin.de/schluesselstellen/quid) in the background which supports
using multiple processes when comparing multiple target texts with the source texts. To use Quid with multiple processes
the command line option `--max-num-processes` is used. The default is 1.

## Training
The library also supports training and testing of custom models. The [Training Readme](Training-Readme.md) gives an introduction to
training models.

## Citation
If you use `ProQuo` or `ProQuoLM` or base your work on our code, please cite our paper:
~~~
@article{arnold2023,
  author = {Frederik Arnold, Robert Jäschke},
  title = {A Novel Approach for Identification and Linking of Short Quotations in Scholarly Texts and Literary Works},
  volume = {2},
  year = {2023},
  url = {https://jcls.io/article/id/3590/},
  issue = {1},
  doi = {10.48694/jcls.3590},
  month = {1},
  publisher={Universitäts- und Landesbibliothek Darmstadt},
  journal = {Journal of Computational Literary Studies}
}
~~~