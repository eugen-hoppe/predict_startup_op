def add_category_columns(
    df: pd.DataFrame,
    category_prefixes: list[str] = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7','c8']
) -> pd.DataFrame:

    exploded_df = df['category_list'].str.split('|').explode().reset_index()
    exploded_df['count'] = exploded_df.groupby('index')['category_list'].transform(
        'count'
    )
    exploded_df = exploded_df.sort_values(
        by=['index', 'count'], ascending=[True, False]
    )
    top_categories = exploded_df.groupby('index').head(len(category_prefixes))
    final_df = df.copy()
    for i, prefix in enumerate(category_prefixes):
        nth_category = (
            top_categories.groupby('index').nth(i)['category_list']
            .reset_index(drop=True)
        )
        final_df[f'{prefix}_cat'] = nth_category.reindex(df.index).fillna('None')

    return final_df
