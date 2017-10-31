# Data Against Diseases (DAD)
![Alt Text](https://github.com/sharbatc/ada2017hw/blob/master/project/mri.gif)
# Abstract

As average human life span has been increasing in the last few years, the threat of neurodegenerative diseases loom large. It has now become a major health problem in the world with annual costs in the USA associated with neurological diseases are around 800 billion dollars, 100 billion more than the US military budget, as mentioned [here](#References).

The causes for neurodegenerative diseases are mostly unknown but their prevalence is on a steep rise all over the world and people are getting affected earlier than ever. One major disease that is prevalent throughout the world is Parkinson's disease. Parkinson’s disease is the second most common neurodegenerative disease after Alzheimer’s. It’s most obvious symptoms include shaking, rigidity and difficulty with walking. There is currently no cure for Parkinson’s but there are ways of keeping its symptoms down and delaying its progression, for example with deep brain stimulation. These methods are most effective when patients begin treatment as early as possible and therefore powerful diagnostic methods are essential. This project aims to help in diagnosis of neurodegenerative diseases in general and Parkinson's Disease in particular. The method could be easily reproduced by clinics in various places around the world and can also be applied for other diseases. Neuroscience research can be progressed in this way. 

<a name="References"></a> 
### References

* Gooch, Clifton L., Etienne Pracht, and Amy R. Borenstein. ["The burden of neurological disease in the United States: a summary report and call to action."](https://www.ncbi.nlm.nih.gov/pubmed/28198092) Annals of neurology 81.4 (2017): 479-484.

# Research questions
* Is it possible to detect and visualise the network connections that are affected by Parkinson'a disease?
* Can we identify biomarkers of Parkinson disease progression?

# Dataset
The [Parkinson's Progression Markers Initiative (PPMI) dataset](http://www.ppmi-info.org/) includes different types of biological data available to the scientific community, included advanced imaging data such as rs-fMRI and anatomical imaging. From the PPMI website it is possible to download the data for each type of imaging already divided in folders corresponding to each patient. The data is anonymised. In particular we are interested to access to anatomical and resting-state-fMRI data. It is necessary to apply for accessing the data. Since we have already been using it, we have already the access to the data, but we would make a new access request with a new proposed analysis specific to this project.
The processing pipeline could be applied, for example following the processing stream proposed by the [openfMRI project](https://openfmri.org/data-processing-stream/  https://github.com/poldrack/openfmri)

The data consists of folders containing DICOM files corresponding to the resting fMRI for both control and Parkinson's Disease patients. 

# A list of internal milestones up until project milestone 2
* The preprocessing includes some steps such as the conversion from DICOM to nifti format, the realignment of fMRI data, co-registeration to anatomical image, normalisation to the standard MNI space, extraction of time courses and computation of the connection matrix.
* The final output of the processing is a connectivity matrix (can be seen as an undirected graph) where each element corresponds to the correlation between the activity of brain regions (the regions depends on the parcellation scheme could be either based on anatomy of the brain or computed through ICA).
* Thinking of the machine learning methods that can be applied to infer about the importance of areas in the brain.

# Questions for TAs
* Is there a way to expand the dataset because we probably have less control subjects vis à vis the number of patients.
