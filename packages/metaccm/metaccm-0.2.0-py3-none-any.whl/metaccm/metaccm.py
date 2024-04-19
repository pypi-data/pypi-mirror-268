
# import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


def logo():
    print("\n",
          '\t', '            ._____  _______            ', '\n',
          '\t', '  |\    /|  |          |       /\      ', '\n',
          '\t', '  | \  / |  |_____     |      /__\     ', '\n',
          '\t', '  |  \/  |  |          |     /    \    ', '\n',
          '\t', '  |      |  |_____     |    /      \   ', '\n',
          "\n",
          '\t', '       .____     .____                 ', '\n',
          '\t', '      /         /        |\    /|     ', '\n',
          '\t', '     |         |         | \  / |     ', '\n',
          '\t', '     \         \         |  \/  |     ', '\n',
          '\t', '      \_____    \_____   |      |     ', '\n')
    print('\t', " Meta-CCM 2024-04", '\n')


def process_nominal(vector):
    return vector


def process_scale(vector):
    var_vector = vector.reshape(-1, 1)  # 将向量转换为二维数组
    # 使用最大最小标准化将数值映射到 0-1 之间
    scaler = MinMaxScaler()
    normalized_vector = scaler.fit_transform(var_vector)
    # 将标准化后的向量再转换回一维数组
    normalized_vector = normalized_vector.flatten()

    return normalized_vector


def process_ordinal(vector):
    var_vector = vector.reshape(-1, 1)  # 将向量转换为二维数组
    # 使用最大最小标准化将数值映射到 0-1 之间
    scaler = MinMaxScaler()
    normalized_vector = scaler.fit_transform(var_vector)
    # 将标准化后的向量再转换回一维数组
    normalized_vector = normalized_vector.flatten()

    return normalized_vector


def process_binary(vector):
    # 使用 LabelEncoder 将字符串类型转换为数字类型
    label_encoder = LabelEncoder()
    encoded_vector = label_encoder.fit_transform(vector)
    # 将第一个类别映射为 0，第二个类别映射为 1
    normalized_vector = encoded_vector - encoded_vector.min()

    return normalized_vector


# 定义一个字典，将不同类型的操作关联起来
process_dict = {
    'nominal': process_nominal,
    'scale': process_scale,
    'ordinal': process_ordinal,
    'binary': process_binary
}

# data=metadata
# standardVars=confoundVars+RequireDiffVar
# varType = varTypes+['nominal']

def standardizedVarValue(data, standardVars, varType):
    """
    Standardizes the data based on the given variable types.

    :param data: (DataFrame) DataFrame containing the data.
    :param standardVars: (list) List of variables to be standardized.
    :param varType: (list) List of types corresponding to each variable.
    :return: (DataFrame) DataFrame after standardization.
    """

    for var, type in zip(standardVars, varType):
        # print(var, type)
        # var, type = 'smokingFreq', 'ordinal'

        vector = data[var].values
        process_func = process_dict.get(type)
        normalized_vector = vector
        if process_func:
            normalized_vector = process_func(vector)
            # print(f"Normalized {var} for type: {type}")

        else:
            print(f"No processing function of {var} for type: {type}")

        data[var] = normalized_vector

    return data


# negS, posS, weight = neg_samples[matchVars], pos_sample[matchVars], weight
# help(matchingScore)
def matchingScore(negS: pd.DataFrame, posS: pd.DataFrame, weight: list[float]):
    """
    The function matchingScore calculates a matching score based on the input negative samples (negS), positive samples
    (posS), and weights (weight).
    Here is a breakdown of the processing steps:

    1) Copy the values of positive samples (posS) to match the number of rows in negative samples (negS) to create an
    expanded DataFrame posS_expanded.
    2) Extract the numerical columns from negative samples, reset the index, extract the corresponding numerical
    columns from posS_expanded, and convert them to numeric type.
    3) Extract the categorical columns from negative samples, reset the index, extract the corresponding categorical
    columns from posS_expanded, and convert them to string type.
    4) Calculate the squared differences of numerical columns, i.e., (negS - posS) ** 2.
    5) Determine the equality of categorical columns and convert the equality status to integers.
    6) Merge the DataFrames diff_squared and char_equal to create the DataFrame result.
    7) Convert the weights (weight) to a NumPy array.
    8) Multiply each row of result with the weights vector to calculate the matching scores.
    9) Return the calculated matching scores as a NumPy array.

    In summary, this function processes numerical column differences squared and categorical column equalities with
    weights to produce an array of matching scores.

    :param negS: (DataFrame) DataFrame of negative samples.
    :param posS: (DataFrame) DataFrame of positive samples.
    :param weight: (array) Array of weights for calculating the score.
    :return: (array) Array of matching scores.
    """

    # negS,posS  = neg_samples[matchVars], pos_sample[matchVars]

    # 复制posS的值以匹配negS的行数
    posS_expanded = pd.DataFrame(np.tile(posS, (len(negS), 1)))
    posS_expanded.columns = negS.columns

    # 提取数值型列
    num_negS = negS.select_dtypes(include='number')
    num_negS = num_negS.reset_index(drop=True)
    num_posS = posS_expanded[num_negS.columns]
    # 将num_posS中的值转换为数值型
    num_posS = num_posS.apply(pd.to_numeric)

    # 提取字符型列
    char_negS = negS.select_dtypes(include='object')
    char_negS =char_negS.reset_index(drop=True)
    char_posS = posS_expanded[char_negS.columns]
    char_posS = char_posS.astype(str)

    # 计算数值型列的差值的平方
    diff_squared = (num_negS - num_posS) ** 2

    # 计算字符型列的相等情况
    char_equal = (char_negS == char_posS).astype(int)

    # 合并数据框X和Y
    result = pd.concat([diff_squared, char_equal], axis=1)

    # 将weight转换为numpy数组
    weight = np.array(weight)

    # 将result中的每一行与weight进行向量相乘
    score = result.apply(lambda row: np.dot(row, weight), axis=1)

    # 返回NumPy数组
    return score


