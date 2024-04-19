from typing import Union, Optional, Dict, List, Any
from quickstats import ConfigScheme, ConfigComponent
from quickstats.core.constraints import ChoiceConstraint

class SampleConfig(ConfigScheme):
    
    sample_dir : ConfigComponent(str, default="./",
                                 description="directory in which the input samples are located")
    
    sample_subdir : ConfigComponent(Dict[str, str], default_factory=dict,
                                    description="a dictionary mapping the sample type to the sub-directory "
                                                "in which the input samples are located; examples of sample "
                                                "type are the mc campaigns and data year for mc and data samples "
                                                "respectively")

    samples : ConfigComponent(Dict[str, Dict[str, Union[str , List[str]]]], default_factory=dict,
                              description="A map from the sample name to the sample path in the form "
                                           "{<sample_type>: <path> or <list_of_paths>}; "
                                           "if path is given by an absolute path, the absolute path is used, "
                                           "otherwise the path {sample_dir}/{sample_subdir}/{path} is used")

    merge_samples: ConfigComponent(Dict[str, List[str]], default_factory=dict,
                                   description="merge the given list of samples into a sample with a given name in "
                                               "the form {<merged_sample_name>: <list_of_samples_to_be_merged>}")

    systematics: ConfigComponent(Dict[str, List[str]], default_factory=dict,
                                 description="A map to the list systematic names in the form "
                                             "<syst_theme>: [<syst_name>]")

    systematic_samples: ConfigComponent(Dict[str, Dict[str, Dict[str, Union[str , List[str]]]]], default_factory=dict,
                                        description="A map to the systematic sample path in the form "
                                                    "<syst_theme>: {<sample_name>: {<sample_type>: <path> or <list_or_paths>}}}; "
                                                    "if path is given by an absolute path, the absolute path is used, "
                                                    "otherwise the path {sample_dir}/{sample_subdir}/{path} is used")

class AnalysisPathConfig(ConfigScheme):
    
    ntuples : ConfigComponent(str, default="./ntuples",
                              description="path to analysis data in root format as precursor to analysis "
                                           "data arrays")
    arrays : ConfigComponent(str, default="./arrays",
                             description="path to analysis data in csv/h5 format used for "
                                          "model training and statistical analysis")
    outputs : ConfigComponent(str, default="./outputs",
                              description="path to analysis outputs")
    models : ConfigComponent(str, default="./models",
                             description="path to machine learning models")
    dummy : ConfigComponent(str, pattern="*",
                            description="any named path")

class AnalysisSamplesConfig(ConfigScheme):
    
    all : ConfigComponent(List[str], default_factory=list,
                          description="list of all analysis samples")
    extra : ConfigComponent(List[str], default_factory=list,
                            description="list of additional analysis samples that exist only "
                                        "in the form of data arrays (i.e. not ntuples)")
    dummy : ConfigComponent(List[str], pattern="*",
                            description="list of analysis samples belonging to a group with the given name")

class AnalysisVariablesConfig(ConfigScheme):
    
    all : ConfigComponent(List[str], default_factory=list,
                          description="list of all input variables")
    dummy : ConfigComponent(List[str], pattern="*",
                            description="list of input variables belonging to a group with the given name")

class AnalysisNamesConfig(ConfigScheme):

    tree_name : ConfigComponent(str, default="output",
                                description="tree name of ntuples used in the analysis")
    
    event_number : ConfigComponent(str, default="event_number",
                                   description="variable name that describes the event number of an event")

    dummy : ConfigComponent(str, pattern="*",
                            description="name of any key object in the analysis")

class AnalysisObservableConfig(ConfigScheme):

    name : ConfigComponent(str, required=True,
                           description="name of discriminant variable")
    eval_expr : ConfigComponent(Optional[str], default=None,
                                description="expression to evaluate to the discriminant from existing input variables")
    bin_range : ConfigComponent(List[Union[float, int]], required=True,
                                description="bin range")
    blind_range : ConfigComponent(Optional[List[Union[float, int]]], default=None,
                                  description="blind range")
    n_bins : ConfigComponent(int, required=True,
                             description="number of bins")

