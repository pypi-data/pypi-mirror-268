
# Changelog

Picsellia SDK Python is a library that allows users to connect to Picsellia backend.

All notable changes to this project will be documented in this file.

## [6.14.1] - 2023-04-16

### Added
- `Datalake.list_data()` can be called with ids to fetch data from their ids.

### Fixed
- When listing data and assets, filtering with tags and filenames was not working
- Downloadable objects such as Data, Asset and Artifact, were syncing before downloading, we don't want to do that anymore

### Minor fixes
- Type hint problem on AnnotationCampaign
- Documentation on AnnotationCampaign
- Tests on AnnotationCampaign

## [6.14.0] - 2023-03-19

### Added
- `DatasetVersion.create_campaign()` can be used to create an AnnotationCampaign.
- `AnnotationCampaign.add_step()` can be used to add a step to an AnnotationCampaign.
- `AnnotationCampaign.launch()` can be used to add assignments to all assets on this campaign of your DatasetVersion.
- `AnnotationCampaign.update()` can be used to update an AnnotationCampaign.
- `DatasetVersion.get_campaign()` can be used to retrieve the AnnotationCampaign of this DatasetVersion.
- `DatasetVersion.export_annotation_file()` can be called with parameter `use_id=True`. Generated files will use asset id insted of filename.
- `Datalake.import_bucket_objects()` can be used to import bucket objects of your S3 that are not yet on the platform.

### Fixed
- Calling `MultiAsset.as_multidata()` with more than 10k assets was bugged
- Some dependencies were fixed on pyproject.toml, such as pyyaml, beartype and orjson. Python 3.11 and Python 3.12 can now be used with the sdk


## [6.13.0] - 2023-02-26

### Added
- `Datalake.upload_data()` can now handle unreadable images (like hdf5) and video ! By default, it will wait for data to be full processed by our services
- `Datalake.create_projection(data)` can be used to create a projection on a data : you have to give a name for this projection, it will be of type CUSTOM.
- `DatasetVersion.export_annotation_file()` can be called with boolean parameter `export_video` to only export video in annotation file

### Fixed
- Default content type assigned to data we cannot read mime type is now application/octet-stream



## [6.12.0] - 2023-01-17

### Added
- `Data`, `MultiData`, `Asset`, `MultiAsset`  can be downloaded with `download(use_id=True)` to use id as filename. Extension of base filename will be used.
- `DatasetVersion.build_coco_file_locally()` can now be called with parameter `use_id=True` to build a coco file with `file_name` keys as `<id>.<extension>`
- When initializing a Client, you can pass parameter `session` with your own requests.Session object, that will be used on each request done by the sdk. It allows configuring a proxy or custom headers.

## [6.11.0] - 2023-01-10
Happy new year everyone !
Some minor features and fixes in this version

### Added
- `Data.update_metadata()` can be called to update metadata of a data.
- `DatasetVersion.load_annotations()` can now be called with parameter `assets` to build a json coco file with only given assets.

### Fixed
- When downloading a file, there was a race condition when creating parent directories of downloaded file.
- Storing an artifact with `do_zip=True` was not creating expected archive name when a dot was present in filename.
- On upload, large file discriminant is now 25MiB and not 5MiB

### Changed
- Major changes in docstrings, a lot of fixes!

## [6.10.3] - 2023-09-22

### Fixed
- PredictionFormat will not raise an exception if one of its list is empty. `Deployment.monitor()` can now be called with empty predictions.

## [6.10.2] - 2023-09-06

### Fixed
- `Deployment.predict_bytes()` needs parameter `filename` to work. It was sending prediction with filename `media`.

## [6.10.1] - 2023-08-31

### Added
- `DatasetVersion.build_coco_file_locally()` now adds area of bounding boxes on generated files for Object Detection.

## [6.10.0] - 2023-08-21
Some deprecation on privacy object creation, it is not possible to create a public dataset, project or model from the sdk anymore.
Attach dataset version to Feedback Loop and Continuous Training settings of your deployments.

