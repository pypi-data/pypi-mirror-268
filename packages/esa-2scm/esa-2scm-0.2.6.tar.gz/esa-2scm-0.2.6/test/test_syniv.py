"""
The esa-2scm package is an implementation of the ESA-2SCM algorithm (Sanghoon Lee, 2024)
For documentation and algorithm/methodology details, please refer to my original article: http://www.snbperi.org/article/230

Should you use this package, please cite my article as follows:
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>


   Copyright 2024 Sanghoon Lee (DSsoli). All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import warnings
import numpy as np
from esa_2scm.syniv import SynIV


X_0Var = [1,1,1]
X_M2 = [1,1,2,3]
X_M3 = [1,1,2,3,4,5]


def capture_warning(func, *args, **kwargs):
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        func(*args, **kwargs)
    
    if w:
        warning_message = str(w[-1].message)
        if len(w) > 1:
            warning_message = str(w[-2].message) + " " + warning_message
            
        return warning_message
    
    else:
        return "no warnings captured"


def get_res(test_sample):
    warnings.filterwarnings("ignore")
    esa_res = SynIV.esa(test_sample, M=5)
    rank_res = SynIV.dense_rank(test_sample)
    split_res = SynIV.m_split(test_sample, strategy="auto")
    
    return esa_res, rank_res, split_res


def get_warnings(test_sample):
    esa_warn = capture_warning(SynIV.esa, test_sample, M=5)
    rank_warn = capture_warning(SynIV.dense_rank, test_sample)
    split_warn = capture_warning(SynIV.m_split, test_sample, strategy='auto')
    
    return esa_warn, rank_warn, split_warn


def test_res_0var():
    esa_res, rank_res, split_res = get_res(X_0Var)
    assert np.array_equal(esa_res, np.array([1,1,1]))
    assert np.array_equal(rank_res, np.array([1,1,1]))
    assert np.array_equal(split_res, np.array([1,1,1]))


def test_warnings_0var():
    esa_warn, rank_warn, split_warn = get_warnings(X_0Var)
    assert "100.00%" in esa_warn
    assert "20.00%" in esa_warn
    assert "0 variance for given sample" in esa_warn
    assert "0 variance for given sample" in rank_warn
    assert "0 variance for given sample" in split_warn


def test_res_M2():
    esa_res, rank_res, split_res = get_res(X_M2)
    assert np.array_equal(esa_res, np.array([1,1,2,2]))
    assert np.array_equal(rank_res, np.array([1,1,2,3]))
    assert np.array_equal(split_res, np.array([-1,-1,1,1]))


def test_warnings_M2():
    esa_warn, rank_warn, split_warn = get_warnings(X_M2)
    assert "50.00%" in esa_warn
    assert "20.00%" in esa_warn
    assert "no warnings captured" in rank_warn
    assert "no warnings captured" in split_warn


def test_res_M3():
    esa_res, rank_res, split_res = get_res(X_M3)
    assert np.array_equal(esa_res, np.array([1,1,2,2,3,3]))
    assert np.array_equal(rank_res, np.array([1,1,2,3,4,5]))
    assert np.array_equal(split_res, np.array([-1,-1,-1,1,1,1]))


def test_warnings_M3():
    esa_warn, rank_warn, split_warn = get_warnings(X_M3)
    assert "33.33%" in esa_warn
    assert "20.00%" in esa_warn
    assert "no warnings captured" in rank_warn
    assert "no warnings captured" in split_warn
