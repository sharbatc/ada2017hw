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
The processing pipeline could be applied, for example following the processing stream proposed by the [openfMRI project](https://openfmri.org/data-processing-stream/) and also [here](https://github.com/poldrack/openfmri)

The data consists of folders containing DICOM files corresponding to the resting fMRI for both control and Parkinson's Disease patients. There are around 170 fMRI images for patients and 20 for controls.

The project is inspired by one of the member's major research interest, gained from experience which comes from the [Medical Image Processing lab](https://miplab.epfl.ch/) at EPFL.

# A list of internal milestones up until project milestone 2
* Preprocessing: conversion from DICOM to nIfTi format, realignment of fMRI data, co-registeration to anatomical image, normalisation to the standard MNI space, smoothing, extraction of time courses (the values of each voxel over time) based on a parcellation scheme (either based on the anatomy of the brain or computed through ICA).
* Construction of a connectivity matrix by computing the correlation coefficients between time courses.
The connectivity matrix can be seen as an undirected graph where nodes correspond to brain regions and edges to functional connections, that are the correlations between activities of brain regions.
* Thinking of the machine learning methods that can be applied to infer about the importance of connections between areas in the brain in order to find meaningful biomarkers that can predict the disease.

# Questions for TAs
* Is there a way to solve the problem of unbalanced dataset because we have less control subjects vis à vis the number of patients?
* Can we use some cluster to work with the data as it is quite heavy to work with our computers?

# Data collection and description (Milestone 2)
For this first milestone, the following tasks were completed:
* File format conversion for all the images
* Organization of the data in the standard BIDS (Brain Imaging Data Structure)
* Examination of converted data and metadata in a python notebook (M2-data\_inspection)
* Building a preprocessing pipeline in a python notebook (M2-preprocessing) and run it on an example subject.

During the format conversion, some images were duplicated and some others were not converted at all.
Among the subjects that were correctly converted in the new format, 17% belong to the control group.
We are still considering the idea of trying to enrich the control data with external subjects, but for the moment we prefer to keep working on the data we have and decide once we will know the performance of our classification.

Building a preprocessing pipeline in Python was not trivial and required more time than expected.
At the moment, it is working on the example subject but the normalization step has still to be added.
The workflow built with the Nypipe library allow us to easily extend the preprocessing to all the subjects by adding their names to the subject list.

The next question is: once the time courses are extracted, how are we going to process them?

We want to construct a connectivity matrix by computing the correlation among each voxel signal or the average signal for a group of voxels. The first case results in a very big matrix. If we group the voxels we could rely on existing brain parcellations or build our own parcels through clustering.
Once the connectivity matrix has been computed, we will try different classification algorithms. For example, we plan to use SVMs with a suitable kernel to allow for proper classification.

Furthermore, we would like to try a second approach based on Convolutional Neural Networks of the time courses. We believe that the [architecture of the CNN](http://cs231n.github.io/convolutional-networks/) is going to be useful for understanding the images and trying to classify them. The neural inspired architecture is suitable for running on the dataset for fMRI images. We aim to find out features which might serve as markers for future research.

# Milestone 3
