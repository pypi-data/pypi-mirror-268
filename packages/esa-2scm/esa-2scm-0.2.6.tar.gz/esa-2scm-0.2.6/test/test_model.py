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


from esa_2scm import Esa2Scm
import numpy as np

def model_simulation():
    correct_count = 0
    wrong_count = 0
    total_runs = 100
    b_list = []

    for _ in range(total_runs):
        np.random.seed(11)
        N = 10000
        x2 = np.random.random(size=N)
        e1 = np.random.normal(size=N)
        b12 = 1.8
        x1 = b12 * x2 + e1
        b_list.append(b12)
        model = Esa2Scm(x1, x2)
        model.fit('esa', M=5)

        if model.causal_direction == "x2->x1":
            correct_count += 1
        else: wrong_count += 1
        
        mean_estimated_causal_impact_coef = np.mean(b_list)
        
    
    return correct_count, wrong_count, mean_estimated_causal_impact_coef, model


def test_model_simulation():
    correct_count, wrong_count, mean_estimated_causal_impact_coef, model = model_simulation()
    
    assert correct_count == 100
    assert wrong_count == 0
    assert np.round(mean_estimated_causal_impact_coef, 2)  == 1.80
    assert round(model.causal_coef, 1) == 1.8
    assert model.causal_direction == "x2->x1"
    assert round(model.esa2scm_score, 2) == 0.21
    assert round(model.posthoc_score, 2) == 0.22
    assert type(model.x1) == np.ndarray
    assert type(model.x2) == np.ndarray
    assert hasattr(model, "x_hat") == True
    assert len(np.unique(model.z1)) == 5
    assert len(np.unique(model.z2)) == 5
    assert hasattr(model, "corr_x1_to_slsiv") == True
    assert hasattr(model, "corr_x2_to_slsiv") == True
    assert hasattr(model, "summary") == True
    

def test_prior_knowledge():
    N = 10000
    shape, scale = 2., 2.
    np.random.seed(11)
    x2 = np.random.gamma(shape, scale, N)
    e1 = np.random.normal(size=N)
    b12 = 1.8
    x1 = b12 * x2 + e1
    model = Esa2Scm(x1, x2, prior_knowledge="x1->x2")
    model.fit()
    assert model.causal_direction == "x1->x2 (prior knowledge)"
    assert round(model.causal_coef, 1) == 0.5
    assert round(model.posthoc_score, 2) == 0.96
    assert hasattr(model, "summary") == True
    assert hasattr(model, "z1") == False
    assert hasattr(model, "syniv2sls_score") == False
    