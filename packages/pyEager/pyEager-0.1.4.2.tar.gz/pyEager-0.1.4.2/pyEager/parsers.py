from json import load
import pandas as pd

#### A set of functions to parse the JSON output of nf-core/eager modules into pandas DataFrames ####


def parse_sexdeterrmine_json(json_path, minimal=False):
    """Parses nf-core/eager sex determination results into a pandas DataFrame.

    Args:
        json_path (string): The path to the json file.
        minimal (bool, optional): Should a minimal Data frame be generated?. Defaults to False.

    Returns:
        pandas.DataFrame: A data frame containing the sample-level data from the json file.
          If minimal is True, then only the relative coverages on the X & Y are returned,
          with their respective errors.
    """

    with open(json_path) as f:
        data = pd.read_json(f, orient="index")
        data = data.drop(index="Metadata", columns=["tool_name", "version"])

        if minimal:
            data = data.drop(
                columns=[
                    "Snps Autosomal",
                    "XSnps",
                    "YSnps",
                    "NR Aut",
                    "NrX",
                    "NrY",
                ]
            )

    ## Reset the index
    data.reset_index(inplace=True, names=["id"])
    return data


def parse_damageprofiler_json(json_path):
    """Parses damageprofiler results into a dictionary of pandas DataFrames.

    Args:
        json_path (string): The path to the json file.

    Returns:
        dict: A dictionary containing each part of the json file as its own pandas data frame.
    """

    damageprofiler_json_attributes = [
        "metadata",
        "lendist_fw",
        "dmg_5p",
        "summary_stats",
        "dmg_3p",
        "lendist_rv",
    ]
    damage_profiler_results = {}

    with open(json_path) as f:
        data = load(f)
        for attr in damageprofiler_json_attributes:
            if attr.startswith("dmg_"):
                damage_profiler_results[attr] = pd.DataFrame(
                    data=data[attr], columns=[attr]
                )
            elif attr.startswith("lendist_"):
                damage_profiler_results[attr] = pd.DataFrame.from_dict(
                    data[attr], orient="index", columns=["count"]
                )
                damage_profiler_results[attr].index.name = "length"
                damage_profiler_results[attr].sort_index(
                    axis=0, ascending=True, inplace=True
                )
            elif attr == "metadata":
                damage_profiler_results[attr] = pd.DataFrame.from_dict(
                    data[attr], orient="index", columns=["value"]
                )
            else:
                damage_profiler_results[attr] = pd.json_normalize(data[attr])

    ## Resetting the index cannot be done here, since the output is not a single data frame.
    ## Instead adding the 'id' column happens in compile_damage_table()
    return damage_profiler_results


def parse_nuclear_contamination_json(json_path):
    """Parses nf-core/eager nuclear_contamination results into a pandas DataFrame.

    Args:
        json_path (string): The path to the json file.

    Returns:
        pandas.DataFrame: A data frame containing the library-level nuclear contamination results from the json file.
    """

    with open(json_path) as f:
        data = load(f)
        contamination_table = pd.DataFrame.from_dict(data["data"], orient="index")

    ## Reset the index
    contamination_table.reset_index(inplace=True, names=["id"])
    return contamination_table


def parse_snp_coverage_json(json_path):
    """Parses eigenstratdatabasetools eigenstrat_snp_coverage results into pandas DataFrame.

    Args:
        json_path (string): The path to the json file.

    Returns:
        pandas.DataFrame: A data frame containing the sample-level SNP coverage results from the json file.
    """

    with open(json_path) as f:
        data = load(f)
        coverage_table = pd.DataFrame.from_dict(data["data"], orient="index")

    ## Reset the index
    coverage_table.reset_index(inplace=True, names=["id"])
    return coverage_table


def parse_endorspy_json(json_path):
    """Parses a single endorspy result JSON into pandas DataFrame.

    Args:
        json_path (string): The path to the json file.

    Returns:
        pandas.DataFrame: A data frame containing the endogenous DNA results from the json file.
    """

    with open(json_path) as f:
        data = load(f)
        endogenous_table = pd.DataFrame.from_dict(data["data"], orient="index")

        ## Reset the index
        endogenous_table.reset_index(inplace=True, names=["id"])
        return endogenous_table


