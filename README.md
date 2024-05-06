# Active Inference Interaction Modeling for the Project: Enhancing Automated Vehicle Safety Through Testing with Realistic Driver Models  
Safety through Disruption (Safe-D) University Transportation Center (UTC), Office of the Secretary for Research and Technology, U.S. Department of Transportation (USDOT)  
2024-05-06  

## Links to Dataset  
Dataset Archive Link: <https://doi.org/10.15787/VTT1/LWA2VP>  
Dataset GitHub Link: <https://github.com/ran-weii/interactive_inference>  

## Summary of Dataset  
  
Driver process models play a central role in the testing, verification, and development of automated and autonomous vehicle technologies. Prior models developed from control theory and physics-based rules are limited in automated vehicle applications due to their restricted behavioral repertoire. Data-driven machine learning models are more capable than rule-based models but are limited by the need for large training datasets and their lack of interpretability. In this project we developed a novel car following modeling approach using active inference, which has comparable behavioral flexibility to data-driven models while maintaining interpretability. We assessed the proposed model, the Active Inference Driving Agent (AIDA), through a benchmark analysis against several benchmarks. The models were trained and tested on a real-world driving dataset using a consistent process. The testing results showed that the AIDA predicted driving controls significantly better than the rule-based Intelligent Driver Model and had similar accuracy to the data driven neural network models in three out of four evaluations. Subsequent interpretability analyses illustrated that the AIDA's learned distributions were consistent with driver behavior theory and that visualizations of the distributions could be used to directly comprehend the model's decision-making process and correct model errors attributable to limited training data.  

