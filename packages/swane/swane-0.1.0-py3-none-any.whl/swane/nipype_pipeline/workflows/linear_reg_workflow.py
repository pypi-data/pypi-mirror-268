from nipype.interfaces.fsl import (BET, FLIRT)
from swane.nipype_pipeline.engine.CustomWorkflow import CustomWorkflow
from swane.nipype_pipeline.nodes.CustomDcm2niix import CustomDcm2niix
from swane.nipype_pipeline.nodes.ForceOrient import ForceOrient
from swane.utils.DataInputList import DataInputList
from nipype import Node
from nipype.interfaces.utility import IdentityInterface
from configparser import SectionProxy


def linear_reg_workflow(name: str, dicom_dir: str, config: SectionProxy, base_dir: str = "/", is_volumetric: bool = True) -> CustomWorkflow:
    """
    Transforms input images in a reference space through a linear registration.

    Parameters
    ----------
    name : str
        The workflow name.
    dicom_dir : path
        The file path of the DICOM files.
    config: SectionProxy
        workflow settings.
    base_dir : path, optional
        The base directory path relative to parent workflow. The default is "/".
    is_volumetric : bool, optional
        True if input is 3D. The default is True.

    Input Node Fields
    ----------
    reference : path
        The reference image for the registration.
    output_name : str
        The name for registered file.
    crop : bool
        If True, enables 3D images (neck removal).

    Returns
    -------
    workflow : CustomWorkflow
        The linear registration workflow.
        
    Output Node Fields
    ----------
    registered_file : string
        Output file in T13D reference space.
    out_matrix_file : path
        Linear registration matrix to T13D reference space.

    """
    
    workflow = CustomWorkflow(name=name, base_dir=base_dir)

    # Input Node
    inputnode = Node(
        IdentityInterface(fields=['reference', 'output_name', 'crop']),
        name='inputnode')
    
    # Output Node
    outputnode = Node(
        IdentityInterface(fields=['registered_file', 'out_matrix_file']),
        name='outputnode')

    # NODE 1: Conversion dicom -> nifti
    conversion = Node(CustomDcm2niix(), name='%s_conv' % name)
    conversion.inputs.source_dir = dicom_dir
    conversion.inputs.bids_format = False
    conversion.inputs.out_filename = name
    workflow.connect(inputnode, 'crop', conversion, 'crop')

    # NODE 2: Orienting in radiological convention
    reorient = Node(ForceOrient(), name='%s_reorient' % name)
    workflow.connect(conversion, "converted_files", reorient, "in_file")

    # NODE 3: Scalp removal
    bet = Node(BET(), '%s_BET' % name)
    if config is not None:
        bet.inputs.frac = config.getfloat_safe('bet_thr')
    if config is not None and config.getboolean_safe('bet_bias_correction'):
        bet.inputs.reduce_bias = True
    else:
        bet.inputs.robust = True
    bet.inputs.mask = True
    workflow.connect(reorient, "out_file", bet, "in_file")

    # NODE 4: Linear registration to reference space
    flirt_2_ref = Node(FLIRT(), name='%s_2_ref' % name)
    flirt_2_ref.long_name = "%s to reference space"
    flirt_2_ref.inputs.out_matrix_file = "%s_2_ref.mat" % name

    if is_volumetric:
        flirt_2_ref.inputs.cost = "mutualinfo"
        flirt_2_ref.inputs.searchr_x = [-90, 90]
        flirt_2_ref.inputs.searchr_y = [-90, 90]
        flirt_2_ref.inputs.searchr_z = [-90, 90]
        flirt_2_ref.inputs.dof = 6
        flirt_2_ref.inputs.interp = "trilinear"
        
    workflow.connect(bet, "out_file", flirt_2_ref, "in_file")
    workflow.connect(inputnode, "output_name", flirt_2_ref, "out_file")
    workflow.connect(inputnode, "reference", flirt_2_ref, "reference")

    workflow.connect(flirt_2_ref, "out_file", outputnode, "registered_file")
    workflow.connect(flirt_2_ref, "out_matrix_file", outputnode, "out_matrix_file")
    
    return workflow