class AnalysisTrainingDatasetSpecItemConfig(ConfigScheme):

    selection : ConfigComponent(str, default="1",
                                description='selection applied to obtain the given dataset')

    variables : ConfigComponent(List[str], default_factory=list,
                                description="list of variables that should be loaded on top of the "
                                "training variables to perform the dataset selection")
    
    effective_weight : ConfigComponent(Union[float, int], default=1.,
                                       description="effective weight of the dataset with respect "
                                                   "to the inclusive data")
    
class AnalysisTrainingDatasetSpecConfig(ConfigScheme):

    dummy : ConfigComponent(AnalysisTrainingDatasetSpecItemConfig, pattern = "*")
    
class AnalysisTrainingDatasetConfig(ConfigScheme):

    specification : ConfigComponent(AnalysisTrainingDatasetSpecConfig)

    split_method : ConfigComponent(str, default="kfold",
                                   description="how to split the dataset for training; custom = use the "
                                               "datasets defined in `specification`; kfold = split the "
                                               "full dataset (or a dataset in `specification`) into k folds "
                                               "; index = select data from a given set of indices (per-sample) "
                                               "which can be the entry number or a column number;"
                                               " manual = use a custom function to split data;",
                                   constraints=[ChoiceConstraint('custom', 'kfold', 'index', 'manual')])
    
    split_options : ConfigComponent(Dict, default_factory=dict,
                                    description="option specific to a given split method")
    
class AnalysisTrainingSampleTranformationConfig(ConfigScheme):
    
    normalize_weight : ConfigComponent(bool, default=False,
                                       description="whether to normalize the event weight in each sample")

class AnalysisTrainingDatasetTranformationConfig(ConfigScheme):
    
    scale_weight_by_mean : ConfigComponent(bool, default=False,
                                           description="whether to rescale the event weight by the mean in"
                                                       " the train/val/test datasets after samples are"
                                                       " merged to the corresponding classes")

    negative_weight_mode : ConfigComponent(int, default=0,
                                           description="how to treat negative weights: 0 = no action performed; "
                                                       "1 = set weight to 0; 2 = set weight to absolute value",
                                           constraints=[ChoiceConstraint(0, 1, 2)])
    
    random_state : ConfigComponent(Optional[int], default=-1,
                                   description="random state for shuffling data; if negative, "
                                               "no shuffling will be made; if None, the global "
                                               "random state instance from numpy.random will "
                                               "be used (so every shuffle will give a different result)")
    
class AnalysisTrainingConfig(ConfigScheme):

    datasets : ConfigComponent(AnalysisTrainingDatasetConfig)

    sample_transformation : ConfigComponent(AnalysisTrainingSampleTranformationConfig)

    dataset_transformation : ConfigComponent(AnalysisTrainingDatasetTranformationConfig)
    

class AnalysisCategorizationBoundaryScanConfig(ConfigScheme):
    
    selection : ConfigComponent(Dict[str, str], default_factory=dict,
                                description="(per-sample) selection applied when performing boundary scan")
    
    datasets : ConfigComponent(Optional[List[str]], default_factory=list,
                               description="dataset(s) that should take non-zero weight when peroforming "
                                           "boundary scan; this is typically the test dataset; if empty, "
                                           "the full dataset is used")
    
    adaptive_dataset : ConfigComponent(bool, default=True,
                                       description="use full dataset for samples not used in training and "
                                                   "the restricted dataset for samples used in training")

class AnalysisCategorizationEvaluationConfig(ConfigScheme):

    datasets : ConfigComponent(Optional[List[str]], default_factory=list,
                               description="dataset(s) that should take the total weight when saving "
                                           "the categorized outputs; this is typically the test dataset; "
                                           "if empty, the full dataset is used")
    
    adaptive_dataset : ConfigComponent(bool, default=True,
                                       description="use full dataset for samples not used in training and "
                                                   "the specified dataset for samples used in training")