## Table of Contents  
 A. [General Information](#a-general-information)  
 B. [Sharing/Access & Policies Information](#b-sharingaccess--policies-information)  
 C. [Data and Related Files Overview](#c-data-and-related-files-overview)  
 D. [Data-Specific Information for: Active Inference Interaction Modeling for the Project: Enhancing Automated Vehicle Safety Through Testing with Realistic Driver Models](#d-data-specific-information)  
 E. [Update Log](#e-update-log)  

## A. General Information  

**Title of Dataset:**  Active Inference Interaction Modeling for the Project: Enhancing Automated Vehicle Safety Through Testing with Realistic Driver Models  

**Description of the Dataset:** Driver process models play a central role in the testing, verification, and development of automated and autonomous vehicle technologies. Prior models developed from control theory and physics-based rules are limited in automated vehicle applications due to their restricted behavioral repertoire. Data-driven machine learning models are more capable than rule-based models but are limited by the need for large training datasets and their lack of interpretability. In this project we developed a novel car following modeling approach using active inference, which has comparable behavioral flexibility to data-driven models while maintaining interpretability. We assessed the proposed model, the Active Inference Driving Agent (AIDA), through a benchmark analysis against several benchmarks. The models were trained and tested on a real-world driving dataset using a consistent process. The testing results showed that the AIDA predicted driving controls significantly better than the rule-based Intelligent Driver Model and had similar accuracy to the data driven neural network models in three out of four evaluations. Subsequent interpretability analyses illustrated that the AIDA's learned distributions were consistent with driver behavior theory and that visualizations of the distributions could be used to directly comprehend the model's decision-making process and correct model errors attributable to limited training data.  

**Dataset Archive Link:** <https://doi.org/10.15787/VTT1/LWA2VP>  

**Authorship Information:**  

>  *Principal Data Creator or Data Manager Contact Information*  
>  Name: McDonald, Anthony [(0000-0001-7827-8828)](https://orcid.org/0000-0001-7827-8828)  
>  Institution: Texas A&M University [(ROR ID: https://ror.org/01f5ytq51)](https://ror.org/01f5ytq51)  
>  Address: 120 Spence, College Station, TX 77843  
>  Email: <mcdonald@tamu.edu>  

>  *Principal Data Creator or Data Manager Contact Information*   
>  Name: Garcia, Alfredo [(0000-0002-2761-7479)](https://orcid.org/0000-0002-2761-7479)  
>  Scopus Author ID: [56341884100](https://www.scopus.com/authid/detail.uri?authorId=56341884100)  
>  Institution: Texas A&M University [(ROR ID: https://ror.org/01f5ytq51)](https://ror.org/01f5ytq51)  
>  Address: 120 Spence, College Station, TX 77843  
>  Email: <alfredo.garcia@tamu.edu>  

>  *GitHub Repository Owner*  
>  Name: Wei, Ran [(0000-0001-7982-0404)](https://orcid.org/0000-0001-7982-0404)  
>  Institution: Texas A&M University [(ROR ID: https://ror.org/01f5ytq51)](https://ror.org/01f5ytq51)  
>  Address: 120 Spence, College Station, TX 77843   

**Information about funding sources that supported the collection of the data:** This project was funded by the Safety through Disruption (Safe-D) National University Transportation Center, a grant from the U.S. Department of Transportation–Office of the Assistant Secretary for Research and Technology, University Transportation Centers Program.  

## B. Sharing/Access and Policies Information  

**Recommended citation for the data:**  

>  Safety through Disruption (Safe-D) University Transportation Center (UTC) (2023). Active Inference Interaction Modeling for the Project: Enhancing Automated Vehicle Safety Through Testing with Realistic Driver Models. <https://doi.org/10.15787/VTT1/LWA2VP>  

**Licenses/restrictions placed on the data:** This document is disseminated under the sponsorship of the U.S. Department of Transportation in the interest of information exchange. This dataset and its code are free and open access.  

**Was data derived from another source?:** Yes, <https://interaction-dataset.com/>  

This document was created to meet the requirements enumerated in the U.S. Department of Transportation's [Plan to Increase Public Access to the Results of Federally-Funded Scientific Research Version 1.1](https://doi.org/10.21949/1520559) and [Guidelines Suggested by the DOT Public Access website](https://doi.org/10.21949/1503647), in effect and current as of December 03, 2020.  

## C. Data and Related Files Overview  

We use the publicly available INTERACTION dataset. The INTERACTION dataset is collected using drones on fixed road segments in the USA, Germany, and China. The dataset provides a lanelet2 format map and a set of time-indexed trajectories of the positions, velocities, and headings of each vehicle in the scene in the map's coordinate system at a sampling frequency of 10 Hz, and the vehicle's length and width for each road segment.

**Instrument or software-specific information needed to interpret the data:** To best view the data, please open the .CSV files in Notepad++, Excel, or OpenRefine.  

### Setup  
* Environment variables are in [environment.yml](environment.yml). You might run into an OMP error installing numpy, scipy along with pytorch in anaconda. You can fix this by first installing nomkl (see [here](https://stackoverflow.com/questions/53014306/error-15-initializing-libiomp5-dylib-but-found-libiomp5-dylib-already-initial)).
* Download the [INTERACTION dataset](https://interaction-dataset.com/) and perform the preprocessing steps described in [here](./doc/preprocess.md).

### Usage  
To train the active inference and basedline agents, run:
```
python ./scripts/train_agent_recurrent.py
```
You can modify observation features, agent size, learning rate, training epochs by specifying additional arguments. You can use the corresponding ``.sh`` script to edit these arguments. Please see the scripts for detailed arguments.  To train agents in colab, clone the repo to google drive and run the corresponding ``.ipynb`` file. 

To test agents on static dataset, run:
```
python ./scripts/eval_offline.py
```

To test agents in simulator, run:
```
python ./scripts/eval_online.py
```
Description of the simulator can be found [here](https://github.com/ran-weii/interactive_inference/blob/master/doc/simulation.md).     

## D. Data-Specific Documentation  

**Map Documentation:** <https://github.com/ran-weii/interactive_inference/blob/master/doc/map.md>  
**Pre-process Documentation:** <https://github.com/ran-weii/interactive_inference/blob/master/doc/preprocess.md>  
**Simulation Documentation:** <https://github.com/ran-weii/interactive_inference/blob/master/doc/simulation.md>  
**Description of Track Data:** <https://github.com/ran-weii/interactive_inference/blob/master/doc/track_data.md>  
**Dataset Archive Page:** <https://dataverse.vtti.vt.edu/dataset.xhtml?persistentId=doi:10.15787/VTT1/LWA2VP>  

## E. Update Log  

This README file was originally created on 2024-05-06 by Peyton Tvrdy [(0000-0002-9720-4725)](https://orcid.org/0000-0002-9720-4725), Data Curator at the National Transportation Library [(ROR ID: https://ror.org/00snbrd52)](https://ror.org/00snbrd52), <peyton.tvrdy.ctr@dot.gov>  

2024-05-06: Original file created  
