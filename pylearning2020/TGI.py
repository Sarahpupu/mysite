import pandas as pd


# 定义高低客单分类标准
def if_high(x):
    if x > 50:
        return "高客单"
    else:
        return "低客单"


if __name__ == '__main__':
    df = pd.read_excel('TGI指数案例数据.xlsx')
    gp_user = df.groupby('买家昵称')['实付金额'].mean().reset_index()
    # print(gp_user.head())
    # print('===========================')

    gp_user["客单类别"] = gp_user['实付金额'].apply(if_high)
    # print(gp_user.head(5))
    # print('===========================')

    df_dup = df.loc[df.duplicated('买家昵称') == False, :]
    # print(df_dup.head())
    df_merge = pd.merge(gp_user, df_dup, right_on='买家昵称', left_on='买家昵称', how='left')
    # print(df_merge.head())

    df_merge = df_merge[['买家昵称', '客单类别', '省份', '城市']]

    result = pd.pivot_table(df_merge, index=['省份', '城市'], columns='客单类别', aggfunc='count')
    # print(result.head())

    # print(result['买家昵称']['高客单'].reset_index().head())

    tgi = pd.merge(result['买家昵称']['高客单'].reset_index(), result['买家昵称']['低客单'].reset_index(),
                   left_on=['省份', '城市'], right_on=['省份', '城市'], how='inner')
    # print(tgi.head())

    tgi['总人数'] = tgi['高客单'] + tgi['低客单']
    tgi['高客单占比'] = tgi['高客单'] / tgi['总人数']

    # print(tgi.head())

    tgi = tgi.dropna()

    # 分母：总人数中高客单占比
    total_percentage = tgi['高客单'].sum() / tgi['总人数'].sum()
    # print(total_percentage)

    # TGI指数计算
    tgi['高客单TGI指数'] = tgi['高客单占比'] / total_percentage * 100
    tgi = tgi.sort_values('高客单TGI指数', ascending=False)
    # print(tgi.head())

    # 排除小城市
    tgi_big_city = tgi.loc[tgi['总人数'] > tgi['总人数'].mean(), :].reset_index()
    print(tgi_big_city.head())

    # 到处数据
    tgi_big_city.to_csv('TGI_result.csv')
    tgi_big_city.to_excel('TGI_result.xlsx')