### Added
- `Deployment.attach_dataset_to_feedback_loop()` can now be called to attach a dataset to Feedback Loop settings of your deployment. Attached datasets can be filled with reviewed prediction from your deployment.
- `Deployment.detach_dataset_from_feedback_loop()` allows detaching dataset from Feedback Loop.
- `Deployment.list_feedback_loop_datasets()` will list attached datasets of your Feedback Loop.
- `Deployment.attach_dataset_to_continuous_training()` can now be called to attach a dataset to Continuous Training settings of your deployment. Attached datasets will be added to your experiment created when Continuous Training is triggered.
- `Deployment.detach_dataset_from_continuous_training()` allows detaching dataset from Continuous Training.

### Deprecated
- Parameter `dataset_version` of `Deployment.setup_feedback_loop()`
- Parameter `dataset_version` and `model_version` of `Deployment.setup_continuous_training()`
- Parameter `private` of `Client.create_model()`
- Parameter `private` of `Model.update()`
- Parameter `private` of `Client.create_project()`
- Parameter `private` of `Project.update()`
- Parameter `private` of `Client.create_dataset()`
- Parameter `private` of `Dataset.update()`

## [6.9.0] - 2023-07-10

### Added
- `Datalake.upload()` can now be called with parameter `fill_metadata`. On upload, set this parameter to True to read exif metadata flags and push metadata to Picsellia. By default, `fill_metadata` is False.
- `Client.get_datalake()` can now be called with parameter `id` or `name` to retrieve the Datalake you want. If nothing is given, this method will retrieve your default datalake.
- `Deployment.predict_bytes()` can now be called if you want to send image as bytes on Serving service
- `ModelVersion.update()` and `Model.create_version()` can now be called with `docker_tag` parameter


## [6.8.0] - 2023-06-12

### Added
- `Datalake.upload_data()` now accept parameter `metadata` which is a dict (or a list of dict if there are multiple filepaths) matching common metadata allowed by Picsellia.
- `DatasetVersion.fork()` can now be called with parameters `with_annotations` and `with_labels` as web application
- `DatasetVersion.export_annotation_file()` can now be called with `AnnotationFileType.YOLO` to retrieve a zip with yolo files
- `Dataset.create_model()` and `DatasetVersion.update()` have parameter `description` to update description of a ModelVersion


### Fixed
- When adding evaluation, allow empty list to be sent as a list of shape

## [6.7.1] - 2023-05-15
Some changes on `monitor()` following an update of our monitoring stack.

### Added
- Property `type` of a deployment.
- Method `Deployment.monitor_bytes()` can be called if you have an image as bytes to send to monitoring.

### Changed
- `Deployment.monitor()` do not use parameters `model_version` and `shadow_model_version` anymore
- Parameter `shadow_raw_predictions` of `Deployment.monitor()` will be replaced by parameter `shadow_prediction` in the future
- You can add `content_type` parameter to monitor() if you don't want sdk to infer it with mimetypes. It will be checked with common content types of the mimetypes library
- `content_type` of monitor_bytes() is mandatory and should be a SupportedContentType enum or string. Current common type supported are "image/png" and "image/jpeg"

## [6.7.0] - 2023-05-05

### Added
- Add `Client.create_deployment()` to create a deployment. Allow user to create it without using Picsellia Serving
- Add `DatasetVersion.retrieve_stats()` to retrieve stats of your dataset version
- Add `DatasetVersion.train_test_val_split()` to split a dataset version into 3 different multi assets
- Add `DatasetVersion.split_into_multi_assets()` to split a dataset version into N multi assets and return their label repartition
- Add `MultiData.split()` and `MultiAsset.split()` to split from a given ratio a multi asset
- Add User-Agent with picsellia version in headers of requests

### Changed
- Framework and type of Model are now configurable into ModelVersion
- Get by id now use parent API to ensures object are in the same organization as the one connected
- Methods manipulating tags on client are now calling other routes
- Some minor fixes on documentation

