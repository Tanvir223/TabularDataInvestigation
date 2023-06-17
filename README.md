---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

<div class="cell markdown" id="lJNrv9lwHw7t">

**This package provide a fast tabular data investigation and it will
eligible for ML model building and also helps to developers in their
projects when needed. Most of the functions return a dataframe or json
as output**

</div>

<div class="cell code" id="HRSU2lZ5Ht9v">

``` python
pip install TabularDataInvestigation
```

</div>

<div class="cell code" execution_count="43" id="VzC1_y2hTSlb">

``` python
from TabularDataInvestigation import tdi
```

</div>

<div class="cell markdown" id="5o29-lUSKmIy">

**tdi.find_index_for_null_values(df, return_type='dataframe')
Parameters:
df: pandas Dataframe
return_type(optional): Default = 'dataframe'**

</div>

<div class="cell markdown" id="vYvrNlAvIDQd">

Some we need to delete or fill the null values each cell specifically
with different methods. some data has meaning and some are unnecceesary.
so using this function we can get all the missing column indexes that we
can use in our project.

</div>

<div class="cell code" execution_count="19"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="TGS5k7JWIqz8" outputId="3663fd25-23cb-4558-a175-5ede1691661d">

``` python
df = pd.DataFrame({'A': [1, None, 3], 'B': ['!', 5, '?'], 'C': ['a', 'b', None]})
df
```

<div class="output execute_result" execution_count="19">

         A  B     C
    0  1.0  !     a
    1  NaN  5     b
    2  3.0  ?  None

</div>

</div>

<div class="cell code" execution_count="20"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}"
id="HLVms92Zn4qW" outputId="669872b8-bce7-456b-afae-37dca420cc49">

``` python
tdi.find_index_for_null_values(df)
```

<div class="output execute_result" execution_count="20">

         A    C
    0  [1]  [2]

</div>

</div>

<div class="cell code" execution_count="21"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}"
id="8_NmdR_UKRWy" outputId="b650a6f9-2f2b-49f8-a3e0-e575a1d74df0">

``` python
tdi.find_index_for_null_values(df, return_type='json')
```

<div class="output execute_result" execution_count="21">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="d9uRAKLzKYDy">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell markdown" id="OSAs6sHgLVf3">

**tdi.check_error_data_types(df, return_type='dataframe')
Parameters:
df: pandas Dataframe
return_type(optional): Default = 'dataframe')**

</div>

<div class="cell markdown" id="OpKOTMPmLl5w">

We usually face some unusual behave in the dataframe. Sometimes we are
seeing there is a numeric type column but after checking it shows object
or string type column. So this function will find the cuase.

</div>

<div class="cell code" execution_count="25"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="WQAv7nOpLktf" outputId="599eb053-4f53-4857-a2a0-52c1c68fc8d3">

``` python
df = pd.DataFrame({'A': [1, 'a', 3], 'B': [1, 5, 2], 'C': [1.3, 3.9,'2,0']})
df
```

<div class="output execute_result" execution_count="25">

       A  B    C
    0  1  1  1.3
    1  a  5  3.9
    2  3  2  2,0

</div>

</div>

<div class="cell code" execution_count="26"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:112}"
id="S8gaMAASbZc4" outputId="0325075a-93e6-4347-bbfc-823e74021772">

``` python
tdi.check_error_data_types(df)
```

<div class="output execute_result" execution_count="26">

      columns error_data error_index
    0       A        [a]         [1]
    1       C      [2,0]         [2]

</div>

</div>

<div class="cell code" execution_count="27"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}"
id="RcCmVNZAMgkH" outputId="4c6315d7-6fd3-4a87-9ef2-4116f47b4401">

``` python
tdi.check_error_data_types(df, return_type='json')
```

<div class="output execute_result" execution_count="27">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="NSjujMp0Mqv1">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell markdown" id="IwI-sfT4MsLG">

