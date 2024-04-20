# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from enum import Enum


class DomainObjectsEnum(Enum):
    """The DomainObjectsEnum defines the supported domain objects"""

    Checkshots = "checkshots"

    GlobalLogContinuous = "global_continuous_log"
    GlobalLogDiscrete = "global_discrete_log"

    Grid = "grid"
    GridContinuousProperty = "grid_continuous_property"
    GridDiscreteProperty = "grid_discrete_property"
    GridZone = "grid_zone"
    # GridSegment = "grid_segment"

    HorizonInterpretation = "horizon_interpretation"
    HorizonInterpretation3D = "horizon_interpretation_3d"
    HorizonInterpretation3DProperty = "horizon_interpretation_3d_property"

    Investigation = "investigation"

    ObservedDataset = "observed_dataset"
    ObservedDatasetForWell = "observed_dataset_for_well"
    ObservedData = "observed_data"

    PointSet = "pointset"

    PolylineSet = "polylineset"

    Seismic2D = "seismic_2d"
    SeismicLine = "seismic_2d"
    Seismic3D = "seismic_3d"
    SeismicCube = "seismic_3d"

    Surface = "surface"
    SurfaceContinuousProperty = "surface_continuous_property"
    SurfaceContinuousAttribute = "surface_continuous_property"
    SurfaceDiscreteProperty = "surface_discrete_property"
    SurfaceDiscreteAttribute = "surface_discrete_property"

    TemplateContinuous = "template_continuous"
    TemplateDiscrete = "template_discrete"
    
    Wavelet = "wavelet"

    WellsFolder = "wells_folder"

    Well = "well"
    WellContinuousLog = "well_continuous_log"
    WellDiscreteLog = "well_discrete_log"

    WellMarkerCollection = "well_marker_collection"
    WellMarkerContinuousProperty = "well_marker_continuous_property"
    WellMarkerDiscreteProperty = "well_marker_discrete_property"

    WellSurvey = "well_survey_xy_z;well_survey_xy_tvd;well_survey_dx_dy_tvd;well_survey_md_inc_azi;well_survey_explicit"
    WellSurvey_XY_Z = "well_survey_xy_z"
    WellSurvey_XY_TVD = "well_survey_xy_tvd"
    WellSurvey_Dx_Dy_TVD = "well_survey_dx_dy_tvd"
    WellSurvey_MD_Inc_Azi = "well_survey_md_inc_azi"
    WellSurvey_Explicit = "well_survey_explicit"
    
    WellPerforation = "well_perforation"
    WellCasing = "well_casing"
    WellCompletion = "well_completion"