### Fixed
- Segmentation format used in `monitor()` was not supported by monitoring service



## [6.6.0] - 2023-04-06

### Added
- `list_data` and `list_assets` have a new parameter `q` that can be used the same way the query language is used in the web platform
- Deployment has new methods: `set_training_data`, `check_training_data_metrics_status` and `disable_training_data_reference`, that can be used for monitoring and unsupervised metrics.
- `as_multidata` of MultiAsset can now be called with parameter
- Artifact, Data, Asset, LoggingFile, ScanFile, ModelFile are now inheriting from Downloadable, and have `url` property that can be used to download files. These urls are presigned and expired at some point in the future.
- Methods `add_evaluation`, `list_evaluations` and `compute_evaluations_metrics` of Experiment can be used to add, list and compute evaluation of an Experiment

### Changed
- Deployment Feedback Loop dataset is now only used as a recipient for new assets submitted after review in the predictions dashboard
- bbox of COCO annotation cannot be a tuple anymore


## [6.5.0] - 2023-03-15

### Added
- Jobs are now handled differently in Picsellia platform
- `get_dataset_version_by_id` can be done in Client
- `get_model_version_by_id` can be done in Client
- `get_experiment_by_id` can be done in Client
- Import yolo files with `import_annotations_yolo_files`
- `upload_data` can be called with an ErrorManager to retrieve errors after upload.

### Fix
- Pascal VOC files parsing allows some fields to not be set
- 502 errors were not handled correctly
- Uploading images that were transposed now correctly send width and height on the platform

### Changed
- Downloading files has a new retry policy
- When importing YOLO, COCO or Pascal VOC files, you need to set type of dataset before.
- Some refactor on import annotations, it should be faster now !


## [6.4.2] - 2023-03-03

### Changed
- Return line after logging chapter
- Allow parameter `enforced_ordered_categories` on `build_coco_file_locally()` to enforce categories of built coco file.

### Fixed
- Do a paginated call in dataset version `train_test_split` when loading assets
- Method `set_type` of dataset version was failing when logging result if a string was given

## [6.4.1] - 2023-02-17

### Fix
- Some methods were using types not compatible with python older than 3.8

## [6.4.0] - 2023-02-16

### Added
- DatasetVersion `list_assets()` will call XGET method when filtering on filenames or object_names, to not have the limit size query error.

### Fix
- Datalake `upload_data()` now allow effectively a Datasource
- Import annotations was limited to 10 000 annotations because `find_assets()` was used. It is now using `list_assets()` which is paginated.

### Changed
- Deployment `update()` cannot change active anymore.

### Deprecated
- DatasetVersion `find_all_assets()`

### Experimental
- DatasetVersion `build_coco_file_locally()` will create a COCOFile object that can be written in a json file


## [6.3.2] - 2023-01-31

### Added
- `Experiment.export_in_existing_model()` method will create a version of given model when exporting experiment.
- Datalake `list_data()` can be used to filter on object_names.

### Fix
- `ModelVersion.store()` was not using `replace` parameter correctly, it will now delete existing model file if it exists

### Changed
- All `max_workers` parameters are now `None` by default, to use cpu count + 4 as default value
- Datalake `list_data()` will call XGET method when filtering on filenames or object_names, to not have the limit size query error.

### Removed
- `AnnotationStatus.REVIEWED` status was never really used and is now removed from Picsellia.


## [6.3.1] - 2023-01-20
This is a patch to fix download dataset on huge datasets

### Fix
- `as_multidata` now uses xget to retrieve all datas with given list of ids

### Changed
- `as_multidata` is not called in `download` from DatasetVersion

## [6.3.0] - 2023-01-19
Happy new year from the Picsellia Team !
This minor version add some useful methods and fix specified COCOFile format.

