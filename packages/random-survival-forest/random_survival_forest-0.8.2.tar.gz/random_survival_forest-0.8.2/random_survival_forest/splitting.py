from sksurv import compare, util
import numpy as np


def _find_split(node):
    """
    Find the best split for a Node.
    :param node: Node to find best split for.
    :return: score of best split, value of best split, variable to split, left indices, right indices.
    """
    score_opt = 0
    split_val_opt = None
    lhs_idxs_opt = None
    rhs_idxs_opt = None
    split_var_opt = None
    for i in node.f_idxs:
        score, split_val, lhs_idxs, rhs_idxs = _find_best_split_for_variable(node, i)

        if score > score_opt:
            score_opt = score
            split_val_opt = split_val
            lhs_idxs_opt = lhs_idxs
            rhs_idxs_opt = rhs_idxs
            split_var_opt = i

    return score_opt, split_val_opt, split_var_opt, lhs_idxs_opt, rhs_idxs_opt


def _find_best_split_for_variable(node, var_idx):
    """
    Find best split for a variable of a Node. Best split for a variable is the split with the highest log rank
    statistics. The logrank_test function of the lifelines package is used here.
    :param node: Node
    :param var_idx: Index of variable
    :return: score, split value, left indices, right indices.
    """
    score, split_val, lhs_idxs, rhs_idxs = logrank_statistics(x=node.x, y=node.y,
                                                              feature=var_idx,
                                                              min_leaf=node.min_leaf)
    return score, split_val, lhs_idxs, rhs_idxs


def logrank_statistics(x, y, feature, min_leaf):
    """
    Compute logrank_test of liflines package.
    :param x: Input samples
    :param y: Labels
    :param feature: Feature index
    :param min_leaf: Minimum number of leafs for each split.
    :return: best score, best split value, left indices, right indices
    """
    x_feature = x.reset_index(drop=True).iloc[:, feature]
    score_opt = 0
    split_val_opt = None
    lhs_idxs = None
    rhs_idxs = None

    unique_vals = np.sort(np.unique(x_feature))

    for split_val in unique_vals:
        feature1 = np.where(x_feature <= split_val)[0]
        feature2 = np.where(x_feature > split_val)[0]

        if len(feature1) < min_leaf or len(feature2) < min_leaf:
            continue

        y_tmp = y.iloc[np.concatenate((feature1, feature2)), :2]
        y_tmp['group_indicator'] = np.nan
        y_tmp.iloc[feature1, -1] = 0
        y_tmp.iloc[feature2, -1] = 1

        try:
            score, p_value = compare.compare_survival(
                util.Surv.from_dataframe("arrest", "week", y_tmp.drop(columns='group_indicator')),
                y_tmp.loc[:, 'group_indicator'], return_stats=False)
        except ValueError:
            continue
        if score > score_opt:
            score_opt = round(score, 3)
            split_val_opt = round(split_val, 3)
            lhs_idxs = feature1
            rhs_idxs = feature2

    return score_opt, split_val_opt, lhs_idxs, rhs_idxs