class AnalysisDataStorageArrayConfig(ConfigScheme):
    
    storage_format: ConfigComponent(str, default="csv",
                                    description="file format used to store the data",
                                    constraints=[ChoiceConstraint('csv', 'h5')])

    storage_options: ConfigComponent(Dict, default_factory=dict,
                                     description="storage options specific to a given storage format")

class AnalysisDataStorageConfig(ConfigScheme):

    analysis_data_arrays : ConfigComponent(AnalysisDataStorageArrayConfig)

class AnalysisCategorizationConfig(ConfigScheme):

    boundary_scan : ConfigComponent(AnalysisCategorizationBoundaryScanConfig)

    evaluation: ConfigComponent(AnalysisCategorizationEvaluationConfig)

    save_variables : ConfigComponent(List[str], default_factory=list,
                                     description="additional variables to save in the categorized outputs")

class AnalysisChannelItemCountingSignificanceConfig(ConfigScheme):
    
    signal : ConfigComponent(List[str], default_factory=list,
                             description='the samples designated as signals when evaluating the counting '
                             'significance in score boundary scans (group label is allowed) '
                             'example: "channel": {"LowPtRegion": {"counting_significance": '
                             '{"signal": ["ggF", "VBF"]}}}')
    
    background : ConfigComponent(List[str], default_factory=list,
                                 description='the samples designated as backgrounds when evaluating the '
                                 'counting significance in score boundary scans (group label is allowed); '
                                 'example: "channel": {"LowPtRegion": {"counting_significance": '
                                 '{"background": ["yj", "yy"]}}}')
    
    n_bins : ConfigComponent(int, required=True,
                             description='Number of bins used in score boundary scan; notice the '
                             'scan time and memory consumption grow exponentially with '
                             'the number of bins used')
    
    n_boundaries : ConfigComponent(int, required=True,
                                   description='Number of score boundaries to apply; you will get '
                                   '(n_boundaries + 1) categories for the given channel  if all '
                                   'categories are kept')
    
    min_yield : ConfigComponent(Dict[str, Union[float, int]], default_factory=dict,
                                description='Minimum yield of specific samples required in all score regions; '
                                'example: "channel": {"LowPtRegion": {"counting_significance": '
                                '{"min_yield": {"yy": 2}}}}')

class AnalysisChannelItemConfig(ConfigScheme):

    selection : ConfigComponent(Optional[str], default=None,
                                description='selection applied on the input variables to isolate the phase '
                                            'space for the given channel; example: '
                                            '"channel": {"LowPtRegion": {"selection": "jet_pt < 125"}}')
    
    selection_variables : ConfigComponent(Optional[List[str]], default=None,
                                          description="variables used for applying the channel selection")
    
    kinematic_region : ConfigComponent(Optional[str], default=None,
                                       description="kinematic region corresponding to the given channel")
    
    train_samples : ConfigComponent(List[str], default_factory=list,
                                    description='training samples used for the given channel (group label is allowed); '
                                    'example: "channel": {"LowPtRegion": {"train_samples": ["signal", "yj", "yy"]}}')
    
    test_samples : ConfigComponent(List[str], default_factory=list,
                                   description='test samples used for the given channel (group label is allowed); '
                                   'categorized outputs will be produced for these samples; example: '
                                   '"channel": {"LowPtRegion": {"test_samples": ["all"]}}')
    
    train_variables : ConfigComponent(List[str], default_factory=list,
                                      description='training variables used for the given channel (group label is allowed); '
                                      'example: "channel": {"LowPtRegion": {"train_variables": ["jets", "pt_H", "m_H"]}}')
    
    class_labels : ConfigComponent(Dict[str, List[str]],
                                   description='a dictionary that maps the class label used in training '
                                   'to the corresponding samples; example: "channel": {"LowPtRegion": '
                                   '{"class_labels": {"0": ["yj", "yy"], "1": ["signal"]}}}')
    
    hyperparameters : ConfigComponent(Dict[str, Any], default_factory=dict,
                                      description='a dictionary specifying the hyperparameters used in the training; '
                                      'example: "channel": {"LowPtRegion": {"hyperparameters": '
                                      '{"learning_rate": 0.01, "batchsize": 100}}}')
    
    SF : ConfigComponent(Dict[str, Union[float, int]], default_factory=dict,
                         description='a dictionary that maps the scale factor applied to the weight '
                         'of a sample used in the training; example: "channel": {"LowPtRegion": {"SF": '
                         '{"ggF": 100, "VBF": 50}}}')
    
    counting_significance : ConfigComponent(AnalysisChannelItemCountingSignificanceConfig)

    exclude_categories : ConfigComponent(List[List[int]], default_factory=list,
                                         description='Remove specific categories from the analysis by their '
                                                     'category index; [0] is the first bin of a 1D (binary '
                                                     'class) boundary scan, [0, 0] is the first bin of a 2D '
                                                     '(multiclass, e.g. [score_signal_1, score_signal_2]) '
                                                     'boundary scan; example: "channel": { "LowPtRegion": '
                                                     '{"exclude_categories": [[0]]}}')
    