# data=data
# sampleID='sampleID'
# label='label'
# matchVars=confoundVars
# weight=weightVars
# RequireDiffVar=RequireDiffVar

# help(matchingVars)
def matchingVars(data: pd.DataFrame, label: str, matchVars: list[str], weight: list[float], RequireDiffVar: list[str]):
    """
    This is a function to realize the matching algorithm, which matches positive and negative samples according to
    specific criteria.
    Here’s a breakdown of the steps involved:

    1) Initialize the pairID and matchType variables.
    2) Loop through the positive samples (pos_var) until either the positive or negative sample list is empty.
    3) Select a positive sample and create a copy of the negative samples.
    4) Check if there are any requirements (RequireDiffVar) for selecting negative samples that are different from the
    positive sample.
    5) Filter out negative samples that do not meet the requirements.
    6) If no suitable negative samples remain, remove the current positive sample and continue to the next iteration.
    7) Calculate a matching score for each remaining negative sample based on certain match variables and weights.
    8) Select the negative sample with the highest matching score.
    9) Assign pairID, matchType, and pair the positive and negative samples together.
    10) Add the matched pairs to separate dataframes and remove them from the sample pool.
    11) Concatenate the matched pairs dataframes, sort them by pairID, and return the balanced data.

    Overall, the function aims to balance the positive and negative samples by creating pairs that meet specific
    criteria. It ensures that each positive sample is matched with a suitable negative sample based on the matching score.

    :param data: (DataFrame) This parameter represents the dataset containing the samples that need to be balanced. It
    could include both positive and negative samples.
    :param label: (String) Represents a label in a dataset. It is used to distinguish between positive and negative
    samples.
    :param matchVars: (List of strings) Is a list of variables that need to be matched, which will be used to calculate
    the matching score between positive and negative samples.
    :param weight: (List of floats) This parameter represents the weight assigned to each match variable when
    calculating the matching score. It allows giving more importance to certain variables in the matching process.
    :param RequireDiffVar: (List of strings) This parameter specifies whether there are any requirements for selecting
    negative samples that are different from positive samples. It could be used to ensure diversity in the matched pairs.
    :return: (DataFrame) This function is expected to return a balanced dataset with pairs of positive and negative
    samples that meet the specified criteria. The pairs are matched based on the matching score calculated using the
    matchVars and weights.
    """

    logo()

    # 保存匹配样本对的数据框
    matched_pos = pd.DataFrame() # 阳性样本池
    matched_neg = pd.DataFrame() # 阴性样本池
    pos_var = data[data[label] == 1]
    neg_var = data[data[label] == 0]
    # pos_var = pos_var.reset_index(drop=True)
    # neg_var = neg_var.reset_index(drop=True)

    pairID = 0 # 初始化
    matchType = 'matchingVars'

    for i in range(len(pos_var)):
        if len(pos_var) == 0 or len(neg_var) == 0:
            break
        # 选择一个阳性样本
        pos_sample = pos_var.sample()
        neg_samples = neg_var.copy()

        # 1) 查看限定条件 RequireDiffVar，选择与阳性样本 RequireDiffVar 不一样的阴性样本
        for difVar in RequireDiffVar:
            # print(difVar)
            # 将 neg_samples[difVar] 和 pos_sample[difVar] 的值转换为集合
            # neg_set = set(neg_samples[difVar])
            pos_set = set(pos_sample[difVar])
            # 找出 neg_samples[difVar] 中不在 pos_sample[difVar] 中的值的位置
            indices = [j for j, val in enumerate(neg_samples[difVar]) if val not in pos_set]
            # 根据 indices 列表提取出符合条件的行
            # iloc方法是根据行的位置（整数位置）来进行选择，而不是根据行的索引（标签）来选择。
            neg_samples = neg_samples.iloc[indices]
        if len(neg_samples) == 0:
            # 没有符合条件的阴性样本，从样本池中移除当前阳性样本
            pos_var = pos_var.drop(pos_sample.index)
            continue

        # 2) 在阴性样本中选取与阳性样本 match score 最大的样本
        score = matchingScore(neg_samples[matchVars], pos_sample[matchVars], weight)
        maxscore_neg_sample = neg_samples.iloc[np.argmax(score), :].to_frame().T

        # 为 pos_sample 和 maxscore_neg_sample 添加 'pairs' 和 'matchType' 信息
        pairID += 1
        pos_sample['pairs'] = pairID
        maxscore_neg_sample['pairs'] = pairID
        pos_sample['matchType'] = matchType
        maxscore_neg_sample['matchType'] = matchType

        # 3) 将匹配的正、负样本分别添加到数据框中，并从样本池中移除
        matched_pos = pd.concat([matched_pos, pos_sample])
        matched_neg = pd.concat([matched_neg, maxscore_neg_sample])
        pos_var = pos_var.drop(pos_sample.index)
        neg_var = neg_var.drop(maxscore_neg_sample.index)


    # 合并正负样本对数据框并保存结果
    matched_pairs_df = pd.concat([matched_pos, matched_neg], axis=0)
    matched_pairs_df = matched_pairs_df.reset_index(drop=True)
    # 按照 pairs 顺序排列行
    balanced_data = matched_pairs_df.sort_values('pairs').reset_index(drop=True)

    return balanced_data
