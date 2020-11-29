# author: Kangyu (Mark) Wang, Jiacheng Wang
# date: 2020-11-26

"""This script reads the train split csv file and produces exploratory data visualizations.
Usage: EDA.py --preprocessed_train=<preprocessed_train> --quality_count_path=<quality_count_path> --quality_fixed_acidity_path=<quality_fixed_acidity_path> --quality_volatile_acidity_path=<quality_volatile_acidity_path> --quality_free_sulfur_dioxide_path=<quality_free_sulfur_dioxide_path> --quality_alcohol_path=<quality_alcohol_path> --quality_citric_acid_path=<quality_citric_acid_path> --quality_residual_sugar_path=<quality_residual_sugar_path> --quality_chlorides_path=<quality_chlorides_path> --quality_total_sulfur_dioxide_path=<quality_total_sulfur_dioxide_path> --quality_density_path=<quality_density_path> --quality_ph_path=<quality_ph_path> --quality_sulphates_path=<quality_sulphates_path> 

Options:
--preprocessed_train=<preprocessed_train>                               Takes the unquoted relative path of the proprecessed train split as a csv file (this is a required option)
--quality_count_path=<quality_count_path>                               Takes the unquoted relative path to place the output png file depicting the distribution of wine quality
--quality_fixed_acidity_path=<quality_fixed_acidity_path>               Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and fixed_acidity
--quality_volatile_acidity_path=<quality_volatile_acidity_path>         Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and volatile_acidity
--quality_free_sulfur_dioxide_path=<quality_free_sulfur_dioxide_path>   Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and free_sulfur_dioxide
--quality_alcohol_path=<quality_alcohol_path>                           Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and alcohol
--quality_citric_acid_path=<quality_citric_acid_path>                   Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and citric_acid
--quality_residual_sugar_path=<quality_residual_sugar_path>             Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and residual_sugar
--quality_chlorides_path=<quality_chlorides_path>                       Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and chlorides
--quality_total_sulfur_dioxide_path=<quality_total_sulfur_dioxide_path> Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and total_sulfur_dioxide
--quality_density_path=<quality_density_path>                           Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and density
--quality_ph_path=<quality_ph_path>                                     Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and ph
--quality_sulphates_path=<quality_sulphates_path>                       Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and sulphates
"""

import altair as alt
from docopt import docopt
import numpy as np
import pandas as pd
import sys


opt = docopt(__doc__)


