# -*- coding: utf-8 -*-

"""
This script generates training data for a machine learning model.
The data is split into training, validation, and test sets using the Apache Beam library.
Earth Engine Python API is used to load and manipulate geospatial data.
The script uses TensorFlow to serialize the data into TFRecord format.
"""

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

import ee
import argparse

try:
    from aces.ee_utils import EEUtils
    from aces.utils import TFUtils, Utils
    from aces.config import Config
except ModuleNotFoundError:
    print("ModuleNotFoundError: Attempting to import from parent directory.")
    import os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    from aces.ee_utils import EEUtils
    from aces.utils import TFUtils, Utils
    from aces.config import Config

# Before running this script, you need to authenticate to Google Cloud:
# https://cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python#before-you-begin

# ToDo: Is there a way to use seed value in the split?

__all__ = ["TrainingDataGenerator"]

class TrainingDataGenerator:
    """
    A class to generate training data for machine learning models.
    This class utilizes Apache Beam for data processing and Earth Engine for handling geospatial data.
    """
    def __init__(self, include_after: bool = False, use_service_account: bool = False):
        """
        Constructor for the TrainingDataGenerator class.

        Parameters:
        include_after (bool): If True, includes "after" images in the generated data. Default is False.
        """
        self.output_bucket = Config.GCS_BUCKET
        self.kernel_size = Config.PATCH_SHAPE_SINGLE
        self.grace = 10
        self.scale = Config.SCALE
        self.include_after = include_after
        self.test_ratio = 0.1
        self.validation_ratio = 0.2
        self.seed = 100
        self.use_service_account = use_service_account

    def load_data(self) -> None:
        """
        Load the necessary data from Earth Engine and prepare it for use.
        """
        EEUtils.initialize_session(use_highvolume=True, key=Config.EE_SERVICE_CREDENTIALS if self.use_service_account else None)
        self.l1 = ee.FeatureCollection("projects/servir-sco-assets/assets/Bhutan/BT_Admin_1")
        self.paro = self.l1.filter(ee.Filter.eq("ADM1_EN", "Paro"))

        # self.sample_locations = ee.FeatureCollection("projects/servir-sco-assets/assets/Bhutan/ACES_2/paro_2021_all_class_samples")
        # self.sample_locations = ee.FeatureCollection("projects/servir-sco-assets/assets/Bhutan/ACES_2/paro_2021_all_class_samples_clipped")
        self.sample_locations = ee.FeatureCollection("projects/servir-sco-assets/assets/Bhutan/ACES_2/paro_2021_all_class_samples_clipped_new")
        self.sample_locations = self.sample_locations.randomColumn("random", self.seed)
        self.training_sample_locations = self.sample_locations.filter(ee.Filter.gt("random", self.validation_ratio + self.test_ratio)) # > 0.4
        print("Training sample size:", self.training_sample_locations.size().getInfo())
        self.validation_sample_locations = self.sample_locations.filter(ee.Filter.lte("random", self.validation_ratio)) # <= 0.2
        print("Validation sample size:", self.validation_sample_locations.size().getInfo())
        self.test_sample_locations = self.sample_locations.filter(ee.Filter.And(ee.Filter.gt("random", self.validation_ratio),
                                                               ee.Filter.lte("random", self.validation_ratio + self.test_ratio))) # > 0.2 and <= 0.4
        print("Test sample size:", self.test_sample_locations.size().getInfo())
        self.sample_size = self.sample_locations.size().getInfo()
        print("Sample size:", self.sample_size)
        self.sample_locations_list = self.sample_locations.toList(self.sample_size + self.grace)

        self.label = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/paro_2021_all_class_label").rename("class").unmask(0, False)
        # self.other = self.label.remap([0, 1], [1, 0]).rename(["other"])

        self.composite_after = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/Paro_Rice_Composite_2021/composite_after")

        self.composite_before = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/Paro_Rice_Composite_2021/composite_before")

        self.composite_during = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/Paro_Rice_Composite_2021/composite_during")

        evi_before = EEUtils.calculate_evi(self.composite_before)
        evi_during = EEUtils.calculate_evi(self.composite_during)
        evi_after = EEUtils.calculate_evi(self.composite_after)

        self.composite_before = self.composite_before.addBands(evi_before)
        self.composite_during = self.composite_during.addBands(evi_during)
        self.composite_after = self.composite_after.addBands(evi_after)

        original_bands = self.composite_before.bandNames().getInfo()
        lowercase_bands = [band.lower() for band in original_bands]

        self.composite_before = self.composite_before.select(original_bands, lowercase_bands)
        self.composite_after = self.composite_after.select(original_bands, lowercase_bands)
        self.composite_during = self.composite_during.select(original_bands, lowercase_bands)

        self.composite_before = self.composite_before.regexpRename("$(.*)", "_before")
        self.composite_after = self.composite_after.regexpRename("$(.*)", "_after")
        self.composite_during = self.composite_during.regexpRename("$(.*)", "_during")

        self.sentinel1_asc_before_composite = ee.Image("projects/servir-sco-assets/assets/Bhutan/Sentinel1Ascending2021/s1AscBefore")
        self.sentinel1_asc_during_composite = ee.Image("projects/servir-sco-assets/assets/Bhutan/Sentinel1Ascending2021/s1AscDuring")

        self.sentinel1_desc_before_composite = ee.Image("projects/servir-sco-assets/assets/Bhutan/Sentinel1Descending2021/s1DescBefore")
        self.sentinel1_desc_during_composite = ee.Image("projects/servir-sco-assets/assets/Bhutan/Sentinel1Descending2021/s1DescDuring")

        self.elevation = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/elevationParo")
        self.slope = ee.Image("projects/servir-sco-assets/assets/Bhutan/ACES_2/slopeParo")

        if self.include_after:
            self.image = self.composite_before.addBands(self.composite_during).addBands(self.composite_after).toFloat()
        else:
            self.image = self.composite_before.addBands(self.composite_during).toFloat()

        if Config.USE_S1:
            self.image = self.image.addBands(self.sentinel1_asc_before_composite).addBands(self.sentinel1_asc_during_composite).addBands(self.sentinel1_desc_before_composite).addBands(self.sentinel1_desc_during_composite).toFloat()
            Config.FEATURES.extend(["vv_asc_before", "vh_asc_before", "vv_asc_during", "vh_asc_during",
                                    "vv_desc_before", "vh_desc_before", "vv_desc_during", "vh_desc_during"])

        if Config.USE_ELEVATION:
            self.image = self.image.addBands(self.elevation).addBands(self.slope).toFloat()
            Config.FEATURES.extend(["elevation", "slope"])

        self.image = self.image.select(Config.FEATURES)
        self.image = self.image.addBands(self.label).toFloat()

        print("Image bands:", self.image.bandNames().getInfo())
        self.selectors = self.image.bandNames().getInfo()

        proj = ee.Projection("EPSG:4326").atScale(10).getInfo()

        # Get scales out of the transform.
        self.scale_x = proj["transform"][0]
        self.scale_y = -proj["transform"][4]

    def generate_training_neighborhood_data(self) -> None:
        """
        Use Apache Beam to generate training, validation, and test patch data from the loaded data.
        """
        from datetime import datetime
        from uuid import uuid4

        export_kwargs = { "bucket": self.output_bucket, "selectors": self.selectors }

        file_prefix = f"experiments_neighbour_{self.kernel_size}x{self.kernel_size}"

        if Config.USE_S1:
            file_prefix += "_s1"

        if Config.USE_ELEVATION:
            file_prefix += "_elevation"

        training_file_prefix = f"{file_prefix}_training/training"
        testing_file_prefix = f"{file_prefix}_testing/testing"
        validation_file_prefix = f"{file_prefix}_validation/validation"

        def _generate_data(image, data, selectors, use_service_account, prefix):
            if "training" in prefix:
                description = "Training"
            elif "validation" in prefix:
                description = "Validation"
            elif "testing" in prefix:
                description = "Testing"
            else:
                description = "Unknown"

            print(f"{description} Data")

            beam_options = PipelineOptions([], direct_num_workers=0, direct_running_mode="multi_processing", runner="DirectRunner")
            with beam.Pipeline(options=beam_options) as pipeline:
                _ = (
                    pipeline
                    | "Create range" >> beam.Create(range(0, data.size().getInfo(), 1))
                    | "Yield sample points" >> beam.Map(EEUtils.beam_yield_sample_points_with_index, data.toList(data.size()), use_service_account)
                    | "Get patch" >> beam.Map(EEUtils.beam_sample_neighbourhood, image, use_service_account)
                    | "Write training data" >> beam.Map(EEUtils.beam_export_collection_to_cloud_storage, start_training=True,
                                                        **{**export_kwargs, "file_prefix": f"{prefix}_{datetime.now().strftime('%Y%m-%d%H-%M-%S_')}",
                                                           "description": f"{description}_{datetime.now().strftime('%Y%m-%d%H-%M-%S_')}",
                                                           "selectors": selectors})
                )

        _generate_data(self.image, self.training_sample_locations, self.selectors, self.use_service_account, training_file_prefix)

        _generate_data(self.image, self.validation_sample_locations, self.selectors, self.use_service_account, validation_file_prefix)

        _generate_data(self.image, self.test_sample_locations, self.selectors, self.use_service_account, testing_file_prefix)

    def generate_training_patch_data(self) -> None:
        """
        Use Apache Beam to generate training, validation, and test patch data from the loaded data.
        """
        beam_options = PipelineOptions([], direct_num_workers=0, direct_running_mode="multi_processing", runner="DirectRunner")
        with beam.Pipeline(options=beam_options) as pipeline:
            training_data, validation_data, test_data = (
                pipeline
                | "Create range" >> beam.Create(range(0, self.sample_size, 1))
                | "Yield sample points" >> beam.Map(EEUtils.beam_yield_sample_points, self.sample_locations_list, self.use_service_account)
                | "Get patch" >> beam.Map(EEUtils.beam_get_training_patches, self.image, self.selectors, self.scale, self.kernel_size, self.use_service_account)
                | "Filter patches" >> beam.Filter(Utils.filter_good_patches)
                | "Serialize" >> beam.Map(TFUtils.beam_serialize)
                | "Split dataset" >> beam.Partition(Utils.split_dataset, 3, validation_ratio=self.validation_ratio, test_ratio=self.test_ratio)
            )

            # Write the datasets to TFRecord files in the output bucket
            training_data | "Write training data" >> beam.io.WriteToTFRecord(
                f"gs://{self.output_bucket}/experiments_paro_{self.kernel_size}x{self.kernel_size}_before_during{'_after' if self.include_after else ''}_training/training", file_name_suffix=".tfrecord.gz"
            )
            validation_data | "Write validation data" >> beam.io.WriteToTFRecord(
                f"gs://{self.output_bucket}/experiments_paro_{self.kernel_size}x{self.kernel_size}_before_during{'_after' if self.include_after else ''}_validation/validation", file_name_suffix=".tfrecord.gz"
            )
            test_data | "Write test data" >> beam.io.WriteToTFRecord(
                f"gs://{self.output_bucket}/experiments_paro_{self.kernel_size}x{self.kernel_size}_before_during{'_after' if self.include_after else ''}_testing/testing", file_name_suffix=".tfrecord.gz"
            )

    def generate_training_patch_seed_data(self) -> None:
        """
        Use Apache Beam to generate training, validation, and test patch data from the loaded data.
        """
        def _generate_data_seed(image, data, selectors, scale, kernel_size, use_service_account, output_path) -> None:
            beam_options = PipelineOptions([], direct_num_workers=0, direct_running_mode="multi_processing", runner="DirectRunner")
            with beam.Pipeline(options=beam_options) as pipeline:
                _ = (
                    pipeline
                    | "Create range" >> beam.Create(range(0, data.size().getInfo(), 1))
                    | "Yield sample points" >> beam.Map(EEUtils.beam_yield_sample_points, data.toList(data.size()), use_service_account)
                    | "Get patch" >> beam.Map(EEUtils.beam_get_training_patches, image, selectors, scale, kernel_size, use_service_account)
                    | "Filter patches" >> beam.Filter(Utils.filter_good_patches)
                    | "Serialize" >> beam.Map(TFUtils.beam_serialize)
                    | "Write training data" >> beam.io.WriteToTFRecord(output_path, file_name_suffix=".tfrecord.gz")
                )

        output_path = f"gs://{self.output_bucket}/unet_{self.kernel_size}x{self.kernel_size}_planet_wo_indices"

        if Config.USE_S1:
            output_path += "_w_s1"

        if Config.USE_ELEVATION:
            output_path += "_w_elevation"

        datasets = [
            {"name": "training", "locations": self.training_sample_locations, "output_path": f"{output_path}/training_70/training"},
            {"name": "testing", "locations": self.test_sample_locations, "output_path": f"{output_path}/testing_10/testing"},
            {"name": "validation", "locations": self.validation_sample_locations, "output_path": f"{output_path}/validation_20/validation"}
        ]

        for dataset in datasets:
            print(f"{dataset['name'].capitalize()} output path:", dataset["output_path"])
            _generate_data_seed(
                self.image, dataset["locations"], self.selectors, self.scale, self.kernel_size,
                self.use_service_account, dataset["output_path"]
            )

    def generate_training_point_data(self) -> None:
        """
        Use Apache Beam to generate training, validation, and test point data from the loaded data.
        """
        training_sample_points = EEUtils.sample_image(self.image, self.training_sample_locations, **Config.__dict__)
        validation_sample_points = EEUtils.sample_image(self.image, self.validation_sample_locations, **Config.__dict__)
        test_sample_points = EEUtils.sample_image(self.image, self.test_sample_locations, **Config.__dict__)

        output_path = f"dnn_planet_wo_indices"

        if Config.USE_S1:
            output_path += "_w_s1"

        if Config.USE_ELEVATION:
            output_path += "_w_elevation"

        datasets = [
            {"name": "training", "sample_points": training_sample_points, "output_path": f"{output_path}/training_70/training"},
            {"name": "testing", "sample_points": test_sample_points, "output_path": f"{output_path}/testing_10/testing"},
            {"name": "validation", "sample_points": validation_sample_points, "output_path": f"{output_path}/validation_20/validation"}
        ]

        export_kwargs = { "bucket": self.output_bucket, "selectors": self.selectors }

        for dataset in datasets:
            print(f"{dataset['name'].capitalize()} output path:", dataset["output_path"])
            EEUtils.export_collection_data(dataset["sample_points"], export_type="cloud", start_training=True, **{**export_kwargs, "file_prefix": dataset["output_path"], "description": dataset["name"].capitalize()})

    def run_patch_generator(self) -> None:
        """
        Run the patch training data generation process.
        """
        self.load_data()
        self.generate_training_patch_data()

    def run_patch_generator_seed(self) -> None:
        """
        Run the patch training data generation process.
        """
        self.load_data()
        self.generate_training_patch_seed_data()

    def run_point_generator(self) -> None:
        """
        Run the point training data generation process.
        """
        self.load_data()
        self.generate_training_point_data()

    def run_neighborhood_generator(self) -> None:
        """
        Run the neighborhood training data generation process.
        """
        self.load_data()
        self.generate_training_neighborhood_data()


if __name__ == "__main__":
    print("Program started..")

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-m", "--mode", help="""Which mode to run? The available modes are: patch, point, neighborhood, patch_seed. \n
                        use as python generate_training_data.py --mode patch \n
                        or python generate_training_data.py --m point""")

    # Read arguments from command line
    mode = "neighborhood"
    if parser.parse_args().mode:
        mode = parser.parse_args().mode
    else:
        print("No mode specified, defaulting to neighborhood.")

    generator = TrainingDataGenerator(use_service_account=Config.USE_SERVICE_ACCOUNT)
    if mode == "patch":
        generator.run_patch_generator()
    elif mode == "patch_seed":
        generator.run_patch_generator_seed()
    elif mode == "point":
        generator.run_point_generator()
    elif mode == "neighborhood":
        generator.run_neighborhood_generator()
    else:
        print("Invalid mode specified.")

    print("\nProgram completed.")