**tdi.check_num_of_min_category(df, return_type='dataframe') Parameters:
df: pandas Dataframe
minimum_threshold : this define the minimum count of a
category(Default=3)
return_type(optional):how want to get the output (Default =
'dataframe')**

</div>

<div class="cell code" execution_count="28"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}"
id="eM1XHOiOM1Fd" outputId="4b9d38f4-fe36-4b69-e47c-971529b56d69">

``` python
df = pd.DataFrame({'A': ['b', 'a', 'b','a'], 'B': ['x', 'x', 'y','x'], 'C': ['p', 'p', 'q','q']})
df
```

<div class="output execute_result" execution_count="28">

       A  B  C
    0  b  x  p
    1  a  x  p
    2  b  y  q
    3  a  x  q

</div>

</div>

<div class="cell code" execution_count="29"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}"
id="EwgrDhQ4C0fj" outputId="7adb6b4a-e039-46f5-9273-93e4299faf54">

``` python
tdi.check_num_of_min_category(df, minimum_threshold=1)
```

<div class="output execute_result" execution_count="29">

      columns category index
    0       B      [y]   [2]

</div>

</div>

<div class="cell code" execution_count="30"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}"
id="zNg1D-hZNwhF" outputId="c4f3bef9-1796-499d-927c-ab572ab08c51">

``` python
tdi.check_num_of_min_category(df, minimum_threshold=1, return_type='json')
```

<div class="output execute_result" execution_count="30">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="FpWRMlBINw0M">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell markdown" id="gXIXp6XBN7NM">

**tdi.check_col_with_one_category(df, return_type='dataframe')
Parameters:
df: pandas Dataframe
return_type(optional):how want to get the output (Default =
'dataframe')**

</div>

<div class="cell markdown" id="YO1-JmApOFDz">

Sometimes we got such categorical column which data have no variation
that means all column's data are same. So this function will findout
those column(s)

</div>

<div class="cell code" execution_count="31"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}"
id="GOO1rwMHN6c0" outputId="288a9482-0ac7-437b-f248-67f5021c8753">

``` python
df = pd.DataFrame({'A': ['b', 'a', 'b','a'], 'B': ['x', 'x', 'x','x'], 'C': ['p', 'p', 'q','q']})
df
```

<div class="output execute_result" execution_count="31">

       A  B  C
    0  b  x  p
    1  a  x  p
    2  b  x  q
    3  a  x  q

</div>

</div>

<div class="cell code" execution_count="32"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}"
id="R_dXOEClEBKg" outputId="c10cbf14-cb6c-49fc-82a6-e37fdd3c4787">

``` python
tdi.check_col_with_one_category(df)
```

<div class="output execute_result" execution_count="32">

      columns category_name
    0       B           [x]

</div>

</div>

<div class="cell code" execution_count="33"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}"
id="m2Fz5iqlO9nM" outputId="1cbbf8e0-c640-47bc-ae60-1a16ef866c60">

``` python
tdi.check_col_with_one_category(df,return_type='json')
```

<div class="output execute_result" execution_count="33">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="uR3g6QQIPFRh">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell markdown" id="zal9tBcxPH5B">

**tdi.find_special_char_index(df, return_type='dataframe')
Parameters:
df: pandas Dataframe
return_type(optional):how want to get the output (Default =
'dataframe')**

</div>

<div class="cell markdown" id="BujDuVwXPRrg">

This function will find out for us those indexes which holding the
double spaces and special characters into the dataframe.

</div>

<div class="cell code" execution_count="34"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="WzJTJwX3O9vR" outputId="3f85f568-b4ad-4a2c-a3d2-8fa68a9099e2">

``` python
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['!', 5, '?'], 'C': [1.2, 2.6, '3,2']})
df
```

<div class="output execute_result" execution_count="34">

       A  B    C
    0  1  !  1.2
    1  2  5  2.6
    2  3  ?  3,2