### Added
- List public models with `list_public_models()` from the Picsellia Hub in Client.
- Find public model with `find_public_model()` from the Picsellia Hub in Client.
- Convert MultiAsset into MultiData with `as_multidata()` and `as_list_of_data()`
- Allow asset tags to be added when adding data to a dataset with `add_data()`
- Method `__repr__` has been added to MultiObjects
- Property `labels` in ModelVersion objects
- Add `get_dataset` in ModelContext to get DatasetVersion from its attached name

### Fix
- **breaking**: COCOFile was wrongly specified: in annotations, only one segmentation was allowed for each shape,
but COCOFile allows multiple polygons. Now you need to give a list of list of coordinates instead of only one list of coordinates.
`import_annotations_coco_file()` should now work fine with COCO files with segmentation.
- Add AuthenticationError again in exceptions, which was used by picsellia-tf2

### Changed
- **may be breaking**: Default value of force_create_label is now True in `import_annotations_coco_file` and `import_annotation_voc_file`.
- Rename `retrieve_experiment` into `get_experiment` in ModelContext
- `retrieve_datasets` in ModelContext now return a dict with attached name as key and dataset version as value
- `download()` a DatasetVersion is not calling assets extended endpoints which was taking a lot of time on huge datasets.
- Imports order with pre-commit cln tool
- Doc generation with all properties docstring

## [6.2.1] - 2022-27-12
### Fixed
- Fixed .predict() behavior by removing mandatory parameters tags and source


## [6.2.0] - 2022-27-12
### Added
- Add docker env variables support on ModelVersion
- Add an experiment.log_parameters() to use experiment.log() with parameters more easily
- Add possibility to attach base parameters when experiment.attach_model()
- Add feedbackloop method check status
- Add `__repr__` methods to DAO objects, for better UX representation
- Add possibility to set tags and source when sending a prediction to serving
- Add get_or_create_datasource() in client

### Changed
- Rename experiment.publish() into experiment.export_as_model()
- Some changes on feedbackloop methods
- Method list_data and list_assets can now use parameter `intersect_tags` to find objects that have all tags given
- Allow Path object in every method that accept path as string
- Some exceptions were renamed, some useless were removed

## [6.1.2] - 2022-11-10
### Fixed
- Use of typing.List instead of list to support python < 3.9

## [6.1.1] - 2022-11-10
### Added
- Add convert_tags_to_classification() in dataset version
- Add get_data_tags() on asset

### Changed
- Github workflow

## [6.1.0] - 2022-11-01
### Added
- Add ONXX in Framework enums
- Possibility to use strings instead of enums in methods

### Changed
- Make duration optional in annotation creation/update/overwrite
- Make duration int compatible
- log() method now create, update or append a log, in only one call to backend
- Remove create_log method
- Optional type hint is now used everywhere
- Prevent user from updating log image via log.update(), only experiment.log can be used for this case

### Fixed
- In log() method, image type data stored bad values

## [6.0.2] - 2022-10-17
### Added
- Logging File for an Experiment

### Changed
- A lot of typos, variable naming, minor formatting
- String .format() into f-strings
- Old package dependencies
- train_test_split() return MultiAsset instead of List[Asset]

### Fixed
- Regeneration of JWT when expired
- When downloading file, open file only if response is ok

## [6.0.1] - 2022-10-04
### Added
- CHANGELOG file.

### Changed
- Fixed test_train_split with breaking changes of query language in list assets.
- Documentation of core functions, minor typos fixes.
- Workflow for testing on staging when push on development and main.

## [6.0.0] - 2022-10-03
### Added
- Annotation are now objects storing Rectangle, Polygon, Classification, Point and Line for an Asset
- Artifact are now Experiment files stored
- DatasetVersion are now used as versions of Dataset
- Datalake objects
- Datasource objects
- Job objects, to wait for tasks to end
- ModelVersion are now used as versions of Model
- ScanFiles are now Scan files stored

### Changed
- Pictures renamed to Asset that are Data objects in a DatasetVersion
- Multithreading usage
- Tags
- Annotations with objects