def main(opt):
    preprocessed_train = opt["--preprocessed_train"]

    # Read in data
    try:
        wine_train = pd.read_csv(preprocessed_train)
    except FileNotFoundError:
        print("Input csv file of train set does not exist.")
        sys.exit(1)

    # Create visualizations
    wine_train["quality"] = wine_train["quality"].astype("category")
    alt.data_transformers.disable_max_rows()

    ## Distribution of outcome variable
    quality_count_path = opt["--quality_count_path"]

    count_chart = (
        alt.Chart(wine_train)
        .mark_bar(size=40)
        .encode(
            x=alt.X("quality:O", type="quantitative"),
            y=alt.Y("count()"),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    count_chart.save(quality_count_path)

    ## Quality ~ fixed_acidity
    quality_fixed_acidity_path = opt["--quality_fixed_acidity_path"]
    # quality_fixed_acidity_path = "../results/quality_fixed_acidity.png"

    fixed_acidity = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(fixed_acidity)", scale=alt.Scale(domain=(6, 8.5))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("fixed_acidity:Q"))
    )

    quality_fixed_acidity = fixed_acidity + error
    quality_fixed_acidity.save(quality_fixed_acidity_path)

    ## Quality ~ volatile_acidity
    quality_volatile_acidity_path = opt["--quality_volatile_acidity_path"]
    # quality_volatile_acidity_path = "../results/quality_volatile_acidity.png"

    volatile_acidity = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(volatile_acidity)", scale=alt.Scale(domain=(0.2, 0.6))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("volatile_acidity:Q"))
    )

    quality_volatile_acidity = volatile_acidity + error
    quality_volatile_acidity.save(quality_volatile_acidity_path)

    ## quality ~ free_sulfur_dioxide

    quality_free_sulfur_dioxide_path = opt["--quality_free_sulfur_dioxide_path"]
    # quality_free_sulfur_dioxide_path = "../results/quality_free_sulfur_dioxide.png"

    free_sulfur_dioxide = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(free_sulfur_dioxide)", scale=alt.Scale(domain=(10, 55))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("free_sulfur_dioxide:Q"))
    )

    quality_free_sulfur_dioxide = free_sulfur_dioxide + error
    quality_free_sulfur_dioxide.save(quality_free_sulfur_dioxide_path)

    ## quality ~ alcohol

    quality_alcohol_path = opt["--quality_alcohol_path"]
    # quality_alcohol_path = "../results/quality_alcohol.png"

    alcohol = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(alcohol)", scale=alt.Scale(domain=(9, 13))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("alcohol:Q"))
    )

    quality_alcohol = alcohol + error
    quality_alcohol.save(quality_alcohol_path)

    ## quality ~ citric acid

    quality_citric_acid_path = opt["--quality_citric_acid_path"]
    citric_acid = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(citric_acid)", scale=alt.Scale(domain=(0.2, 0.45))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("citric_acid:Q"))
    )

    quality_citric_acid = citric_acid + error
    quality_citric_acid.save(quality_citric_acid_path)

    ## quality ~ residual sugar
    quality_residual_sugar_path = opt["--quality_residual_sugar_path"]
    residual_sugar = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(residual_sugar)"),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("residual_sugar:Q"))
    )

    quality_residual_sugar = residual_sugar + error
    quality_residual_sugar.save(quality_residual_sugar_path)

    ## quality ~ chlorides
    quality_chlorides_path = opt["--quality_chlorides_path"]
    chlorides = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(chlorides)"),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("chlorides:Q"))
    )

    quality_chlorides = chlorides + error
    quality_chlorides.save(quality_chlorides_path)

    ## quality ~ total sulfur dioxide
    quality_total_sulfur_dioxide_path = opt["--quality_total_sulfur_dioxide_path"]
    total_sulfur_dioxide = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(total_sulfur_dioxide)", scale=alt.Scale(domain=(95, 150))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("total_sulfur_dioxide:Q"))
    )

    quality_total_sulfur_dioxide = total_sulfur_dioxide + error
    quality_total_sulfur_dioxide.save(quality_total_sulfur_dioxide_path)

    ## quality ~ density
    quality_density_path = opt["--quality_density_path"]
    density = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(density)", scale=alt.Scale(domain=(0.988, 0.998))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("density:Q"))
    )

    quality_density = density + error
    quality_density.save(quality_density_path)

    ## quality ~ ph
    quality_ph_path = opt["--quality_ph_path"]
    ph = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(ph)", scale=alt.Scale(domain=(3.2, 3.35))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("ph:Q"))
    )

    quality_ph = ph + error
    quality_ph.save(quality_ph_path)

    ## quality ~ sulphates
    quality_sulphates_path = opt["--quality_sulphates_path"]
    sulphates = (
        alt.Chart(wine_train)
        .mark_bar()
        .encode(
            x=alt.X("quality"),
            y=alt.Y("mean(sulphates)", scale=alt.Scale(domain=(0.4, 0.55))),
            color=alt.Color("quality", title="Wine Grade"),
        )
        .properties(width=400)
    )

    error = (
        alt.Chart(wine_train)
        .mark_errorbar()
        .encode(x=alt.X("quality"), y=alt.Y("sulphates:Q"))
    )

    quality_sulphates = sulphates + error
    quality_sulphates.save(quality_sulphates_path)


if __name__ == "__main__":
    main(opt)