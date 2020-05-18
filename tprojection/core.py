##{
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import tprojection.utils as ut
##}

__all__ = ["Tprojection"]

font = {'size'   : 12}

matplotlib.rc('font', **font)

##{
class Tprojection:
    """
    this class allows to study the relation between the target and a single feature, with the specificity to display a chart type adapted
    to the type of the input variables (categorical or continuous)
    """

    def __init__(self, df, target, feature,
                 target_type="", feature_type="",
                 target_modality="",
                 nb_modalities=0, n_estimators=1,
                 continuous_threshold=0.05):
        """
        Parameters
        ----------
        df: pandas DataFrame
        target: string
        feature: string
        target_type: string
           can take the values "categorical" or "continuous"
        feature_type: string
           can take the values "categorical" or "continuous"
        target_modality: string
            will be used for multiclass problem (not implemented yet)
        nb_modalities: int (0)
            if > 0, encode feature on nb_modalities dummy modalities if the cardinality is to high
        n_estimators: int (1)
            if > 1, use boostrapping to evaluate estimator variance (only relevant for categorical target and features)
        """


        self.df = df.copy()
        self.target = target
        self.feature = feature
        self.target_type =  target_type
        self.feature_type = feature_type
        self.target_modality = target_modality
        self.nb_modalities = nb_modalities
        self.continuous_threshold = continuous_threshold
        self.n_estimators = n_estimators

        self._infer_type()
        self._check_dtype_consistency()
        self._infer_target_modality()
        self._sanitize_target()

    def plot(self):
        self.fig, self.ax1 = plt.subplots()
        self.ax2 = self.ax1.twinx()

        if self.feature_type == "categorical":
            self._cat2all_prep()
            show_boxplot = np.where(self.target_type == "categorical", 0, 1)
            self._cat2all_plot(show_boxplot)
        else:
            if self.target_type == "categorical":
                self._con2bin_plot()
            else:
                self._con2con_plot()

        plt.tight_layout()
        plt.show(block=False)

    def _infer_type(self):
        if self.target_type == "":
            self.target_type = np.where(ut.is_continuous(self.df[self.target], self.continuous_threshold), "continuous", "categorical")
        if self.feature_type == "":
            self.feature_type = np.where(ut.is_continuous(self.df[self.feature], self.continuous_threshold), "continuous", "categorical")

    def _check_dtype_consistency(self):
        def set_dtype(var):
            mydtype = str if getattr(self, var + '_type') == 'categorical' else float
            self.df[getattr(self, var)] = self.df[getattr(self, var)].astype(mydtype).copy()
        set_dtype("feature")
        set_dtype("target")

    def _infer_target_modality(self):
        if self.target_type == "categorical" and self.target_modality == "":
            self.target_modality = self.df[self.target].value_counts().sort_values().index[0]

    def _sanitize_target(self):
        if self.target_type == 'categorical':
            self.df["target_san"] = np.where(self.df[self.target] == self.target_modality, 1, 0)
        else:
            self.df['target_san'] = self.df[self.target]

    def _bootstrap(self, feature):
        dg = pd.DataFrame()
        replace = np.where(self.n_estimators > 1, True, False)
        count = self.df.groupby(feature)[self.target].count()
        for ii in range(self.n_estimators):
            dtmp = self.df.sample(frac=1, replace=replace)
            dg = dg.append(dtmp.groupby(feature)["target_san"].mean())
        dboot= dg.aggregate(["mean", "min", "max"], axis=0)
        dboot.loc["count",:] = count.values
        return dboot.T


    def _cat2all_prep(self):

        if self.nb_modalities:
            self.encoding = ut.get_encoding(self.df, 'target_san', self.feature, self.nb_modalities)
        else:
            self.encoding = {v: v for v in self.df[self.feature].unique()}
        self.df[self.feature + "_encoded"] = self.df[self.feature].map(self.encoding)
        dg = self._bootstrap(self.feature + "_encoded")
        dg['baseline'] = self.df["target_san"].mean()
        dg.sort_values(by="count", ascending=False, inplace=True)
        segment = self.feature + "_encoded"

        self.dg = dg
        self.segment = segment


    def _cat2all_plot(self, show_boxplot=False):
        self.dg["count"].plot(kind="bar", color="blue", ax=self.ax1, alpha=0.5)
        xlabels = self.ax1.get_xticklabels()
        self.ax1.set_xticklabels(xlabels, rotation=45)
        self.dg["mean"].plot(color="red", marker="o", markersize=5, linewidth=2,  ax=self.ax2)
        self.dg["min"].plot(color="red", linewidth=1, linestyle="--", ax=self.ax2)
        self.dg["max"].plot(color="red", linewidth=1, linestyle="--", ax=self.ax2)
        self.ax2.fill_between(self.ax2.get_xticks(), self.dg["min"], self.dg["max"], facecolor="red", alpha=0.2)

        self.dg["baseline"].plot(color="black", linestyle="--", linewidth=2, ax=self.ax2)

        if show_boxplot:
            sns.boxplot(x=self.segment, y=self.target, data=self.df, order=self.dg.index,
                   color="white", boxprops=dict(alpha=0.5))

        self.ax1.set_xlim([-0.6, len(self.dg)-0.5])
        self.ax1.set_xlabel(self.feature)
        self.ax2.set_ylabel(self.target)
        self.ax1.set_ylabel("count")

    def _con2bin_plot(self):
        """
        plot two histograms, one for each class of the target if the target is
        binary and the feature continuous
        """
        pos = self.df.query("target_san == 1")[self.feature]
        neg = self.df.query("target_san == 0")[self.feature]
        lb = np.min([pos.min(), neg.min()])
        ub = np.max([pos.max(), neg.max()])
        bins = np.linspace(lb, ub, int(np.round(len(pos)**0.5)))
        sns.distplot(neg, kde=False, norm_hist=True, bins=bins, ax=self.ax1)
        sns.distplot(pos, kde=False, norm_hist=True, bins=bins, ax=self.ax1)
        self.ax1.legend(["neg. ({})".format(len(neg)), "pos. ({})".format(len(pos))])

    def _con2con_plot(self):
        """ display a simple scatter plot if both target and feature are continuous
        """
        self.ax1.scatter(self.df[self.feature], self.df[self.target], alpha=0.5)
        self.ax1.set_xlabel(self.feature)
        self.ax1.set_ylabel(self.target)

##}


