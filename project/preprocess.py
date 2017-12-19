#Import modules
import nipype
from os.path import join as opj
import os
import json
from nipype.interfaces.fsl import (BET, ExtractROI, FAST, FLIRT, ImageMaths,
                                   MCFLIRT, SliceTimer, Threshold)
from nipype.interfaces.spm import Smooth
from nipype.interfaces.utility import IdentityInterface, Merge
from nipype.interfaces.io import SelectFiles, DataSink, FreeSurferSource
from nipype.algorithms.rapidart import ArtifactDetect
from nipype.pipeline.engine import Workflow, Node, MapNode
from nipype.interfaces.ants import Registration, ApplyTransforms
from nipype.interfaces.fsl import Info
from nipype.interfaces.freesurfer import FSCommand, MRIConvert, BBRegister
from nipype.interfaces.c3 import C3dAffineTool
from nipype.interfaces.matlab import MatlabCommand

from os.path import join as opj
from nipype.interfaces.spm import Normalize12
from nipype.interfaces.utility import IdentityInterface
from nipype.interfaces.io import SelectFiles, DataSink
from nipype.algorithms.misc import Gunzip
from nipype.pipeline.engine import Workflow, Node, MapNode

from nilearn import image, plotting
import numpy as np
import pylab as plt
import numpy as np

MatlabCommand.set_default_paths('/home/messina/spm12')
MatlabCommand.set_default_matlab_cmd("matlab -nodesktop -nosplash")

# location of template in form of a tissue probability map to normalize to
template = '/home/messina/spm12/tpm/TPM.nii'

basedir = '/home/messina/ada_project/workingdir/PPMI/'

experiment_dir = '/home/messina/ada_project'

#experiment_dir = '/Users/elisabettamessina/Desktop/ADA/ada2017hw/project/ExampleFolder2'
working_dir = 'workingdir'
output_dir = 'output_folder'
input_dir_1st = 'output_folder' 
# defining the subjec list 
# Specify variables

# list of subject identifiers
subject_list = []
for fn in os.listdir(basedir):
    if fn[0]=='3' or fn[0]=='4':
        subject_list.append(fn)
# list of session identifiers
task_list = ['rs']

# Smoothing widths to apply
fwhm = [4, 8]

# TR of functional images
TR = 2.4 

# Isometric resample of functional images to voxel size (in mm)
iso_size = 4

# ExtractROI - skip dummy scans
extract = Node(ExtractROI(t_min=4, t_size=-1),
               output_type='NIFTI',
               name="extract")

# MCFLIRT - motion correction
mcflirt = Node(MCFLIRT(mean_vol=True,
                       save_plots=True,
                       output_type='NIFTI'),
               name="mcflirt")

# SliceTimer - correct for slice wise acquisition
slicetimer = Node(SliceTimer(index_dir=False,
                             interleaved=True,
                             output_type='NIFTI',
                             time_repetition=TR),
                  name="slicetimer")

# Smooth - image smoothing
smooth = Node(Smooth(), name="smooth")
smooth.iterables = ("fwhm", fwhm)

# Gunzip - unzip the structural image
gunzip_struct = Node(Gunzip(), name="gunzip_struct")

# Gunzip - unzip the contrast image
gunzip_con = MapNode(Gunzip(), name="gunzip_con",
                     iterfield=['in_file'])

# Normalize - normalizes functional and structural images to the MNI template
normalize = Node(Normalize12(jobtype='estwrite',
                             tpm=template,
                             write_voxel_sizes=[1, 1, 1]),
                 name="normalize")

# Artifact Detection - determines outliers in functional images
art = Node(ArtifactDetect(norm_threshold=2,
                          zintensity_threshold=3,
                          mask_type='spm_global',
                          parameter_source='FSL',
                          use_differences=[True, False],
                          plot_type='svg'),
           name="art")

# BET - Skullstrip anatomical Image
bet_anat = Node(BET(frac=0.5,
                    robust=True,
                    output_type='NIFTI_GZ'),
                name="bet_anat")

# FAST - Image Segmentation
segmentation = Node(FAST(output_type='NIFTI_GZ'),
                name="segmentation")

# Select WM segmentation file from segmentation output
def get_wm(files):
    return files[-1]