class AnalysisChannelConfig(ConfigScheme):
    
    dummy : ConfigComponent(AnalysisChannelItemConfig, pattern = "*")
    
class AnalysisConfig(ConfigScheme):
    
    paths : ConfigComponent(AnalysisPathConfig)

    samples : ConfigComponent(AnalysisSamplesConfig)
    
    kinematic_regions : ConfigComponent(Optional[List[str]], default=None,
                                        description="kinematic regions of the analysis; if defined, input "
                                                    "datasets are assumed to be split according to these "
                                                    "regions; these regions typically correpond to the "
                                                    "relevant analysis channels")
    
    variables : ConfigComponent(AnalysisVariablesConfig)

    names : ConfigComponent(AnalysisNamesConfig)

    observable : ConfigComponent(AnalysisObservableConfig)

    training : ConfigComponent(AnalysisTrainingConfig)

    categorization : ConfigComponent(AnalysisCategorizationConfig)

    data_storage : ConfigComponent(AnalysisDataStorageConfig)

    channels : ConfigComponent(AnalysisChannelConfig)


class SystematicEvalConfig(ConfigScheme):

    observable : ConfigComponent(str, required=True,
                                 description="Branch name of the observable in the root file")

    weight : ConfigComponent(Optional[str], default=None,
                             description="Branch name of the event weight in the root file")
    
    index : ConfigComponent(Union[str , List[str]], required=True,
                            description="Branch name(s) used to index an event in the root file "
                                        "(e.g. event number, run number)")
    
    category_selection: ConfigComponent(Dict[str, str], required=True,
                                        description='A map from the category to the corresponding selection'
                                        'criteria; example: "category_selection": {"cat1": "cat_index == 1", '
                                        '"cat2": "cat_index==2"}')

    systematics : ConfigComponent(Dict[str, List[str]], default_factory=dict,
                                  description="A map to the list systematic names in the form "
                                  "<syst_theme>: [<syst_name>]")
    
    samples: ConfigComponent(List[str], default_factory=list,
                             description="List of samples to evaluate the systematics")
    
    prune_significative : ConfigComponent(bool, default=True,
                                          description="Whether to prune non-significative systematics")
    
    prune_threshold : ConfigComponent(Union[float, int], default=0,
                                      description="Magnitude of systematic below which should be pruned")
    
    n_toys : ConfigComponent(int, default=100,
                             description="Number of bootstrap toys to use when evaluating shape systematics")
    
    norm_syst_eval_method : ConfigComponent(str, default="analytic",
                                            description="Method by which normalization systematics should be evaluated")
    
    shape_syst_eval_method : ConfigComponent(str, default="bootstrap",
                                             description="Method by which shape systematic should be evaluated")
    
    shape_estimator : ConfigComponent(str, default="mean_IQR",
                                      description="How the shape parameters (position, spread) should be estimated")
    
    shape_syst_eval_options : ConfigComponent(dict, default_factory=dict,
                                              description="Options passed to the shape systematics evaluator")
    
    norm_syst_eval_options : ConfigComponent(dict, default_factory=dict,
                                             description="Options passed to the normalization systematics evaluator")
    
    shape_estimator_options : ConfigComponent(dict, default_factory=dict,
                                               description="Options passed to the shape estimator")
