import json
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from generalization.utils.scores import compute_el2n_scores
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from tqdm import tqdm

import wandb


def check_local(table_names: set, base_dir: str = "./artifacts", verbose=False):
    base_dir = Path(base_dir)
    if not base_dir.exists():
        return set(), []
    artifact_dirs = set([f.name for f in base_dir.iterdir() if f.is_dir()])

    # intersection
    local_table_names = table_names.intersection(artifact_dirs)

    # get file in local artifacts, recursively
    if verbose:
        print("base_dir", base_dir)
        print("local_table_names", local_table_names)
    local_table_names = [
        list(Path(base_dir / local_table_name).glob("**/*"))[0]
        for local_table_name in local_table_names
    ]
    return artifact_dirs, local_table_names


def get_scores(run_id, project, merge_all=False, verbose=False):
    api = wandb.Api()
    run = api.run(f"{project}/{run_id}")

    # list all artifacts, filtered by type
    table_names = set(
        [a.name for a in run.logged_artifacts() if "sample_metrics" in a.name]
    )

    local_ids, _ = check_local(table_names, base_dir=f"./artifacts/{run_id}")
    todo_table_names = table_names.difference(local_ids)
    if verbose:
        print("todo_table_names", todo_table_names)
    # download
    for table_id in tqdm(todo_table_names):
        filepath_ = api.artifact(f"{project}/{table_id}").download(
            root=f"./artifacts/{run_id}/{table_id}"
        )
        if verbose:
            print("downloaded", filepath_)

    _, local_table_paths = check_local(table_names, base_dir=f"./artifacts/{run_id}")

    if not merge_all:
        local_table_paths = [local_table_paths[-1]]

    tables = []
    for table_name in tqdm(local_table_paths):
        json_dict = json.load(open(table_name, "r"))
        df = pd.DataFrame(json_dict["data"], columns=json_dict["columns"])
        tables.append(df)

    return pd.concat(tables)


def score_by_pct_hist(score_by_pct, ax, score_name, epoch_idx=0):
    ax = sns.barplot(x=score_by_pct.index, y=score_by_pct.values, ax=ax)
    ax.set_title(f"{score_name} by percentile for epoch {epoch_idx}")
    ax.set_xlabel("Percentile")
    ax.set_ylabel(score_name)
    return ax


def compute_score_percentile(df, score_name):
    # group by epoch and compute the percentile of the column score, use round to have groups of 0.1
    return df.groupby("epoch")[score_name].rank(pct=True).round(1)


def score_histograms(scores_df, to_compare_scores=None, apply_norm=False):
    if to_compare_scores is None:
        fig, axs = plt.subplots(
            figsize=(12, 8),
            nrows=4,
            ncols=1,
            sharey="row",
        )
    else:
        fig = plt.figure(figsize=(12, 8), layout="tight")

        gs = GridSpec(5, 2, figure=fig)
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax3 = fig.add_subplot(gs[1, 0])
        ax4 = fig.add_subplot(gs[1, 1])
        ax5 = fig.add_subplot(gs[2, 0])
        ax6 = fig.add_subplot(gs[2, 1])
        ax7 = fig.add_subplot(gs[3, 0])
        ax8 = fig.add_subplot(gs[3, 1])
        ax9 = fig.add_subplot(gs[4, :])
        axs = [ax1, ax3, ax5, ax7, ax2, ax4, ax6, ax8, ax9]
        # axs = [ax1, ax2, ax3, ax4, ax5, ax6, ax7]

    def plot_acc(df, ax):
        acc_by_pct = df.set_index("loss_pct")["accuracy"]
        ax = score_by_pct_hist(acc_by_pct, ax=ax, score_name="Accuracy")
        return acc_by_pct

    def plot_loss(df, ax):
        loss_by_pct = df.set_index("loss_pct")["loss"]
        if apply_norm:  # normalize loss between 0 and 1
            loss_by_pct = loss_by_pct.apply(
                lambda x: (x - df["loss"].min()) / (df["loss"].max() - df["loss"].min())
            )

        ax = score_by_pct_hist(loss_by_pct, ax=ax, score_name="Loss")
        return loss_by_pct

    def plot_el2n(df, ax):
        df["el2n"] = compute_el2n_scores(
            np.array(df["logits"].tolist()),
            np.array(df["target"].tolist()),
        )
        el2n_by_pct = df.set_index("loss_pct")["el2n"]
        ax = score_by_pct_hist(el2n_by_pct, ax=ax, score_name="EL2N")
        return el2n_by_pct

    def plot_diff(score_1, score_2, ax):
        # difference between loss and el2n
        score_diff = score_1 - score_2
        normalized_score_diff = (score_diff - score_diff.min()) / (
            score_diff.max() - score_diff.min()
        )
        ax = score_by_pct_hist(normalized_score_diff, ax=ax, score_name="Loss - EL2N")
        return score_diff

    acc_by_pct = plot_acc(scores_df, axs[0])
    loss_by_pct = plot_loss(scores_df, axs[1])
    el2n_by_pct = plot_el2n(scores_df, axs[2])
    plot_diff(loss_by_pct, el2n_by_pct, axs[3])

    if to_compare_scores is not None:
        acc_by_pct_2 = plot_acc(to_compare_scores, axs[4])
        loss_by_pct_2 = plot_loss(to_compare_scores, axs[5])
        el2n_by_pct_2 = plot_el2n(to_compare_scores, axs[6])
        plot_diff(loss_by_pct_2, el2n_by_pct_2, axs[7])

        # plot difference between scores
        # plot_diff(el2n_by_pct, el2n_by_pct_2, axs[8])

    plt.tight_layout()

    return fig, axs
