#!../venv/bin/python

#
# Chapter 06
#
# Exercise 51
#

import sys
import polars as pl
from sklearn.model_selection import train_test_split

STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def rename_header(df, column_names):
    header_dict = dict()
    for idx, column_name in enumerate(column_names):
        original = "column_" + str(idx+1)
        header_dict[original] = column_name
    return df.rename(header_dict)

def make_features(df, uniq_list):
    title_df = df.select(
        NEW_TITLE=pl.col("TITLE")
        .str.to_lowercase()
        .str.replace_all(r"[^a-z ]", " ")
        .str.split(by=" ")
    )
    for word in uniq_list:
        title_df = title_df.with_columns(
            pl.col("NEW_TITLE").list.contains(word).cast(pl.Int32).alias(word)
        )
    return title_df.drop(pl.col("NEW_TITLE"))

def main():
    args = sys.argv

    # Number of command line argments must be 1
    assert len(args) == 2, "Usage: {} file".format(args[0])
    file_name = args[1]

    try:
        df = pl.read_csv(
            file_name,
            has_header=False,
            quote_char=None,
            separator="\t"
        )
    except:
        print("Could not read {} ...".format(file_name))
        sys.exit()

    # ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP
    column_names = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
    df = rename_header(df, column_names)
    df = df.filter(
        pl.col("PUBLISHER").is_in(
            [
                "Reuters",
                "Huffington Post",
                "Businessweek",
                "Contactmusic.com",
                "Daily Mail"
            ]
        )
    ).drop("ID")

    train, valid_test = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
    )

    valid, test = train_test_split(
        valid_test,
        test_size=0.5,
        random_state=42,
    )

    tmp = train.select(
        NEW_TITLE=pl.col("TITLE")
        .str.to_lowercase()
        .str.replace_all(r"[^a-z ]", " ")
        .str.split(by=" ")
    )

    tmp = tmp.rows()

    uniq_list = list()
    for record in tmp:
        uniq_list += record[0]

    uniq_list = list(set(uniq_list))
    uniq_list = list(filter(lambda x: len(x) > 2, uniq_list))
    uniq_list = list(filter(lambda x: x not in STOP_WORDS, uniq_list))
    uniq_list = sorted(uniq_list)
    #print(uniq_list)

    new_train = make_features(train, uniq_list)
    new_train = pl.concat([train.drop("TITLE"), new_train], how="horizontal")
    print(new_train)
    new_valid = make_features(valid, uniq_list)
    new_valid = pl.concat([valid.drop("TITLE"), new_valid], how="horizontal")
    print(new_valid)
    new_test  = make_features(test,  uniq_list)
    new_test  = pl.concat([test.drop("TITLE"), new_test],   how="horizontal")
    print(new_test)



    try:
        new_train.write_csv("./data/train.feature.txt", separator="\t")
        print("train: {}".format(train.height))
        new_valid.write_csv("./data/valid.feature.txt", separator="\t")
        print("valid: {}".format(valid.height))
        new_test.write_csv("./data/test.feature.txt",   separator="\t")
        print("test:  {}".format(test.height))
    except:
        print("Could not write ...")
        sys.exit()

if __name__ == "__main__":
    main()