# Threshold - Threshold WM probability image
threshold = Node(Threshold(thresh=0.5,
                           args='-bin',
                           output_type='NIFTI_GZ'),
                name="threshold")

# FLIRT - pre-alignment of functional images to anatomical images
coreg_pre = Node(FLIRT(dof=6, output_type='NIFTI_GZ'),
                 name="coreg_pre")

# FLIRT - coregistration of functional images to anatomical images with BBR
coreg_bbr = Node(FLIRT(dof=6,
                       cost='bbr',
                       schedule=opj(os.getenv('FSLDIR'),
                                    'etc/flirtsch/bbr.sch'),
                       output_type='NIFTI_GZ'),
                 name="coreg_bbr")

# Apply coregistration warp to functional images
applywarp = Node(FLIRT(interp='spline',
                       apply_isoxfm=iso_size,
                       output_type='NIFTI'),
                 name="applywarp")

# Apply coregistration warp to mean file
applywarp_mean = Node(FLIRT(interp='spline',
                            apply_isoxfm=iso_size,
                            output_type='NIFTI_GZ'),
                 name="applywarp_mean")


# Create a coregistration workflow
coregwf = Workflow(name='coregwf')
coregwf.base_dir = opj(experiment_dir, working_dir)

# Connect all components of the coregistration workflow
coregwf.connect([(bet_anat, segmentation, [('out_file', 'in_files')]),
                 (segmentation, threshold, [(('partial_volume_files', get_wm),
                                             'in_file')]),
                 (bet_anat, coreg_pre, [('out_file', 'reference')]),
                 (threshold, coreg_bbr, [('out_file', 'wm_seg')]),
                 (coreg_pre, coreg_bbr, [('out_matrix_file', 'in_matrix_file')]),
                 (coreg_bbr, applywarp, [('out_matrix_file', 'in_matrix_file')]),
                 (bet_anat, applywarp, [('out_file', 'reference')]),
                 (coreg_bbr, applywarp_mean, [('out_matrix_file', 'in_matrix_file')]),
                 (bet_anat, applywarp_mean, [('out_file', 'reference')]),
                 ])

# Infosource - a function free node to iterate over the list of subject names
infosource = Node(IdentityInterface(fields=['subject_id', 'task_name']),
                  name="infosource")
infosource.iterables = [('subject_id', subject_list),
                        ('task_name', task_list)]

# SelectFiles - to grab the data (alternativ to DataGrabber)
anat_file = opj('{subject_id}', 'ep2d_RESTING_STATE', 'anat', 'anat.nii')
func_file = opj('{subject_id}', 'ep2d_RESTING_STATE', 'func',
                'rest.nii')

templates = {'anat': anat_file,
             'func': func_file}
selectfiles = Node(SelectFiles(templates,
                               base_directory= experiment_dir + '/workingdir/PPMI/'),
                   name="selectfiles")

# Datasink - creates output folder for important outputs
datasink = Node(DataSink(base_directory=experiment_dir,
                         container=output_dir),
                name="datasink")

## Use the following DataSink output substitutions
substitutions = [('_subject_id_', ''),
                 ('_task_name_', '/task-'),
                 ('_fwhm_', 'fwhm-'),
                 ('_roi', ''),
                 ('_mcf', ''),
                 ('_st', ''),
                 ('_flirt', ''),
                 ('.nii_mean_reg', '_mean'),
                 ('.nii.par', '.par'),
                 ]
subjFolders = [('fwhm-%s/' % f, 'fwhm-%s_' % f) for f in fwhm]
substitutions.extend(subjFolders)
datasink.inputs.substitutions = substitutions

# Create a preprocessing workflow
preproc = Workflow(name='preproc')
preproc.base_dir = opj(experiment_dir, working_dir)