</div>

</div>

<div class="cell code" execution_count="35"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="OhApZcUnENOd" outputId="934cef2f-027e-44b0-f5e8-574664df530a">

``` python
tdi.find_special_char_index(df)
```

<div class="output execute_result" execution_count="35">

      columns has_special_char_at
    0       A                  []
    1       B              [0, 2]
    2       C                 [2]

</div>

</div>

<div class="cell code" execution_count="36"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:53}"
id="BpYx5OUJP6TR" outputId="a4ba4445-0265-4826-a059-b7103b62b763">

``` python
tdi.find_special_char_index(df, return_type='json')
```

<div class="output execute_result" execution_count="36">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="CBfT0D9sP6ho">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell markdown" id="78DYtKBjQFDA">

**tdi.duplicate_columns(df)
Parameters:
df: pandas Dataframe**

</div>

<div class="cell markdown" id="rKojcLDDQXC4">

This function return a list of column names those containg the same
value column name may different but data is same

</div>

<div class="cell code" execution_count="37"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="h3KeKIY6Q1Hn" outputId="e6dd6b1d-eade-4120-ce55-ae9a5bc92896">

``` python
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['!', 5, '?'], 'C': [1, 2, 3]})
df
```

<div class="output execute_result" execution_count="37">

       A  B  C
    0  1  !  1
    1  2  5  2
    2  3  ?  3

</div>

</div>

<div class="cell code" execution_count="38"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="oLt8h-ksEQCf" outputId="93387b3e-d8d1-4df3-8071-4884039a9575">

``` python
l = tdi.duplicate_columns(df)
l
```

<div class="output execute_result" execution_count="38">

    ['A', 'C']

</div>

</div>

<div class="cell markdown" id="ii508Ja0Q87v">

So here 'A' and 'C' columns contain the same data

</div>

<div class="cell markdown" id="_tH4YAE-SIKl">

**tdi.correlated_columns(df, return_type='dataframe')
Parameters:
df: pandas Dataframe
return_type(optional):how want to get the output (Default =
'dataframe')**

</div>

<div class="cell markdown" id="9QYFkYRQSQb-">

This function will return a dataframe or json which will define that
different column but the data is more than 90% correlated

</div>

<div class="cell code" execution_count="40"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}"
id="qTs0jpchFPHD" outputId="e49b0c80-9db3-478d-d2f0-301cb27b9c75">

``` python
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 5, 'b'], 'C': [1, 2, 3]})
df
```

<div class="output execute_result" execution_count="40">

       A  B  C
    0  1  a  1
    1  2  5  2
    2  3  b  3

</div>

</div>

<div class="cell code" execution_count="41"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:167}"
id="zwpXXkFPFAFH" outputId="34fe3c23-24ed-41ea-b0b6-888c1449cd73">

``` python
tdi.correlated_columns(df, return_type='dataframe')
```

<div class="output stream stderr">

    /usr/local/lib/python3.10/dist-packages/TabularDataInvestigation/tdi.py:116: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
      correalated_df = df.corr()

</div>

<div class="output execute_result" execution_count="41">

      columns correlated_columns correlation
    0       A                [C]       [1.0]
    1       C                [A]       [1.0]

</div>

</div>

<div class="cell code" execution_count="42"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:107}"
id="1_5JXsFgFIdg" outputId="cf45f62e-cd6e-4fed-9803-d2a30b4f4f95">

``` python
tdi.correlated_columns(df, return_type='json')
```

<div class="output stream stderr">

    /usr/local/lib/python3.10/dist-packages/TabularDataInvestigation/tdi.py:116: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
      correalated_df = df.corr()

</div>

<div class="output execute_result" execution_count="42">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="AMpvo2RYS92c">

Here return type is optional ('dataframe' or 'json'). Default: dataframe

</div>

<div class="cell code" id="6uyQ5pVcS5VG">

``` python
```

</div>
