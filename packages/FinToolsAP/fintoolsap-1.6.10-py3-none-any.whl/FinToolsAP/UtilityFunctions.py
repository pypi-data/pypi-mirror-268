from __future__ import annotations

# standard imports
import os
import tqdm
import numpy
import typing
import polars
import pandas
import pathlib
import functools
import statsmodels.api

def group_quantile(df: pandas.DataFrame | polars.DataFrame, 
                   gr: typing.Optional[typing.Union[str, list[str]]] = None, 
                   vr: typing.Optional[typing.Union[str, list[str]]] = None, 
                   q: typing.Optional[int] = None,
                   quantiles: typing.Optional[dict[str, typing.Union[int, list[float]]]] = None,
                   interpolation: typing.Optional[str] = 'linear',
                   no_merge: typing.Optional[bool] = False,
                   set_index: typing.Optional[bool] = False
                ) -> pandas.DataFrame | polars.DataFrame:
    
    """
    Compute quantiles for specified variables in a DataFrame, optionally grouping by certain columns.

    Parameters:
        df (pandas.DataFrame | polars.DataFrame): The DataFrame containing the data.
        gr (str or list[str], optional): Column(s) to group by. Default is None.
        vr (str or list[str], optional): Variable(s) to compute quantiles for. Default is None.
        q (int, optional): Number of quantiles to compute. Default is None.
        quantiles (dict[str, Union[int, list[float]]], optional): Custom quantiles to compute for each variable.
            Keys are variable names, values are lists of quantile values. Default is None.
        interpolation (str, optional): Interpolation method to use. Default is 'linear'.
        no_merge (bool, optional): If True, returns the DataFrame without merging. Default is False.

    Returns:
        pandas.DataFrame | polars.DataFrame: DataFrame containing quantiles for specified variables,
        optionally grouped by specified columns.

    Raises:
        TypeError: If input DataFrame is not of type pandas.DataFrame or polars.DataFrame,
            or if input arguments have incorrect types.
        ValueError: If input arguments are invalid.

    Notes:
        - If `quantiles` is None, `vr` and `q` must be specified.
        - If `quantiles` is provided, it takes precedence over `q`.
        - Available interpolation methods are 'linear', 'lower', 'higher', 'midpoint', and 'nearest'.
    """
    
    DECILES_QTILES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    QUINTIL_QTILES = [0.2, 0.4, 0.6, 0.8]
    QUARTIL_QTILES = [0.25, 0.5, 0.75]
    TERCILE_QTILES = [0.33, 0.66]
    MEDIAN_QTILESS = [0.5]
    
    # (0) type check
    # (0b) value check
    # (1) package information into dictionary
    # (2) compute quantiles item by item
    # (3) package results and return
    
    if(quantiles is None):
        # vr and q used
        if(vr is None):
            raise ValueError('vr: if quantiles is not specified then vr must be specified.')
        if(q is None):
            raise ValueError('q: if quantiles is not specified then q must be specified.')

    # type check df
    is_pandas = isinstance(df, pandas.DataFrame)
    if(not (is_pandas or isinstance(df, polars.DataFrame))):
        raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')
    
    if(gr is not None):
        # type check gr
        if(not (isinstance(gr, str) or isinstance(gr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(df).__name__!r}')
        if(isinstance(gr, list)):
            if(not all(isinstance(x, str) for x in gr)):
                raise TypeError(f'gr: expected a list of only strings, got {type(gr).__name__!r}')
        if(isinstance(gr, str)):
            gr = [gr]
        
    if(vr is not None):
        # type check vr
        if(not (isinstance(vr, str) or isinstance(vr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(vr).__name__!r}')
        if(isinstance(vr, list)):
            if(not all(isinstance(x, str) for x in vr)):
                raise TypeError(f'gr: expected a list of only str, got {type(vr).__name__!r}')
        if(isinstance(vr, str)):
            vr = [vr]

    if(q is not None):
        # type check q
        if(not isinstance(q, int)):
            raise TypeError(f'q: expected type int, got {type(q).__name__!r}')
            
    if(quantiles is not None):
        if(not isinstance(quantiles, dict)):
            raise TypeError(f'quantiles: expected a dict[str, list[float]], got {type(quantiles).__name__!r}')
        for k, v in quantiles.items():
            if(not isinstance(k, str)):
                raise TypeError(f'quantiles.keys(): expected a str, got {type(k).__name__!r}')
            if(not all(isinstance(x, float) for x in v)):
                raise TypeError(f'quantiles.values(): expected list[float], got {type(v).__name__!r}')
            
    # group or not
    group = gr is not None

    # package info into dictionary
    info_dict = {}
    
    if(quantiles is None):
        for var in vr:
            if(q == 2):
                info_dict[var] = MEDIAN_QTILESS
            elif(q == 3):
                info_dict[var] = TERCILE_QTILES
            elif(q == 4):
                info_dict[var] = QUARTIL_QTILES
            elif(q == 5):
                info_dict[var] = QUINTIL_QTILES
            elif(q == 10):
                info_dict[var] = DECILES_QTILES
            else:
                raise ValueError(f'q: if specified as int must take value 2, 3, 4, 5, or 10, got {q}')
    else:
        info_dict = quantiles

    # compute quantiles
    is_polars = isinstance(df, polars.DataFrame)

    if(is_pandas):
        res = []
        for var, qtiles in info_dict.items():
            ptiles = [f'{int(100 * q)}%' for q in qtiles]
            if(group):
                comp = df.groupby(by = gr)[var].describe(percentiles = qtiles)
                comp = comp[ptiles]
                comp = comp.add_prefix(f'{var}_')
                res.append(comp)
            else:
                comp = df[var].describe(percentiles = qtiles)
                comp = comp.to_frame()    
                comp = comp.loc[ptiles]
                res.append(comp)
        if(group):
            fin = functools.reduce(lambda x, y: pandas.merge(x, y, right_index = True, left_index = True), res)
            fin = fin.reset_index(drop = False)
            if(no_merge):
                if(set_index):
                    fin = fin.set_index(gr)
                    return(fin)
                return(fin)
            else:
                fin = df.merge(fin, how = 'inner', on = gr)
                if(set_index):
                    fin = fin.set_index(gr)
                    return(fin)
                return(fin)
        else:
            fin = functools.reduce(lambda x, y: pandas.merge(x, y, how = 'outer', right_index = True, left_index = True), res)
            return(fin)
    elif(is_polars):
        res_list = []
        for var, qtiles in info_dict.items():
            if(group):
                for q in qtiles:
                    comp = df[gr + [var]].group_by(gr).quantile(q, interpolation = interpolation)
                    comp = comp.rename(mapping = {var: f'{var}_{int(100 * q)}%'})
                    comp = comp.to_pandas()
                    res_list.append(comp)
            else:
                res_dict = {}
                for q in qtiles:
                    comp = df[var].quantile(q, interpolation = interpolation)
                    res_dict[f'{int(100 * q)}%'] = [comp]
                res = pandas.DataFrame(res_dict)
                res = res.transpose()
                res = res.rename(columns = {0: var})
                res = res_list.append(res)

        if(group):
            fin = functools.reduce(lambda x, y: pandas.merge(x, y, how = 'inner', on = gr), res_list)
            fin = fin.sort_values(by = gr)
            fin = fin.reset_index(drop = True)
            fin = polars.from_pandas(fin)
            if(no_merge):
                return(fin)
            else:
                fin = df.join(other = fin, how = 'inner', on = gr)
                return(fin)
        else:
            fin = functools.reduce(lambda x, y: pandas.merge(x, y, how = 'outer', right_index = True, left_index = True), res_list)
            fin = fin.reset_index(drop = False)
            fin = fin.rename(columns = {'index': 'ptile'})
            fin = polars.from_pandas(fin)
            return(fin)
    else:
        # type error
        raise TypeError('idk how u got here fam')

def group_nunique(df: polars.DataFrame | pandas.DataFrame, 
                  gr: str | list[str], 
                  vr: str | list[str], 
                  name: typing.Optional[typing.Union[str, dict[str, str]]] = None, 
                  no_merge: typing.Optional[bool] = False, 
                  merge_how: typing.Optional[str] = 'left',
                  set_index: typing.Optional[bool] = False
                ) -> polars.DataFrame | pandas.DataFrame:
        """
        Group by specified columns and calculate the number of unique values for each group.

        Parameters:
            df (polars.DataFrame or pandas.DataFrame): Input DataFrame.
            gr (str or list[str]): Grouping column(s).
            vr (str or list[str]): Column(s) on which to calculate the number of unique values.
            name (str or dict[str, str], optional): Custom name(s) for the resulting columns. 
                If a string is provided, it will be appended to the column names specified in `vr`.
                If a dictionary is provided, it should map original column names to new names.
                Defaults to None.
            no_merge (bool, optional): Whether to merge the result back to the original DataFrame. 
                on `gr`. Defaults to False.
            merge_how (str, optional): Method of merging if `no_merge` is False. 
                Possible values: 
                    Pandas: {`left`, `inner`, `outer`, `cross`, `right`}
                    Polars: {`left`, `inner`, `outer`, `cross`, `asof`, `semi`, `anti`}
                Defaults to 'left'.
            set_index (bool, optional): Weather or not to set the index with `gr`. Default False.
                Only applicable to pandas.DataFrame

        Returns:
            polars.DataFrame or pandas.DataFrame: DataFrame with the grouped results.

        Raises:
            TypeError: If input `df` is not a pandas.DataFrame or polars.DataFrame.
            TypeError: If input `gr` is not a string or a list of strings.
            TypeError: If input `vr` is not a string or a list of strings.
            TypeError: If input `name` is not a string, a dictionary with string keys and string values, or None.
            TypeError: If input `no_merge` is not a boolean.
        """
        
        # type check df
        is_pandas = isinstance(df, pandas.DataFrame)
        if(not (is_pandas or isinstance(df, polars.DataFrame))):
            raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')
        
        # type check gr
        if(not (isinstance(gr, str) or isinstance(gr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(df).__name__!r}')
        
        # tpye check vr
        if(isinstance(gr, list)):
            if(not all(isinstance(x, str) for x in gr)):
                raise TypeError(f'gr: expected a list of only strings, got {type(gr).__name__!r}')
            
        # type check vr
        if(not (isinstance(vr, str) or isinstance(vr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(vr).__name__!r}')
            
        if(isinstance(vr, list)):
            if(not all(isinstance(x, str) for x in vr)):
                raise TypeError(f'gr: expected a list of only str, got {type(vr).__name__!r}')
            
        if(isinstance(vr, str)):
            vr = [vr]
        
        # tpye check name
        if(name is not None):
            if(not (isinstance(name, str) or isinstance(name, dict))):
                raise TypeError(f'name: expected type str or dict[str:str], got {type(name).__name__!r}')
            
            if(isinstance(name, dict)):
                if(not all(isinstance(x, str) for x in name.keys())):
                    raise TypeError(f'name: expected all keys of type str, got {type(name).__name__!r}')
                if(not all(isinstance(x, str) for x in name.values())):
                    raise TypeError(f'name: expected all values of type str, got {type(name).__name__!r}')

        # type check no_merge     
        if(not isinstance(no_merge, bool)):
            raise TypeError(f'no_merge: expected type bool, got {type(no_merge).__name__!r}')

        names = {}
        if(isinstance(name, str)):
            # append name to column names in vr
            for col in vr:
                names[col] = f'{col}{name}'
        else:
            names = name

        if(is_pandas):
            res = df.groupby(by = gr)[vr].nunique()
            res = res.reset_index(drop = False)
            if(name is not None):
                res = res.rename(columns = names)
        else:
            res = df.group_by(gr).agg(polars.col(vr).n_unique())
            if(name is not None):
                res = res.rename(mapping = names)

        if(no_merge):
            if(set_index and is_pandas):
                res = res.set_index(gr)
                return(res)
            return(res)
        else:
            if(is_pandas):
                res = df.merge(res, how = merge_how, on = gr)
                if(set_index):
                    res = res.set_index(gr)
                    return(res)
                return(res)
            else:
                res = df.join(res, how = merge_how, on = gr)
            return(res)
        
def group_avg(df: pandas.DataFrame | polars.DataFrame, 
              gr: str | list[str], 
              vr: str | list[str], 
              wt: typing.Optional[str] = None,
              ignore_nan: typing.Optional[bool] = True,
              name: typing.Optional[typing.Union[str, list[str]]] = None,
              no_merge: typing.Optional[bool] = False,
              merge_how: typing.Optional[str] = 'left',
              suppress_ouput: typing.Optional[bool] = False,
              desc: typing.Optional[str] = None,
              set_index: typing.Optional[bool] = False
            ) -> pandas.DataFrame | polars.DataFrame:
        """
        Compute group-wise averages in a pandas DataFrame.

        Parameters:
            - df (pandas.DataFrame or polars.DataFrame): The input DataFrame.
            - gr (str or list[str]): The column(s) used for grouping.
            - vr (str or list[str]): The column(s) whose average is to be
                calculated.
            - wt (str or None, optional): The weight column for weighted 
                averages. Default is None. If None, equal weighted average 
                is calculated.
            - return_nan (bool, optional): If True, return numpy.nan in the
                case of a ZeroDivideError else return equal weighted
                mean. Default is False.
            - name (str, dict[str: str] or None, optional): Name(s) to append 
                to the resulting column(s). If str, it will be appended to 
                all columns in 'vr'. If dict, keys are column names in 'vr' and 
                values are the corresponding new names. Default is None.
            - no_merge (bool, optional): If True, the resulting DataFrame 
                will not be merged with the original DataFrame. Default is 
                False. DataFrames are merged on gr.
            - merge_how (str, optional): Type of merge operation when 
                no_merge is False. Default is 'left'.
            - suppress_output: (bool, optional): If True, the output from
                tqdm.tqdm is suppressed when calculating the average of 
                many columns for a pandas dataframe. Default is False.

        Returns:
            - pandas.DataFrame: A DataFrame with group-wise averages. 
                If no_merge is False, it is the original DataFrame merged 
                with the calculated averages.

        Raises:
            - TypeError: If the input arguments are not of the expected 
                types.

        Notes:
            - Ignores numpy.nan in calculation of means.
        """
        
        # type check df
        is_pandas = isinstance(df, pandas.DataFrame)
        if(not (is_pandas or isinstance(df, polars.DataFrame))):
            raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')
        
        # type check gr
        if(not (isinstance(gr, str) or isinstance(gr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(df).__name__!r}')
        
        # tpye check vr
        if(isinstance(gr, list)):
            if(not all(isinstance(x, str) for x in gr)):
                raise TypeError(f'gr: expected a list of only strings, got {type(gr).__name__!r}')
            
        # type check vr
        if(not (isinstance(vr, str) or isinstance(vr, list))):
            raise TypeError(f'gr: expected type str or list[str], got {type(vr).__name__!r}')
            
        if(isinstance(vr, list)):
            if(not all(isinstance(x, str) for x in vr)):
                raise TypeError(f'gr: expected a list of only str, got {type(vr).__name__!r}')
            
        if(isinstance(vr, str)):
            vr = [vr]
            
        # type check wt
        if(wt is not None):
            if(not isinstance(wt, str)):
                raise TypeError(f'wt: expected type str, got {type(wt).__name__!r}')
        
        # tpye check name
        if(name is not None):
            if(not (isinstance(name, str) or isinstance(name, dict))):
                raise TypeError(f'name: expected type str or dict[str:str], got {type(name).__name__!r}')
            
            if(isinstance(name, dict)):
                if(not all(isinstance(x, str) for x in name.keys())):
                    raise TypeError(f'name: expected all keys of type str, got {type(name).__name__!r}')
                if(not all(isinstance(x, str) for x in name.values())):
                    raise TypeError(f'name: expected all values of type str, got {type(name).__name__!r}')

        # type check no_merge     
        if(not isinstance(no_merge, bool)):
            raise TypeError(f'no_merge: expected type bool, got {type(no_merge).__name__!r}')
        
        DESCRIPTION = 'Calculating weigted average'
        if(isinstance(desc, str)):
            DESCRIPTION = desc
                    
        # Weighted average
        # can be used with groupby:  df.groupby('col1').apply(wavg, 'avg_name', 'weight_name')
        # ML: corrected by ML to allow for missing values
        # AP: corrected by AP to remove RunTimeWarning double_scalars
        def _wavg_py(gr, vr, wt):
            x = gr[[vr, wt]].dropna()
            den = x[wt].sum()
            if(den == 0):
                if(not ignore_nan):
                    return(numpy.nan)
                else:
                    return(gr[vr].mean())
            else:
                return((x[vr] * x[wt]).sum() / den)

        if(name is not None):
            names = {}
            if(isinstance(name, str) and isinstance(vr, list)):
                # append name to column names in vr
                for col in vr:
                    names[col] = f'{col}{name}'
            if(isinstance(name, dict)):
                names = name    
        
        if(is_pandas):
            # wt is None equal weighted average
            if(wt is None):
                res = df.groupby(by = gr).mean(numeric_only = True)[vr]
                if(isinstance(res, pandas.Series)):
                    res = res.to_frame()
                res = res.reset_index(drop = False)
            else:
                dfs_to_merge = []
                for col in tqdm.tqdm(vr, 
                                     desc = DESCRIPTION, 
                                     disable = suppress_ouput):
                    res = df.groupby(by = gr).apply(_wavg_py, col, wt, include_groups = False)
                    if(isinstance(res, pandas.Series)):
                        res = res.to_frame()
                    res = res.reset_index(drop = False)
                    if(0 in list(res.columns)):
                        res = res.rename(columns = {0: col})
                    dfs_to_merge.append(res)
                res = functools.reduce(lambda x, y: pandas.merge(x, y, on = gr), 
                                       dfs_to_merge
                                    )
            if(name is not None):
                res = res.rename(columns = names)
        else:
            df = df.fill_nan(None)
            if(wt is None):
                res = df.group_by(gr, maintain_order = True).agg(polars.col(vr).mean())
            else:
                mask_wt = polars.col(wt) * polars.col(vr).is_not_null()
                wavg = (polars.col(vr) * polars.col(wt)).sum() / mask_wt.sum()
                if(not ignore_nan):
                    res = df.group_by(gr, maintain_order = True).agg(wavg)
                else:
                    res = df.group_by(gr, maintain_order = True).agg(
                        polars.when(polars.col(wt).filter(polars.col(vr).is_not_null()).sum() == 0)
                            .then(polars.col(vr).mean())
                            .otherwise(wavg))
            if(name is not None):
                res = res.rename(mapping = names)

        if(no_merge):
            if(set_index and is_pandas):
                res = res.set_index(gr)
                return(res)
            return(res)
        else:
            if(is_pandas):
                res = df.merge(res, how = merge_how, on = gr)
                if(set_index):
                    res = res.set_index(gr)
                    return(res)
                return(res)
            else:
                res = df.join(res, how = merge_how, on = gr)
            return(res)
        
def group_sum(df: pandas.DataFrame | polars.DataFrame, 
              gr: str | list[str], 
              vr: str | list[str], 
              wt: typing.Optional[str] = None,
              name: typing.Optional[typing.Union[str, list[str]]] = None,
              no_merge: typing.Optional[bool] = False,
              merge_how: typing.Optional[str] = 'left',
              set_index: typing.Optional[bool] = False
            ) -> pandas.DataFrame | polars.DataFrame:
    """
    Groups the DataFrame by specified column(s), calculates the sum of specified column(s)
    for each group, and optionally merges the result back to the original DataFrame.

    Parameters:
    - df (pandas.DataFrame or polars.DataFrame): The input DataFrame.
    - gr (str or list[str]): The column(s) to group by.
    - vr (str or list[str]): The column(s) to sum within each group.
    - wt (str, optional): Weight column to use when aggregating.
    - name (str or dict[str, str], optional): A suffix to append to the column names in the output DataFrame
                                              or a dictionary mapping column names to their new names.
    - no_merge (bool, optional): If True, the result is not merged back to the original DataFrame.
                                 Default is False.
    - merge_how (str, optional): Method to use when merging the result back to the original DataFrame.
                                 Options are 'left', 'right', 'outer', 'inner'. Default is 'left'.

    Returns:
    - pandas/polars.DataFrame: The DataFrame with groups summarized by summing the specified columns,
                         optionally merged back to the original DataFrame.
    Raises:
    - TypeError: If the input types are invalid or not supported.

    Note:
    - If the input DataFrame is of type 'polars.DataFrame', it will use Polars library for aggregation,
      otherwise, it will use Pandas.
    - If 'name' is a string, it appends the name to the column names in 'vr'.
    - If 'no_merge' is True, the result DataFrame is returned without merging.
    - If 'no_merge' is False, the result DataFrame is merged back to the original DataFrame based on 'merge_how'.
    """

    # type check df
    is_pandas = isinstance(df, pandas.DataFrame)
    if(not (is_pandas or isinstance(df, polars.DataFrame))):
        raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')
    
    # type check gr
    if(not (isinstance(gr, str) or isinstance(gr, list))):
        raise TypeError(f'gr: expected type str or list[str], got {type(df).__name__!r}')
    
    # tpye check vr
    if(isinstance(gr, list)):
        if(not all(isinstance(x, str) for x in gr)):
            raise TypeError(f'gr: expected a list of only strings, got {type(gr).__name__!r}')
        
    # type check vr
    if(not (isinstance(vr, str) or isinstance(vr, list))):
        raise TypeError(f'gr: expected type str or list[str], got {type(vr).__name__!r}')
        
    if(isinstance(vr, list)):
        if(not all(isinstance(x, str) for x in vr)):
            raise TypeError(f'gr: expected a list of only str, got {type(vr).__name__!r}')
        
    if(isinstance(vr, str)):
        vr = [vr]
        
    # type check wt
    if(wt is not None):
        if(not isinstance(wt, str)):
            raise TypeError(f'wt: expected type str, got {type(wt).__name__!r}')
    
    # tpye check name
    if(name is not None):
        if(not (isinstance(name, str) or isinstance(name, dict))):
            raise TypeError(f'name: expected type str or dict[str:str], got {type(name).__name__!r}')
        
        if(isinstance(name, dict)):
            if(not all(isinstance(x, str) for x in name.keys())):
                raise TypeError(f'name: expected all keys of type str, got {type(name).__name__!r}')
            if(not all(isinstance(x, str) for x in name.values())):
                raise TypeError(f'name: expected all values of type str, got {type(name).__name__!r}')
            
    # type check no_merge     
    if(not isinstance(no_merge, bool)):
        raise TypeError(f'no_merge: expected type bool, got {type(no_merge).__name__!r}')
    
    names = {}
    if(isinstance(name, str)):
        # append name to column names in vr
        for col in vr:
            names[col] = f'{col}{name}'
    else:
        names = name

    if(is_pandas):
        res = df.groupby(by = gr)[vr].sum()
        res = res.reset_index(drop = False)
        if(name is not None):
            res = res.rename(columns = names)
    else:
        df = df.fill_nan(None)
        res = df.group_by(gr).agg(polars.col(vr).sum())
        if(name is not None):
            res = res.rename(mapping = names)
        
    if(no_merge):
        if(set_index and is_pandas):
            res = res.set_index(gr)
            return(res)
        return(res)
    else:
        if(is_pandas):
            res = df.merge(res, how = merge_how, on = gr)
            if(set_index):
                res = res.set_index(gr)
                return(res)
            return(res)
        else:
            res = df.join(res, how = merge_how, on = gr)
        return(res)
    
def compound(x: pandas.Series) -> float:
    """
    Calculate the compound return of a pandas Series representing a sequence of returns.

    This function takes a pandas Series of returns as input and calculates the compound return
    by multiplying all elements of the Series together after adding 1 to each element, then
    subtracting 1 from the product.

    Parameters:
        x (pandas.Series): A pandas Series containing a sequence of returns.

    Returns:
        float: The compound return calculated from the input Series.

    Example:
        >>> import pandas as pd
        >>> returns = pd.Series([0.1, 0.05, -0.02])
        >>> compound_return = compound(returns)
        >>> print(compound_return)
        0.1276
    """
    return((1 + x).prod() - 1)
    

def create_lags(df: typing.Union[pandas.DataFrame, polars.DataFrame],
                vr: typing.Optional[typing.Union[str, list[str]]] = None, 
                lag: typing.Optional[typing.Union[int, dict[str, int | list[int]]]] = 1,
                gr: typing.Optional[typing.Union[str, list[str]]] = None,
            ) -> pandas.DataFrame | polars.DataFrame:
    
    """
    Create lagged variables in a DataFrame.

    This function creates lagged variables in a pandas DataFrame or a 
        polars DataFrame.
    Lagged variables are created by shifting the values of selected 
        variables by a specified number of time periods.

    Parameters:
        df (pandas.DataFrame or polars.DataFrame): The DataFrame containing 
            the variables.
        vr (str or list of str, optional): The name(s) of the variable(s) 
            for which lagged variables will be created. Default is None.
        lag (int or dict, optional): The number of time periods to lag the 
            variable(s) by. If a dict is provided, it should map variable 
            names to lag values. Default is 1.
        gr (str or list of str, optional): The variable(s) to group by before 
            creating lagged variables. Default is None.

    Returns:
        pandas.DataFrame or polars.DataFrame: The DataFrame with lagged 
            variables added.

    Raises:
        ValueError: If both 'vr' and dictionary 'lag' are specified, or 
            if neither 'vr' nor dictionary 'lag' are specified.
        ValueError: If 'vr' is specified but 'lag' is not of type int.
        TypeError: If 'df' is not a pandas.DataFrame or polars.DataFrame.

    Example:
        >>> import pandas as pd
        >>> data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
        >>> df = pd.DataFrame(data)
        >>> df_lagged = create_lags(df, vr=['A', 'B'], lag=2)
        >>> print(df_lagged)
           A  B  A_L1  B_L1  A_L2  B_L2
        0  1  10   NaN   NaN   NaN   NaN
        1  2  20   1.0  10.0   NaN   NaN
        2  3  30   2.0  20.0   1.0  10.0
        3  4  40   3.0  30.0   2.0  20.0
        4  5  50   4.0  40.0   3.0  30.0
    """
    
    is_pandas = isinstance(df, pandas.DataFrame)
    is_polars = isinstance(df, polars.DataFrame)
    grouped = gr is not None

    if(vr is not None and isinstance(lag, dict)):
        raise ValueError('vr and dictionary lag can not both be specified.')
    
    if(vr is None and (lag is None or isinstance(lag, int))):
        raise ValueError('one of vr or dictionary lag must be specified.')
    
    if(vr is not None and not isinstance(lag, int)):
        raise ValueError(f'if vr is specified then lag must be of type int, got {type(lag).__name__!r}')
    
    if(isinstance(vr, str)):
        vr = [vr]
    
    var_int = vr if(vr is not None) else list(lag.keys())

    lag_int = {}
    for var in var_int:
        if(isinstance(lag, dict)):
            if(isinstance(lag[var], int)):
                lag_int[var] = list(range(1, lag[var] + 1))
            else:
                lag_int[var] = lag[var]
        else:
            lag_int[var] = list(range(1, lag + 1))

    for var in var_int:
        for lg in lag_int[var]:
            if(is_pandas):
                if(grouped):
                    df[f'{var}_L{lg}'] = df.groupby(by = gr)[var].shift(lg)
                else:
                    df[f'{var}_L{lg}'] = df[var].shift(lg)
            elif(is_polars):
                if(grouped):
                    df = df.with_columns(polars.col(var).shift(lg).over(gr).alias(f'{var}_L{lg}'))
                else:
                    df = df.with_columns(polars.col(var).shift(lg).alias(f'{var}_L{lg}'))
            else:
                raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')
            
    return(df)

def group_score(df: pandas.DataFrame | polars.DataFrame,
                gr: str | list[str] = None,
                vr: typing.Optional[typing.Union[str, list[str]]] = None,
                q: typing.Optional[typing.Union[int, dict[str, typing.Union[int, list[float]]]]] = 2,
                **kwargs
            ) -> pandas.DataFrame | polars.DataFrame:
    
    """
    Calculate group scores based on quantiles of specified variables.

    This function calculates group scores based on quantiles of specified variables 
        in a pandas DataFrame or a polars DataFrame.
    Group scores are assigned based on the quantiles, with each group assigned a score f
        rom 1 to the number of quantiles.

    Parameters:
        df (pandas.DataFrame or polars.DataFrame): The DataFrame containing the variables.
        gr (str or list of str, optional): The variable(s) to group by before calculating 
            group scores. Default is None.
        vr (str or list of str, optional): The name(s) of the variable(s) for which group 
            scores will be calculated. Default is None.
        q (int or dict, optional): The number of quantiles to divide the variable(s) into. 
            If a dict is provided, it should map variable names to either the number of 
            quantiles or a list of quantile boundaries. Default is 2.
        **kwargs: Additional keyword arguments to be passed to pandas.qcut or polars.qcut.

    Returns:
        pandas.DataFrame or polars.DataFrame: The DataFrame with group scores added.

    Raises:
        ValueError: If both 'vr' and dictionary 'q' are specified.
        TypeError: If 'df' is not a pandas.DataFrame or polars.DataFrame, or if keyword 
            arguments are incompatible with pandas.qcut or polars.qcut.

    Example:
        >>> import pandas as pd
        >>> data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
        >>> df = pd.DataFrame(data)
        >>> df_grouped = group_score(df, vr=['A', 'B'], q=3)
        >>> print(df_grouped)
           A   B A_scr3 B_scr3
        0  1  10      1      1
        1  2  20      2      2
        2  3  30      3      3
        3  4  40      3      3
        4  5  50      3      3
    """

    is_pandas = isinstance(df, pandas.DataFrame)
    is_polars = isinstance(df, polars.DataFrame)
    grouped = gr is not None

    if(vr is not None and isinstance(q, dict)):
        raise ValueError('vr and dictionary quantiles can not both be specified.')
    
    if(isinstance(vr, str)):
        vr = [vr]

    vr_int = vr if(vr is not None) else list(q.keys())

    quantiles_int = {}
    if(isinstance(q, int)):
        for var in vr_int:
            quantiles_int[var] = q
    else:
        quantiles_int = q

    for var in vr_int:
        tmp_q = quantiles_int[var]
        if(is_pandas):
            n = tmp_q if(isinstance(tmp_q, int)) else (len(tmp_q) - 1)
            labels_int = range(1, n + 1)
            try:
                if(grouped):
                    df[f'{var}_scr{n}'] = df.groupby(by = gr)[var].transform(
                        lambda g: pandas.qcut(g, 
                                              q = tmp_q,
                                              labels = labels_int,
                                              **kwargs
                                           )
                                        )
                else:
                    df[f'{var}_scr{n}'] = pandas.qcut(df[var], 
                                                      q = tmp_q,
                                                      labels = labels_int,
                                                      **kwargs
                                                    )
            except Exception as e:
                print(e)
                raise TypeError(f'one of the keyword arguments is incompatible with pandas.qcut or pandas.qcut raised the exception above')
        elif(is_polars):
            n = tmp_q if(isinstance(tmp_q, int)) else (len(tmp_q) + 1)
            labels_int = range(1, n + 1)
            labels_int = [str(i) for i in labels_int]
            try:
                if(grouped):
                    df = df.with_columns(polars.col(var).qcut(quantiles = tmp_q, 
                                                              labels = labels_int,
                                                              **kwargs
                                                            ).over(gr).alias(f'{var}_scr{n}'))
                else:
                    df = df.with_columns(polars.col(var).qcut(quantiles = tmp_q, 
                                                              labels = labels_int,
                                                              **kwargs
                                                            ).alias(f'{var}_scr{n}'))
                df = df.cast({f'{var}_scr{n}': polars.Int64})
            except Exception as e:
                print(e)
                raise TypeError(f'one of the keyword arguments is incompatible with polars.qcut or polars.qcut raised the exception above')
        else:
            raise TypeError(f'df: expected type pandas.DataFrame or polars.DataFrame, got {type(df).__name__!r}')

    return(df)

def lh_regression(endog: typing.Union[list, numpy.ndarray, pandas.Series], 
                  exog: typing.Union[list, numpy.ndarray, pandas.Series], 
                  horizon: int, 
                  se_type: typing.Union[str, list[str]],
                  add_constant: bool = True
                ) -> typing.Tuple:
    
    """
    Perform linear regression with a rolling window approach.

    Parameters:
    - endog (Union[list, numpy.ndarray, pandas.Series]): The dependent variable.
    - exog (Union[list, numpy.ndarray, pandas.Series]): The independent variable.
    - horizon (int): The number of periods to roll the window.
    - se_type (Union[str, list[str]]): Type of standard error(s) to 
        calculate.
    - add_constant (bool, optional): Whether to add a constant to 
        the independent variable. Default is True.

    Returns:
    Tuple: A tuple containing:
        - float: The estimated coefficient for the independent variable.
        - dict: A dictionary containing standard error(s) with their 
            corresponding type as keys.
        - float: The R-squared value of the regression.
        - numpy.ndarray: The residuals of the regression.

    Notes:
    - If endog or exog is a pandas Series, it will be converted to a 
        numpy array for processing.
    - The rolling window approach is implemented by differencing the 
        dependent variable over the horizon.
    - Standard error types supported:
        - 'R': Robust standard errors (HC0).
        - 'NW': Newey-West standard errors (HAC) with maxlags set to the horizon.
        - 'HH': Heteroskedasticity and autocorrelation robust standard 
            errors (HAC) with maxlags set to the horizon and uniform kernel.
        - Any other string: Assumes the string corresponds to a specific 
            covariance type.
    """
    
    if(isinstance(endog, pandas.Series)):
        endog = endog.values

    if(isinstance(endog, pandas.Series)):
        exog = exog.values

    ### k-horizon difference
    _Y =(numpy.roll(endog, -horizon) - endog)[:-horizon]

    if(add_constant):
        _X = statsmodels.api.add_constant(exog[:-horizon])

    _model_fit = statsmodels.api.OLS(_Y, _X).fit()

    ### point estimate
    _beta = _model_fit.params.iloc[-1]
    
    if(isinstance(se_type, str)):
        se_type = [se_type]

    ### SEs:
    _ses = {}
    for _se in se_type:
        if(_se == 'R'):
            _ses[_se] = _model_fit.get_robustcov_results(cov_type = 'HC0').bse[-1]
        elif(_se == 'NW'):
            _ses[_se] = _model_fit.get_robustcov_results(cov_type = 'HAC', 
                                                         maxlags = horizon
                                                        ).bse[-1]
        elif(_se == 'HH'):
            _ses[_se] = _model_fit.get_robustcov_results(cov_type = 'HAC', 
                                                         maxlags = horizon, 
                                                         kernel = 'uniform'
                                                        ).bse[-1]
        else:
            _ses[_se] = _model_fit.get_robustcov_results(cov_type = _se).bse[-1]

    # R^2
    _r2 = _model_fit.rsquared

    # Resiudals
    _resid = _model_fit.resid
    
    return(_beta, _ses, _r2, _resid)

def long_horizon_regssions(endog: typing.Union[list, numpy.ndarray, pandas.Series], 
                           exog: typing.Union[list, numpy.ndarray, pandas.Series], 
                           se_type: typing.Union[str, list[str]],
                           horizons: typing.Union[int, list[int]] = 10,
                           add_constant: bool = True,
                           return_resid: bool = False
                        ) -> pandas.DataFrame:
    
    """
    Perform linear regression with a rolling window approach for multiple horizons.

    Parameters:
    - endog (Union[list, numpy.ndarray, pandas.Series]): The dependent variable.
    - exog (Union[list, numpy.ndarray, pandas.Series]): The independent variable.
    - se_type (Union[str, list[str]]): Type of standard error(s) to calculate.
    - horizons (Union[int, list[int]], optional): The list of horizons or maximum 
        horizon if integer provided. Default is 10.
    - add_constant (bool, optional): Whether to add a constant to the independent 
        variable. Default is True.
    - return_resid (bool, optional): Whether to return residuals in addition to 
        regression results. Default is False.

    Returns:
    pandas.DataFrame: A DataFrame containing regression results for each horizon.
    
    If return_resid is True, a tuple containing the DataFrame and a dictionary 
        of residuals for each horizon is returned.
    """
    
    if(isinstance(horizons, int)):
        horizons = list(range(1, horizons + 1))

    res = pandas.DataFrame(index = horizons)
    resids = {}
    for k in horizons:
        _b, _ses, _r2, _resid = lh_regression(endog = endog, 
                                              exog = exog, 
                                              horizon = k,
                                              se_type = se_type, 
                                              add_constant = add_constant
                                            )
        res.loc[k, 'b'] = _b
        for _se, _values in _ses.items():
            res.loc[k, _se] = _values
        res.loc[k, 'R2'] = _r2
        resids[k] = _resid

    if(return_resid):
        return(res, resids)
    else:
        return(res)
    
def list_dir(path: typing.Union[str, pathlib.Path],
             only_dir: bool = False,
             extension: str = None,
             only_files: bool = True,
             keep_hidden: bool = False,
             absolute_paths: bool = False
            ) -> list[typing.Union[str, pathlib.Path]]:
    """
    List directories and/or files in a given path with optional filtering.

    Parameters:
    - path (Union[str, pathlib.Path]): The path to list contents from.
    - only_dir (bool, optional): Whether to list only directories. Default is False.
    - extension (str, optional): Filter files by extension. Default is None.
    - only_files (bool, optional): Whether to list only files. Default is True.
    - keep_hidden (bool, optional): Whether to include hidden files. Default is False.
    - absolute_paths (bool, optional): Whether to return absolute paths. Default is False.

    Returns:
    list[str]: A list of directory and/or file names.

    Notes:
    - If only_dir is True, only directories will be included.
    - If only_files is True, only files will be included.
    - If keep_hidden is True, hidden files will be included.
    - If extension is provided, only files with that extension will be included.
    - If absolute_paths is True, the full paths of directories and/or files will be returned.
    """
    
    path = pathlib.Path(path)
    path = path.resolve()
    _tmp = os.listdir(path)

    res = []
    for _obj in _tmp:
        _obj_path = path / _obj
        if(_obj_path.is_dir() and only_dir):
            res.append(_obj)
        elif(_obj_path.is_file() and only_files):
            if(keep_hidden or not _obj_path.stem.startswith('.')):
                if(extension is None or _obj_path.suffix == extension):
                    res.append(_obj)
    if(absolute_paths):
        res = [path / f for f in res]

    return(res)

def list_to_sql_str(lst: list[typing.Any], table: str = None, delimit: bool = False) -> str:
    """
    Convert a list of values into a string representation for SQL queries.

    Parameters:
    - lst (list): The list of values.
    - table (str, optional): The table name to prefix the column names with. Default is None.
    - delimit (bool, optional): Whether to delimit values with single quotes. Default is False.

    Returns:
    str: A string representation of the list for SQL queries.

    Example:
    >>> list_to_sql_str(['name', 'age'], 'person', delimit=True)
    "'person.name', 'person.age'"
    """
    res = ''
    for var in lst:
        if(table is None):
            if(delimit):
                res += f'\'{var}\', '
            else:
                res += f'{var}, '
        else:
            res += f'{table}.{var}, '
    res = res[:-2]
    return(res)
    
                