# Connect all components of the preprocessing workflow
preproc.connect([(infosource, selectfiles, [('subject_id', 'subject_id'),
                                            ('task_name', 'task_name')]),
                 (selectfiles, extract, [('func', 'in_file')]),
                 (extract, mcflirt, [('roi_file', 'in_file')]),
                 (mcflirt, slicetimer, [('out_file', 'in_file')]),

                 (selectfiles, coregwf, [('anat', 'bet_anat.in_file'),
                                         ('anat', 'coreg_bbr.reference')]),
                 (mcflirt, coregwf, [('mean_img', 'coreg_pre.in_file'),
                                     ('mean_img', 'coreg_bbr.in_file'),
                                     ('mean_img', 'applywarp_mean.in_file')]),
                 (slicetimer, coregwf, [('slice_time_corrected_file', 'applywarp.in_file')]),
                 
                 (coregwf, smooth, [('applywarp.out_file', 'in_files')]),

                 (mcflirt, datasink, [('par_file', 'preproc.@par')]),
                 (smooth, datasink, [('smoothed_files', 'preproc.@smooth')]),
                 (coregwf, datasink, [('applywarp_mean.out_file', 'preproc.@mean')]),

                 (coregwf, art, [('applywarp.out_file', 'realigned_files')]),
                 (mcflirt, art, [('par_file', 'realignment_parameters')]),

                 (coregwf, datasink, [('coreg_bbr.out_matrix_file', 'preproc.@mat_file'),
                                      ('bet_anat.out_file', 'preproc.@brain')]),
                 (art, datasink, [('outlier_files', 'preproc.@outlier_files'),
                                  ('plot_files', 'preproc.@plot_files')]),
                 ])


# DEBUG MODE:
preproc.config['execution'] = {'stop_on_first_rerun': 'False',
                                   'hash_method': 'timestamp'}
from nipype import config, logging
config.enable_debug_mode()
logging.update_logging(config)

preproc.run('MultiProc', plugin_args={'n_procs': 4})

 # Gunzip - unzip the structural image
gunzip_struct = Node(Gunzip(), name="gunzip_struct")

# Gunzip - unzip the contrast image
gunzip_con = MapNode(Gunzip(), name="gunzip_con",
                     iterfield=['in_file'])

# Normalize - normalizes functional and structural images to the MNI template
normalize = Node(Normalize12(jobtype='estwrite',
                             tpm=template,
                             write_voxel_sizes=[1, 1, 1]),
                 name="normalize")

# Specify Normalization-Workflow & Connect Nodes
normflow = Workflow(name='normflow')
normflow.base_dir = opj(experiment_dir, working_dir)

# Connect up ANTS normalization components
normflow.connect([(gunzip_struct, normalize, [('out_file', 'image_to_align')]),
                  (gunzip_con, normalize, [('out_file', 'apply_to_files')]),
                  ])

# Infosource - a function free node to iterate over the list of subject names
infosource = Node(IdentityInterface(fields=['subject_id']),
                  name="infosource")
infosource.iterables = [('subject_id', subject_list)]

# SelectFiles - to grab the data (alternativ to DataGrabber)
anat_file = opj(working_dir, 'PPMI', '{subject_id}', 'ep2d_RESTING_STATE', 'anat', 'zipped', 'anat.nii.gz')
con_file = opj(output_dir, 'preproc', '{subject_id}', 'task-rs',
                        'rest_mean.nii.gz')


templates = {'anat': anat_file,
             'con': con_file,
             }
selectfiles = Node(SelectFiles(templates,
                               base_directory=experiment_dir),
                   name="selectfiles")

# Datasink - creates output folder for important outputs
datasink = Node(DataSink(base_directory=experiment_dir,
                         container=output_dir),
                name="datasink")

# Use the following DataSink output substitutions
substitutions = [('_subject_id_', '')]
datasink.inputs.substitutions = substitutions

# Connect SelectFiles and DataSink to the workflow
normflow.connect([(infosource, selectfiles, [('subject_id', 'subject_id')]),
                  (selectfiles, gunzip_struct, [('anat', 'in_file')]),
                  (selectfiles, gunzip_con, [('con', 'in_file')]),
                  (normalize, datasink, [('normalized_files',
                                          'normalized.@files'),
                                         ('normalized_image',
                                          'normalized.@image'),
                                         ('deformation_field',
                                          'normalized.@field'),
                                         ]),
                  ])

# DEBUG MODE:
normflow.config['execution'] = {'stop_on_first_rerun': 'False',
                                   'hash_method': 'timestamp'}
from nipype import config, logging
config.enable_debug_mode()
logging.update_logging(config)

normflow.run('MultiProc', plugin_args={'n_procs': 8})