def parse_eager_tsv(tsv_path):
    """Parse an nf-core/eager input TSV into a pandas DataFrame.

    Args:
        tsv_path (string): The path to the TSV file.

    Returns:
        pandas.DataFrame: A data frame containing the data of the TSV, with additional columns specifying what merging steps took place.
    """
    ## TODO Eventually, could add renaming of columns here to keep output consistent between eager 2.* and 3.*
    with open(tsv_path) as f:
        tsv_table = pd.read_table(f, sep="\t")

        ## Check what merging took place
    ## First: Post-dedup merging of libraries with shared UDG-treatment/Sample/Strandedness
    merged_after_dedup = (
        tsv_table.filter(["Sample_Name", "Library_ID", "Strandedness", "UDG_Treatment"])
        .groupby(["Sample_Name", "Strandedness", "UDG_Treatment"])
        .nunique()
    )
    merged_after_dedup["initial_merge"] = merged_after_dedup["Library_ID"].apply(
        lambda f: f > 1
    )
    merged_after_dedup.drop(columns=["Library_ID"], inplace=True)

    ## Next, merging of libraries across UDG-treatment that share Sample/Strandedness
    merged_after_trimming = (
        merged_after_dedup.reset_index()
        .filter(["Sample_Name", "Strandedness", "UDG_Treatment"])
        .groupby(["Sample_Name", "Strandedness"])
        .nunique()
    )
    merged_after_trimming["additional_merge"] = merged_after_trimming[
        "UDG_Treatment"
    ].apply(lambda f: f > 1)
    merged_after_trimming.drop(columns=["UDG_Treatment"], inplace=True)

    ## Finally, check if there are any samples have in multiple strandedness values
    multiple_strandedness_per_ind = (
        merged_after_trimming.reset_index()
        .filter(["Sample_Name", "Strandedness"])
        .groupby(["Sample_Name"])
        .nunique()
    )
    multiple_strandedness_per_ind["strandedness_clash"] = multiple_strandedness_per_ind[
        "Strandedness"
    ].apply(lambda f: f > 1)
    multiple_strandedness_per_ind.drop(columns=["Strandedness"], inplace=True)

    ## Create tsv table that includes decision tree results
    decision_tree = (
        pd.merge(
            tsv_table,
            merged_after_dedup,
            on=["Sample_Name", "Strandedness", "UDG_Treatment"],
            how="left",
        )
        .merge(merged_after_trimming, on=["Sample_Name", "Strandedness"], how="left")
        .merge(multiple_strandedness_per_ind, on=["Sample_Name"], how="left")
    )

    return decision_tree


## Takes the output of parse_eager_tsv() and adds the foreign keys at different levels
def infer_merged_bam_names(tsv_data, skip_deduplication=None, run_trim_bam=None):
    """Infer the names of eager output files based on the merging steps that took place.

    Args:
        tsv_data (pandas.DataFrame):  A dataframe with the TSV data, as returned from parse_eager_tsv.
        skip_deduplication (boolean): Was deduplication skipped during the nf-core/eager run?
        run_trim_bam (boolean):       Was BAM trimming activated during the nf-core/eager run?
    """
    ## Ensure tsv_dta is a pandas DataFrame
    if not isinstance(tsv_data, pd.DataFrame):
        raise ValueError("tsv_data must be a pandas DataFrame.")

    ## Ensure skip deduplication and run_trim_bam are booleans if they are not None
    if skip_deduplication:
        if not isinstance(skip_deduplication, bool):
            raise ValueError("skip_deduplication must be a boolean.")
    if run_trim_bam:
        if not isinstance(run_trim_bam, bool):
            raise ValueError("run_trim_bam must be a boolean.")

    ## TODO Implement inference of names when deduplication is skipped.
    ## Inner functions that applies conditional logic to infer the merged BAM names
    ## Get initial merge BAM name
    def initial_bam_name(row, run_trim_bam):
        ## No initial merge
        if not row["initial_merge"] and not run_trim_bam:
            return f"{row['Library_ID']}_rmdup.bam"
        elif not row["initial_merge"] and run_trim_bam:
            return f"{row['Library_ID']}.trimmed.bam"
        ## Initial merge
        elif row["initial_merge"] and not run_trim_bam:
            return f"{row['Sample_Name']}_udg{row['UDG_Treatment']}_libmerged_rmdup.bam"
        elif row["initial_merge"] and run_trim_bam:  ## i.e. else, but more explicit
            return (
                f"{row['Sample_Name']}_udg{row['UDG_Treatment']}_libmerged.trimmed.bam"
            )

    ## Get additional merge BAM name
    def additional_bam_name(row):
        ## No additional merge
        if not row["additional_merge"]:
            return row["initial_bam_name"]
        ## Additional merge
        elif row["additional_merge"]:
            return f"{row['Sample_Name']}_libmerged_add.bam"

    ## Get sex determination BAM name
    def sexdet_bam_name(row):
        return (
            row["additional_bam_name"]
            .replace(".bam", f"_{row['Strandedness']}strand.bam")
            .replace("_udgnone_", "_")
        )

    ## Add columns with inferred BAM names
    tsv_data["initial_bam_name"] = tsv_data.apply(
        initial_bam_name, axis=1, run_trim_bam=run_trim_bam
    )
    tsv_data["additional_bam_name"] = tsv_data.apply(additional_bam_name, axis=1)
    tsv_data["sexdet_bam_name"] = tsv_data.apply(sexdet_bam_name, axis=1)

    return tsv_data


def parse_general_stats_table(general_stats_path):
    """Parse the general_stats_table.txt output of MultiQC into a pandas DataFrame.

    Args:
        general_stats_path (string): The path to the `general_stats_table.txt` TSV file.

    Returns:
        pandas.DataFrame: A data frame containing the data of the TSV.
    """
    with open(general_stats_path) as f:
        data = pd.read_table(f, sep="\t")

    return data
